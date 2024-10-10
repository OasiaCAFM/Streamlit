import streamlit as st
import random
import time

# タイトル
st.title('クレーンゲーム')

# 説明
st.write('クレーンが動いている間にボタンを押してアイテムを掴もう！')

# セッションの初期化
if 'crane_position' not in st.session_state:
    st.session_state['crane_position'] = 0

if 'item_position' not in st.session_state:
    st.session_state['item_position'] = random.randint(0, 10)

if 'game_over' not in st.session_state:
    st.session_state['game_over'] = False

if 'win' not in st.session_state:
    st.session_state['win'] = False

# クレーンの動き
if not st.session_state['game_over']:
    st.session_state['crane_position'] = (st.session_state['crane_position'] + 1) % 11
    st.write(f'クレーンの位置: {st.session_state["crane_position"]}')

# ボタン
if st.button('クレーンを下げる') and not st.session_state['game_over']:
    st.session_state['game_over'] = True
    if st.session_state['crane_position'] == st.session_state['item_position']:
        st.session_state['win'] = True
        st.write('おめでとう！アイテムを掴みました！')
    else:
        st.write('残念！アイテムは掴めませんでした。')

# 再スタートボタン
if st.session_state['game_over']:
    if st.button('もう一度挑戦する'):
        st.session_state['crane_position'] = 0
        st.session_state['item_position'] = random.randint(0, 10)
        st.session_state['game_over'] = False
        st.session_state['win'] = False
        st.write('新しいゲームが始まりました！')

# クレーンとアイテムの位置を可視化
crane_line = ['-' for _ in range(11)]
crane_line[st.session_state['crane_position']] = 'C'  # クレーンの位置
item_line = ['-' for _ in range(11)]
item_line[st.session_state['item_position']] = 'I'  # アイテムの位置

st.write('クレーン:', ' '.join(crane_line))
st.write('アイテム:', ' '.join(item_line))
