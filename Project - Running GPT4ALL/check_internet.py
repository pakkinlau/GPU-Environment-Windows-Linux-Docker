import requests

def check_internet():
    url = 'http://www.google.com/'
    timeout = 5
    try:
        response = requests.get(url, timeout=timeout)
        print('Connected to the internet')
        print(response.status_code)
    except requests.ConnectionError:
        print('No internet connection available.')

if __name__ == '__main__':
    check_internet()