from selenium import webdriver
import time

veri = input("#Arama : ")
browser = webdriver.Firefox(executable_path=r""C:\Program Files\Google\Chrome\Application\chrome.exe"")
browser.get("https://twitter.com/search?q="+veri+"&src=typed_query&f=live")
browser.maximize_window()


time.sleep(2)

sonuc = []
tweet = browser.find_elements_by_xpath("//div[@data-testid='tweetText']")
time.sleep(3)
print("------------------------------\n" + str(len(tweet)) + "adet tweet başarıyla çekildi \n------------------------------")
for i in tweet:
    sonuc.append(i.text)

sayac = 0
son = browser.execute_script("return document.documentElement.scrollHeight")
while True:
    if sayac > 10 :
        break
    browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
    time.sleep(2)
    yeni = browser.execute_script("return document.documentElement.scrollHeight")
    if son == yeni :
        break
    son = yeni
    sayac += 1
    tweet = browser.find_elements_by_xpath("//div[@data-testid='tweetText']")
    time.sleep(3)
    print("------------------------------\n" + str(len(tweet)) + "adet tweet başarıyla çekildi \n------------------------------")
    for i in tweet:
        sonuc.append(i.text)

adet = 1
with open("tweetler.txt","w",encoding="UTF-8") as file :
    for a in sonuc :
        file.write(f"{adet} - {a}\n")
        adet += 1
print("tweetler.txt dosyasına tweetler başarı ile kaydedildi")
    


    




