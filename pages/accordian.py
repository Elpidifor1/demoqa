from pages.base_page import BasePage
from components.components import WebElement

class AccordianPage (BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver,self.base_url)
        self.accordian_btn_one = WebElement(driver, "#accordianContainer > div > div:nth-child(1) > h2 > button")
        self.accordian_section_one = WebElement(driver, "#accordianContainer > div > div:nth-child(1) > div > div > p")
        self.accordian_section_two_part_1 = WebElement(driver, "#accordianContainer > div > div:nth-child(2) > div > div > p:nth-child(1)")
        self.accordian_section_two_part_2 = WebElement(driver, "#accordianContainer > div > div:nth-child(2) > div > div > p:nth-child(2)")
        self.accordian_section_three = WebElement(driver, "#accordianContainer > div > div:nth-child(3) > div > div > p")
