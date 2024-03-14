import requests
import cv2

# Function to check if image has a cat
def has_cat(image_path):
    # Load Haar Cascade Classifier for cat detection
    cat_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')

    # Read the image from the given path
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect cats in the image
    cats = cat_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Return True if cats are detected, False otherwise
    return len(cats) > 0

# Function to fetch a cat image using an API
def fetch_cat_image():
    # API endpoint for cat images
    url = "https://api.thecatapi.com/v1/images/search"
    
    # Make GET request to fetch the image
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code == 200:
        # Get the URL of the image from the response
        image_url = response.json()[0]['url']
        
        # Download the image
        image_response = requests.get(image_url)
        
        # Save the image to a file
        with open('cat_image.jpg', 'wb') as f:
            f.write(image_response.content)
        
        return 'cat_image.jpg'
    else:
        print("Failed to fetch cat image.")
        return None

# Main function
def main():
    # Fetch a cat image
    image_path = fetch_cat_image()
    
    if image_path:
        # Check if the image has a cat
        if has_cat(image_path):
            print("Cat detected in the image!")
        else:
            print("No cat detected in the image.")
    else:
        print("Could not perform cat detection.")

if __name__ == "__main__":
    main()
