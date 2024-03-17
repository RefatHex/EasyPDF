from PIL import Image
import requests
import io
from keys import Unsplash_api


def get_image(category):
    url = f"https://api.unsplash.com/photos/random?query={category}&orientation=landscape&content_filter=high&client_id={Unsplash_api}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        img_url = data["urls"]["regular"]
        img_data = requests.get(img_url).content

        # Open the image using PIL
        image = Image.open(io.BytesIO(img_data))


        image.save('x.jpg')
        return image
    else:
        print("Failed to fetch image.")
        return None
