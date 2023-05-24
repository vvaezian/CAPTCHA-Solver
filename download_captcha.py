import requests
import os
import threading

url = 'https://www.game2.cn/verifyCode.php'
if not os.path.exists("./images/"):
    # Create a new directory because it does not exist
    os.makedirs("./images/")

def download_image(index):
    response = requests.get(url)

    if response.status_code == 200:
        with open(f'./images/image_{index}.jpg', 'wb') as f:
            f.write(response.content)
    else:
        print(f'Error occurred while downloading Image {index}.')
        
threads = []
for i in range(3000): # number of images to save
    thread = threading.Thread(target=download_image, args=(i,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()