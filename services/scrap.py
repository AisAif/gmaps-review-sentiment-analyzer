from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time

def run(url):
    driver = webdriver.Chrome()

    driver.get(url)

    driver.implicitly_wait(60)

    button = driver.find_elements(by=By.CLASS_NAME, value="hh2c6 ")[1]
    ActionChains(driver).move_to_element(button).click(button).perform()

    # first scroll
    time.sleep(5)
    topElement = driver.find_element(By.CLASS_NAME, "m6QErb.tLjsW")
    scroll_origin = ScrollOrigin.from_element(topElement)
    ActionChains(driver).scroll_from_origin(scroll_origin, 0, 1000).perform()


    # looping scroll
    while True:
        lastReview = driver.find_elements(By.CLASS_NAME, "wiI7pd")[-1]
        scroll_origin = ScrollOrigin.from_element(lastReview)
        time.sleep(2)
        ActionChains(driver).scroll_from_origin(scroll_origin, 0, 1000).perform()
        time.sleep(2)
        if lastReview == driver.find_elements(By.CLASS_NAME, "wiI7pd")[-1]:
            break

    allReviews = []

    reviews = driver.find_elements(by=By.CLASS_NAME, value="wiI7pd")
    with open("assets/reviews.csv", "w", encoding="utf-8") as f:
        for review in reviews:
            text = review.text.replace("\n", "")
            f.write(f"'{text}'\n")