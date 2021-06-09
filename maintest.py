# http://demos.telerik.com/kendo-ui/dragdrop/index
# http://demos.telerik.com/kendo-ui/upload/initialfiles
import datetime
import os
import socket
import sys
import time
import unittest

import pyautogui
import pygetwindow as gw
from loguru import logger
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import \
    visibility_of_element_located as visibility
from selenium.webdriver.support.ui import WebDriverWait as waiter

from build_log import StreamToLogger, build_logger


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        log_path = os.getcwd()
        setup_log(log_path)
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        options.add_experimental_option(
            "prefs",
            {
                'credentials_enable_service': False,
                'profile': {'password_manager_enabled': False},
                # "download.default_directory": download_path,
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True,
                "plugins.always_open_pdf_externally": True,
            },
        )
        self.driver = webdriver.Chrome(options=options, executable_path=r'.\chromedriver.exe')
        # return super().setUp()

    def test_my_work1(self):
        # move small circle into big circle
        test_page = 'http://demos.telerik.com/kendo-ui/dragdrop/index'
        logger.info(f'Navigate to test page {test_page}')
        self.driver.get(test_page)
        xpath = '//*[@class ="kd-title" and contains(text(),"Basic usage")]'
        wait_for_element_visible(self.driver, xpath, By.XPATH, 15)

        # find element
        xpath_drag = '//*[@id="draggable"]'
        xpath_drop = '//*[@id="droptarget"]'
        source1 = self.driver.find_element_by_xpath(xpath_drag)
        target1 = self.driver.find_element_by_xpath(xpath_drop)
        actions2 = ActionChains(self.driver)
        actions2.drag_and_drop(source1, target1).perform()

        # assert result text
        text = 'You did great!'
        result = self.driver.find_element_by_xpath(xpath_drop)
        self.assertEqual(result.text, text)

    def test_my_work2(self):
        # upload file
        test_page = 'http://demos.telerik.com/kendo-ui/upload/initialfiles'
        logger.info(f'Navigate to test page {test_page}')
        self.driver.get(test_page)
        xpath = '//*[@class ="kd-title" and contains(text(),"Initial Files")]'
        wait_for_element_visible(self.driver, xpath, By.XPATH, 15)

        # click select files
        xpath = '//*[@id="example"]/div/div/div/div/div'
        waiter(self.driver, 60).until(visibility((By.XPATH, xpath))).click()
        wait_for_window('Open')
        activate_window('Open')
        filepath = os.path.join(os.getcwd(), 'text.txt')
        time.sleep(3)
        pyautogui.write(filepath)
        pyautogui.hotkey('Enter')

        # assert result text
        result_xpath = '//strong[@class="k-upload-status k-upload-status-total" and contains(text(),"Done")]'
        waiter(self.driver, 15).until(visibility((By.XPATH, result_xpath)))
        text = "Done"
        result = self.driver.find_element_by_xpath(result_xpath)
        self.assertEqual(result.text, text)

    def tearDown(self):
        # close the browser window
        self.driver.quit()


def setup_log(log_path):
    """Setup logger"""
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    log_file = os.path.join(log_path, "test_log_%s.log" % datetime.datetime.today().strftime('%d-%m-%Y_%H-%M-%S'))
    sys.stdout = StreamToLogger(logger, "INFO")
    sys.stderr = StreamToLogger(logger, "ERROR")
    build_logger(log_file, 'DEBUG')
    logger.info(f'Machine: {socket.gethostname()}')


def assert_text(driver, text, selector="html", by=By.CSS_SELECTOR, timeout=None):
    if wait_for_element_visible(driver, selector, by, timeout):
        element = driver.find_element(by=by, value=selector)
        if element.is_displayed() and text in element.text:
            return True
        else:
            return False


def wait_for_element_visible(driver, selector, by=By.CSS_SELECTOR, timeout=None):
    if waiter(driver, timeout).until(visibility((by, selector))):
        return True
    else:
        raise Exception('Timeout - Element not visible')


def wait_for_window(window_name, timeout=60):
    for _ in range(timeout):
        try:
            window = gw.getWindowsWithTitle(window_name)[0]
            return
        except IndexError:
            pass
        time.sleep(1)


def activate_window(window_name):
    window = gw.getWindowsWithTitle(window_name)[0]
    window.activate()


if __name__ == '__main__':
    unittest.main()
