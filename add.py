
from bs4 import BeautifulSoup
import requests
f = open("file.txt", "w")



def parse():
    url = 'https://omgtu.ru/general_information/faculties/' # передаем необходимы URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4

    block = soup.findAll('div', id='pagecontent') # находим  контейнер с нужным id
    description = ''
    for data in block: # проходим циклом по содержимому контейнера
        if data.find('li'): # находим тег
            description = data.text # записываем в переменную содержание тега

    print(description, file=f)

parse()

f.close()
