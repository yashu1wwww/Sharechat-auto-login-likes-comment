#first time in github sharechat auto login,likes,comment 

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://sharechat.com/signin?redirect_uri=%2Fprofile")

driver.find_element_by_css_selector('#root > div.Pos\(f\).Start\(0\).W\(100\%\).T\(0\).H\(100\%\).Ov\(a\).Z\(100\).Bgc\(\$white\) > div > main > div > div > div:nth-child(9) > div > div').click()

time.sleep(4)

driver.find_element_by_css_selector('#root > div.Pos\(r\).T\(0\).W\(100\%\).Mih\(90vh\).Pb\(\$3xl\).Pt\(\$2xl\) > main > section > div:nth-child(2) > form > div.D\(f\).Jc\(c\).Ai\(c\).Mb\(\$lg\).Px\(\$md\) > div.Px\(\$md\).Fxg\(1\).Bd\(\$bdinput\).Bdw\(\$bdleft\) > div > input').send_keys("9090909090") #replace with your no

time.sleep(2)

driver.find_element_by_css_selector('#root > div.Pos\(r\).T\(0\).W\(100\%\).Mih\(90vh\).Pb\(\$3xl\).Pt\(\$2xl\) > main > section > div:nth-child(2) > form > div:nth-child(2) > div > button > div > div').click()

time.sleep(16) #with in 15 sec enter otp 

driver.get("https://sharechat.com/explore?referer=bottomNav")

time.sleep(15)

driver.find_element_by_css_selector('#root > div.Pos\(r\).T\(0\).W\(100\%\).Mih\(90vh\).Pb\(\$3xl\).Pt\(\$3xl\).Bgc\(\$white3\) > main > div > div:nth-child(1) > div > a:nth-child(24) > div > img').click()

time.sleep(6)

driver.find_element_by_xpath('//*[@id="root"]/div[1]/main/a[1]/div/div').click()

time.sleep(4)

driver.find_element_by_xpath('//*[@id="root"]/div[1]/main/div/div[2]/div/section/div[1]/div/div[3]/div[1]/div[2]/button/div/span').click()

time.sleep(6)

driver.find_element_by_css_selector('#root > div.Pos\(r\).T\(0\).W\(100\%\).Mih\(90vh\).Pb\(\$3xl\).Pt\(\$2xl\).Bgc\(\$white3\) > main > div > div.infinite-list-wrapper > div > section > div:nth-child(1) > div > div.D\(f\).Jc\(sb\).W\(100\%\).Py\(\$xs\) > div.D\(f\).Ai\(c\).Fxg\(1\) > div:nth-child(3) > button > div > span').click()

time.sleep(3)

driver.find_element_by_css_selector('#root > div.Pos\(f\).Start\(0\).W\(100\%\).T\(0\).H\(100\%\).Z\(300\).Bgc\(\$modal\) > div > div > div.Fxs\(0\).W\(100\%\).Bdt\(\$bdinput\).Bgc\(white\).Op\(1\) > form > textarea').send_keys("comments putting") #replace with your cmt

time.sleep(3)

driver.find_element_by_css_selector('#root > div.Pos\(f\).Start\(0\).W\(100\%\).T\(0\).H\(100\%\).Z\(300\).Bgc\(\$modal\) > div > div > div.Fxs\(0\).W\(100\%\).Bdt\(\$bdinput\).Bgc\(white\).Op\(1\) > form > div > button > div > div > div > svg').click()

time.sleep(10)
