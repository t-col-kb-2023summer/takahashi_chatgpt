import streamlit as st


# UIの記述
st.title("My AI Assistant")
st.write("ChatGPT APIを使ったチャットボットです。")

user_input = st.text_input("メッセージを入力してください。")

st.write(user_input)
