#Author: BumBum
from os import system;system('clear')
import requests
from bs4 import BeautifulSoup
from time import sleep
from sys import exit
def log(email,password):
    s = requests.Session()
    payload = {'username': email, 'password': password}
    
    res = s.post("https://elearning.smkitnurulhuda.sch.id/Login/", data=payload)
    
    if res.ok:
        sleep(1)
        print('Status Login: √')
        sleep(1)
    else:
        print('Status Login: ×')
        exit()
    return s

session = log(input('Login Ke akun Sekolah!\nMasukan Username: '),input('Masukan Password: '))

def namaGuru():
    
    url = 'https://elearning.smkitnurulhuda.sch.id/Guru/listsiswa'
    r = session.patch(url).text

    soup = BeautifulSoup(r,'html.parser')
    print('\nMemuat Data')
    sleep(1)
    print('\n','-' * 12,'Data Guru Smk IT Nurul Huda Cianjur', '-' * 12)
    for status in soup.find_all('div', class_="col-12 col-sm-6 col-md-4 d-flex align-items-stretch"):
        nama = status.find('h2',class_='lead')
        #print(nama.text)

        about = status.find('p', class_="text-muted text-sm")
        #print(about.text)

        address = status.find('ul', class_="ml-4 mb-0 fa-ul text-muted")
        address = address.text.replace('\n ', '').replace('Phone','\nPhone')
        
        sleep(1)
        a = (f'\nNama: {nama.text}\n{about.text}\n{address}')
        print(a)
        print('-'*20)
        with open('data.txt','a') as f:
            f.write(f'\n{nama.text}\n{about.text}\n{address}\n')


def main():
    print('''\n1.Data Guru Smk
2.Data saya
3.Absen Sekolah\n''')
    select = int(input('Masukan pilihan: '))
    if select == 1:
        namaGuru()

main()



#print(r)

#merubah no hp
#r = session.post("https://elearning.smkitnurulhuda.sch.id/Setting/editprofil", data={'nohp':'12345678910'})
#print(f'Status Perubahan No Hp: {r.ok}')

#buat absen
#url = 'https://elearning.smkitnurulhuda.sch.id/Absen/simpan_absen_bysiswa'
#files = {'file':open('/data/data/com.termux/files/home/latihanPython/regex/requests/poto.jpg','rb')}
#poto = session.patch(url,files=files)
#print(poto.status_code)
#print(poto.text)
