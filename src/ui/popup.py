import customtkinter as ctk

class ResponsePopup(ctk.CTkToplevel):
    def __init__(self, text_content):
        super().__init__()
        
        self.title("Gemini Response")
        self.geometry("400x300")
        self.overrideredirect(True) # Frameless
        self.attributes("-topmost", True)
        
        # Position near mouse
        self.update_idletasks()
        mouse_x = self.winfo_pointerx()
        mouse_y = self.winfo_pointery()
        self.geometry(f"+{mouse_x}+{mouse_y}")
        
        # Main Frame
        self.frame = ctk.CTkFrame(self, corner_radius=10)
        self.frame.pack(fill="both", expand=True, padx=2, pady=2)
        
        # Close Button (Top Right)
        self.close_btn = ctk.CTkButton(
            self.frame, 
            text="X", 
            width=24, 
            height=24, 
            command=self.destroy,
            fg_color="transparent",
            text_color="gray",
            hover_color="#ddd"
        )
        self.close_btn.pack(anchor="ne", padx=5, pady=(5, 0))

        # Quit App Button (Top Right, below Close)
        self.quit_btn = ctk.CTkButton(
            self.frame, 
            text="Quit App", 
            width=60, 
            height=20, 
            font=("Arial", 10),
            command=self.quit_app,
            fg_color="#ffcccc",
            text_color="red",
            hover_color="#ffaaaa"
        )
        self.quit_btn.pack(anchor="ne", padx=5, pady=(2, 5))
        
        # Scrollable Text Area
        self.textbox = ctk.CTkTextbox(
            self.frame, 
            wrap="word", 
            corner_radius=5
        )
        self.textbox.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        self.textbox.insert("0.0", text_content)
        self.textbox.configure(state="disabled") # Read-only
        
        # Bind Esc to close
        self.bind("<Escape>", lambda e: self.destroy())
        self.bind("<FocusOut>", lambda e: self.destroy()) # Close on focus loss

        # Dragging logic
        self.frame.bind("<ButtonPress-1>", self.start_move)
        self.frame.bind("<ButtonRelease-1>", self.stop_move)
        self.frame.bind("<B1-Motion>", self.do_move)
        self.x = 0
        self.y = 0

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")

    def quit_app(self):
        """Terminates the entire application."""
        import sys
        import os
        print("Quitting application...")
        # Force kill the process to ensure threads die
        os._exit(0)
