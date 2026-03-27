📦 Amazon GUI Image Tool

A simple desktop GUI application for processing images using background removal (rembg) with a clean Tkinter interface.
Supports both local execution and Windows EXE builds via GitHub Actions.

✨ Features
Load images from file system
Remove background automatically using AI
Save processed images
Simple GUI built with Tkinter
Packaged as a standalone Windows .exe
🖥️ Tech Stack
Python 3.10+
Tkinter (GUI)
Pillow (image handling)
rembg (background removal AI)
onnxruntime (ML backend)
PyInstaller (EXE packaging)
📂 Project Structure
.
├── amazon_gui.py
├── requirements.txt
├── .github/
│   └── workflows/
│       └── build.yml
└── README.md
🚀 How to Run Locally
1. Clone repo
git clone https://github.com/chumpycorn-spec/ama-app.git
cd ama-app
2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
3. Install dependencies
pip install -r requirements.txt
4. Run app
python amazon_gui.py
🧾 requirements.txt

Make sure you include:

pillow
rembg
onnxruntime
numpy
opencv-python
🏗️ Build Windows EXE (GitHub Actions)

This project automatically builds a Windows executable using GitHub Actions.

How it works:
Push code to GitHub
GitHub Actions runs PyInstaller on Windows runner
Produces .exe file
Download from Actions → Artifacts
⚙️ Build Configuration (PyInstaller)

The EXE is built using:

pyinstaller --onefile --noconsole --collect-all rembg --collect-all onnxruntime amazon_gui.py
📦 Download EXE
Go to GitHub → Actions
Open latest successful build

Download artifact:

AmazonGUI.zip

Extract and run:

AmazonGUI.exe
⚠️ Notes
First launch may be slow (ML model loading)
EXE size is large due to AI dependencies
Windows Defender may warn (false positive due to packaging)
🧠 Troubleshooting
❌ “No module named PIL”

Ensure pillow is installed.

❌ “No module named rembg”

Ensure rembg is included in requirements and build step.

❌ EXE opens then closes

Run from terminal to see error output.

📌 Future Improvements
Faster startup (model optimization)
Smaller EXE packaging
Drag-and-drop UI
Progress bar for processing
👤 Author

Built as a lightweight image processing desktop tool using Python + AI background removal.
