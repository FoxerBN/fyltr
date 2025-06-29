# Fyltr 🚀🖼️

Fyltr is a user-friendly desktop app for converting multiple PNG and JPG images to the efficient WEBP format—quickly and easily, with a modern drag-and-drop interface!

[![Download .EXE](https://img.shields.io/badge/⬇️%20One%20Click%20Download-fyltr.exe-blue?style=for-the-badge)](https://github.com/FoxerBN/fyltr/releases/download/v1.0/fyltr.exe)
[👉 See all releases](https://github.com/FoxerBN/fyltr/releases/tag/v1.0)

---

## ✨ Features

- 🖱️ **Drag & Drop**: Instantly add images by dragging PNG/JPG files into the app
- 📂 **Batch Conversion**: Select and convert multiple images at once
- 🎚️ **Quality Slider**: Adjust the WEBP output quality from 1 to 100
- ⚡ **Fast & Easy**: Convert your images in just a few clicks
- 📦 **ZIP Archive**: Download all your converted images in a single ZIP file
- 💾 **Choose Save Location**: Save the archive wherever you want
- 🌈 **Beautiful UI**: Modern, clean, and dark-styled interface
- 🧹 **Auto Cleanup**: Temporary files are automatically deleted after use

---

## 🚀 How to Use

1. **Download** the app  
   👉 [⬇️ One-click Download (.exe for Windows)](https://github.com/FoxerBN/fyltr/releases/download/v1.0/fyltr.exe)
2. **Open Fyltr** and drag your images into the window
3. **Adjust quality** with the slider (optional)
4. **Click Convert** and save the ZIP archive with your new WEBP images!

---

## 🐍 Running from Source

1. Clone the repo:  
   ```bash
   git clone https://github.com/FoxerBN/fyltr.git
   cd fyltr
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:  
   ```bash
   python main.py
   ```

---

## 📦 Dependencies

- Python 3.8+
- [Pillow](https://python-pillow.org)
- [ttkbootstrap](https://ttkbootstrap.readthedocs.io/)
- [tkinterdnd2](https://github.com/pmgagne/tkinterdnd2)

---

## 🗂️ Project Structure (partial)
- `main.py`: App entry point
- `gui/app.py`: Main GUI and logic
- `utils/`: Image conversion, zipping, and file management
- `requirements.txt`: Python dependencies

