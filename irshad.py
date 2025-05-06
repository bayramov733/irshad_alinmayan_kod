import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# Define URL (Iphone listings)
url = "https://irshad.az/mehsullar?q=iphone"

# Request page
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Prepare Excel
wb = Workbook()
ws = wb.active
ws.title = "Iphone"
ws.append(["name", "details", "colors"])

# Scrape listings
phone = soup.find_all("div", class_="product")

for iphone in phone:
    name_tag =iphone.find("div", class_="product__name")
    details_tag =iphone.find("div", class_="product__details")
    colors_tag =iphone.find("div", class_="product__colors")
 
    

    name = name_tag.get_text(strip=True) if name_tag else ""
    details = details_tag.get_text(strip=True) if details_tag else ""    
    colors = colors_tag.get_text(strip=True) if colors_tag else ""    
  

    if name and details and colors:
        ws.append([name, details,colors])

# Save Excel
wb.save("Iphone_listings.xlsx")
print("Done: Iphone_listings.xlsx")
