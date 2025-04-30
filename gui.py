from g_comply_stapler import package_pdfs
from tkinter import Tk, Button, Label, filedialog
import os

# package_pdfs takes a folder path as its only argument. 
# Create tkinter GUI with a folder selector and a run button.

def gui():
    root = Tk()
    root.title("gComply Stapler")
    root.geometry("600x300")
    # Use bmc.ico icon if available
    icon_path = os.path.join(os.path.dirname(__file__), 'bmc.ico')
    if os.path.exists(icon_path): root.iconbitmap(icon_path)

    # Add feedback label and folder path label
    feedback_label = Label(root, text="Select a folder to package PDFs")
    feedback_label.pack(pady=10)
    path_label = Label(root, text="")
    path_label.pack(pady=5)

    def update_feedback(message):
        feedback_label.config(text=message)

    def update_path(path):
        path_label.config(text=path)

    def select_folder():
        try:
            folder_path = filedialog.askdirectory()
            if folder_path:
                update_path(folder_path)
                update_feedback("Running...")
                package_pdfs(folder_path)
                update_feedback("PDF packages created successfully!")
                # open the packages folder
                packages_dir = os.path.join(folder_path, 'packages')
                if os.path.exists(packages_dir) and os.path.isdir(packages_dir):
                    update_feedback("Opening packages folder...")
                    os.startfile(packages_dir)
            else:
                update_feedback("Warning: No folder selected.")
        except Exception as e:
            update_feedback(f"Error: {str(e)}")

    select_button = Button(root, text="Select Folder", command=select_folder)
    select_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    gui()