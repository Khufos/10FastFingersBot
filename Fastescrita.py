"Version Python 3.8.7 64bits"
"Você precisa de duas bibliotecas Selenium e pyautogui"
"10 fast fingers" "TRADUÇÃO , DEDOS RAPIDOS."
'''WebDriver é uma ferramenta de código aberto para teste automatizado de aplicativos da web em vários navegadores. 
Ele fornece recursos para navegar para páginas da web, entrada do usuário, execução de JavaScript e muito mais. 
ChromeDriver é um servidor autônomo que implementa  o padrão W3C WebDriver . 
ChromeDriver está disponível para Chrome em Android e Chrome em Desktop 
(Mac, Linux, Windows e ChromeOS). ''' 


from selenium import webdriver
import pyautogui as cursor
from time import sleep

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://10fastfingers.com/typing-test/portuguese')
sleep(5)
cursor.moveTo(x=781, y=395, duration=0.1)
cursor.click()
word_list = driver.execute_script("return document.getElementById('wordlist').innerHTML")
words = word_list.split("|")
for word in words:
	driver.find_element_by_id("inputfield").send_keys(word+ " ")
sleep(0.15)