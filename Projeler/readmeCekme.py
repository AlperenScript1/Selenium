from selenium import webdriver #Selenium web için gerekli driver kurulumu. 
import chromedriver_autoinstaller #Otomatik tarayıcı sürümünü güncellemesi için gerekli kütüphane
from selenium.webdriver.common.by import By
from time import sleep

chromedriver_autoinstaller;

driver = webdriver.Chrome(); 

url = "https://github.com/AlperenScript1";
driver.get(url);

try:
    repo = driver.find_element(By.CLASS_NAME, "repo");
    print("find");
    repo.click();
    sleep(2);
    readme = driver.find_element(By.XPATH, "//div[@class='Box-sc-62in7e-0 js-snippet-clipboard-copy-unpositioned DirectoryRichtextContent-module__SharedMarkdownContent--BTKsc']").get_attribute("innerHTML");
    print(str(readme));
except:
    print("Err.");

# <article class="markdown-body entry-content container-lg" itemprop="text"><div class="markdown-heading" dir="auto"><h1 tabindex="-1" class="heading-element" dir="auto">🐍 Python Selenium</h1><a id="user-content--python-selenium" class="anchor" aria-label="Permalink: 🐍 Python Selenium" href="#-python-selenium"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
# <p dir="auto">Bu repo, Python + Selenium öğrenirken tuttuğum kişisel notlardan oluşmaktadır.
# Her konuyu ayrı .py dosyasında ele alıyorum, zamanla küçük otomasyon projelerini de ekleyeceğim.</p>
# <p dir="auto">Ayrıca VS Code içinde kodları düzenli tutmak için şu etiketleri kullanıyorum:
# #TODO, #!, #?
# Bu etiketleri vurgulamak için  👉 <a href="https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments" rel="nofollow">Better Comments</a> eklentisini kullanmanızı öneririm.</p>
# </article>


sleep(1);
driver.quit();