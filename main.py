

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver import ActionChains

class CarLearn:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.login_url = "https://ac.carslearning.ca/public/login"
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def login(self):
        self.driver.get("https://ac.carslearning.ca/public/login")
        print(self.driver.title)
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(1024, 768)
        time.sleep(5)
        input_id = self.driver.find_element("id", "mat-input-0")
        input_password = self.driver.find_element("id", "mat-input-1")
        input_id.send_keys("") #username
        input_password.send_keys("") #pw
        login_but = self.driver.find_element("css selector","button[class='mat-raised-button mat-button-base mat-primary']")
        login_but.click()
        time.sleep(5)
        input_2step = self.driver.find_element("id", "mat-input-2")
        input_2step.send_keys("hong kong")
        # answer_but = self.driver.find_element("css selector",
        #                                      "button[class='mat-raised-button mat-button-base mat-primary']")
        # self.action.move_to_element(answer_but).click(answer_but).perform()
        # hand click
        print("click answer button in 30 seconds")
        time.sleep(30)
        start_course_but = self.driver.find_element("css selector",
                                             "button[class='mat-raised-button mat-button-base mat-primary']")
        start_course_but.click()
        time.sleep(5)


    def syllabus(self):
        syllabus_herf = self.driver.find_element("css selector",
                                                 "a[class='no-decoration mr10']")
        syllabus_herf.click()
        time.sleep(10)

    def course(self):
        course_href  = self.driver.find_element("css selector",
                                                 "a[class='no-decoration mr10']")
        course_href.click()
        time.sleep(10)


    def get_progressbar(self):
        iframe = self.driver.find_element("tag name",
                                             "iframe")
        self.driver.switch_to.frame(iframe)
        progress_bar = self.driver.find_element("css selector",
                                             "div[class='progressbar__label']")
        progress=progress_bar.text
        progress_array = progress.split("/")
        all = int(progress_array[1])
        current = int(progress_array[0])
        print("total:" + progress_array[1])
        while current != all:
            self.wait_and_click(current)
            # iframe = self.driver.find_element("tag name",
            #                                   "iframe")
            # self.driver.switch_to.frame(iframe)
            progress_bar = self.driver.find_element("css selector",
                                                    "div[class='progressbar__label']")
            progress = progress_bar.text
            progress_array = progress.split("/")
            all = int(progress_array[1])
            current = int(progress_array[0])
            print("total:" + progress_array[1])




    def wait_and_click(self, current: int):
        print("current:" + str(current))
        current_wait_time = self.driver.find_element("css selector",
                                             "div[class='progressbar__label progressbar__label_type_time']")
        current_wait_time_text = current_wait_time.text
        current_wait_time_text_array = current_wait_time_text.split('/')
        current_wait_time = current_wait_time_text_array[1]
        current_wait_time_array = current_wait_time.split(':')
        minutes = int(current_wait_time_array[0])
        seconds = int(current_wait_time_array[1])
        wait_seconds = minutes*60 + seconds
        print("wait_seconds:" + str(wait_seconds))
        time.sleep(wait_seconds)
        next_but = self.driver.find_element("css selector",
                                             "button[class='universal-control-panel__button universal-control-panel__button_next universal-control-panel__button_right-arrow']")
        try:
            next_but.click()
        except:
            try:
                print("no next button")
                continue_but = self.driver.find_element("css selector",
                                             "button[class='universal-control-panel__button universal-control-panel__button_next universal-control-panel__button_right-arrow']")
                continue_but.click()
            except:
                print("Error occur. pls Diy!!!")
                val = input("enter after input")

        time.sleep(5)



if __name__ == "__main__":
    carlearn = CarLearn()
    carlearn.login()
    carlearn.syllabus()
    carlearn.get_progressbar()
    # mdLand.get_searchbar()
    # # mdLand.try_select_for_patient()
    # mdLand.get_search_result()
    # mdLand.display_patient_list()
