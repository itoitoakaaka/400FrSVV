# 400FrSVV

Animated visualization of swimming speed variability (SVV) for each 50m lap of the 400m freestyle event.

## Overview

This tool creates an animated GIF showing how swimming speed changes across each 50m split for all swimmers in a 400m freestyle race. It reads timing data from an Excel file and generates a smooth lap-by-lap animation using Matplotlib's `FuncAnimation`.

## Features

- **Speed Animation**: Animated line chart showing speed progression for each swimmer across 8 × 50m splits (50m to 400m).
- **Multi-Swimmer Comparison**: Displays all swimmers simultaneously with individual color-coded lines and legend labels.
- **GIF Export**: Saves the animation as a lightweight GIF file using Pillow.

## Requirements

- Python 3.8+
- pandas
- Matplotlib
- openpyxl (for reading .xlsx files)
- Pillow (for GIF export)

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python 400Fr.py <excel_file_path>
# Example:
python 400Fr.py japan_open_400fr_results.xlsx
```

### Expected Excel Format

| Column | Description |
|--------|-------------|
| `名前` (Name) | Swimmer name |
| `所属` (Team) | Team affiliation |
| `50m` – `400m` | Speed (m/s) for each 50m split |

## Output

- `freestyle_speed_animation.gif`: Animated speed chart.
