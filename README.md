# Responsive Image Optimizer

A small Python utility that generates multiple WebP image sizes from images in the script's directory. Useful for preparing responsive assets for websites.

## What it does

- Processes `.png`, `.jpg`, `.jpeg`, `.bmp`, `.gif`, and `.tiff` files.
- Exports WebP versions at **480, 800, 1200, and 2400 pixels wide**.
- Preserves the original aspect ratio when calculating height.
- Uses Pillow's LANCZOS resampling and quality 85.

## Requirements

- Python 3
- [Pillow](https://pillow.readthedocs.io/)

```bash
python -m pip install Pillow
```

## Usage

1. Clone this repository and open its directory.
2. Place the images you want to process beside `responsive_image_optimizer.py`.
3. Run:

```bash
python responsive_image_optimizer.py
```

The script writes files such as `photo-480.webp`, `photo-800.webp`, `photo-1200.webp`, and `photo-2400.webp` into `resized_images/` (relative to your current working directory).

## Configuration

Edit the `sizes` list near the bottom of the script to change output widths. Change `output_folder` to select a different destination.

**Note:** This is a batch conversion script, not a CLI with flags. Running it again can overwrite generated files with the same names. Review output sizes and visual quality before using the images in production.
