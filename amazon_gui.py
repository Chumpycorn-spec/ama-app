import os
import io
from pathlib import Path
from PIL import Image
from rembg import remove
import tkinter as tk
from tkinter import filedialog, messagebox

TARGET_SIZE = 800


def process_image(input_path, output_dir):
    try:
        img = Image.open(input_path).convert("RGBA")

        # Remove background
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        removed = remove(buf.getvalue())
        subject = Image.open(io.BytesIO(removed)).convert("RGBA")

        # Crop tight
        bbox = subject.getbbox()
        if bbox:
            subject = subject.crop(bbox)

        # Resize
        scale = min(TARGET_SIZE / subject.width, TARGET_SIZE / subject.height)
        new_size = (int(subject.width * scale), int(subject.height * scale))
        subject = subject.resize(new_size, Image.Resampling.LANCZOS)

        # White canvas
        canvas = Image.new("RGB", (TARGET_SIZE, TARGET_SIZE), (255, 255, 255))

        # Center
        offset = (
            (TARGET_SIZE - subject.width) // 2,
            (TARGET_SIZE - subject.height) // 2
        )
        canvas.paste(subject, offset, subject)

        # Save
        name = Path(input_path).stem + "_amazon.jpg"
        save_path = os.path.join(output_dir, name)
        canvas.save(save_path, "JPEG", quality=95)

    except Exception as e:
        print(f"Error: {e}")


def process_files(file_paths):
    desktop = Path.home() / "Desktop"
    output_dir = desktop / "Amazon_Output"
    output_dir.mkdir(exist_ok=True)

    for file in file_paths:
        process_image(file, output_dir)

    messagebox.showinfo("Done", f"Images saved to:\n{output_dir}")


def select_files():
    files = filedialog.askopenfilenames(
        filetypes=[("Images", "*.jpg *.jpeg *.png *.webp")]
    )
    if files:
        process_files(files)


# GUI
app = tk.Tk()
app.title("Amazon Image Tool")
app.geometry("400x200")
app.configure(bg="white")

label = tk.Label(
    app,
    text="Drag & Drop Images\nor Click to Select",
    bg="white",
    fg="black",
    font=("Segoe UI", 14)
)
label.pack(expand=True)

button = tk.Button(
    app,
    text="Select Images",
    command=select_files,
    font=("Segoe UI", 10)
)
button.pack(pady=10)

app.mainloop()