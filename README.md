# 400FrSVV

Python-based visualization of swimming-speed variability across a 400 m freestyle race.

## Project history

The initial analysis / visualization work was developed during my earlier research and technical-training period (2023–2024). The code was later cleaned and published on GitHub, so repository dates should not be interpreted as the original development dates.

## Overview

This tool reads lap-level swimming-speed data from an Excel file and generates an animated visualization of how speed changes across eight 50 m segments of a 400 m freestyle race.

## What this project demonstrates

- Python-based sports / human-performance data analysis
- tabular data handling with pandas
- scientific visualization with Matplotlib
- conversion of numerical race data into interpretable visual feedback
- early experience connecting analysis outputs with coaching / performance contexts

## Features

- **Lap-wise speed visualization** across 8 × 50 m segments
- **Multi-swimmer comparison**
- **Animated GIF export**
- command-line input for reusable analysis

## Requirements

- Python 3.8+
- pandas
- matplotlib
- openpyxl
- Pillow

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python 400Fr.py <excel_file_path>
```

Expected columns:

| Column | Description |
|---|---|
| `名前` | Swimmer name |
| `所属` | Team affiliation |
| `50m`–`400m` | Swimming speed for each 50 m segment |

## Output

`freestyle_speed_animation.gif`

## Portfolio note

This is a compact example of my earlier Python-based movement / performance analysis work. More recent repositories extend this direction toward computer vision, human sensing, and computational modeling.
