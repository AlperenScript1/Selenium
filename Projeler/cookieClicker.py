from selenium import webdriver #Selenium web için gerekli driver kurulumu. 
import chromedriver_autoinstaller #Otomatik tarayıcı sürümünü güncellemesi için gerekli kütüphane
from selenium.webdriver.common.by import By
from time import sleep

chromedriver_autoinstaller;

driver = webdriver.Chrome(); 
driver.set_window_size(1920, 800);
driver.implicitly_wait(10);

url = "https://orteil.dashnet.org/cookieclicker/"; 
driver.get(url); 

try:
   selectLang = driver.find_element(By.ID,"langSelect-EN");
   selectLang.click();
   print("Find: lang");
   sleep(1);
   selectCookie = driver.find_element(By.ID,"bigCookie");

   i = 0;
   while i != 100:
       selectCookie.click();
       i+=1
       print(str(i) +". defa Tıklandı :)");
except:
    print("Err..");

sleep(1);
driver.quit();
