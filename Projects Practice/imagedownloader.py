import os 
import requests

def get_extension(image_url:str)-> str | None:
    extensions: list[str] = ['.png','.jpg','.jpeg','.gif','.svg']
    for ext in extensions:
        if ext in image_url:
            return ext
        
def download_image(image_url:str,name:str,folder:str=None):
    if ext := get_extension(image_url):
        if folder:
            image_name = f'{folder}/{name}'       

     