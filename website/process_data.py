import base64
from PIL import Image
from io import BytesIO
from pyzbar.pyzbar import decode
import re

def process_data(data) -> str:
    # Extract base64-encoded image data
    _, encoded_data = data.split(',', 1)
    image_data = base64.b64decode(encoded_data)

    image = Image.open(BytesIO(image_data))
    image.save("website/static/captured_image.png")
    decoded_object  = decode(image)
    if len(decoded_object) > 0:
        data = decoded_object[0].data.decode('utf-8')
        pattern = r'([0-9a-f-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})'
        data = re.search(pattern, data).group(1)
        return data
    return ''
    
