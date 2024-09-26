from PIL import Image

def compress_image(input_path, output_path, quality=60):
    with Image.open(input_path) as img:
        original_format= img.format
        img.save(output_path, original_format, quality=quality)