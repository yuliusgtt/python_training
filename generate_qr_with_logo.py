import os
from PIL import Image, ImageDraw
import qrcode
from urllib.parse import urlparse
from qrcode.exceptions import DataOverflowError
import traceback

def clean_url_for_filename(qr_url):
    parsed_url = urlparse(qr_url)
    netloc = parsed_url.netloc
    if netloc.startswith("www."):
        netloc = netloc[4:]
    path = parsed_url.path.strip("/")
    filename = f"{netloc}_{path.replace('/', '_')}" if path else netloc
    filename = "".join(c if c.isalnum() or c in "._-" else "_" for c in filename)
    return filename

def validate_url(qr_url):
    parsed_url = urlparse(qr_url)
    if not parsed_url.scheme:
        qr_url = f"http://{qr_url}"
        parsed_url = urlparse(qr_url)
    if not parsed_url.netloc:
        raise ValueError("URL is not valid.")
    return qr_url

def create_qr_with_logo(qr_url, file_path):
    try:
        qr_url = validate_url(qr_url)

        url_name = clean_url_for_filename(qr_url)
        img = Image.open(file_path).convert("RGBA")
        wpercent = (100 / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        logo = img.resize((100, hsize), Image.Resampling.LANCZOS)

        if logo.mode in ('RGBA', 'P'):  
            white_bg = Image.new("RGB", logo.size, (255, 255, 255))
            white_bg.paste(logo, mask=logo.split()[3]) 
            logo = white_bg

        QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
        QRcode.add_data(qr_url)
        QRcode.make()
        QRimg = QRcode.make_image(fill_color='black', back_color="white").convert("RGB")


        pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)
        QRimg.paste(logo, pos)

        directory = os.path.dirname(file_path)
        filename, _ = os.path.splitext(os.path.basename(file_path))
        output_dir = os.path.join(directory, f"qr_output_{url_name}")
        os.makedirs(output_dir, exist_ok=True)

        png_path = os.path.join(output_dir, f"qr_output_{url_name}.png")
        QRimg.save(png_path)

        print(f'Files saved in {output_dir}')
    except FileNotFoundError:
        print('The specified file was not found. Please check the file path and try again.')
    except IOError:
        print('The specified file is not a valid image or cannot be opened.')
    except DataOverflowError:
        print("Error: The input data is too large for the QR code version.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        traceback.print_exc()


# Inputs
qr_url = input("Enter URL for QR code: ")
file_path = input("Enter the image logo file name or path: ")
create_qr_with_logo(qr_url, file_path)
