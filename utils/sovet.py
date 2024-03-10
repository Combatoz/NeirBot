import requests

def sovet():
    url = 'https://yesno.wtf/api'
    response = requests.get(url)
    if response.status_code:
        data = response.json()
        return data.get('image')

if __name__ == '__main__':
    sovet()