import os
import shutil

# Guide for the user
def show_guide():
    print("""
📂 File Organizer - Automatically Sort Your Files!
-------------------------------------------------
HOW TO USE:
1️⃣ Place this script (`file_organizer.py`) in the folder you want to organize.
2️⃣ Run the script by:
   - Double-clicking it (if Python is set up correctly).
   - Or opening it in IDLE and pressing F5.
3️⃣ The script will:
   ✅ Scan all files in the current folder.
   ✅ Sort them into categorized folders (Images, Documents, Code, etc.).
   ✅ Leave unknown files untouched.
4️⃣ Press '0' and Enter to close when done.

📌 NOTE: You can customize file categories in the script!
-------------------------------------------------
""")

# Define file categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Music": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".tar"],
    "Code": [".py", ".html", ".css", ".js", ".cpp", ".java"]
}

# Get the directory where the script is located
directory = os.path.dirname(os.path.abspath(__file__))

# Function to organi
