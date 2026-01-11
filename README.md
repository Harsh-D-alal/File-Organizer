File Organizer (Python)

A simple Python script that organizes files in a folder into categorized subfolders based on their file extensions.

Overview

This project automatically sorts files into folders such as Images, Videos, Documents, Music, Code, etc.
Files that don’t match any predefined category are moved into an Others folder.
The script uses only Python’s standard library and is safe to run multiple times.

Features

Organizes files by extension
Automatically creates required folders
Skips existing directories
Handles unknown file types
Cross-platform (Windows, Linux, macOS)
No external dependencies

Supported Categories

Images: .jpg, .jpeg, .png, .gif
Videos: .mp4, .mkv, .avi
Documents: .pdf, .docx, .txt, .pptx
Music: .mp3, .wav
Archives: .zip, .rar, .tar
Code: .py, .js, .cpp, .java

All other files are moved to Others.

How to Run

Make sure Python 3 is installed
Clone the repository or download the script

Run:

python file_organizer.py
Enter the full path of the folder you want to organize


Example


Before

Downloads/
├── image.png
├── song.mp3
├── notes.pdf
├── script.py


After

Downloads/
├── Images/
├── Music/
├── Documents/
├── Code/
├── Others/


Why This Project

This project was built to practice:
File system operations in Python
Working with directories and paths
Writing safe automation scripts
Handling edge cases like folders vs files

Future Improvements

Organize files by date
Add duplicate file handling
Add undo functionality
Add command-line flags (dry run, custom categories)
Add logging


Requirements

Python 3.x
No third-party libraries required


License
This project is open source and free to use for learning and personal use.
