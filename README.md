# Dell Service Tag Information Retrieval
This Python script utilizes Selenium to retrieve information about Dell products using their service tags.

## 1. Import Requirements

The script requires the following Python libraries to be installed:

- Python Version 3
- Selenium
- `webdriver` for the specific browser (e.g., `geckodriver` for Firefox)

You can install these dependencies using pip:
```
pip install selenium
```
Make sure to have the appropriate web driver executable for your browser installed and added to your system's PATH.

## 2. How to Input - Save all Dell Service Tags into File `service-tag.txt`

To use this script, follow these steps:
1. Save all Dell Service Tags into a file named `service-tag.txt`, with each service tag on a separate line.
2. Ensure the `service-tag.txt` file is located in the same directory as the Python script.

## 3. Result - User Will Get Model, Purchase Date, and Expire Date as CSV Format

After running the script, the user will get a CSV file named `product-detail.csv` containing the following information for each service tag:

- Service Tag
- Product Name
- Purchase Date
- Expire Date

The script will fetch this information from Dell's support website and save it into the CSV file.
```
serviceTag, productName, purchaseDate, expireDate
ABC123, Dell Laptop, 05/19/2023, 05/26/2026
DEF456, Dell Printer, 05/19/2023, 05/26/2026
GHI789, Dell Monitor, 05/19/2023, 05/26/2026
```
