# Gemini "Select-to-Ask" Desktop Assistant

A Python-based productivity tool that allows you to highlight text anywhere on your screen, press a hotkey (default: `Alt+X`), and instantly get an explanation or answer from Google Gemini in a floating popup.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)

## Features

- **Global Hotkey:** Works system-wide over any application (Browser, IDE, PDF, etc.).
- **Smart Clipboard:** Automatically captures highlighted text without manual copying.
- **Gemini Integration:** Powered by Google's `gemini-2.5-flash` model for fast, accurate responses.
- **Modern UI:** Clean, frameless, "Always-on-Top" popup built with `customtkinter`.
- **Robust Error Handling:** Detects rate limits and API connectivity issues gracefully.

## Setup

### 1. Prerequisites
- Python 3.8 or higher.
- A Google API Key from [Google AI Studio](https://aistudio.google.com/).

### 2. Installation

Clone the repository:
```bash
git clone https://github.com/yourusername/gemini-desktop-assistant.git
cd gemini-desktop-assistant
```

Create and activate a virtual environment (Recommended):
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Configuration

1.  Copy the example environment file:
    - Rename `.env.example` to `.env`.
2.  Open `.env` and configure your settings:
    ```ini
    GOOGLE_API_KEY=AIzaSyYourKeyHere...
    HOTKEY=<alt>+x
    ```

## Usage

1.  Run the application:
    ```bash
    python run_app.py
    ```
    *Alternatively, you can run:* `python -m src.main`

    **To run in the background (hidden window):**
    Double-click `run_background.pyw` or run:
    ```bash
    pythonw run_background.pyw
    ```

2.  Highlight any text on your screen.
3.  Press `Alt+X` (or your configured hotkey).
4.  **Release the keys immediately**.
5.  Wait for the popup to appear with the answer.
6.  **To Close:**
    - Click `X` to close just the popup.
    - Click `Quit App` (red button) to terminate the entire application.

## Troubleshooting

- **"No text selected"**: 
    - Ensure you release the hotkey quickly.
    - Some applications (like PDFs or remote desktops) might block programmatic copying.
- **"GOOGLE_API_KEY not found"**:
    - Ensure your `.env` file is named exactly `.env` (not `.env.txt`).
    - Open `.env` and ensure it has content (sometimes it saves as empty).
- **"Rate Limit Exceeded"**:
    - If you are on the Free Tier, wait 1 minute before trying again.
- **"404 Not Found" (Model Error)**:
    - Run the included utility to check which models you have access to:
      ```bash
      python list_models.py
      ```

## Development Tools

Included in the repo are helper scripts for debugging:
- `debug_api.py`: Tests your connection to Google's servers.
- `list_models.py`: Lists all Gemini models available to your API Key.

## Future Improvements

- [ ] **Context Awareness**: Include more context from the active window.
- [ ] **Chat History**: Allow follow-up questions within the popup.
- [ ] **Markdown Support**: Render response with proper Markdown formatting (Bold, Code blocks).
- [ ] **Settings UI**: A graphical interface to change Hotkeys and API Keys easily.

## License

This project is open source and available under the [MIT License](LICENSE).
