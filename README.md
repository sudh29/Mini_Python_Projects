# Mini Python Projects Collection

A comprehensive collection of mini Python projects demonstrating various programming concepts and libraries. This repository showcases practical implementations of games, utilities, and data processing applications.

## Project Overview

### 📁 Project Structure

```
Mini_Python_Projects/
├── game/                          # Game implementations
│   ├── minesweeper_game/         # Classic Minesweeper game with Tkinter
│   ├── snake_game/               # Snake game implementation
│   └── tic_tac_toe/              # Tic-Tac-Toe game
├── multi_threading/               # Concurrency demonstrations
│   ├── 1_basic_threading.py      # Threading basics
│   ├── 2_lock_threading.py       # Thread synchronization with locks
│   ├── 3_multiprocessing.py      # CPU-bound parallel processing
│   └── 4_asyncio.py              # Async I/O with event loop
├── music_player/                  # Kivy-based music player GUI
├── notepad/                       # Tkinter text editor application
├── pdf/                           # PDF utilities
│   ├── image2pdf.py              # Convert images to PDF
│   └── read_pdf.py               # Extract text from PDF files
├── text_extraction_image/         # OCR and image text extraction
│   └── image_to_text.py          # Extract text from images
├── web_scraping/                  # Web scraping projects
│   ├── web_scraping.py           # Basic web scraping utility
│   ├── web_project0/             # YouTube data analysis (Jupyter notebooks)
│   └── web_project1/             # Indian stock market sentiment analysis
└── requirements.txt               # Project dependencies
```

## 🎮 Game Projects

### Minesweeper Game

- Classic Minesweeper implementation with grid-based gameplay
- Cell reveal and flag mechanics
- Mine detection and numbering system

### Snake Game

- Real-time snake movement and growth
- Food collection mechanics
- Collision detection

### Tic-Tac-Toe

- Two-player game implementation
- Win detection and draw scenarios
- Interactive board interface

## ⚙️ Multi-Threading & Concurrency

Learn about different concurrency models in Python:

1. **Basic Threading** - Introduction to thread creation and lifecycle
2. **Lock-based Threading** - Thread synchronization and resource sharing
3. **Multiprocessing** - CPU-bound parallel execution (bypasses GIL)
4. **Async I/O** - Event-driven I/O operations with asyncio

Each module includes:

- Detailed docstrings and type hints
- Real-world use case examples
- Performance comparisons
- Best practices documentation

## 🎵 Music Player

Kivy-based cross-platform music player featuring:

- Play/pause/stop controls
- Volume adjustment
- Playlist management
- Support for MP3, WAV, OGG, FLAC formats
- Real-time progress tracking
- File browser integration

## 📝 Notepad Application

Feature-rich text editor built with Tkinter:

- New, Open, Save, Save As functionality
- Undo/Redo support
- Cut, Copy, Paste operations
- Line and column position tracking
- Keyboard shortcuts
- Multi-format file support
- Cross-platform compatibility (Windows, Linux, macOS)

## 📄 PDF Utilities

### image2pdf.py

Convert multiple image files to a single PDF document

- Supports PNG, JPG, JPEG formats
- Batch processing
- Configurable output directory

### read_pdf.py

Extract text content from PDF files

- Text extraction with formatting
- Multi-page support
- Error handling for corrupted PDFs

## 🖼️ Text Extraction from Images (OCR)

### image_to_text.py

Extract text from images using OCR technology:

- Supports JPEG, PNG formats
- Multi-language text detection
- Configurable output formatting

## 🕷️ Web Scraping Projects

### web_scraping.py

General-purpose web scraping utility with:

- Beautiful Soup for HTML parsing
- Requests library for HTTP requests
- Error handling and retry logic
- User-agent rotation

### web_project0/

YouTube analytics project using Jupyter notebooks:

- `1_clinic_data.ipynb` - Healthcare data analysis
- `2_download_image.ipynb` - Image downloading utilities
- `2_youtube_views.ipynb` & `4_youtube_views.ipynb` - YouTube view analytics

### web_project1/

Indian Stock Market Intelligence System:

- Mock data collection with sentiment analysis
- Data processing pipeline with Pandas/Parquet
- Sentiment analysis on financial data
- Visualization of sentiment distribution

Features:

- Modular architecture (collection, processing, analysis)
- Logging integration
- Data export to Parquet format
- PNG visualization generation

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or higher
- pip or conda package manager

### Installation

1. Clone or download the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. For specific projects, install additional dependencies:

```bash
# For music player
pip install kivy python-vlc

# For GUI applications
pip install pillow

# For web scraping
pip install beautifulsoup4 requests selenium

# For PDF operations
pip install PyPDF2 img2pdf

# For OCR
pip install pytesseract pillow

# For data analysis projects
pip install pandas numpy matplotlib seaborn scikit-learn
```

### Running Projects

**Games:**

```bash
cd game/minesweeper_game
python main.py

cd game/snake_game
python main.py
```

**Utilities:**

```bash
# Notepad
python notepad/notepad.py

# Music Player
python music_player/music_player.py

# Web Scraping
python web_scraping/web_scraping.py
```

**Concurrency Examples:**

```bash
cd multi_threading
python 1_basic_threading.py
python 2_lock_threading.py
python 3_multiprocessing.py
python 4_asyncio.py
```

## 📋 Features

### Code Quality

- ✅ Type hints on all functions
- ✅ Comprehensive docstrings
- ✅ Error handling and logging
- ✅ PEP 8 compliant formatting

### Project Benefits

- Learning resource for Python concepts
- Real-world application examples
- Modular and reusable code
- Cross-platform compatibility

## 🛠️ Technologies Used

- **Python 3.12+** - Main programming language
- **Tkinter** - GUI for notepad and games
- **Kivy** - Cross-platform GUI framework
- **Threading/Multiprocessing** - Concurrency models
- **Asyncio** - Asynchronous I/O
- **Pandas** - Data analysis and manipulation
- **Matplotlib** - Data visualization
- **Beautiful Soup** - Web scraping
- **Selenium** - Browser automation
- **img2pdf** - Image to PDF conversion
- **PyTesseract** - OCR text extraction

## 📚 Learning Outcomes

This project collection demonstrates:

1. Object-oriented programming (OOP)
2. Concurrency models (threading, multiprocessing, async)
3. GUI development with Tkinter and Kivy
4. Web scraping and data collection
5. Data processing and analysis pipelines
6. File I/O and format handling
7. Error handling and logging best practices
8. Type hints and documentation standards

## ⚠️ Known Limitations

- WSL users: Audio playback in music player requires ffmpeg installation
- PDF operations: Requires pdf-related packages
- OCR: Requires Tesseract engine installation on system
- Web scraping: Some websites may block automated requests

## 🔧 Troubleshooting

### Import Errors

Ensure all dependencies are installed: `pip install -r requirements.txt`

### Audio Issues (Music Player)

- Install ffmpeg: `sudo apt-get install ffmpeg`
- On macOS: `brew install ffmpeg`

### Tkinter Issues on Linux

```bash
sudo apt-get install python3-tk
```

### OCR Issues

Install Tesseract:

```bash
# Linux
sudo apt-get install tesseract-ocr

# macOS
brew install tesseract

# Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki
```

## 📝 License

This project collection is provided as-is for educational purposes.

## 👨‍💻 Contributing

Feel free to enhance these projects by:

- Adding new features
- Improving code quality
- Creating additional project examples
- Fixing bugs and issues

---

**Last Updated:** December 2025
