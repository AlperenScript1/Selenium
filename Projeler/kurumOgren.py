from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver #Selenium web için gerekli driver kurulumu. 
import chromedriver_autoinstaller #Otomatik tarayıcı sürümünü güncellemesi için gerekli kütüphane
from time import sleep, time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chromedriver_autoinstaller;
options = Options()
options.add_argument("--window-size=1920,1080") #? Sayfa görünür olmasa bile çözünürlüğü ayarlar.

#options.add_argument("--headless") #! "--headless" KULLANMIYORUZ ÇÜNKÜ BOT OLARAK ALGILANABİLİR VE ENGELLENEBİLİR
options.add_argument("--window-position=-32000,-32000") #! Onun yerine
driver = webdriver.Chrome(options=options); #! options=options

url = "https://ekap.kik.gov.tr/EKAP/YeniIhaleArama.aspx?qs=1&dt=true";
driver.get(url);
driver.implicitly_wait(10);

yil = "25"; #! Aratılan Yıl
kurumID = "1762647" \
""; #! Aratılan Kurum ID 1779189

driver.set_window_size(1920, 800);
try:
    if yil == "25": #? Yıl değerini select içindeki indexe göre ayarladım.
        yil = "0"
    elif yil == "24":
        yil = "1"
    elif yil == "23":
        yil = "2"
    elif yil == "22":
        yil = "3"
    else:
        print("Girilen yil 25-22 arasında değil veya başka bir hata oluştu.") #? Kullanıcının girdiği değer yanlıi veya 25-22 aralığında değil ise uyarı verir.

    driver.find_element(By.CSS_SELECTOR, "div[placeholder='Lütfen Yıl Seçiniz'] span[aria-label='Select box activate']").click(); #? Yıl seçme yerine click func uyguluyor.

    driver.find_element(By.CSS_SELECTOR, f"div[id='ui-select-choices-row-0-{yil}'] a[class='ui-select-choices-row-inner']").click(); #? Girilen yıla göre seçim yapıyor.
    print("Seçilen yil: " + yil);

    driver.find_element(By.CSS_SELECTOR, "input[placeholder='DT No']").send_keys(kurumID); #? Kurum ID giriliyor.
    driver.find_element(By.ID, "btnFilter").click();    #? Filtreleme butonuna tıklıyor.
     
    try:
        wait = WebDriverWait(driver, 10)
        toast_locator =(By.CSS_SELECTOR, ".alert.alert-info")
        elements = wait.until(EC.presence_of_all_elements_located(toast_locator))
        print("geliyor")
        if toast_locator:
             element = elements[0]
             print("innerText:", element.get_attribute("innerText"))
             print("text:", element.text)
    except:
        print("Hiç alert bulunamadı.")
        print("else girdi")
        driver.find_element(By.CSS_SELECTOR,".fa.fa-th").click();
        print("yatay moda geçiş yapıldı.");
        kurumu = driver.find_element(By.CSS_SELECTOR,".idareIl.ng-binding").get_attribute("innerHTML");
        print(str(kurumu));

except :
    print("Err..");

driver.quit();