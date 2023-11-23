"""Utils for preprocessing data"""
import base64

IMAGE_FORMAT_LEN = 16
BASE64_FORMAT_LEN = 7


def from_text_image_url_to_bytes(image_url: str) -> bytes:
    """
    Transform text image url to bytes using cutting and decoding
    image_url has format "data:image/jpeg;base64,/9j/4AAQSkZJ..."
    """
    data = image_url.encode()
    data = data[IMAGE_FORMAT_LEN + BASE64_FORMAT_LEN :]
    image = base64.decodebytes(data)
    return image
