from selenium import webdriver 
import chromedriver_autoinstaller 
from selenium.webdriver.common.by import By
from time import sleep
chromedriver_autoinstaller;

driver = webdriver.Chrome();

url = "https://the-internet.herokuapp.com/add_remove_elements/"; 
driver.get(url);

try: #! outerHTML tek değişkene dahil edemiyoruz onu için ayrı bir değişken tanımlamak zorundayız.
  #TODO:Butonu oluşturuyorum.
  butonCreate = driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']");
  element = driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']").get_attribute("outerHTML");
  print("Buldundu: " + element);
  sleep(2);
  butonCreate.click();
  print("Tıklandı: " + element);
  sleep(2);
  #TODO:Butonu oluşturdum.
  #TODO: Oluşturduğum butonu siliyoru.
  sleep(2);
  butonDelete = driver.find_element(By.CLASS_NAME, "added-manually");   
  butonDelete.click();
  #TODO: Oluşturduğum butonu sildim.
except:
    print("Bulunamadı..");

#Terminal Çıktısı:
# DevTools listening on ws://127.0.0.1:58353/devtools/browser/3df83620-b6de-4fcf-9ae9-2dff51d49dd4
# Buldundu: <button onclick="addElement()">Add Element</button>
# Tıklandı: <button onclick="addElement()">Add Element</button>

sleep(1);
driver.quit();