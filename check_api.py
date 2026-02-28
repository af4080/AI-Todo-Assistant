import requests

url = "http://127.0.0.1:8000/chat"
data = {"message": "תוסיף לי משימה לקנות חלב מחר בבוקר תחת קטגוריה אישי"}

try:
    print("שולח בקשה לשרת...")
    response = requests.post(url, json=data, timeout=30)
    print("סטטוס קוד:", response.status_code)
    print("תשובת השרת:", response.json())
except Exception as e:
    print("הבדיקה נכשלה:", e)