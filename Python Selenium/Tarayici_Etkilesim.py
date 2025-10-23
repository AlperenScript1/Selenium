from selenium import webdriver #? Selenium web için gerekli driver kurulumu. 
import chromedriver_autoinstaller #? Otomatik tarayıcı sürümünü güncellemesi için gerekli kütüphane
from time import sleep
chromedriver_autoinstaller; 

driver = webdriver.Chrome();
url = "https://www.selenium.dev/";
driver.get(url);

#! Selenium ile tarayıcı etkileşimleri [driver.'dan sonra yazılır]
#? "set_window_size(1024, 768)" → Tarayıcı penceresinin genişliğini ve yüksekliğini ayarlar.            1
#? "set_window_position(65,25);" → Tarayıcı penceresinin konumunu ayarlar.                              2
#? "minimize_window()" → Tarayıcıyı görev çubuğuna küçültür (görünmez hâle getirir).                    3
#? "maximize_window()" → Tarayıcıyı ekranın tamamını kaplayacak şekilde büyütür.                        4
#? "refresh()" → Açık sayfayı yeniden yükler (yeniden render eder).                                     5
#? "back()" → Tarayıcı geçmişinde bir önceki sayfaya gider.                                             6
#? "forward()" → Tarayıcı geçmişinde bir sonraki sayfaya gider (geri gitmişsen).                        7
#? "execute_script("window.open('https://www.google.com', '_blank', 'width=800,height=600');")"         8
#? "switch_to.window(window_handle)" → Çoklu pencere veya sekme varsa aktif pencereyi değiştirir.       9
#? "execute_script("window.scrollTo(0, document.body.scrollHeight);")" → Sayfayı en alta kaydırır.      10
#? "current_url" → Şu an açık olan sayfanın URL’sini verir.                                             11
#? "title" → Sayfanın başlığını (title) verir.                                                          12
#? "page_source" → Sayfanın HTML kaynak kodunu verir.                                                   13
#? "quit()" → Tarayıcıyı ve tüm bağlı süreçleri kapatır.                                                14

#TODO Adım adım kullanımları:                                                                         

#TODO: "set_window_size(1024, 768)" kullanımı:                                                          1
driver.set_window_size(1024, 768);
sleep(1);

#TODO: "driver.set_window_position(65,25);" kullanımı:                                                  2
driver.set_window_position(125, 25);
sleep(1);

#TODO: "minimize_window()" kullanım:                                                                    3
driver.minimize_window();
sleep(1);
#! Eğer aratılan element sitenin penceresi küçük iken gözükmüyor ise selenium da bulamıyor 

#TODO: "maximize_window()" kullanım:                                                                    4
driver.maximize_window();
sleep(1);
#! Eğer aratılan element sitenin penceresi küçük iken gözükmüyor ise selenium da bulamıyor 

#TODO: "refresh()" kullanımı:                                                                           5
driver.refresh();
sleep(1);

#TODO: "back()" kullanımı:                                                                              6
url = "https://www.python.org/";
driver.get(url);
driver.back();
sleep(1);

#TODO: "forward()" kullanımı:                                                                           7
url = "https://www.selenium.dev/";
driver.get(url);
driver.forward();
sleep(1);

#TODO: "execute_script("window.open('https://www.google.com', '_blank');")" kullanımı:                  8
driver.execute_script("window.open('https://www.google.com', 'width=800,height=600');")
sleep(1);

#TODO: "switch_to.window(window_handle)" kullanımı:                                                     9                 
handles = driver.window_handles;
driver.switch_to.window(handles[0]);
sleep(1);

#TODO: "execute_script("window.scrollTo(0, document."body.scrollHeight);")" kullanımı:                 10                 
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);");
sleep(2);

#TODO: "current_url" kullanımı:                                                                        11
print(driver.current_url);


#TODO: "title" kullanımı:                                                                              12
print(driver.title);


#TODO: "page_source" kullanımı:                                                                        13
print(driver.page_source);


#TODO: "quit()" kullanımı:                                                                             14

driver.quit();
