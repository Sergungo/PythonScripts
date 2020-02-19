# connect python with webbrowser-chrome
from selenium import webdriver


# from selenium.webdriver.common.keys import Keys
# import pyautogui as pag


def main():
    # url of LinkedIn
    url = "https://www.linkedin.com/login"
    # url of LinkedIn network page
    # network_url = "http://linkedin.com/mynetwork/"
    # path to browser web driver

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=options,
                              executable_path='F:\\LOADED\\chromedriver_win32\\chromedriver.exe')
    driver.get(url)

    login(driver)

    print('Done')
    print(driver.current_url)

    driver.get('https://www.linkedin.com/in/golenkos/')
    print(driver.current_url)


def login(driver):
    # Getting the login element
    username = driver.find_element_by_id("username")
    # Sending the keys for username
    username.send_keys("")
    # Getting the password element
    password = driver.find_element_by_id("password")
    # Sending the keys for password
    password.send_keys("")
    # Getting the tag for submit button
    driver.find_element_by_css_selector("div.login__form_action_container").click()


# Driver's code
if __name__ == "__main__":
    main()
