import os
import sys

try:
    from PIL import Image
    from pillow_heif import register_heif_opener
    register_heif_opener()
    print("pillow-heif is available.")
except ImportError:
    print("pillow-heif not found. Attempting to install...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow-heif", "pillow"])
    from PIL import Image
    from pillow_heif import register_heif_opener
    register_heif_opener()

def convert_heic_to_jpg(directory="."):
    for filename in os.listdir(directory):
        if filename.lower().endswith(".heic"):
            filepath = os.path.join(directory, filename)
            try:
                print(f"Processing: {filename}")
                image = Image.open(filepath)
                # Convert to RGB (required for JPG)
                if image.mode != "RGB":
                    image = image.convert("RGB")
                
                # Create clean filename
                new_filename = os.path.splitext(filename)[0].replace(" ", "_") + ".jpg"
                save_path = os.path.join(directory, new_filename)
                
                image.save(save_path, "JPEG", quality=90)
                print(f"  --> Successfully saved as: {new_filename}")
            except Exception as e:
                print(f"  !! Error converting {filename}: {e}")

if __name__ == "__main__":
    # Get the directory where the script is located
    target_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Starting conversion in {target_dir}")
    convert_heic_to_jpg(target_dir)
    print("Done!")
