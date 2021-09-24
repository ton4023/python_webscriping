from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TourismThailand:
    
    DRIVER_PATH = './chromedriver'
    URL_PATH = 'https://www.tourismthailand.org/Destinations'
    
    def __init__(self):
        self.options = Options()
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path=self.DRIVER_PATH,options=self.options)
        self.driver.get(self.URL_PATH)
    
    def destination(self):
        titleDestination = []   
        tab = self.driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div/div[2]/ul')
        tabclick =  tab.find_elements_by_tag_name('li')

        for item in tabclick:
            item.click()
            topfive = self.driver.find_element_by_class_name('top-fives-listbox')
            toplable = [i.text for i in topfive.find_elements_by_tag_name('li')]
            subDestination = {}
            subDestination['region'] = item.text
            subDestination['topFives'] = toplable
            titleDestination.append(subDestination)
            
        print(titleDestination)    
        return titleDestination
        
if __name__ == "__main__":
    tourismThailand = TourismThailand()
    tourismThailand.destination()

