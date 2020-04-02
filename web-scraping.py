import requests
import urllib.request
from bs4 import BeautifulSoup


def run():
    for i in range(1, 6):
        response = requests.get('https://xkcd.com/{}'.format(i))
        soup = BeautifulSoup(response.content, 'html.parser')
        
        imageContainer = soup.find(id='comic')
        imageUrl = imageContainer.find('img')['src']
        imageName = imageUrl.split('/')[-1]

        print('Downloading image {}'.format(imageName))
        urllib.request.urlretrieve('https:{}'.format(imageUrl), imageName)

if __name__ == '__main__':
    run()
