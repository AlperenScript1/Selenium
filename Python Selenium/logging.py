from drivers.library import *
from pages.ilkPage import Islemler
from pages.sonrakiPage import AramaIslem
from pages.Logging import userLogin

driver = webdriver.Chrome()
url = "https://the-internet.herokuapp.com/login"
driver.get(url)

#! Log Rotation         →  Her yeni bir gün için yeni bir logging dosyası oluşturulur.
#! Size-Based Rotation  →  Dosya belirli bir boyuta gelince yenisi oluşurmak için kullanılır.

logging.basicConfig(
    filename = "Proje2/Logs/test.txt", #Oluşturulacak dosyanın yolu ve adı.
    filemode = "a",   #Dosyanın modu PHP yazdırma gibi.
    encoding="utf-8", #TR karakter için.
    # 'w' → Dosyanın içeriğini siler, yeni log ile başlar. Her çalıştırmada eski log kaybolur.
    # 'a' → Dosyanın mevcut içeriğinin sonuna ekler. Önceki loglar kaybolmaz, ekleme yapılır.
    level=logging.INFO, # info ve üstü seviyeleri yaz demek.
    format="%(asctime)s ||  %(levelname)s - %(message)s"
    # 'asctime'       →  2025-11-27 12:30:15
    # '%(levelname)s' →  INFO, ERROR, WARNING, CRITICAL
    # '%(message)s'   →  "Başarılı işlem"
)
#! Level	    Kullanım:
#? DEBUG    →	Detaylı bilgi geliştirme aşaması.
#? INFO     →   Normal akış kullanıcıya bilgi vermek.
#? WARNING  →	Uyarı dikkat edilmesi gereken durum.
#? ERROR    →	Hata oluştu işlem tamamlanamadı.
#? CRITICAL →	Çok ciddi hata program devam edemez.

#! Terminalde yazdırmak için
console_handler = logging.StreamHandler()  # terminal / console
console_handler.setLevel(logging.DEBUG)

hataAyiklama = userLogin(driver)

hataAyiklama.login("tomsmithx","SuperSecretPassword!x")

sleep(1)
driver.quit()