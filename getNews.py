import requests
from bs4 import BeautifulSoup
import sys
import io

args = sys.argv
page = '0'
if len(args) > 1:
    page = args[1]
    if not page.isnumeric():
        while True:
            page = input('Informe o número da página: ')
            if page.isnumeric():
                break
            else:
                print('\nValor inválido!!\n')
else:
    while True:
        page = input('Informe o número da página: ')
        if page.isnumeric():
            break
        else:
            print('\nValor inválido!!\n')

print(page)
try:
    arquivo = open(f"{page}.txt", "a")
    print('PASSOU')
    print(arquivo.readlines())
except io.UnsupportedOperation: 
    res = requests.get(f'https://www.ifsudestemg.edu.br/noticias/barbacena/?b_start:int={int(page)*20}')


    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup.prettify())


    titles = soup.find_all("a", {"class": "summary url"})

    for title in titles:
        print('\n\t- ', title.contents[0])
        arquivo.write(f'\n\t- {title.contents[0]}')