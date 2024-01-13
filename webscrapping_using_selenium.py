import json
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service

def scrape_data():
    # Specify the path to your chromedriver executable
    executable_path = r'C:\Users\Max\Documents\GitHub\Fornova Support\chromedriver.exe'

    # Create a Chrome service instance
    service = Service(executable_path)

    # Create a Chrome driver instance with the service
    driver = Chrome(service=service)

    # Navigate to the desired URL
    driver.get('https://www.qantas.com/hotels/properties/18482?adults=2&checkIn=2023-10-30&checkOut=2023-10-31&children=0&infants=0&location=London%2C%20England%2C%20United%20Kingdom&page=1&payWith=cash&searchType=list&sortBy=popularity')

    # Create BeautifulSoup object using the HTML source from Selenium
    soup = BeautifulSoup(driver.page_source, "lxml")

    # Find all divs with class "css-du5wmh-Box" under the main div
    target_divs = soup.find_all("div", class_="css-du5wmh-Box")

    # Initialize a dictionary to store rate information
    rates = {}

    # Loop through each target_div
    for target_div in target_divs:
        # Find the h3 elements with the specified class inside each target_div
        h3_elements = target_div.find_all("h3", class_="css-19vc6se-Heading-Heading-Text e13es6xl3")

        # Loop through each h3_element
        for h3_element in h3_elements:
            rate_name = h3_element.text
            room_info = {"Room Name": rate_name}

            # Find the div with the specified class under h3_element
            nested_div = h3_element.find_parent("div", class_="css-o4ex2l-Box-Flex e1yh5p90")

            # Find the div with class="css-2r3ilu-Box e1yh5p92" under nested_div
            specific_div = nested_div.find("div", class_="css-2r3ilu-Box e1yh5p92")

            # Find all divs with specific classes under specific_div
            sub_divs = specific_div.find_all("div", class_=["css-wcj7p9-Box", "css-wcj7p9-Box", "css-1sokv5k-Box e1m6xhuh0"])

            # Loop through each sub_div and extract information
            for index, sub_div in enumerate(sub_divs):
                # Extract information and add it to room_info with a unique key
                class_name = f"Room Details {index + 1}"

                try:
                    # Extract additional information from sub_div
                    rate_name_elements = sub_div.find_all("div", class_="css-5ct7le-Box")  
                    no_of_guests_elements = sub_div.find_all("span", class_="css-zapqsm-Text")  
                    cancel_policy_elements = sub_div.find_all("button", class_="css-12hhnd3")
                    price_elements = sub_div.find_all("span", class_="css-1bjudru")  
                    top_deal_elements = sub_div.find_all("span", class_="css-1jr3e3z-Text-BadgeText")  
                    currency_elements = sub_div.find_all("div", class_="css-1dvtiwl-Box e1m6xhuh0")  
                    amenities_elements = sub_div.find_all("h3", class_="css-10yvquw-Heading-Heading-Text e13es6xl3")  

                    # Process the extracted information and add it to room_info
                    room_info[class_name] = {
                        "Rate Name": rate_name_elements[0].text.strip() if rate_name_elements else "N/A",
                        "No of Guests": no_of_guests_elements[0].text.strip() if no_of_guests_elements else "N/A",
                        "Cancel Policy": cancel_policy_elements[0].text.strip() if cancel_policy_elements else "N/A",
                        "Price": price_elements[0].text.strip() if price_elements else "N/A",
                        "Top Deal": 1 if top_deal_elements else 0,  
                        "Currency": currency_elements[0].text.strip() if currency_elements else "N/A",
                        "Amenities": amenities_elements[0].text.strip() if amenities_elements else "N/A",
                    }
                except Exception as e:
                    print(f"Error processing {class_name}: {e}")

            # Add the room_info dictionary to the rates dictionary
            rates[rate_name] = room_info

    # Wrap the rates dictionary within a "rates" key
    rates_data = {"rates": rates}

    # Convert rates_data to JSON format and print
    json_result = json.dumps(rates_data, indent=2)
    print(json_result)

    # Close the browser
    driver.quit()

# Call the function to execute the scraping
scrape_data()
