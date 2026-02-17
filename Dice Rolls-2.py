import tkinter as tk
import random
import time
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Yu Gothic'


# サイコロの目を描く関数
def draw_dice(canvas, number):
    canvas.delete("all")
    dots = {
        1: [(100, 100)],
        2: [(60, 60), (140, 140)],
        3: [(60, 60), (100, 100), (140, 140)],
        4: [(60, 60), (60, 140), (140, 60), (140, 140)],
        5: [(60, 60), (60, 140), (100, 100), (140, 60), (140, 140)],
        6: [(60, 60), (60, 100), (60, 140), (140, 60), (140, 100), (140, 140)]
    }
    canvas.create_rectangle(20, 20, 180, 180, fill="white", outline="black", width=3)
    for x, y in dots[number]:
        canvas.create_oval(x-10, y-10, x+10, y+10, fill="black")

# 1回だけ振る（アニメーション付き）
def roll_once():
    for _ in range(10):
        n = random.randint(1, 6)
        draw_dice(canvas, n)
        root.update()
        time.sleep(0.05)

    result = random.randint(1, 6)
    draw_dice(canvas, result)

    counts[result-1] += 1
    update_labels()

# n回まとめて振る
def roll_n_times():
    try:
        n = int(entry.get())
    except ValueError:
        return

    for _ in range(n):
        result = random.randint(1, 6)

        draw_dice(canvas, result)
        root.update()
        time.sleep(0.02)

        counts[result-1] += 1

    update_labels()

# 集計ラベル更新（割合表示付き）
def update_labels():
    total = sum(counts)
    for i in range(6):
        if total == 0:
            percent = 0.0
        else:
            percent = counts[i] / total * 100
        labels[i].config(text=f"{i+1} の回数：{counts[i]}   （{percent:.1f} %）")

# リセット機能
def reset_counts():
    global counts
    counts = [0] * 6
    update_labels()
    canvas.delete("all")

# GUIセットアップ
root = tk.Tk()
root.title("サイコロアニメーション（1回・n回・割合表示・リセット）")

canvas = tk.Canvas(root, width=200, height=200, bg="lightgray")
canvas.pack(pady=10)

# 1回だけ振るボタン
button1 = tk.Button(root, text="1回振る", font=("Arial", 14), command=roll_once)
button1.pack(pady=5)

# n回振る入力欄
frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="n回まとめて振る：", font=("Arial", 12)).pack(side="left")
entry = tk.Entry(frame, width=5)
entry.pack(side="left")

button2 = tk.Button(frame, text="実行", font=("Arial", 12), command=roll_n_times)
button2.pack(side="left", padx=5)

# リセットボタン
reset_button = tk.Button(root, text="リセット", font=("Arial", 12), command=reset_counts)
reset_button.pack(pady=10)

# 集計表示
counts = [0] * 6
labels = []

for i in range(6):
    lbl = tk.Label(root, text=f"{i+1} の回数：0   （0.0 %）", font=("Arial", 12))
    lbl.pack()
    labels.append(lbl)

root.mainloop()
