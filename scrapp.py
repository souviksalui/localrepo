import bs4  # BeautifulSoup
import requests
from urllib3.exceptions import InsecureRequestWarning

# Suppress InsecureRequestWarning
Warnings.filterwarnings("ignore", category=InsecureRequestWarning) #Warnings.simplefilter('ignore', InsecureRequestWarning)

URL = "https://www.amazon.in/s?k=laptops&crid=19RYX729JP3B6&sprefix=laptops%2Caps%2C247&ref=nb_sb_noss_2"

# Headers for request
HEADERS = ({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36', 
    'Accept-Language': 'en-US, en;q=0.5'
})

# HTTP Request
webpage = requests.get(URL, headers=HEADERS, verify=False) #, verify=False

# Soup Object containing all data
soup = bs4.BeautifulSoup(webpage.content, "html.parser")

# Fetch links as List of Tag Objects (these are product links)
links = soup.find_all("a", attrs={'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})

# Loop through all found links and extract the product name and link
for link in links:
    href = link.get('href')
    product_name = link.get('title')  # 'title' attribute usually contains the product name
    
    if href and product_name:  # Ensure the link and product name are present
        # Construct the full URL for the product
        full_url = f"https://www.amazon.in{href}"
        print(f"Product Name: {product_name} - URL: {full_url}")

# Solutions to remove the warning
# Enable SSL certificate verification (recommended):
# The best practice is to enable SSL certificate verification by either removing verify=False or setting verify=True (which is the default behavior). This ensures that the connection is securely verified, and you won't see the warning.

# Update your code like this:

# python
# Copy code
# # HTTP Request with certificate verification
# webpage = requests.get(URL, headers=HEADERS)
# By not setting verify=False, the SSL certificate of the server will be checked, and the warning should be gone.

# Suppress the warning (not recommended):
# If you don't want to see the warning but still want to disable SSL verification, you can suppress the warning by using Python's warnings module. However, this is not a secure solution and should only be used if you absolutely need to bypass SSL verification.

# Here's how you can suppress the warning:

# python
# Copy code
# import requests
# import warnings
# from urllib3.exceptions import InsecureRequestWarning

# # Suppress InsecureRequestWarning
# warnings.simplefilter('ignore', InsecureRequestWarning)

# # HTTP Request with certificate verification disabled
# webpage = requests.get(URL, headers=HEADERS, verify=False)
# This will suppress the warning, but keep in mind that it's still not a secure practice to disable SSL verification.

# Conclusion:
# The recommended approach is to remove verify=False and let requests verify the SSL certificate. This will ensure you're securely connecting to Amazon's servers and avoid the warning.
# Only suppress the warning if you are fully aware of the potential security risks involved in bypassing SSL verification.



