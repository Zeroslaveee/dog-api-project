import requests

def get_random_dog_image():
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        image_url = data['message']
        
        # Витягуємо назву породи з URL (наприклад: https://.../hound-afghan/n02088094_1003.jpg)
        breed_parts = image_url.split('/')[4].split('-')
        breed = ' '.join(breed_parts).capitalize()
        
        print(f"🐶 URL зображення: {image_url}")
        print(f"📛 Порода: {breed}")
    else:
        print("❌ Не вдалося отримати зображення.")

get_random_dog_image()
