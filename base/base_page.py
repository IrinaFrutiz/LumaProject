import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    URL = None

    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.wait = WebDriverWait(browser, 20, poll_frequency=0.5)
        self.action = ActionChains(browser)

    @allure.step("Open page")
    def open(self):
        if self.URL:
            self.browser.get(self.URL)
        else:
            raise NotImplementedError

    @allure.step("Find a locator")
    def find(self, locator):
        return self.browser.find_element(*locator)

    @allure.step("Find locators")
    def find_all(self, locator):
        return self.browser.find_elements(*locator)

    @allure.step("Check visibility of the element")
    def check_element_visibility_(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Check not visibility of the element")
    def check_element_not_visible_(self, locator):
        return self.wait.until_not(EC.visibility_of_element_located(locator))

    @allure.step("Check visibility of all elements")
    def check_all_visibility_(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def check_element_presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Click a button")
    def click_button(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Click all the buttons")
    def click_all_buttons(self, locator):
        for button in self.find_all(locator):
            button.click()

    @allure.step("Choose random element from elements")
    def click_to_random_element(self, locator):
        import random
        random.choice(self.find_all(locator)).click()

    @allure.step("Field a form with some data")
    def field_form(self, locator, data):
        self.find(locator).clear()
        self.find(locator).send_keys(data)

    @allure.step("Get text and return it")
    def get_text(self, locator):
        return self.check_element_visibility_(locator).text

    @allure.step("Get list of text and return it")
    def get_all_text(self, locator):
        return [webelement.text for webelement in self.find_all(locator)]

    @allure.step("Check URL")
    def check_url_is_(self, url):
        return self.browser.current_url == url

    @allure.step("Check Success Message Text is Correct")
    def check_success_message_is_(self, locator, text):
        return self.get_text(locator) == text

    @allure.step("Check Page Title")
    def check_page_title_is_(self, title):
        return self.browser.title == title

    @allure.step("Check the page is reload")
    def check_page_loaded(self):
        self.wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

    @allure.step("Hover Over Element")
    def hover(self, locator):
        self.action.move_to_element(self.check_element_visibility_(locator)).perform()

    @allure.step("Mouse over an element")
    def mouse_over_element_(self, locator):
        achains = ActionChains(self.browser)
        return achains.move_to_element(self.find(locator)).perform()
