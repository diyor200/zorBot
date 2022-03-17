import requests

from data import config


async def toonify(url):
    r = requests.post(
        "https://api.deepai.org/api/toonify",
        data={
            'image': f'{url}',
        },
        headers={'api-key': config.API_TOKEN}
    )
    data = r.json()
    try:
        return data['output_url']
    except:
        return None


if __name__ == "__main__":
    print(toonify('https://api.telegram.org/file/bot5030534231:AAHiS63E8jPsjBHPEa8P-k0uDQhZQfjrO7o/photos/file_3.jpg'))
