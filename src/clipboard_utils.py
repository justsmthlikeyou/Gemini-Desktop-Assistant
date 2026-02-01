import time
import pyperclip
from pynput.keyboard import Controller, Key

keyboard = Controller()

def capture_selection():
    """
    Simulates Ctrl+C to copy selected text to clipboard 
    and returns the content.
    """
    # clear clipboard first
    original_clipboard = pyperclip.paste()
    pyperclip.copy("") 
    
    # Hack: Wait a split second for the user to potentially release keys
    # or just to separate the hotkey event from the copy event.
    time.sleep(0.2)
    
    # Press Ctrl+C
    # We explicitly release sensible modifiers just in case, though physical keys override.
    # But a small delay usually helps avoiding the 'Alt+Ctrl+C' issue.
    with keyboard.pressed(Key.ctrl):
        keyboard.press('c')
        keyboard.release('c')
    
    # Wait for clipboard to update (increased from 0.1 to 0.3)
    time.sleep(0.3)
    
    content = pyperclip.paste()
    
    # Retry once if failed (maybe timing was tight)
    if not content:
        time.sleep(0.3)
        content = pyperclip.paste()
    
    if not content:
        # Restore (optional)
        # pyperclip.copy(original_clipboard)
        return ""
        
    return content
