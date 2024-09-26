from PIL import Image

def resize_image(input_path, output_path, size):
    with Image.open(input_path) as img:
        img = img.resize(size, Image.Resampling.LANCZOS)
        img.save(output_path)