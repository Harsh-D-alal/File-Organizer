import os
import shutil

path = input("Enter the path of the Folder you wanna organize : ").strip()

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar"],
    "Code": [".py", ".js", ".cpp", ".java"]
}

for folder in FILE_TYPES:
    os.makedirs(os.path.join(path, folder), exist_ok=True)

os.makedirs(os.path.join(path, "Others"), exist_ok=True)

for item in os.listdir(path):
    item_path = os.path.join(path, item)

    if not os.path.isfile(item_path):
        continue

    ext = os.path.splitext(item)[1].lower()
    moved = False

    for folder, extensions in FILE_TYPES.items():
        if ext in extensions:
            shutil.move(item_path, os.path.join(path, folder, item))
            moved = True
            break

    if not moved:
        shutil.move(item_path, os.path.join(path, "Others", item))
