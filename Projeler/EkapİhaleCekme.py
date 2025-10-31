from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from time import sleep
chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.set_window_size(1920, 800);
driver.implicitly_wait(10);

driver.get("https://ekap.kik.gov.tr/EKAP/YeniIhaleArama.aspx?qs=1&dt=true");
ekapListeSonuc = []; #? Bulduğum değerleri atacağım bir liste oluşturuyorum.
    
son_Yukseklik = driver.execute_script("return document.body.scrollHeight") #? Başlangıçta sayfa yüksekliğini al.
i = 0;
while True: #? Kırılana kadar tekrar eden döngü.
    ekapAdi = driver.find_elements(By.CLASS_NAME, "ihaleAdi")[i].get_attribute("innerHTML"); #? ihale adını alıyorum.
    ekapID = driver.find_elements(By.CLASS_NAME, "listIknNo")[i].get_attribute("innerHTML"); #? ihale ID alıyorum. 
    ekapListeSonuc.append(ekapAdi); #? ihale adını 'ekapListeSonuc' listesine ekliyorum.
    ekapListeSonuc.append(ekapID); #? ihale ID 'ekapListeSonuc' listesine ekliyorum.
    i += 1; #= i değerini artırıyorum ki bir sonraki elemanı alabilmek için.

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #? Sayfanın en altına kaydır.
    sleep(5); #? Yeni içerik yüklenmesi için kısa bekleme.
    
    yeni_Yukseklik = driver.execute_script("return document.body.scrollHeight"); #? Yeni yüksekliği al.
    if yeni_Yukseklik == son_Yukseklik: #? Eğer yükseklik değişmediyse, sayfanın sonuna geldik.
        print("Sayfanın sonuna ulaşıldı!" + "Toplam alınan ihale sayisi: " + str(i));
        print(ekapListeSonuc);
        break

    son_Yukseklik = yeni_Yukseklik;

driver.quit();