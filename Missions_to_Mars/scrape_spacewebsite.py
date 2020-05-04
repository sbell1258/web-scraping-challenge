from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit website to screen scrap
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the latest news
    news_title = soup.find('div', id='news_title')

    # Get the paragraph test
    news_p = soup.find('strong', id='news_p')


    url1 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    # Find the src for the Mars image
    relative_image_path = soup.find_all('img')[2]["src"]
    featured_image_url = url1 + relative_image_path

    # Store data in a dictionary
    space_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return space_data