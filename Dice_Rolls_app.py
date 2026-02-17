import streamlit as st
import random
import time
import matplotlib.pyplot as plt

st.set_page_config(page_title="サイコロシミュレーション", layout="centered")
st.title("🎲 サイコロシミュレーション（1回・n回・割合表示・リセット）")

# セッション状態の初期化
if "counts" not in st.session_state:
    st.session_state.counts = [0] * 6

# サイコロの目を描く関数（matplotlib）
def draw_dice(number):
    fig, ax = plt.subplots(figsize=(2, 2))
    ax.set_xlim(0, 200)
    ax.set_ylim(0, 200)
    ax.set_facecolor("lightgray")
    ax.add_patch(plt.Rectangle((20, 20), 160, 160, fill=True, color="white", ec="black", lw=3))

    dots = {
        1: [(100, 100)],
        2: [(60, 60), (140, 140)],
        3: [(60, 60), (100, 100), (140, 140)],
        4: [(60, 60), (60, 140), (140, 60), (140, 140)],
        5: [(60, 60), (60, 140), (100, 100), (140, 60), (140, 140)],
        6: [(60, 60), (60, 100), (60, 140), (140, 60), (140, 100), (140, 140)]
    }

    for x, y in dots[number]:
        ax.add_patch(plt.Circle((x, y), 10, color="black"))

    ax.axis("off")
    return fig

# 1回振る
if st.button("🎲 1回振る"):
    result = random.randint(1, 6)
    st.session_state.counts[result - 1] += 1
    st.pyplot(draw_dice(result))

# n回振る
n = st.number_input("n回まとめて振る", min_value=1, max_value=10000, value=10, step=1)
if st.button("▶ n回実行"):
    for _ in range(n):
        result = random.randint(1, 6)
        st.session_state.counts[result - 1] += 1
    st.pyplot(draw_dice(result))

# リセット
if st.button("🔄 リセット"):
    st.session_state.counts = [0] * 6

# 集計表示
st.subheader("📊 結果")
total = sum(st.session_state.counts)

for i in range(6):
    percent = (st.session_state.counts[i] / total * 100) if total > 0 else 0
    st.write(f"{i+1} の回数：{st.session_state.counts[i]}　（{percent:.1f} %）")
