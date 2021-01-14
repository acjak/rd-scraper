#!/usr/local/bin/python3.8

import requests
from bs4 import BeautifulSoup

r = requests.get('https://rd.dk/da-dk/privat/koeb-bolig/Kurser-og-renter/Pages/aktuelle-kurser.aspx?valutakode=DKK')
soup = BeautifulSoup(r.content, 'html.parser')

t1 = soup.select('#ctl00_m_g_88a3ff31_a0da_4002_9fec_f54a3232962b_grdData1_\#_1004')[0]

print(t1.select(".gs-gridLinkColCell.gs-gridCell2 a")[1].text)