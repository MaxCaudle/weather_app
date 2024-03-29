import requests, urllib, os

def get_gif(data, query):
    """ Returns a gif from Giphy"""

    # grab one random image, based on the query
    giphy_url = f"http://api.giphy.com/v1/gifs/random?"+\
                f"api_key={data['giphy_api_key']}&tag={query.replace(' ','+').lower()}&limit=1"

    data=requests.get(giphy_url).json()
    image_url = data['data']['images']['downsized_large']['url']
    image_path = os.path.join(os.path.dirname(__file__), 'myfile1.gif')
    file, headers = urllib.request.urlretrieve(image_url, image_path)

    return file