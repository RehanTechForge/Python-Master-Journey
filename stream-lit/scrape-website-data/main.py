# import streamlit as st
# import google.generativeai as genai
# import requests
# from bs4 import BeautifulSoup

# # Google Gemini API Key
# GEMINI_API_KEY = "AIzaSyBI2xchvI-1dDq5P6ZR34LDGIDYD1Apm2Q"  # 🔹 Replace with your API Key
# genai.configure(api_key=GEMINI_API_KEY)

# # Function to Scrape the Main Page & Extract Product Links
# def scrape_page(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, "html.parser")

#         # Extract all product page links
#         product_links = []
#         for a_tag in soup.find_all("a", href=True):
#             link = a_tag["href"]
#             if "product" in link:  # 🔹 Filtering relevant product links
#                 full_link = requests.compat.urljoin(url, link)
#                 product_links.append(full_link)

#         return response.text, product_links  # 🔹 Return HTML + extracted links
#     else:
#         return None, []

# # Function to Scrape Individual Product Pages
# def scrape_product_pages(links):
#     product_html_data = []
#     for link in links:
#         response = requests.get(link)
#         if response.status_code == 200:
#             product_html_data.append(response.text)
    
#     return product_html_data

# # Function to Extract Product Info Using Gemini AI
# def extract_products(html_content, product_pages_html):
#     model = genai.GenerativeModel("gemini-1.5-flash")  # 🔹 Using "gemini-1.5-flash"

#     # Send main page HTML & product pages HTML to Gemini
#     prompt = f"""
#     1. Extract all product details (name, price, description) from the following main HTML:
#     {html_content}

#     2. Now, extract more product details from these product pages:
#     {product_pages_html}
#     """

#     response = model.generate_content(prompt)
#     return response.text if response else "No products found"

# # Streamlit UI
# st.title("Advanced Web Scraper with Gemini AI")

# url = st.text_input("Enter URL to Scrape", "https://webscraper.io/test-sites/e-commerce/static")

# if st.button("Scrape and Extract Products"):
#     st.info("Scraping the page...")
#     main_html, product_links = scrape_page(url)

#     if main_html:
#         st.success(f"Page Scraped Successfully! Found {len(product_links)} product links.")

#         # Scrape the extracted product links
#         st.info("Scraping Product Pages...")
#         product_pages_html = scrape_product_pages(product_links)
        
#         st.info("Extracting Products using Gemini AI...")
#         extracted_products = extract_products(main_html, product_pages_html)

#         st.subheader("Extracted Products")
#         st.text_area("Product Details", extracted_products, height=300)
#     else:
#         st.error("Failed to scrape the page. Please check the URL.")
import streamlit as st
import google.generativeai as genai
import requests
from bs4 import BeautifulSoup

# Configure Google Gemini API
GEMINI_API_KEY = ""  # 🔹 Replace with your actual API Key
genai.configure(api_key=GEMINI_API_KEY)

# Function to Scrape Main Page & Extract Product Links
def scrape_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        product_links = [requests.compat.urljoin(url, a["href"]) for a in soup.find_all("a", href=True) if "product" in a["href"]]
        return response.text, product_links  # 🔹 Return HTML & product links
    return None, []

# Function to Scrape Individual Product Pages
def scrape_product_pages(links):
    return [requests.get(link).text for link in links if requests.get(link).status_code == 200]

# Function to Extract Product Info Using Gemini AI
def extract_products(main_html, product_pages_html):
    model = genai.GenerativeModel("gemini-1.5-flash")  # 🔹 Using Gemini AI Model
    prompt = f"""
    Extract product details (name, price, description) from the following main HTML:
    {main_html}
    
    Now, extract more product details from these product pages:
    {product_pages_html}
    """
    response = model.generate_content(prompt)
    return response.text if response else "No products found"

# Streamlit UI Setup
st.set_page_config(page_title="AI-Powered Web Scraper", layout="wide")
st.title("🔍 AI-Powered Web Scraper for E-Commerce Sites")
st.markdown("Enter a URL below to scrape product information using Google Gemini AI.")

# User Input URL
url = st.text_input("Enter Website URL", "https://webscraper.io/test-sites/e-commerce/static")

if st.button("🔎 Scrape and Extract Products"):
    with st.spinner("Scraping the main page..."):
        main_html, product_links = scrape_page(url)
    
    if main_html:
        st.success(f"✅ Page scraped successfully! Found {len(product_links)} product links.")
        
        with st.spinner("Scraping product pages..."):
            product_pages_html = scrape_product_pages(product_links)
        
        with st.spinner("Using Gemini AI to extract product details..."):
            extracted_products = extract_products(main_html, product_pages_html)
        
        st.subheader("🛒 Extracted Product Details")
        st.text_area("Product Information", extracted_products, height=300)
    else:
        st.error("❌ Failed to scrape the page. Please check the URL.")