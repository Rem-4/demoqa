from components.components import WebElement
from pages.base_page import BasePage
class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)
        self.btn_small_modal = WebElement(driver, '#showSmallModal')
        self.btn_large_modal = WebElement(driver, '#showLargeModal')
        self.btn_close_sm = WebElement(driver, '#closeSmallModal')
        self.btn_close_lm = WebElement(driver, '#closeLargeModal')
        self.icon = WebElement(driver, '#app > header > a')
        self.btn_elements = WebElement(driver, '#app > div > div > div > div:nth-child(1) > div > div > '
                                               'div:nth-child(3) > div >ul >li')