import requests
import socket
from bs4 import BeautifulSoup
import re


domain = 'sstmk.ru'
url = 'https://' + domain
'''1'''
response = requests.get(url)
assert response.status_code == 200, f'Website error. Get status code {response.status_code}'
'''2'''
ip = socket.gethostbyname_ex(domain)
print(f'ip-address for domain {ip[0]}\n{ip[2]}')
'''3'''
soup = BeautifulSoup(response.text, 'html.parser')
tel = soup.findAll('div', class_='phone-number')
assert len(tel) == 1, f'Error with getting phone number \n tel = {tel}'
'''4'''
ph_num = tel[0].text.replace(' ', '')
reg_num = re.fullmatch(r"[+]?\d{0,3}\(\d+\)\d+-\d+-\d+", ph_num)
if reg_num:
    print(f'Phone number: {reg_num[0]}')
else:
    raise Exception(f'Wrong number on website: {ph_num}')
