from PIL import Image

def to_black_and_white(input_path: str, output_path: str) -> None:
    """
    Convert an image to black and white and save it to output_path.
    """
    img = Image.open(input_path).convert("L")  # L-mode gray scale
    img.save(output_path)
