# מאגר המשימות בזיכרון
tasks = []
id_counter = 1

def add_task(title, task_type="אישי", **kwargs):
    global id_counter
    task = {
        "id": id_counter,
        "title": title,
        "type": task_type,
        "status": "פתוח"
    }
    tasks.append(task)
    id_counter += 1
    return f"משימה '{title}' נוספה בהצלחה עם מספר מזהה {task['id']}"

def get_tasks(status=None, **kwargs):
    global tasks
    filtered_tasks = tasks
    if status:
        filtered_tasks = [t for t in tasks if t['status'] == status]

    if not filtered_tasks:
        return "רשימת המשימות ריקה כרגע."

    # בניית מחרוזת אחת ברורה עבור הסוכן
    readable_list = "להלן רשימת המשימות שלך:\n"
    for t in filtered_tasks:
        readable_list += f"- מזהה {t['id']}: {t['title']} (סטטוס: {t['status']}, קטגוריה: {t['type']})\n"
    return readable_list

def update_task(task_id, new_status, **kwargs):
    global tasks
    try:
        t_id = int(task_id)
        for t in tasks:
            if t['id'] == t_id:
                t['status'] = new_status
                return f"הסטטוס של משימה {t_id} עודכן ל-{new_status}."
        return f"לא נמצאה משימה עם מזהה {t_id}."
    except:
        return "שגיאה בעיבוד מספר המשימה."

def delete_task(task_id, **kwargs):
    global tasks
    original_len = len(tasks)
    try:
        t_id = int(task_id)
        tasks = [t for t in tasks if t['id'] != t_id]
        if len(tasks) < original_len:
            return f"משימה {t_id} נמחקה."
        return f"לא נמצאה משימה עם מזהה {t_id}."
    except:
        return "שגיאה בעיבוד מספר המשימה למחיקה."