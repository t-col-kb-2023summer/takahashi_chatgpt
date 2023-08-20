import streamlit as st


def communicate(): # on_changeイベントで呼び出される関数を追加する
      # 1. ここでChatCPT APIを利用し、テキストボックスの内容を投げる
      # 2. APIからの応答をセッションに保存する
      session_state[“messages”] = st.session_state[“user_input”] # 今は仮で入力された文字を保存する
      st.session_state["user_input"] = ""  # 入力欄を消去


# UIの記述
st.title("My AI Assistant")
st.write("ChatGPT APIを使ったチャットボットです。")

st.text_input("メッセージを入力してください。", key="user_input", on_change=communicate)
st.write(session_state[“messages”])

