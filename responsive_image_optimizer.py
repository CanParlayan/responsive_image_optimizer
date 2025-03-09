from PIL import Image
import os


def resize_image(image_path, output_folder, sizes, format='webp'):
    with Image.open(image_path) as img:

        base_name = os.path.splitext(os.path.basename(image_path))[0]

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for size in sizes:
            width = size['width']
            height = size.get('height', None)

            if height is None:
                w_percent = (width / float(img.size[0]))
                height = int((float(img.size[1]) * float(w_percent)))

            resized_img = img.resize((width, height), Image.ANTIALIAS)

            output_name = f"{base_name}-{width}.{format}"
            output_path = os.path.join(output_folder, output_name)

            resized_img.save(output_path, format=format, quality=85)
            print(f"Saved {output_path}")


def process_current_directory(output_folder, sizes):
    current_directory = os.path.dirname(os.path.abspath(__file__))

    for filename in os.listdir(current_directory):

        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):

            image_path = os.path.join(current_directory, filename)

            resize_image(image_path, output_folder, sizes)
        else:
            print(f"Skipping non-image file: {filename}")


sizes = [
    {'width': 480},
    {'width': 800},
    {'width': 1200},
    {'width': 2400}
]

output_folder = 'resized_images'

process_current_directory(output_folder, sizes)
