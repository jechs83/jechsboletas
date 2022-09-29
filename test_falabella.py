from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by  import By 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

web="https://www.falabella.com.pe/falabella-pe/product/882314412/LED-58-58A6GSA-4K-HDR-Android-Smart-TV/882314412"

options = Options()
#options.add_argument('--headless')
options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get(web)

driver.implicitly_wait(20) # gives an implicit wait for 20 seconds

def login():
  driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/header[1]/div[3]/div[1]/div[4]/ul[1]/li[1]/div[1]/div[2]/div[1]/p[1]").click()
  driver.find_element(By.XPATH,"/html[1]/body[1]/div[9]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/input[1]").send_keys("javier.chung@gmail.com"+ Keys.TAB + "Jazmine.2013")
  time.sleep(2)
  driver.find_element(By.XPATH,"/html[1]/body[1]/div[9]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/button[1]/span[1]").click()
  time.sleep(5)

  driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/section[2]/div[2]/div[1]/div[2]/div[2]/div[1]/button[1]").click()
  driver.find_element(By.XPATH,"//a[@id='linkButton']").click()
  driver.find_element(By.XPATH,"//button[contains(text(),'Continuar compra')]").click()
  time.sleep(4)
  driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[3]/div[1]/div[2]/button[1]/span[1]").click()
  time.sleep(5)
  print("paso por aqui")
  driver.find_element(By.XPATH("//body/div[@id='__next']/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]")).click()
  driver.quit()


login()



