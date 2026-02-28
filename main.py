from fastapi import FastAPI
from pydantic import BaseModel
from agent_service import agent

app = FastAPI(title="AI Todo Agent API")

print("--- השרת מתחיל לעלות ---")
app = FastAPI()
print("--- השרת עלה בהצלחה ---")
class ChatRequest(BaseModel):
    message: str


@app.get("/")
def read_root():
    return {"status": "The Agent is online and waiting for your tasks!"}



@app.post("/chat")
def chat_with_agent(request: ChatRequest):
    response = agent(request.message)

    return {"reply": response}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)