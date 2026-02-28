import openai
import json
import os
import httpx
from dotenv import load_dotenv
from todo_service import add_task, get_tasks, update_task, delete_task

load_dotenv()
os.environ['CURL_CA_BUNDLE'] = ''
client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
    http_client=httpx.Client(verify=False)
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "add_task",
            "description": "הוספת משימה חדשה",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {"type": "string", "description": "כותרת המשימה"},
                    "task_type": {"type": "string", "enum": ["עבודה", "אישי", "לימודים"]}
                },
                "required": ["title"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_tasks",
            "description": "שליפת כל המשימות הקיימות"
        }
    },
    {
        "type": "function",
        "function": {
            "name": "update_task",
            "description": "עדכון סטטוס משימה קיימת לפי ID",
            "parameters": {
                "type": "object",
                "properties": {
                    "task_id": {"type": "integer"},
                    "new_status": {"type": "string", "enum": ["פתוח", "הושלם"]}
                },
                "required": ["task_id", "new_status"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "delete_task",
            "description": "מחיקת משימה לפי ID",
            "parameters": {
                "type": "object",
                "properties": {
                    "task_id": {"type": "integer"}
                },
                "required": ["task_id"]
            }
        }
    }
]


def agent(query):
    try:
        messages = [
            {"role": "system", "content": "אתה עוזר ניהול משימות. חובה להשתמש בכלים לכל פעולה. ענה תמיד בעברית."},
            {"role": "user", "content": query}
        ]

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )

        msg = response.choices[0].message
        if not msg.tool_calls:
            return msg.content

        # הוספת הודעת האסיסטנט להיסטוריה
        messages.append({
            "role": "assistant",
            "tool_calls": [
                {
                    "id": t.id,
                    "type": "function",
                    "function": {"name": t.function.name, "arguments": t.function.arguments}
                } for t in msg.tool_calls
            ]
        })

        funcs = {"add_task": add_task, "get_tasks": get_tasks, "update_task": update_task, "delete_task": delete_task}

        for tool_call in msg.tool_calls:
            fn_name = tool_call.function.name
            fn_args = json.loads(tool_call.function.arguments)

            result = funcs[fn_name](**fn_args)

            # הוספת הודעת ה-tool פעם אחת בלבד!
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            })

        final_res = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages
        )
        return final_res.choices[0].message.content

    except Exception as e:
        return f"שגיאה: {str(e)}"