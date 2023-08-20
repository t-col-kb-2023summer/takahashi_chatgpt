import streamlit as st

# session_stateの初期化
#if "messages" not in st.session_state:
#    st.session_state["messages"] = ""


# on_changeイベントで呼び出される関数
def communicate():
      # Todo1. ここでChatCPT APIを利用し、テキストボックスの内容を投げたい
      # Todo2. APIからの応答をセッションに保存する
      st.session_state["messages"] = st.session_state["user_input"] # 今は仮で入力された文字を保存する
      st.session_state["user_input"] = ""  # 入力欄を消去


# UIの記述
st.title("My AI Assistant")
st.write("ChatGPT APIを使ったチャットボットです。")

st.text_input("メッセージを入力してください。", key="user_input", on_change=communicate)
if st.session_state["messages"]:
    st.write(st.session_state["messages"])
