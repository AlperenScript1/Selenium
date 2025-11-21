from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller #Otomatik tarayıcı sürümünü güncellemesi için gerekli kütüphane
from selenium import webdriver #Selenium web için gerekli driver kurulumu. 
from time import sleep, time


chromedriver_autoinstaller;

#driver = webdriver.Firefox(); #! farklı tarayıcılar için Firefox için.

driver = webdriver.Chrome(); #? Selenium'un Chrome tarayıcısını kontrol eden neseneyi oluşturuyoruz.
#? Yani bu satır "driver = webdriver.Chrome();"" bilgisayarda Chrome tarayıcısını açar ve Python’un onu otomatik kontrol etmesini sağlar.
#? "driver" değişkeni artık taracıyla konuşabileceğin bir değişken.
#? Örnek olarak bu driver üzerinden tıklama, yazı yazma, sayfa açma gibi işlemleri yapabilirsin.

url = ""; #? Gidilecek url giriyoruz.
driver.get(url); #? "driver.get() Tarayucıyı açar ve "url" değişkenine verilen değeri aratır."
#? Sayfa yüklendikten sonra selenium erişebilir.

sleep(1);

driver.quit(); #! Seleniumu sonlandırmak için.

