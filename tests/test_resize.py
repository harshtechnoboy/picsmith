import unittest
from PIL import Image
from image_processes.resize import resize_image

class TestResize(unittest.TestCase):

    def test_resize(self):
        input_path = "images/fruit1.jpg"
        output_path = "images/fruit1_resized.jpg"
        
        resize_image(input_path, output_path, (600, 600))
        
        with Image.open(output_path) as img:
            self.assertEqual(img.size, (600, 600))

if __name__ == '__main__':
    unittest.main()