# http://demos.telerik.com/kendo-ui/dragdrop/index
import os
import socket
import sys
import datetime
from loguru import logger
from selenium import webdriver
from selenium.webdriver import ChromeOptions

from build_log import StreamToLogger, build_logger


def main():
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
    driver = webdriver.Chrome(options=options, executable_path=r'.\chromedriver.exe')
    test_page = 'https://duckduckgo.com'
    logger.info(f'Navigate to test page {test_page}')
    driver.get(test_page)

def setup_log(log_path):
    """Setup logger"""
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    log_file = os.path.join(log_path, "test_log_%s.log" % datetime.datetime.today().strftime('%d-%m-%Y_%H-%M-%S'))
    sys.stdout = StreamToLogger(logger, "INFO")
    sys.stderr = StreamToLogger(logger, "ERROR")
    build_logger(log_file, 'DEBUG')
    logger.info(f'Machine: {socket.gethostname()}')

main()
