import urllib
from PIL import Image
import io
import numpy as np
import tensorflow as tf
SAMPLE_VALID_URL = "https://images.pexels.com/photos/13530051/pexels-photo-13530051.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=627&w=1200"


def download_image(url:str) -> bytes:
    """
    Function used to download an image from a url.
    If the download fails, it returns None, indicating the image does not exist or is not valid.

    Args:
        - url (str): the url of the image to download.
    
    Returns:
        - image_data (bytes) or None: el contenido de la imagen en bytes.
    """

    try:
        # Download image
        request = urllib.request.Request(
        url=url,
        headers={
            ## Specify the user Agent
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            ## Accepted formats
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            ## Accepted encodings
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'DNT': '1'
        }
        )
    
        with urllib.request.urlopen(request) as response:
           image_data = response.read()
        
        return image_data

    except Exception as e:
        print(f"Invalid url {url} has been detected.")
        print("Image not valid, skipping")
        return None



class Imagen(Image):

    def __init__(self, url):
        self.__url = url
        self.__image = self.__build()

    def get_url(self):
        return self.__url
    
    def get_image(self):
        return self.__image
    
    def invalidate_url(self):
        self.__url = None

    def to_numpy(self):
        try:
            return np.array(self.__image)
        except Exception as e:
            raise ValueError(f"Cannot convert {self.__image} to numpy")

    def to_tensor(self):
        try:
            array = self.to_numpy()
            return tf.convert_to_tensor(array, dtype=tf.float32)

        except Exception as e:
            raise ValueError(f"Cannot convert {self.__image} to tensor")

        

    def __download(self) -> bytes:

        """
        Function used to download an image from a url.
        If the download fails, it returns None, indicating the image does not exist or is not valid.

        Args:
            - url (str): the url of the image to download.
    
        Returns:
            - image_data (bytes) or None: el contenido de la imagen en bytes.
        """
        if self.__url:

            try:
                # Download image
                request = urllib.request.Request(
                url=self.__url,
                headers={
                ## Specify the user Agent
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                ## Accepted formats
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.9',
                 ## Accepted encodings
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'DNT': '1'
                }
                )
    
                with urllib.request.urlopen(request) as response:
                
                    image_data = response.read()
        
                return image_data

            except Exception as e:
                print(f"Invalid url {self.__url} has been detected.")
                print("Image not valid, skipping")
                self.invalidate_url()
            
                return None
            
            else:
                raise ValueError("Cannot download from an empty url")

        def __build(self):
            buffer = io.BytesIO(image)
            buffer.seek(0)
            image = Image.open(buffer)
            return image
        
