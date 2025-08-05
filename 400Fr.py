import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import rcParams
rcParams['font.family'] = 'Hiragino Sans'  # システムフォントに合わせて設定

# エクセルファイルからデータを読み込む
file_path = ''  # エクセルファイルのパス
df = pd.read_excel(file_path)

# データの準備
names = df['名前']  # A列の名前
teams = df['所属']  # B列の所属
distances = ['50m', '100m', '150m', '200m', '250m', '300m', '350m', '400m']  # C列〜J列の距離
speeds = df[distances]  # 各50mごとの泳速度

# アニメーションの準備
fig, ax = plt.subplots()
lines = []  # 選手ごとのラインを保存するリスト
for name, team in zip(names, teams):
    line, = ax.plot([], [], label=f"{name} ({team})")
    lines.append(line)

# 軸の設定
ax.set_xlim(0, len(distances) - 1)  # 0から400mまで
ax.set_ylim(speeds.values.min() * 0.9, speeds.values.max() * 1.1)  # 最小速度と最大速度を基準に調整
ax.set_xticks(range(len(distances)))
ax.set_xticklabels(distances)
ax.set_xlabel('Distance')
ax.set_ylabel('Speed (m/s)')
ax.set_title('2024ジャパンオープンMen400mHeat')
ax.legend()

# アニメーションの更新関数
def update(frame):
    for i, line in enumerate(lines):
        # 選手ごとのデータを取得
        line.set_data(range(frame + 1), speeds.iloc[i, :frame + 1])
    return lines

# アニメーションの作成
ani = FuncAnimation(fig, update, frames=len(distances), interval=500, blit=True)

# アニメーションを保存する場合
ani.save('freestyle_speed_animation.gif', writer='pillow')

# 表示
plt.show()