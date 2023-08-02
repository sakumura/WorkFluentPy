from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def login_cybozu(subdomain, username, password, headless=False):
    # Create a new instance of the Chrome driver
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    # Generate the cybozu login page URL
    url = f"https://{subdomain}.cybozu.com/login?"

    # Go to the cybozu login page
    driver.get(url)

    # Find the username field and enter the username
    username_field = driver.find_element_by_id("username-:0-text")
    username_field.send_keys(username)

    # Find the password field and enter the password
    password_field = driver.find_element_by_id("password-:1-text")
    password_field.send_keys(password)

    # Find the login button and click it
    login_button = driver.find_element_by_class_name("login-button")
    login_button.click()

    # Wait for the page to load (optional, depends on the page)
    driver.implicitly_wait(10) 

    return driver

if __name__ == "__main__":
    # Cofigure the subdomain, username and password
    subdomain = "subdomain"
    username = "username"
    password = "password"

    # Login to cybozu
    driver = login_cybozu(subdomain, username, password, headless=True)

    # Do something with the logged in page
    # ...

    # Close the browser
    driver.close()