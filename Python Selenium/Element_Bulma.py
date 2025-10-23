from selenium import webdriver
import chromedriver_autoinstaller 
from selenium.webdriver.common.by import By #? Selenium’da elementleri bulmak için kullanılan locator tiplerini (ID, NAME, CLASS_NAME, XPATH, CSS_SELECTOR vb.) By üzerinden çağırabilmek.
from time import sleep
chromedriver_autoinstaller;


url ="https://www.python.org/#content";
driver = webdriver.Chrome();
driver.get(url);

#! Element bulma ve etkileşim
#? Elementleri kullanabilmek için "from selenium.webdriver.common.by import By" kullanıyoruz. 
#? "find_element()" → Tek bir elementi bulmak için kullanılır. Genelde buton, giriş alanı, yazı veya bağlantı gibi HTML öğelerini seçmeni sağlar.   
#? "find_elements()" → Bu ise çoğul hâlidir, yani birden fazla elementi bulur. Sonuç olarak bir liste döndürür.                                          

#! Element bulma yöntemleri: 
#? "get_attribute();" HTML elementlerini almak için kullanılır JavaScript gibi  
#TODO:
#! "get_attribute("href");"
#! "get_attribute("a");"
#! "get_attribute("div");" 

#? ".get_attribute("outerHTML"));" → Element + içerik
#? ".get_attribute("innerHTML"));" → Sadece içerik
#? ".get_attribute("href"));" → href içerigini "google.com"

#? "By.ID" → Elementi id özelliğine göre bulur.                                                                                                                1
#? "By.NAME" → name özniteliğine göre bulur.                                                                                                                   2
#? "By.CLASS_NAME" → class'ı ismine göre bulur.                                                                                                                3           
#? "By.TAG_NAME" → HTML etiket adına göre bulur (örnek: input, button, a).                                                                                     4
#? "By.LINK_TEXT" → Bir bağlantının (linkin) görünen tam metnine göre bulur.                                                                                   5
#? "By.PARTAL_LINK_TEXT" → "<a>" elementinin innerHTML yani text kısmının sadece bir kısmını yazarak bulur.                                                    6
#? "By.CSS_SELECTOR" → CSS seçicileriyle bulur (örnek: .btn-primary, div > a) Birden fazla class varsa aratılan class var ise eğer onlarıda bulur.             7
#? "By.XPATH" → Xpath yukarda kullanılan tüm kullanımları kapsar sorgusuyla bulur (çok güçlü, karmaşık seçimler için).  Gereksiz kullanım performans düşürür.  8                                                                                    8

#TODO Adım adım kullanımları:
                                                                          
#TODO .get_attribute("outerHTML")); kullanımı:                                                                                                                 
#print(driver.find_element(By.CLASS_NAME, "psf-widget").get_attribute("outerHTML")); #! Çıktısında <div>"psf-widget"</div> dahil verir.         
sleep(1);
#! Çıktı:
# <div class="psf-widget">
#   <h1>Başlık</h1>
#   <p>Alt yazı</p>
# </div>

# #TODO .get_attribute("innerHTML")); kullanımı:
# print(driver.find_element(By.CLASS_NAME, "main-header").get_attribute("innerHTML")); #! Çıktısı sadece belirtilen etiketin içeriğini verir.      
# sleep(1);
#! Çıktı: 
# <h1>Başlık</h1>
# <p>Alt yazı</p>

#TODO By.ID                                                                                                                                                      1
# driver.find_element(By.ID, "ornekID");
# sleep(1);

#TODO By.NAME                                                                                                                                                    2
#driver.find_element(By.NAME, "ornekNAME");
#sleep(1);

#TODO By.CLASS_NAME                                                                                                                                              3
#print(driver.find_element(By.CLASS_NAME, "main-header")); 

#TODO By.LINK_TEXT                                                                                                                                               4
#print(driver.find_element(By.LINK_TEXT, "Donate"));
#! Çıktısı:
# <selenium.webdriver.remote.webelement.WebElement (session="2261e1adc201ed7fe1b07b1f040fbd8a"
#! "href" link e ulaşmak için  ".get_attribute("href");" kullanıyoruz.
# link = driver.find_element(By.LINK_TEXT, "Donate").get_attribute("href");
# print(link);

#TODO "By.PARTIAL_LINK_TEXT" kullanımı:                                                                                                                          5
#driver.find_element(By.PARTIAL_LINK_TEXT, "");

#TODO "By.CSS_SELECTOR" kullanımı:                                                                                                                               6
#driver.find_element(By.CSS_SELECTOR, "btn");


#TODO "By.XPATH" kullanımı [Genel Kapsayıcı]:                                                                                                                     7
print(driver.find_element(By.XPATH, "//a").get_attribute("href"));
#https://www.python.org/#content 


#! XPATH
#XPath = //tagname[@Attribute='Value']

#TODO: Bunu parçalara ayırırsak:

# html
#   └── body
#       ├── div
#       │    └── button
#       └── div
#            └── button
#! XPath, bu ağacın içinde hangi düğüme ulaşacağını tarif eder.

#? // → “Herhangi bir yerden başla” anlamına gelir. Yani sayfanın neresinde olursa olsun, tagname ile eşleşen elementleri arar.

#? tagname → Bulmak istediğin HTML etiketinin adı. Örnekler: div, input, button, img vs.

#? [@Attribute='Value'] → Bu, belirli bir attribute’a sahip elementi seçmek için kullanılır.

#? Attribute → Aradığın özellik adı, örneğin id, class, name, onclick vb.

#? Value → Bu attribute’un değerini belirtirsin.

#! Temel XPath Sözdizimi
#xpath = "//tagname[@attribute='value']"

#TODO: Örnek:
#? //button[@id='submitBtn'] → Sayfada id'si submitBtn olan tüm <button> elementlerini seçer.

#? //input[@name='username'] → name attribute’u username olan <input> elementini seçer.

#? //div[@class='container'] → class attribute’u container olan tüm <div> elementlerini seçer.

#! XPATH VE DİĞER YOLLARI KOLAY ALMAK İÇİN  selectorshub eklentisi kullanılabilir işleri kolaylaştırır.
#TODO:https://selectorshub.com/selectorshub  
#! (Yeni başladıysanız öğrenim aşamasında kullanmanızı önermem)


driver.quit();
