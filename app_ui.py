import streamlit as st
import requests

st.set_page_config(page_title="AI Todo Assistant", page_icon="📝")

st.title("📝 סוכן המשימות החכם שלי")


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("מה תרצה להוסיף לרשימה?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # פנייה לשרת ה-FastAPI שלנו
    with st.chat_message("assistant"):
        with st.spinner("חושב..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/chat",
                    json={"message": prompt},
                    timeout=30
                )
                if response.status_code == 200:
                    reply = response.json().get("reply", "לא התקבלה תשובה")
                    st.markdown(reply)
                    st.session_state.messages.append({"role": "assistant", "content": reply})
                else:
                    st.error("השרת החזיר שגיאה")
            except Exception as e:
                st.error(f"שגיאת חיבור: {e}")

with st.sidebar:
    st.header("ניהול")
    if st.button("נקה היסטוריית צ'אט"):
        st.session_state.messages = []
        st.rerun()