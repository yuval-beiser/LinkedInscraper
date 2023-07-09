from random import randint
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

def send_intro_lec():
    print("inside")
    # driver.get(url)
    # time.sleep(2)

    all_buttons = driver.find_elements_by_tag_name("button")
    connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]

    txt = """
היי מה שלומך? 
אנחנו מגייסים מרצה לקורס פיתוח/ סייבר לבני נוער.
המשרה יכולה להיות גם מלאה וגם חלקית (פעמיים בשבוע בערבים ל-3 שעות)

מתאים לחבר׳ה טכנולוגים שאוהבים הדרכה ומחפשים עוד איזה חוויה להרצות לנוער בנושאים ממש מגניבים

צריך ידע ברמת תיכון ב:
JS
C#
Python
Wireshark

אם רלוונטי אשמח שנדבר
            """

    i = 1
    print("I have {} buttons to send here ".format(len(connect_buttons)))
    for btn in connect_buttons:
        print(i)
        i += 1
        sleep(randint(2, 10))
        driver.execute_script("arguments[0].click();", btn)
        time.sleep(2)
        add_note = driver.find_element_by_xpath("//button[@aria-label='Add a note']")
        driver.execute_script("arguments[0].click();", add_note)

        text_area = driver.find_element_by_id("custom-message")
        text_area.send_keys(txt)

        send = driver.find_element_by_xpath("//button[@aria-label='Send now']")
        driver.execute_script("arguments[0].click();", send)

        # close = driver.find_element_by_xpath("//button[@aria-label='Dismiss']")
        # driver.execute_script("arguments[0].click();", close)

        time.sleep(2)
def loop_throw_pages_lec(page_number):
    while True:
        print("page number "+str(page_number))
        send_intro_lec()
        print("finish send intro")
        time.sleep(2)
        button_next_page = driver.find_elements_by_xpath("//button[@aria-label='Page "+str(page_number+1)+"']")
        time.sleep(2)
        try:
            button_next_page[0].click()
            page_number+=1
        except:
            print("Please help me move to next page")
        time.sleep(5)

email = "admin@8200academy.com"
password= "YuvalDean123!"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.linkedin.com')
time.sleep(2)

username = driver.find_element_by_xpath("//input[@name='session_key']")
password_driver = driver.find_element_by_xpath("//input[@name='session_password']")

username.send_keys(email)
password_driver.send_keys(password)

submit = driver.find_element_by_xpath("//button[@type='submit']").click()

time.sleep(2)

developer = "https://www.linkedin.com/search/results/people/?keywords=fullstack%20developer&origin=FACETED_SEARCH&page=3&pastCompany=%5B%2217877948%22%5D&sid=jyd"
driver.get(developer)
time.sleep(2)
loop_throw_pages_lec(1)