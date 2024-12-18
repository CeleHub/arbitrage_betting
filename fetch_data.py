import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Fetch odds from a static website using requests + BeautifulSoup
def fetch_odds_from_static_site(url, class_name):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        odds = [float(tag.text) for tag in soup.find_all("span", class_=class_name)]  # Adjust tag/class name
        return odds
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return []

# Fetch odds from a dynamic website using Selenium
def fetch_odds_from_dynamic_site(url, class_name):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)

    try:
        odds_elements = driver.find_elements(By.CLASS_NAME, class_name)
        odds = [float(element.text) for element in odds_elements]
    except Exception as e:
        print(f"Error fetching odds: {e}")
        odds = []
    finally:
        driver.quit()

    return odds

# Combine odds from multiple sources
def fetch_odds():
    static_site_url = "https://sportybet.com/static"  # Replace with actual URL
    dynamic_site_url = "https://1xbet.com/dynamic"  # Replace with actual URL
    class_name = "odds-class"  # Replace with the actual class name

    # Fetch from static site
    odds_static = fetch_odds_from_static_site(static_site_url, class_name)
    print("Static Site Odds:", odds_static)

    # Fetch from dynamic site
    odds_dynamic = fetch_odds_from_dynamic_site(dynamic_site_url, class_name)
    print("Dynamic Site Odds:", odds_dynamic)

    # Combine results
    return odds_static + odds_dynamic
