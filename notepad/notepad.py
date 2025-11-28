import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Global variables for window size
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400


def open_file():
    # Open a file dialog to select a file
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not filepath:
        return
    # Clear the text editor
    text_editor.delete(1.0, tk.END)
    # Read the content of the selected file and insert it into the text editor
    with open(filepath, "r") as f:
        content = f.read()
        text_editor.insert(tk.END, content)
    # Update the window title
    window.title(f"Open file: {filepath}")


def save_file():
    # Open a file dialog to save the file
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt")])
    if not filepath:
        return
    # Write the content of the text editor to the selected file
    with open(filepath, "w") as f:
        content = text_editor.get(1.0, tk.END)
        f.write(content)
    # Update the window title
    window.title(f"Save file: {filepath}")


def main():
    # Create the main window
    global window
    window = tk.Tk()
    window.title("Notebook")

    # Configure the window size
    window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    # Create the text editor
    global text_editor
    text_editor = tk.Text(window, font="Helvetica 18")
    text_editor.grid(row=0, column=1)

    # Create a frame for buttons
    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    frame.grid(row=0, column=0, sticky="ns")

    # Create buttons for Save and Open actions
    save_button = tk.Button(frame, text="Save", command=save_file)
    open_button = tk.Button(frame, text="Open", command=open_file)
    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

    # Bind keyboard shortcuts for Save and Open actions
    window.bind("<Control-s>", lambda x: save_file())
    window.bind("<Control-o>", lambda x: open_file())

    # Start the Tkinter event loop
    window.mainloop()


if __name__ == "__main__":
    main()
