from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
import pickle

def login_twitter(driver, username, password, email):
    driver.get("https://x.com/login")
    
    username_input = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element(By.XPATH, "//*[@id=\"layers\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input")
    )
    username_input.send_keys(username)
    
    next_button = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element(By.XPATH, "//*[@id=\"layers\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]")
    )
    next_button.click()

    try:
        recovery_email = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element(By.XPATH, "//*[@id=\"layers\"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
        )
        recovery_email.send_keys(email)

        next_button = WebDriverWait(driver, 10).until(
            lambda driver : driver.find_element(By.XPATH, "//*[@id=\"layers\"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button")
        )
        next_button.click()

    except:
        pass

    password_input = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element(By.XPATH, "//*[@id=\"layers\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
    )
    password_input.send_keys(password)

    next_button = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element(By.XPATH, "//*[@id=\"layers\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button")
    )
    next_button.click()

    # with open("cookies.pkl", "wb") as f:
    #     pickle.dump(driver.get_cookies(), f)

def get_tweets(username, password, email, user, count = 100):
    chrome_options = Options()
    chrome_options.add_argument("--user-data-dir=C:/Users/theat/AppData/Local/Google/Chrome/User Data")
    driver = webdriver.Chrome(options=chrome_options)
    # with open("cookies.pkl", "rb") as f:
    #     cookies = pickle.load(f)

    # if cookies is None:
    # try:
    #     login_twitter(driver, username, password, email)
    #     # with open("cookies.pkl", "rb") as f:
    #     #     cookies = pickle.load(f)
    # except:
    #     print("Login failed")
    #     driver.quit()
    #     return None
    
    driver.get(f"https://x.com/{user}")
    time.sleep(20)

    # last_height = driver.execute_script("return document.documentElement.scrollHeight")
    # while True:
    #         driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    #         WebDriverWait(driver, 7).until(
    #             lambda driver: driver.execute_script("return document.documentElement.scrollHeight") > last_height
    #         )
    #         last_height = driver.execute_script("return document.documentElement.scrollHeight")
    #         if last_height >= 5000:
    #             break

    tweet_elements = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div/div/div/article/div/div/div[2]/div[2]/div[2]/div")
    )
    print(tweet_elements.text)

get_tweets("pewpewnowdie", "madeofgreat", "kshitijtyagi281@gmail.com", "pewpewnowdie")