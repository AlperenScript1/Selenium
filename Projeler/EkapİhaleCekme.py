from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from time import sleep, time
chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.set_window_size(1920, 800);
driver.implicitly_wait(10);

driver.get("https://ekap.kik.gov.tr/EKAP/YeniIhaleArama.aspx?qs=1&dt=true");
ekapListeSonuc = []; #? Bulduğum değerleri atacağım bir liste oluşturuyorum.
    
#!Filtre değiştirmek için Mal/Yapım/Hizmet for='rdIhaleTur_1' kısmından seçim yapılabilir.

#TODO: for='rdIhaleTur_1' => Mal
#TODO: for='rdIhaleTur_2' => Yapım
#TODO: for='rdIhaleTur_3' => Hizmet

filtreAdi = driver.find_element(By.CSS_SELECTOR, "label[for='rdIhaleTur_1']").get_attribute("innerHTML"); #? Ekap sayfasından filtreler kısmından hangi filtreyi seçtiğimi alıyorum.
filtre = driver.find_element(By.CSS_SELECTOR, "label[for='rdIhaleTur_1']").click(); #? Ekap sayfasından filtreler kısmından 'Yapım' seçiyorum.
filtreleButton = driver.find_element(By.ID, "btnFilter").click(); #? Filtreleme butonuna tıklıyorum.
sleep(5); #? Filtreleme için bekliyorum.
print("Secilen filtre: " + str(filtreAdi));

son_Yukseklik = driver.execute_script("return document.body.scrollHeight") #? Başlangıçta sayfa yüksekliğini al.
i = 0;
while True: #? Kırılana kadar tekrar eden döngü.
    ekapAdi = driver.find_elements(By.CLASS_NAME, "ihaleAdi")[i].get_attribute("innerHTML"); #? ihale adını alıyorum.
    ekapID = driver.find_elements(By.CLASS_NAME, "listIknNo")[i].get_attribute("innerHTML"); #? ihale ID alıyorum. 
    ekapListeSonuc.append(ekapAdi); #? ihale adını 'ekapListeSonuc' listesine ekliyorum.
    ekapListeSonuc.append(ekapID); #? ihale ID 'ekapListeSonuc' listesine ekliyorum.
    i += 1; #= i değerini artırıyorum ki bir sonraki elemanı alabilmek için.

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #? Sayfanın en altına kaydır.
    sleep(1); #? Yeni içerik yüklenmesi için kısa bekleme.
    
    yeni_Yukseklik = driver.execute_script("return document.body.scrollHeight"); #? Yeni yüksekliği al.
    if yeni_Yukseklik == son_Yukseklik: #? Eğer yükseklik değişmediyse, sayfanın sonuna geldik.
        print("\nSayfanın sonuna geldiniz.\n \n" + "Toplam alınan ihale sayisi: " + str(i) + "\n");
        print(ekapListeSonuc);
        break

    son_Yukseklik = yeni_Yukseklik;

driver.quit();
