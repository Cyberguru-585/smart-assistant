import streamlit as st
import requests

# ✅ MUST BE FIRST
st.set_page_config(page_title="Smart Assistant", page_icon="🤖")

st.title("🤖 Smart Assistant")

# ✅ CSS (right place)
st.markdown("""
<style>
    .stTextInput>div>div>input {
        font-size: 18px;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# ✅ Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input
user_input = st.text_input("Type your message...")

if st.button("Send") and user_input:
    st.session_state.messages.append(("user", user_input))

    with st.spinner("Thinking..."):
        res = requests.post(
            "http://127.0.0.1:8000/chat",
            params={"user_input": user_input}
        )

    bot_reply = res.json()["response"]
    st.session_state.messages.append(("bot", bot_reply))

# Display chat
for role, msg in st.session_state.messages:
    if role == "user":
        st.markdown(f"""
        <div style='
            text-align:right;
            background:#1E88E5;
            color:white;
            padding:10px;
            border-radius:12px;
            margin:8px 0;
            max-width:70%;
            margin-left:auto;
        '>
        {msg}
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown(f"""
        <div style='
            text-align:left;
            background:#2E2E2E;
            color:white;
            padding:10px;
            border-radius:12px;
            margin:8px 0;
            max-width:70%;
        '>
        {msg}
        </div>
        """, unsafe_allow_html=True)