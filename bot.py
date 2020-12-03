# coding: utf8
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import json
from openpyxl import load_workbook
import unicode2utf8
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import matplotlib.pyplot as plt

import time

url = 'https://www.booking.com'

browser = webdriver.Firefox()
browser.get(url)

busca = browser.find_element_by_xpath('//*[@id="ss"]')
busca.send_keys('Ubatuba')
busca = browser.find_element_by_xpath('//*[@id="frm"]/div[1]/div[2]/div[1]/div[2]/div/div/div/div/span')
busca.click()
busca = browser.find_element_by_xpath(
    '//*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr[4]/td[3]')
print("dia de entrada: ", busca.text)
busca.click()
busca = browser.find_element_by_xpath(
    '//*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[3]/div[2]/table/tbody/tr[1]/td[3]')
print("dia de saida: ", busca.text)
busca.click()
busca = browser.find_element_by_xpath('//*[@id="frm"]/div[1]/div[4]/div[2]/button')
busca.click()

Filtro = browser.find_element_by_id('sortbar_dropdown_button')
Filtro.click()
Filtro = browser.find_element_by_class_name('sort_price ')
Filtro.click()
time.sleep(8)

TodosHoteis = browser.find_element_by_xpath('//*[@id="hotellist_inner"]')
ListaHotel = TodosHoteis.find_elements_by_class_name('sr-hotel__name')
Valores = TodosHoteis.find_elements_by_class_name('bui-price-display__value')

print("Hoteis com preco mais barato: ")
# printar texto de uma LISTA
n = 0
texts = []
precos = []


for NomeHotel in ListaHotel:
    text = NomeHotel.text
    texts.append(text)


for preco in Valores:
    valor = preco.text
    precos.append(valor)


df1 = pd.DataFrame([texts])
df2 = pd.DataFrame([precos])

plt.title("Hoteis com precos mais baratos")

x = (precos[0:24])
y = (texts[0:24])
plt.bar(y,x)
plt.show()

#df = pd.concat([df1,df2])
#df.to_excel("teste.xlsx")


