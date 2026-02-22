import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="一次関数の交点", layout="centered")

st.markdown(
    "<h2 style='color:navy;'>2本の一次関数のグラフと交点を調べよう</h2>",
    unsafe_allow_html=True
)

# セッション状態の初期化
if "a1" not in st.session_state:
    st.session_state.a1 = 1
    st.session_state.b1 = 0
    st.session_state.a2 = -1
    st.session_state.b2 = 0

# 表示・非表示チェック
col_toggle = st.columns(2)
show_line1 = col_toggle[0].checkbox("直線① を表示", value=True)
show_line2 = col_toggle[1].checkbox("直線② を表示", value=True)

# スライダー
st.subheader("パラメータ調整")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 直線①（青）")
    a1 = st.slider("傾き a₁", -5.0, 5.0, st.session_state.a1, 0.1)
    b1 = st.slider("切片 b₁", -5.0, 5.0, st.session_state.b1, 0.1)

with col2:
    st.markdown("### 直線②（赤）")
    a2 = st.slider("傾き a₂", -5.0, 5.0, st.session_state.a2, 0.1)
    b2 = st.slider("切片 b₂", -5.0, 5.0, st.session_state.b2, 0.1)

# 値を保存
st.session_state.a1 = a1
st.session_state.b1 = b1
st.session_state.a2 = a2
st.session_state.b2 = b2

# グラフ描画
x = np.linspace(-10, 10, 400)
fig, ax = plt.subplots(figsize=(7, 5))

# 直線①
if show_line1:
    y1 = a1 * x + b1
    ax.plot(x, y1, color="blue", label=f"①  y = {a1:.1f}x + {b1:.1f}")

# 直線②
if show_line2:
    y2 = a2 * x + b2
    ax.plot(x, y2, color="red", label=f"②  y = {a2:.1f}x + {b2:.1f}")

# 交点計算
st.subheader("交点")

if show_line1 and show_line2:
    if a1 != a2:
        x_int = (b2 - b1) / (a1 - a2)
        y_int = a1 * x_int + b1
        ax.scatter([x_int], [y_int], color="green", s=80, zorder=5)
        st.markdown(
            f"<h4 style='color:green;'>交点： ( x , y ) = ( {x_int:.2f} , {y_int:.2f} )</h4>",
            unsafe_allow_html=True
        )
    else:
        st.markdown("<h4 style='color:green;'>交点： 平行なため存在しない</h4>", unsafe_allow_html=True)
else:
    st.markdown("<h4 style='color:green;'>交点： ---（直線が2本とも表示されているときに計算）</h4>", unsafe_allow_html=True)

# 軸設定
ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linewidth=1)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.grid(True, alpha=0.3)

# 凡例
handles, labels = ax.get_legend_handles_labels()
if len(handles) > 0:
    ax.legend(loc="upper left", fontsize=12)

ax.set_xlabel("x", fontsize=12)
ax.set_ylabel("y", fontsize=12)

st.pyplot(fig)