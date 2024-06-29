import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", autouse=True)
def browser(request):
    options_chrome = Options()
    options_chrome.add_argument("--window-size=1920,1080")
    options_chrome.add_argument("--headless")
    options_chrome.add_argument("--no-sandbox")
    options_chrome.add_argument("--disable-dev-shm-usage")
    browser = webdriver.Chrome(
        options=options_chrome)

    failed_before = request.session.testsfailed

    yield browser

    if request.session.testsfailed != failed_before:
        attach = browser.get_screenshot_as_png()
        from datetime import datetime
        allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    browser.quit()
