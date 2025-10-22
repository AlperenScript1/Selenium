from selenium import webdriver
import chromedriver_autoinstaller 
from selenium.webdriver.common.by import By #? Selenium’da elementleri bulmak için kullanılan locator tiplerini (ID, NAME, CLASS_NAME, XPATH, CSS_SELECTOR vb.) By üzerinden çağırabilmek.
from time import sleep
chromedriver_autoinstaller;

url = "https://www.selenium.dev/selenium/web/web-form.html"; #TODO The Internet selenium test etmek için hazır bir site 
driver = webdriver.Chrome();
driver.get(url);

driver.implicitly_wait(10);

#? ".implicitly_wait(10);" → Selenium’a “Tüm element aramalarında, element DOM’da görünene kadar maksimum saniye kadar bekle” diyen global bekleme ayarıdır.
#! Eğer site yüklenmezse belirtilen süre içinde kodu çalıştırmaz.

#? ".click()" → Buton, link, checkbox gibi elementleri tıklamak için kullanılır.                                                                                                     1
#? ".send_keys()" → input ve textarea veri girebilmek için kullanılır.                                                                                                               2
#? ".clear()" → input'u temizlemek için kullanılır.                                                                                                                                  3
#? ".submit()" → Sadece form elemanlarında çalışır göndermek için.                                                                                                                   4

#TODO: ".click()"                                                                                                                                                                    1
#try:#! "try - except" ile elementi buldu mu/hata varmı kontrolü yapıyorum
#find = driver.find_element(By.LINK_TEXT, "A/B Testing");
#print("A/B Testing bulundu.");
#find.click();
#print("tıklandı");
#sleep(2);
#except:
#print("Bulunamadı.."); 

#TODO: 1- "find" adında değişken oluşturdum. 
#TODO: 2- "find_element(By.LINK_TEXT)" kullanarak  "<a>"" elementinde  "A/B Testing" innerHTML/TEXT değerini aratıyorum. 
#! Eğer ".get_attribute(innerHTML);" kullanılırsa ".click()" işlemi geçersiz olur çünkü ".get_attribute(innerHTML);" string bir değer döndürür bu sayde ".click()" etkisiz kalır.

#TODO: ".send_keys()"                                                                                                                                                               2                                                                                                                                                        
#! Yeni url:https://the-internet.herokuapp.com/key_presses "The internet" sitesinden baslangic sayfasını değiştirdim sadece öenmli bir şey değil!
#input = driver.find_element(By.ID,"target");
#input.send_keys("Hello ");
#sleep(2);
#input.send_keys("World");
#! Çıktısı: "Hello World" 

#input.clear(); #! Alttaki kodları etkilememesi için yazılanları temizliyorum.

#TODO: ".clear()"                                                                                                                                                                   3
#url = "https://the-internet.herokuapp.com/key_presses";
#input = driver.find_element(By.ID,"target");
#input.send_keys("Hello ");
#sleep(1);
#input.clear(); #! Temizledim 
#sleep(1);
#input.send_keys("World");
#sleep(2);
#! Çıktısı: "World"

#TODO: ".submit()"                                                                                                                                                                  4
#! Yeni url: https://www.selenium.dev/selenium/web/web-form.html
input = driver.find_element(By.ID, "my-text-id");
input.send_keys("Alperen");
sleep(1);
input.submit();
sleep(1);


driver.quit();