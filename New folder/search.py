from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Define global XPath variables
SEARCHBOX_XPATH = '/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input'
SEARCH_BUTTON_XPATH = "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/button"

# Define global search query
SEARCH_QUERY = "selenium and python automation"

def perform_youtube_search(search_query):
    try:
        # Initialize the Chrome WebDriver
        driver = webdriver.Chrome()

        # Open the YouTube homepage
        driver.get("https://www.youtube.com/")

        # Locate the search box element using the global XPath variable
        searchbox = driver.find_element_by_xpath(SEARCHBOX_XPATH)

        # Input the search query
        searchbox.send_keys(search_query)

        # Locate the search button element using the global XPath variable
        search_button = driver.find_element_by_xpath(SEARCH_BUTTON_XPATH)

        # Click the search button
        search_button.click()

        # import pdb; pdb.set_trace() # To stop the program

    except NoSuchElementException as e:
        print("Element not found:", e)not

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the WebDriver and clean up resources
        if 'driver' in locals():
            driver.quit()

# Comment and run this section to test the script
if __name__ == "__main__":
    perform_youtube_search(SEARCH_QUERY)
