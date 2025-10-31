from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from time import sleep

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.set_window_size(1920, 800)
driver.implicitly_wait(10)

driver.get("https://ekap.kik.gov.tr/EKAP/YeniIhaleArama.aspx?qs=1&dt=true")


son_Yukseklik = driver.execute_script("return document.body.scrollHeight") #? Başlangıçta sayfa yüksekliğini al

while True: #? Kırılana kadar tekrar eden döngü
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #? Sayfanın en altına kaydır
    
    sleep(2); #? Yeni içerik yüklenmesi için kısa bekleme

    #? Yeni yüksekliği al
    yeni_Yukseklik = driver.execute_script("return document.body.scrollHeight");

    #? Eğer yükseklik değişmediyse, sayfanın sonuna geldik.
    if yeni_Yukseklik == son_Yukseklik:
        print("Sayfanın sonuna ulaşıldı!");
        break

    son_Yukseklik = yeni_Yukseklik;

driver.quit();