import streamlit as st
import openai


# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key


# session_stateの初期化
if "messages" not in st.session_state:
    st.session_state["messages"] = ""


# on_changeイベントで呼び出される関数
def communicate():
    all_msg = st.session_state["messages"] #過去のやり取りをセッションから取得
    user_msg = {"role": "user", "content": st.session_state["user_input"]} # テキストボックス内文字列でJson形式作成
    all_msg.append(user_msg) #今回のチャット内容をやり取りの末尾に追加
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = all_msg
    )
    bot_msg = response["choices"][0]["message"]
    messages.append(bot_msg)
    st.session_state["user_input"] = ""  # 入力欄を消去


# UIの記述
st.title("My AI Assistant")
st.write("ChatGPT APIを使ったチャットボットです。")

st.text_input("メッセージを入力してください。", key="user_input", on_change=communicate)
if st.session_state["messages"]:
    st.write(st.session_state["messages"])