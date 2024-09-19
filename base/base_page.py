import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    URL = None

    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.wait = WebDriverWait(browser, 20, poll_frequency=0.5)

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

    @allure.step("Check visibility of all elements")
    def check_all_visibility_(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    @allure.step("Click a button")
    def click_button(self, locator):
        self.find(locator).click()

    @allure.step("Field a form with some data")
    def field_form(self, locator, data):
        self.find(locator).send_keys(data)

    @allure.step("Get text and return it")
    def get_text(self, locator):
        return self.find(locator).text

    @allure.step("Check URL")
    def check_url_is_(self, url):
        return self.browser.current_url == url

    @allure.step("Check Page Title")
    def check_page_title_is_(self, title):
        return self.browser.title == title
