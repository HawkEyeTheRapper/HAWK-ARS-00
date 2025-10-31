import os
import json

# Define the folder containing the notebooks
folder_path = "/Users/theandromedaproject/Dev/FinalForm/EverLights-Rite/notebooks/HawkEye_Lyric_Book_Full/02_Behold_A_Pale_Horse_2020"

# Define the desired header format
desired_header = [
    "# 🎵 Behold A Pale Horse",
    "",
    "**Album:** Behold A Pale Horse 2020",
    "",
    "**Performed by:** Hawk Eye The Rapper  ",
    "**Label:** LulzSwag Records  ",
    "**Genre:** Rap  ",
    "**UPC:** 885007879206  ",
    "",
    "🗃️ **Track Metadata**  ",
    "• Track #: 01  ",
    "• Title: Warning Shots  ",
    "• Artist: Hawk Eye The Rapper  ",
    "• Project: Behold A Pale Horse  ",
    "released July 4th, 2020",
    "**Dedicated to the late Milton William Cooper**",
    ""
]

# Function to update header cells in a notebook
def update_notebook_headers(file_path):
    with open(file_path, 'r') as f:
        notebook = json.load(f)

    updated = False
    for cell in notebook.get("cells", []):
        if cell.get("cell_type") == "markdown" and "# 🎵 Behold A Pale Horse" in "".join(cell.get("source", [])):
            cell["source"] = desired_header
            updated = True

    if updated:
        with open(file_path, 'w') as f:
            json.dump(notebook, f, indent=4)
        print(f"Updated: {file_path}")
    else:
        print(f"No changes made: {file_path}")

# Iterate through all .ipynb files in the folder
for root, _, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".ipynb"):
            update_notebook_headers(os.path.join(root, file))