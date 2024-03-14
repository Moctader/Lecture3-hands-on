import requests

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = 'live_X3bxuVnIpp1jrlaffiZGbqbR66PRgNoyanW5hhr4MjDbonSJYojZmtbYIjIHAQcg'

def get_random_cat_image():
    url = 'https://api.thecatapi.com/v1/images/search'
    headers = {
        'x-api-key': API_KEY
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data:
            image_url = data[0]['url']
            return image_url
    return None

def main():
    cat_image_url = get_random_cat_image()
    if cat_image_url:
        print("Here's your random cat image:", cat_image_url)
    else:
        print("Failed to fetch a cat image.")

if __name__ == "__main__":
    main()
