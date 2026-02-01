import threading
import queue
import customtkinter as ctk
from pynput import keyboard
from src.config import get_hotkey
from src.clipboard_utils import capture_selection
from src.gemini_client import GeminiClient
from src.ui.popup import ResponsePopup

# UI Queue to communicate between listener thread and main GUI thread
ui_queue = queue.Queue()

def process_queue(root):
    """Checks the queue for new messages to display."""
    try:
        while True:
            msg = ui_queue.get_nowait()
            if msg:
                # Show popup
                popup = ResponsePopup(msg)
                popup.lift()
                popup.focus_force()
    except queue.Empty:
        pass
    finally:
        root.after(100, process_queue, root)

def on_activate():
    """Triggered when hotkey is pressed."""
    print("Hotkey pressed! Capturing selection...")
    text = capture_selection()
    if not text.strip():
        print("No text selected.")
        return

    print(f"Captured text: {text[:50]}...")
    
    # Query Gemini (this might take a second, best done in a thread if we want to avoid freezing,
    # but since capture_selection is already in the listener thread, we are fine)
    try:
        client = GeminiClient()
        response = client.get_response(f"Explain or answer this: {text}")
        
        # Send response to UI thread
        # Note: We need to pass the response to the main thread to create the UI
        # because tkinter is not thread-safe.
        
        # Start a separate thread to send the request so we don't block the listener too long?
        # Actually listener thread is fine to block for a bit, but pynput might complain if it takes too long.
        # Let's do the request here for simplicity first.
        
        ui_queue.put(response)
        
    except Exception as e:
        print(f"Error: {e}")

def start_listener(hotkey_str):
    # Parse hotkey string to pynput format if needed, 
    # but GlobalHotKeys accepts strings like '<alt>+x'
    
    with keyboard.GlobalHotKeys({
        hotkey_str: on_activate
    }) as h:
        h.join()

def main():
    hotkey = get_hotkey()
    print(f"Starting Gemini Assistant. Listening for {hotkey}...")
    
    # Start listener in a separate daemon thread
    listener_thread = threading.Thread(target=start_listener, args=(hotkey,), daemon=True)
    listener_thread.start()
    
    # Start hidden root window for event loop
    root = ctk.CTk()
    root.withdraw() # Hide the main window
    
    # Start processing queue
    root.after(100, process_queue, root)
    
    root.mainloop()

if __name__ == "__main__":
    main()
