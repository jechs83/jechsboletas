from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by  import By 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

import pandas as pd
archivo = '/Users/javier/GIT/Boletas_emitir/valores.xlsx'
df = pd.read_excel(archivo, sheet_name='Sheet1' ,header=None)

options = Options()
#options.add_argument('--headless')
options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://app2.facturaonline.pe/")

driver.implicitly_wait(20) # gives an implicit wait for 20 seconds

def login():
  driver.find_element(By.CSS_SELECTOR, ".input-group:nth-child(3) > .form-control").send_keys("10442743709")
  driver.find_element(By.CSS_SELECTOR, ".input-group:nth-child(4) > .form-control").send_keys("Administrador")
  pwd = driver.find_element(By.CSS_SELECTOR, ".mb-4 > .form-control")
  pwd.send_keys("JtOdAgVG")
  pwd.send_keys(Keys.TAB + Keys.SPACE)
  time.sleep(4)
  #  HASTA AQUI SE LOGUEA

def emitir(val):
  driver.find_element(By.XPATH,"//body/div[1]/div[1]/div[1]/div[1]/nav[1]/section[1]/ul[1]/li[4]/a[1]").click()
  time.sleep(5)
  


  for i in range(val):
        
        x = df.loc[i,0]
        monto = str(x)
      
        codigo=driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/input[1]")
        codigo.send_keys("aaa" + Keys.ENTER)
        time.sleep(4)
        driver.find_element(By.XPATH, "//div[contains(text(),'Varios cod.999')]").click()
        precio= driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/input[1]")
        precio.clear()
        precio.send_keys(monto)
        driver.find_element(By.XPATH, "//body/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/button[1]").click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        driver.find_element(By.XPATH,"//body/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/div[2]/div[4]/div[2]/button[1]").click()
        print("deberia darl click a preview")
        time.sleep(1)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[5]/div[2]/button[1]").click()
        time.sleep(5)

        driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/header[1]/button[1]").click()
        time.sleep(3)



login()
emitir(22)
driver.quit()

