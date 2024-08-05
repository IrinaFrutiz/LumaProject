import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    URL = None

    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.wait = WebDriverWait(browser, 20, poll_frequency=0.5)

    @allure.step("Open Login page")
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
        return self.browser.find_elements(locator)

    @allure.step("Click a button")
    def click_button(self, locator):
        self.find(locator).click()

    @allure.step("Field a form with some data")
    def field_form(self, locator, data):
        self.find(locator).send_keys(data)

    @allure.step("Get text and return it")
    def get_text(self, locator):
        return self.find(locator).text

    @allure.step("Get URL")
    def get_url(self):
        return self.browser.current_url

    @allure.step("Check URL")
    def check_url_(self, url):
        assert self.browser.current_url == url, \
            f"Current URL {self.browser.current_url} is not equal {url}"

    @allure.step("Check URL")
    def check_url_is_(self, url):
        return self.browser.current_url == url
