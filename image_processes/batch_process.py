import os
from .resize import resize_image
from .compress import compress_image

def batch_resize(directory, size):
    for filename in os.listdir(directory):
        if filename.endswith((".jpg", ".jpeg", ".png")):
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, "resized_" + filename)
            resize_image(input_path, output_path, size)

def batch_compress(directory, quality):
    for filename in os.listdir(directory):
        if filename.endswith((".jpg", ".jpeg", ".png")):
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, "compressed_" + filename)
            compress_image(input_path, output_path, quality)