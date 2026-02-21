import streamlit as st
import pandas as pd
import numpy as np
from math import comb
import matplotlib.pyplot as plt
from scipy.stats import norm

st.set_page_config(page_title="2項分布 B(n, p) 可視化", layout="centered")

st.title("🎲 2項分布 B(n, p) と正規分布の比較")

# --- 初期値 ---
if "n" not in st.session_state:
    st.session_state.n = 10
if "d" not in st.session_state:  # 分母
    st.session_state.d = 2
if "started" not in st.session_state:
    st.session_state.started = False

# --- リセットボタン ---
if st.button("🔄 リセット（n=10, p=1/2 に戻す）"):
    st.session_state.n = 10
    st.session_state.d = 2
    st.session_state.started = False

# --- パラメータ入力 ---
st.session_state.n = st.slider("標本数 n（試行回数）", 1, 100, st.session_state.n)
st.session_state.d = st.slider("成功確率 p = 1 / d の d（分母）", 1, 20, st.session_state.d)

n = st.session_state.n
d = st.session_state.d
p = 1 / d

st.write(f"### 選択された分布： B(n={n}, p=1/{d}={p:.3f})")

# --- スタートボタン ---
if st.button("▶ スタート"):
    st.session_state.started = True

# --- スタートするまで計算しない ---
if not st.session_state.started:
    st.info("「スタート」ボタンを押すと計算を開始します。")
    st.stop()

# --- 2項分布の計算 ---
k_values = np.arange(0, n + 1)
probabilities = np.array([comb(n, k) * (p**k) * ((1-p)**(n-k)) for k in k_values])

df = pd.DataFrame({
    "k（成功回数）": k_values,
    "P(X=k)": probabilities
})

# --- 表の表示 ---
st.subheader("📊 2項分布の確率表")
st.dataframe(df.style.format({"P(X=k)": "{:.5f}"}), height=400)

# --- グラフ（2項分布 + 正規分布） ---
st.subheader("📈 2項分布と正規分布の比較")

fig, ax = plt.subplots(figsize=(8, 4))

# 2項分布（棒グラフ）
ax.bar(k_values, probabilities, color="skyblue", label="2項分布 B(n,p)")

# 正規分布の近似
mu = n * p
sigma = np.sqrt(n * p * (1 - p))

x = np.linspace(0, n, 400)
normal_pdf = norm.pdf(x, mu, sigma)

# 棒グラフのスケールに合わせて正規分布を調整
normal_pdf_scaled = normal_pdf * (1 / np.sum(normal_pdf)) * np.sum(probabilities)

ax.plot(x, normal_pdf_scaled, "r--", linewidth=2, label="正規近似 N(np, np(1-p))")

ax.set_xlabel("k（成功回数）")
ax.set_ylabel("確率")
ax.legend()

st.pyplot(fig)

# --- 期待値と分散 ---
expected = mu
variance = sigma**2

st.write(f"### 📌 期待値 E[X] = {expected:.3f}")
st.write(f"### 📌 分散 Var[X] = {variance:.3f}")