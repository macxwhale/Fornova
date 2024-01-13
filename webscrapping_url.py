import os
import random
from datetime import datetime, timedelta
import requests
import csv

def generate_random_date(year):
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)

    random_days = random.randint(0, (end_date - start_date).days)
    random_date = start_date + timedelta(days=random_days)

    return random_date.strftime("%Y-%m-%d")

def generate_random_url():
    hotel_id = random.randint(0, 99999)
    check_in = generate_random_date(2024)
    check_out = datetime.strptime(check_in, "%Y-%m-%d") + timedelta(days=1)

    url = f"https://www.qantas.com/hotels/properties/{hotel_id}?adults=2&checkIn={check_in}&checkOut={check_out}&children=0&infants=0&location=London%2C%20England%2C%20United%20Kingdom&page=1&payWith=cash&searchType=list&sortBy=popularity"
    
    return hotel_id, check_in, check_out, url

# Try to get exactly 25 URLs with status code 200
urls_with_200_status = []
while len(urls_with_200_status) < 25:
    hotel_id, check_in, check_out, url = generate_random_url()
    
    # Make a request to the URL
    response = requests.get(url)

    # Check the status code
    if response.status_code == 200:
        print(f"URL {url} returned status code 200 - Success!")
        urls_with_200_status.append((hotel_id, check_in, check_out))

# Get the current working directory
current_directory = os.getcwd()

# Construct the CSV file path in the root directory
csv_file_path = os.path.join(current_directory, "successful_urls.csv")

# Write the successful URLs to the CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Hotel ID", "Check-in", "Check-out"])
    writer.writerows(urls_with_200_status)

print(f"CSV file '{csv_file_path}' created successfully.")
