from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TourismThailand:

    DRIVER_PATH = './chromedriver'
    URL_PATH = 'https://www.tourismthailand.org/Destinations'

    def __init__(self):
        self.options = Options()
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(
            executable_path=self.DRIVER_PATH, options=self.options)
        self.driver.get(self.URL_PATH)

    def regionDestination(self):

        titleDestination = []

        try:
            self.driver.implicitly_wait(10)
            elems = self.driver.find_elements_by_class_name(
                'tab-groups')[0]

            for item in elems.find_elements_by_tag_name('li'):
                item.click()
                topfive = self.driver.find_element_by_class_name(
                    'top-fives-listbox')
                toplable = [
                    i.text for i in topfive.find_elements_by_tag_name('li')]
                subDestination = {}
                subDestination['region'] = item.text
                subDestination['topFives'] = toplable
                titleDestination.append(subDestination)

            return titleDestination

        finally:
            pass

    def themeDestination(self):

        try:
            self.driver.implicitly_wait(10)

            themeTravel = []

            elems = self.driver.find_elements_by_class_name('row')[1]

            for i in range(4):
                place = elems.find_elements_by_class_name('caption')[i]
                img = elems.find_elements_by_tag_name('img')[i]
                theme = {}
                theme['placeName'] = place.text
                theme['imagePath'] = img.get_attribute('data-src')
                themeTravel.append(theme)

            return themeTravel

        finally:
           pass




