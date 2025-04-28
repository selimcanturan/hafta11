from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
 
driver = webdriver.Chrome()
# class url:
#     def __init__(self, url):
#         self.url = url
class scrap:
    def __init__(self):
 
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 60)
        self.link_listesi = []
 
    def close(self):
        self.driver.quit()
 
    def get_links(self, url):
        driver = self.driver
        driver.get(url)
 
 
 
 
 
url = "https://eksisozluk.com/basliklar/gundem"
driver.get(url)
driver.maximize_window()
 
wait = WebDriverWait(driver, 60)
container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".topic-list.partial")))
 
link_listesi = []
 
import time
time.sleep(5)
 
li = container.find_elements(By.TAG_NAME, "li")
 
for i in li:
    try:
        a = i.find_element(By.TAG_NAME, 'a')
        link = a.get_attribute('href')
        link_listesi.append(link)
    except:
        continue
 
 
daha_fazla = driver.find_element(By.ID, "quick-index-continue-link")
driver.execute_script("arguments[0].click();", daha_fazla)
 
time.sleep(5)
container1 = driver.find_element(By.CSS_SELECTOR, ".topic-list.partial")
li1 = container1.find_elements(By.TAG_NAME, "li")
 
for j in li1:
    try:
        a1 = j.find_element(By.TAG_NAME, 'a')
        link1 = a1.get_attribute('href')
        link_listesi.append(link1)
    except:
        continue
 
 
son = driver.find_element(By.CLASS_NAME, "last")
driver.execute_script("arguments[0].click();", son)
 
time.sleep(5)
container1 = driver.find_element(By.CSS_SELECTOR, ".topic-list.partial")
li2 = container1.find_elements(By.TAG_NAME, "li")
 
for k in li2:
    try:
        a2 = k.find_element(By.TAG_NAME, 'a')
        link2 = a2.get_attribute('href')
        link_listesi.append(link2)
    except:
        continue
 
print(link_listesi)
driver.quit()
 
chromedriver_autoinstaller.install()
 
driver = webdriver.Chrome()
 
for i in range(len(link_listesi)):
    driver.get(link_listesi[i])
    driver.maximize_window()
    wait = WebDriverWait(driver, 60)
 
    try:
        sayfa_sayisi = driver.find_element(By.CLASS_NAME, "pager")
        sayi = sayfa_sayisi.find_elements(By.TAG_NAME, "a")
 
        for a in sayi:
            text = a.text.strip()
            if text.isdigit():
                sayi_int = int(text)
 
    except:
        sayi_int = 1
 
    for j in range(1, sayi_int + 1):
        if j != 1:
            driver.get(link_listesi[i] + f"&p={j}")
 
        wait.until(EC.presence_of_element_located((By.ID, "entry-item-list")))
        container = driver.find_element(By.ID, "entry-item-list")
        li_elements = container.find_elements(By.TAG_NAME, "li")
 
        for li in li_elements:
            try:
                content = li.find_element(By.CLASS_NAME, "content")
                with open("veriler.txt", "a", encoding="utf-8") as f:
                    f.write(content.text + "\n" + "é")
            except:
                continue
 
# driver.quit()
if __name__ == "__main__":
    scraper = scrap()
    url = "https://eksisozluk.com/basliklar/gundem"
    scraper.get_links(url)
    scraper.close()