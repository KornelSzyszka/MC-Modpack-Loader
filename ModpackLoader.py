import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


def copy_mods():
    selected_mods_folder = filedialog.askdirectory(title="Select folder with mods")
    if not selected_mods_folder:
        return

    mc_mods_folder = os.path.join(os.getenv('APPDATA'), '.minecraft', 'mods')

    if os.path.exists(mc_mods_folder):
        shutil.rmtree(mc_mods_folder)

    shutil.copytree(selected_mods_folder, mc_mods_folder)
    messagebox.showinfo("Success", "Mods have been copied!")


def copy_saves():
    selected_saves_folder = filedialog.askdirectory(title="Select folder with saves")
    if not selected_saves_folder:
        return

    mc_saves_folder = os.path.join(os.getenv('APPDATA'), '.minecraft', 'saves')

    if os.path.exists(mc_saves_folder):
        shutil.rmtree(mc_saves_folder)

    shutil.copytree(selected_saves_folder, mc_saves_folder)
    messagebox.showinfo("Success", "Saves have been copied!")


def copy_saves_to_destination():
    selected_destination_folder = filedialog.askdirectory(title="Select destination folder for saves")
    if not selected_destination_folder:
        return

    mc_saves_folder = os.path.join(os.getenv('APPDATA'), '.minecraft', 'saves')

    if not os.path.exists(mc_saves_folder):
        messagebox.showerror("Error", "No saves found in .minecraft/saves folder.")
        return

    for save_folder in os.listdir(mc_saves_folder):
        source_save_path = os.path.join(mc_saves_folder, save_folder)
        destination_save_path = os.path.join(selected_destination_folder, save_folder)

        if os.path.exists(destination_save_path):
            shutil.rmtree(destination_save_path)

        shutil.copytree(source_save_path, destination_save_path)

    messagebox.showinfo("Success", "Saves have been copied to the destination folder!")


def main():
    root = tk.Tk()
    root.title("Copy Mods and Saves to Minecraft")
    root.geometry("400x250")

    root.iconbitmap("icon.ico")

    background_image = Image.open("background.png")
    background_imageTk = ImageTk.PhotoImage(background_image)

    canvas = tk.Canvas(root, width=400, height=250)
    canvas.pack()
    canvas.create_image(0, 0, anchor=tk.NW, image=background_imageTk)

    label_mods = tk.Label(root, text="Choose modpack to load.", bg='gray', fg='white')
    label_mods.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    button_mods = tk.Button(root, text="Load mods", command=copy_mods, bg='gray', fg='white')
    button_mods.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    label_saves = tk.Label(root, text="Choose save folder for modpack.", bg='gray', fg='white')
    label_saves.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    button_saves = tk.Button(root, text="Load saves", command=copy_saves, bg='gray', fg='white')
    button_saves.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    label_destination = tk.Label(root, text="Copy your actual saves before changing modpack!", bg='gray', fg='white')
    label_destination.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    button_destination = tk.Button(root, text="Import saves", command=copy_saves_to_destination, bg='gray', fg='white')
    button_destination.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    root.mainloop()


if __name__ == "__main__":
    main()
