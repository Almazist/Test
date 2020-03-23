
import os
import sys
import time
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.common.by import By
#from selenium.common.exceptions import NoSuchElementException
#from selenium.webdriver.common.keys import Keys

#os.system('taskkill /im chromedriver.exe /f')
#os.system('taskkill /im chrome.exe /f')

my_getdir = os.path.dirname(os.path.abspath(__file__))
print(my_getdir)
options = Options()
options.add_argument("--headless")  # скрытый режим
# options.add_argument("window-size=10,10")

print()

try:
    proxy = []
    options.binary_location = "D:\\Program Files\\GoogleChromePortable\\App\\Chrome-bin\\chrome.exe"
    browser = webdriver.Chrome(chrome_options=options, executable_path=my_getdir+r'\\chromedriver.exe')
    #browser.set_window_position(800, 50)
    #browser.set_window_size(500, 300)
    browser.get('http://free-proxy.cz/')

    print()

    element = browser.find_element_by_id("frmsearchFilter-protocol-5").click()
    element = browser.find_element_by_id("frmsearchFilter-send").click()
    element = browser.find_element_by_id("clickexport").click()
    elem = browser.find_element_by_id("zkzk").text
    i = 0
    while True:
        with open(my_getdir+"\\element.txt", "w", encoding="utf-8") as file:
            print(*elem, file=file)

        l = []
        with open(my_getdir+"\\element.txt", 'r') as f:
            l = f.read().splitlines()

        i += 1
        print('Page '+str(i))

        for s in l:
            s = s.replace(' ', '')
            proxy.append(s)
            print(s)

        element = browser.find_elements_by_partial_link_text("Next ")
        if len(element) > 0:
            element[0].click()
            elem = browser.find_element_by_id("clickexport").click()
            elem = browser.find_element_by_id("zkzk").text
        else:
            break
except:
    print(traceback.format_exc())
finally:
    browser.quit()


print()
p = []
with open(my_getdir+"\\proxy.txt", 'r') as f:
    p = f.read().splitlines()

# добавить в proxy.txt только уникальные записи
i = 0
for s in proxy:
    if s not in p:
        p.append(s)
        i += 1


with open(my_getdir+"\\proxy.txt", "w") as f:
    for s in p:
        f.write(str(s) + '\n')


print("Добавлено: "+str(i))
print("OK")
time.sleep(5)
