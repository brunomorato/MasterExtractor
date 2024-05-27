import os
import piexif
from PIL import Image
from tkinter import Tk, filedialog

def extract_metadata(image_path):
    # Extract metadata using piexif
    try:
        exif_data = piexif.load(image_path)
        if exif_data:
            for ifd in ("0th", "Exif", "GPS", "1st"):
                print(f"=== {ifd} IFD ===")
                for tag in exif_data[ifd]:
                    tag_name = piexif.TAGS[ifd][tag]["name"]
                    tag_value = exif_data[ifd][tag]
                    print(f"{tag_name}: {tag_value}")
        else:
            print("A imagem não contém informações EXIF.")
    except Exception as e:
        print(f"Ocorreu um erro ao extrair metadados: {e}")

def select_image():
    root = Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename()
    if not file_path:
        print("Nenhum arquivo selecionado.")
        return

    return file_path

def main():
    # Select the image file
    image_path = select_image()

    # Check if the file is selected
    if not image_path:
        return

    # Extract metadata
    extract_metadata(image_path)

if __name__ == "__main__":
    main()
