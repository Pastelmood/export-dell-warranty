from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime
import csv
import time

DRIVER = webdriver.Firefox()

def format_date(product_date: str):
    # Convert string to datetime object
    date_obj = datetime.strptime(product_date, '%d %b %Y')
    # Format datetime object to desired format
    formatted_date = date_obj.strftime('%m/%d/%Y')
    return formatted_date

def read_service_tag_from_file(file_path="service-tag.txt"):
    data_list = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                data_list.append(line.strip())  # strip() removes leading/trailing whitespaces and newline characters
    except FileNotFoundError:
        print("File not found.")
    return data_list

def get_product_detail(service_tag: str):
    # Open web dell support
    global DRIVER
    driver = DRIVER

    # Open dell support
    driver.get("https://www.dell.com/support/home/en-us")

    # Search box button element
    while True:
        try:
            time.sleep(1.5)
            print("Step 1: Enter Service Tag ... " + service_tag)
            driver.find_element(By.ID, "mh-search-input")
            break
        except:
            pass

    elem_search_box = driver.find_element(By.ID, "mh-search-input")
    elem_search_box.send_keys(service_tag)
    time.sleep(1)
    elem_search_box.send_keys(Keys.RETURN)

    # Search Review Service link
    check_score = 0
    while True:
        try:
            time.sleep(1.5)
            print("Step 2: Finding product ... " + service_tag)
            driver.find_element(By.ID, "viewDetailsWarranty")
            break
        except:
            check_score = check_score + 1

        if check_score == 20:
            print("Step 2: Product not found ... " + service_tag)
            return service_tag + ", NOT_FOUND, NOT_FOUND, NOT_FOUND"

    elem_review_service = driver.find_element(By.ID, "viewDetailsWarranty")
    time.sleep(1)
    elem_review_service.click()

    # Warranty detail

    # Check warranty header element
    while True:
        try:
            time.sleep(1.5)
            driver.find_element(By.ID, "warrantyDetailsHeader")
            break
        except:
            pass

    # Product name
    try:
        elem_product_name = driver.find_element(By.TAG_NAME, "h1")
        result_product_name = elem_product_name.text
    except:
        result_product_name = "NOT_FOUND"

    # Purchase date
    try:
        elem_purchase_date = driver.find_element(By.ID, "dsk-purchaseDt")
        result_purchase_date = format_date(elem_purchase_date.text)
    except:
        result_purchase_date = "NOT_FOUND"

    # Expire date
    try:
        elem_expire_date = driver.find_element(By.ID, "dsk-expirationDt")
        result_expire_date = format_date(elem_expire_date.text)
    except:
        result_expire_date = "NOT_FOUND"

    result = f"{service_tag}, {result_product_name}, {result_purchase_date}, {result_expire_date}"

    print(service_tag + " ... Done!")

    return result

def save_csv(data_list, file_path="product-detail.csv"):
    header = ["serviceTag", "productName", "purchaseDate", "expireDate"]
    try:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            for entry in data_list:
                entry_parts = entry.split(", ")
                writer.writerow(entry_parts)
        print("Data exported successfully to", file_path)
    except IOError:
        print("Error writing to file.")


if __name__ == "__main__":
    print("Start retrieve Dell Computer Detail from Service Tag.")

    the_service_tags = read_service_tag_from_file()

    result = []

    for service_tag in the_service_tags:
        result.append(get_product_detail(service_tag))

    save_csv(result)

    DRIVER.close()
