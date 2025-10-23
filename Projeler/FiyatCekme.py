from selenium import webdriver #Selenium web için gerekli driver kurulumu. 
import chromedriver_autoinstaller #Otomatik tarayıcı sürümünü güncellemesi için gerekli kütüphane
from selenium.webdriver.common.by import By
from time import sleep

chromedriver_autoinstaller;

driver = webdriver.Chrome(); 
url = "https://halledersiniz.com/"; 
driver.get(url);

driver.implicitly_wait(10);

try:
 driver.maximize_window();
 urun = driver.find_element(By.XPATH, "//span[contains(text(),'3D Yazıcılar')]");
 print("Bulundu");
 urun.click();
 sleep(1);
 urun = driver.find_element(By.LINK_TEXT, "Bambu Lab A1 3D Printer (Önsipariş)");
 urun.click();
 sleep(1);
 fiyat = driver.find_element(By.CLASS_NAME, "price-item").get_attribute("innerHTML");
 print(str(fiyat));
except:
 print("Err..");

sleep(1);
driver.quit(); 