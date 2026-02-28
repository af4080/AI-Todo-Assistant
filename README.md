הנה קובץ `README.md` מסודר ומקצועי בעברית, שמתאר את פרויקט סוכן המשימות החכם שבנית:

---

# 📝 סוכן המשימות החכם שלי (AI Todo Assistant)

מערכת לניהול משימות המבוססת על בינה מלאכותית (LLM), המאפשרת למשתמש לנהל את המשימות שלו בשפה חופשית (עברית). הסוכן מסוגל להבין כוונות, להוסיף משימות, להציג אותן, לעדכן סטטוס ולמחוק משימות באמצעות שימוש ב-Tools (Function Calling).

## 🚀 תכונות עיקריות

* **ממשק צ'אט אינטראקטיבי:** מבוסס Streamlit לעבודה נוחה ומהירה.
* **הבנת שפה טבעית:** שימוש במודל `Llama 3.3 70B` דרך Groq API להבנת בקשות בעברית.
* **ניהול משימות מלא:** הוספה, צפייה, עדכון ומחיקה.
* **ארכיטקטורת סוכנים:** הפרדה מלאה בין הלוגיקה של ה-AI (`agent_service.py`) לבין ניהול הנתונים (`todo_service.py`).

## 🛠 טכנולוגיות

* **Python 3.10+**
* **FastAPI:** שרת Backend המתווך בין הממשק לסוכן.
* **Streamlit:** ממשק משתמש (Frontend).
* **Groq API / OpenAI SDK:** מנוע הבינה המלאכותית.
* **Pydantic:** אימות נתונים.

## 📂 מבנה הפרויקט

* `app_ui.py`: קוד ממשק המשתמש ב-Streamlit.
* `main.py`: שרת ה-FastAPI המריץ את ה-API.
* `agent_service.py`: הלוגיקה של הסוכן, הגדרת הכלים (Tools) והתקשורת עם ה-LLM.
* `todo_service.py`: ניהול רשימת המשימות (כרגע בזיכרון השרת).
* `.env`: קובץ הגדרות למפתחות API (יש ליצור באופן ידני).

## ⚙️ התקנה והרצה

1. **התקנת ספריות:**
```bash
pip install fastapi uvicorn openai streamlit httpx python-dotenv

```


2. **הגדרת מפתח API:**
צרו קובץ בשם `.env` בתיקייה הראשית והוסיפו את המפתח שלכם:
```env
OPENAI_API_KEY=your_groq_api_key_here

```


3. **הרצת שרת ה-API:**
```bash
python main.py

```


4. **הרצת ממשק המשתמש:**
בטרמינל חדש, הריצו:
```bash
streamlit run app_ui.py

```



## 📝 דוגמאות לשימוש

* "תוסיף לי משימה לקנות חלב מחר"
* "מה המשימות שלי?"
* "תעדכן את משימה 1 כבוצעה"
* "תמחק את משימת הריקוד"

---

### הערות למפתחים

המערכת משתמשת ב-`verify=False` בלקוח ה-HTTP כדי לעקוף בעיות תעודת SSL בסביבות פיתוח מסוימות. בשימוש בסביבת ייצור, מומלץ להגדיר תעודות כראוי.
