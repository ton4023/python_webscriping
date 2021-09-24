from selenium import webdriver
from selenium.webdriver.chrome.options import Options


DRIVER_PATH = './chromedriver'
options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(executable_path=DRIVER_PATH,options=options)
driver.get('https://www.tourismthailand.org/Destinations')

tab = driver.find_element_by_class_name('tab-groups')
tablabel = [i.text for i in tab.find_elements_by_tag_name('li')]
tabclick = tab.find_elements_by_tag_name('li')

destination = []

for item in tabclick:
    item.click()
    topfive = driver.find_element_by_class_name('top-fives-listbox')
    toplable = [i.text for i in topfive.find_elements_by_tag_name('li')]
    subDestination = {}
    subDestination['region'] = item.text
    subDestination['topFives'] = toplable
    destination.append(subDestination)
    
print(destination)
driver.close()


# destination = [
# 	{
# 	'region' : 'North',
# 	'topFives': ['Chiang Mai','Chiang Rai','Mae Hong Son','Lampang','Sukhothai']
# 	},
# ]