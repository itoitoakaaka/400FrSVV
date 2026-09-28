import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import rcParams
import sys

rcParams["font.family"] = "Hiragino Sans"


def main():
    if len(sys.argv) < 2:
        print("Usage: python 400Fr.py <excel_file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    df = pd.read_excel(file_path)

    required = ["名前", "所属", "50m", "100m", "150m", "200m", "250m", "300m", "350m", "400m"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    names = df["名前"]
    teams = df["所属"]
    distances = ["50m", "100m", "150m", "200m", "250m", "300m", "350m", "400m"]
    speeds = df[distances]

    fig, ax = plt.subplots()
    lines = []
    for name, team in zip(names, teams):
        line, = ax.plot([], [], label=f"{name} ({team})")
        lines.append(line)

    ax.set_xlim(0, len(distances) - 1)
    ax.set_ylim(speeds.values.min() * 0.9, speeds.values.max() * 1.1)
    ax.set_xticks(range(len(distances)))
    ax.set_xticklabels(distances)
    ax.set_xlabel("Distance")
    ax.set_ylabel("Speed (m/s)")
    ax.set_title("400 m Freestyle Speed Profile")
    ax.legend()

    def update(frame):
        for i, line in enumerate(lines):
            line.set_data(range(frame + 1), speeds.iloc[i, : frame + 1])
        return lines

    animation = FuncAnimation(
        fig,
        update,
        frames=len(distances),
        interval=500,
        blit=True,
    )
    animation.save("freestyle_speed_animation.gif", writer="pillow")
    print("Saved: freestyle_speed_animation.gif")


if __name__ == "__main__":
    main()
