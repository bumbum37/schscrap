#Download File Using Python
from os import system;system('clear')
import requests

r = requests.get('https://cdn.pixabay.com/photo/2016/12/16/15/25/christmas-1911637_640.jpg')

namefile = r.url.split('/')[-1]

with open(namefile, 'bw') as f:
    f.write(r.content)
    print(f'Download Sucsess\nFile Saved with Name: {namefile}')

