import streamlit as st
import random
import time
import matplotlib.pyplot as plt

st.set_page_config(page_title="サイコロアニメーション", layout="centered")

# タイトル（緑色）
st.markdown(
    "<h2 style='color: green;'>🎲 1 の目の出る確率を求めてみよう！</h2>",
    unsafe_allow_html=True
)

# セッション状態の初期化
if "counts" not in st.session_state:
    st.session_state.counts = [0] * 6

# サイコロの目を描く関数（1 の目は赤）
def draw_dice(number):
    fig, ax = plt.subplots(figsize=(2, 2))
    ax.set_xlim(0, 200)
    ax.set_ylim(0, 200)
    ax.set_facecolor("lightgray")
    ax.add_patch(plt.Rectangle((20, 20), 160, 160, fill=True, color="white", ec="black", lw=3))

    # 1 の目は赤、それ以外は黒
    color = "red" if number == 1 else "black"

    dots = {
        1: [(100, 100)],
        2: [(60, 60), (140, 140)],
        3: [(60, 60), (100, 100), (140, 140)],
        4: [(60, 60), (60, 140), (140, 60), (140, 140)],
        5: [(60, 60), (60, 140), (100, 100), (140, 60), (140, 140)],
        6: [(60, 60), (60, 100), (60, 140), (140, 60), (140, 100), (140, 140)]
    }

    for x, y in dots[number]:
        ax.add_patch(plt.Circle((x, y), 10, color=color))

    ax.axis("off")
    return fig

# アニメーション表示領域
placeholder = st.empty()

# 1回振る（アニメーション付き）
if st.button("🎲 1回振る"):
    for _ in range(10):
        n = random.randint(1, 6)
        placeholder.pyplot(draw_dice(n))
        time.sleep(0.05)

    result = random.randint(1, 6)
    placeholder.pyplot(draw_dice(result))
    st.session_state.counts[result - 1] += 1

# n回まとめて振る
n = st.number_input("n回まとめて振る", min_value=1, max_value=10000, value=10, step=1)
if st.button("▶ n回実行"):
    for _ in range(n):
        result = random.randint(1, 6)
        placeholder.pyplot(draw_dice(result))
        time.sleep(0.02)
        st.session_state.counts[result - 1] += 1

# リセット
if st.button("🔄 リセット"):
    st.session_state.counts = [0] * 6
    placeholder.empty()

# 理論値と実験値の比較
st.subheader("📘 理論値と実験値の比較")
total = sum(st.session_state.counts)

if total > 0:
    theo = 100 / 6
    actual = st.session_state.counts[0] / total * 100
    diff = actual - theo
    st.write(f"理論値：1/6 ≈ 16.7%　｜　実験値：{actual:.1f}%　（差：{diff:+.1f}%）")
else:
    st.write("理論値：1/6 ≈ 16.7%")

# 集計表示
st.subheader("📊 結果")
for i in range(6):
    percent = (st.session_state.counts[i] / total * 100) if total > 0 else 0
    st.write(f"{i+1} の回数：{st.session_state.counts[i]}　（{percent:.1f} %）")
