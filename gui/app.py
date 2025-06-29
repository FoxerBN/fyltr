# GUI, Styles
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap import Style
from tkinter.filedialog import askopenfilenames, asksaveasfilename
from tkinterdnd2 import DND_FILES, TkinterDnD
# Utils
from utils.converter import convert_images_to_webp
from utils.zipper import save_images_to_zip
from utils.clear_folder import clear_folders
from utils.update_file_list import update_file_list
# System tools
import shutil, os

input_folder = "input_images"
output_folder = "output_archives"

def run_app():
    clear_folders(input_folder, output_folder)
    
    app = TkinterDnD.Tk()
    app.title("Image to WEBP Converter")
    app.geometry("500x450")
    app.resizable(False, False)

    style = Style(theme="superhero") 
    style.master = app
    selected_files = []

    def on_drop(event):
        files = app.tk.splitlist(event.data)
        update_file_list(files, selected_files, lbl_selected)

    def select_files():
        files = askopenfilenames(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
        if files:
            update_file_list(files, selected_files, lbl_selected)

    def update_quality_label(value):
        lbl_quality_value.config(text=f"Quality: {int(float(value))}")

    def convert_images():
        if not selected_files:
            lbl_selected.config(text="Please select images first!", foreground="red")
            return

        for file_path in selected_files:
            shutil.copy(file_path, input_folder)

        webp_quality = int(quality_slider.get())
        images_webp = convert_images_to_webp(input_folder, webp_quality)
        save_images_to_zip(images_webp, output_folder)
        
        btn_save_zip.configure(state=NORMAL)
        lbl_selected.config(text="Conversion successful!", foreground="green")

    def save_zip():
        zip_files = os.listdir(output_folder)
        if zip_files:
            source_zip = os.path.join(output_folder, zip_files[0])
            save_path = asksaveasfilename(defaultextension=".zip", filetypes=[("ZIP Files", "*.zip")])
            if save_path:
                shutil.move(source_zip, save_path)
                lbl_selected.config(text=f"ZIP saved to: {save_path}", foreground="white")
                clear_folders(input_folder, output_folder)
                btn_save_zip.configure(state=DISABLED)
                selected_files.clear()

    drop_frame = ttk.Frame(app, bootstyle="info")
    drop_frame.pack(pady=10, padx=20, fill="both", expand=False, ipadx=10, ipady=10)

    drop_label = ttk.Label(drop_frame, text="⬇ Drop PNG/JPG images here ⬇", font=("Helvetica", 12), anchor="center")
    drop_label.pack(expand=True, fill="both", pady=10)

    drop_frame.drop_target_register(DND_FILES)
    drop_frame.dnd_bind("<<Drop>>", on_drop)

    lbl_selected = ttk.Label(app, text="No files selected", font=("Helvetica", 12))
    lbl_selected.pack(pady=10)

    # Quality slider section
    quality_frame = ttk.Frame(app)
    quality_frame.pack(pady=10)

    lbl_quality_value = ttk.Label(quality_frame, text="Quality: 20", font=("Helvetica", 10))
    lbl_quality_value.pack()

    quality_slider = ttk.Scale(quality_frame, from_=1, to=100, orient="horizontal", 
                              length=300, command=update_quality_label)
    quality_slider.set(20)  # Default value
    quality_slider.pack(pady=5)

    quality_info = ttk.Label(quality_frame, text="1 = Lowest quality, 100 = Highest quality", 
                            font=("Helvetica", 8), foreground="gray")
    quality_info.pack()

    ttk.Button(app, text="Select Images", command=select_files, bootstyle=PRIMARY).pack(pady=5)
    ttk.Button(app, text="Convert Images", command=convert_images, bootstyle=SUCCESS).pack(pady=5)

    btn_save_zip = ttk.Button(app, text="Save ZIP Archive", command=save_zip, bootstyle=INFO, state=DISABLED)
    btn_save_zip.pack(pady=5)

    copyright_label = ttk.Label(app, text="© FoxerBN", font=("Helvetica", 8), foreground="gray")
    copyright_label.pack(side="bottom", anchor="se", padx=10, pady=5)

    app.mainloop()