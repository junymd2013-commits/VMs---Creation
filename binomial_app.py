import streamlit as st
import pandas as pd
import numpy as np
from math import comb

st.set_page_config(page_title="2項分布 B(n, p) 可視化", layout="centered")

st.title("🎲 2項分布 B(n, p) を調べてみよう")

# --- 初期値 ---
if "n" not in st.session_state:
    st.session_state.n = 10
if "p" not in st.session_state:
    st.session_state.p = 0.5

# --- リセットボタン ---
if st.button("🔄 リセット（n=10, p=0.5 に戻す）"):
    st.session_state.n = 10
    st.session_state.p = 0.5

# --- パラメータ入力 ---
st.session_state.n = st.slider("標本数 n（試行回数）", 1, 50, st.session_state.n)
st.session_state.p = st.slider("成功確率 p", 0.0, 1.0, st.session_state.p, step=0.01)

n = st.session_state.n
p = st.session_state.p

st.write(f"### 選択された分布： B(n={n}, p={p})")

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

# --- グラフ ---
st.subheader("📈 2項分布のグラフ")
st.bar_chart(df.set_index("k（成功回数）"))

# --- 期待値と分散 ---
expected = n * p
variance = n * p * (1 - p)

st.write(f"### 📌 期待値 E[X] = {expected:.3f}")
st.write(f"### 📌 分散 Var[X] = {variance:.3f}")