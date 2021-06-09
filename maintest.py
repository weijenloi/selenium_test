# http://demos.telerik.com/kendo-ui/dragdrop/index
from selenium import webdriver
from selenium.webdriver import ChromeOptions

def main():

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
    driver.get('https://duckduckgo.com')
    input()


main()
