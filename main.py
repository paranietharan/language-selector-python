import tkinter as tk
from ui import LanguageSelectorUI

def main():
    """Main entry point for the application"""
    root = tk.Tk()
    app = LanguageSelectorUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()