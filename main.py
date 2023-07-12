from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard
import time
import sys

DELAY = 0.2

def main(delay):
    driver = webdriver.Chrome()
    driver.get("https://monkeytype.com/")

    keyboard.wait("backspace")
    time.sleep(1)

    typer(driver, delay)

def typer(driver, delay):
    while True:
        try:
            if keyboard.is_pressed("backspace"):
                break
            if keyboard.is_pressed("escape"):
                break

            active_word_div = driver.find_element(By.CSS_SELECTOR, "div.word.active")
            letter_elements = active_word_div.find_elements(By.TAG_NAME, "letter")

            if not letter_elements:
                raise Exception("No letters found")

            letter_texts = [letter.text for letter in letter_elements]

            for letter_text in letter_texts:
                time.sleep(delay)
                driver.find_element(By.CSS_SELECTOR, "input").send_keys(letter_text)

            time.sleep(delay)
            driver.find_element(By.CSS_SELECTOR, "input").send_keys(" ")
        except:
            pass
    
    keyboard.wait("escape")

if __name__ == "__main__":
    try:
        DELAY = float(sys.argv[1])
    except:
        pass

    print(f"Delay is set to {DELAY}")

    main(DELAY)
