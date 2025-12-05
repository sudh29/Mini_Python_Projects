"""
Simple Notepad Application

A feature-rich text editor built with Python's Tkinter library.

Features:
- New, Open, Save, Save As functionality
- Undo/Redo support
- Cut, Copy, Paste operations
- Line and column position tracking
- Keyboard shortcuts
- Status bar
- Multi-format file support
"""

import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox

# Fix for XCB error in WSL2/Linux - MUST be done before any display imports
if sys.platform.startswith("linux"):
    try:
        import ctypes

        # Set environment variable before loading X11
        os.environ["GDK_SCALE"] = "1"
        os.environ["GDK_DPI_SCALE"] = "1"
        # Try to initialize X11 threading
        try:
            x11 = ctypes.cdll.LoadLibrary("libX11.so.6")
            x11.XInitThreads()
        except (OSError, AttributeError):
            # X11 not available or can't load library
            pass
    except Exception:
        pass


class Notepad:
    """Simple notepad application with menu-driven interface."""

    def __init__(self, root: tk.Tk) -> None:
        """
        Initialize the Notepad application.

        Args:
            root: The Tkinter root window
        """
        self.root = root
        self.root.title("Untitled - Notepad")
        self.root.geometry("800x600")
        self.file_path = None

        # Create Text Area with scrollbar
        self.text_area = tk.Text(self.root, font=("Consolas", 12), undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=1)

        self.scrollbar = tk.Scrollbar(self.text_area)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_area.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text_area.yview)

        # Status Bar showing line and column
        self.status_bar = tk.Label(self.root, text="Ln 1, Col 1", anchor=tk.E)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Create Menu Bar
        self._create_menu_bar()

        # Bind keyboard shortcuts
        self._bind_shortcuts()

        # Update status on text changes
        self.text_area.bind("<KeyRelease>", self.update_status)
        self.text_area.bind("<ButtonRelease-1>", self.update_status)

        # On Close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def _create_menu_bar(self) -> None:
        """Create the menu bar with File, Edit, and Help menus."""
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        # File Menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(
            label="Open", command=self.open_file, accelerator="Ctrl+O"
        )
        file_menu.add_command(
            label="Save", command=self.save_file, accelerator="Ctrl+S"
        )
        file_menu.add_command(
            label="Save As", command=self.save_as_file, accelerator="Ctrl+Shift+S"
        )
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.on_closing)

        # Edit Menu
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(
            label="Undo", command=self.text_area.edit_undo, accelerator="Ctrl+Z"
        )
        edit_menu.add_command(
            label="Redo", command=self.text_area.edit_redo, accelerator="Ctrl+Y"
        )
        edit_menu.add_separator()
        edit_menu.add_command(
            label="Cut",
            command=lambda: self.root.focus_get().event_generate("<<Cut>>"),
            accelerator="Ctrl+X",
        )
        edit_menu.add_command(
            label="Copy",
            command=lambda: self.root.focus_get().event_generate("<<Copy>>"),
            accelerator="Ctrl+C",
        )
        edit_menu.add_command(
            label="Paste",
            command=lambda: self.root.focus_get().event_generate("<<Paste>>"),
            accelerator="Ctrl+V",
        )
        edit_menu.add_separator()
        edit_menu.add_command(
            label="Select All", command=self.select_all, accelerator="Ctrl+A"
        )

        # Help Menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def _bind_shortcuts(self) -> None:
        """Bind keyboard shortcuts to their respective functions."""
        self.root.bind("<Control-n>", lambda e: self.new_file())
        self.root.bind("<Control-o>", lambda e: self.open_file())
        self.root.bind("<Control-s>", lambda e: self.save_file())
        self.root.bind("<Control-Shift-S>", lambda e: self.save_as_file())
        self.root.bind("<Control-a>", lambda e: self.select_all())

    def new_file(self) -> None:
        """Create a new file."""
        self.text_area.delete(1.0, tk.END)
        self.file_path = None
        self.root.title("Untitled - Notepad")
        self.update_status()

    def open_file(self) -> None:
        """Open a file dialog and load the selected file."""
        file_path = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if file_path:
            self.file_path = file_path
            self.root.title(f"{os.path.basename(self.file_path)} - Notepad")
            self.text_area.delete(1.0, tk.END)
            try:
                with open(self.file_path, "r", encoding="utf-8") as f:
                    self.text_area.insert(1.0, f.read())
                self.update_status()
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file:\n{e}")

    def save_file(self) -> None:
        """Save the current file or open Save As dialog if no file is set."""
        if self.file_path:
            try:
                with open(self.file_path, "w", encoding="utf-8") as f:
                    f.write(self.text_area.get(1.0, tk.END))
                messagebox.showinfo("Success", "File saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file:\n{e}")
        else:
            self.save_as_file()

    def save_as_file(self) -> None:
        """Save the current file with a new name or location."""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if file_path:
            self.file_path = file_path
            self.save_file()
            self.root.title(f"{os.path.basename(self.file_path)} - Notepad")

    def select_all(self, event=None) -> str:
        """Select all text in the editor."""
        self.text_area.tag_add(tk.SEL, "1.0", tk.END)
        self.text_area.mark_set(tk.INSERT, "1.0")
        self.text_area.see(tk.INSERT)
        return "break"

    def update_status(self, event=None) -> None:
        """Update the status bar with current line and column position."""
        cursor = self.text_area.index(tk.INSERT)
        line, col = cursor.split(".")
        self.status_bar.config(text=f"Ln {line}, Col {int(col) + 1}")

    def show_about(self) -> None:
        """Show About dialog."""
        messagebox.showinfo(
            "About", "Simple Notepad\nVersion 1.0\nBuilt with Python and Tkinter"
        )

    def on_closing(self) -> None:
        """Handle window closing event."""
        if self.text_area.get(1.0, tk.END) != "\n":
            response = messagebox.askyesnocancel(
                "Unsaved Changes", "Do you want to save your changes before closing?"
            )
            if response is None:
                return
            elif response:
                self.save_file()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop()
