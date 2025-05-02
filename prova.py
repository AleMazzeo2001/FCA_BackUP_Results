from pathlib import Path

path = Path("Run_01/Rolling_10/risultati_rolling_temp.pkl")

# Directory padre
parent_dirs = path.parent         # Run_01/Rolling_10
dir1 = parent_dirs.parent.name    # Run_01
dir2 = parent_dirs.name           # Rolling_10

# Nome del file
file_name = path.name             # risultati_rolling_temp.pkl

print(f"Dir1: {dir1}, Dir2: {dir2}, File: {file_name}")