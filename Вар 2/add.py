from bs4 import BeautifulSoup
import requests
f = open("file.txt", "w")



def parse():
    url = 'https://omgtu.ru/general_information/faculties/' # передаем необходимы URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4

    block = soup.findAll('div', id ="pagecontent") # находим  контейнер с нужным id
    description = ''
    for data in block: # проходим циклом по содержимому контейнера
        if data.find('a'): # находим тег
            description = data.text # записываем в переменную содержание тега

    print(description, file=f)
    #print(description)

parse()
f.close()
f = open("file.txt", "r")
def workFile():
    k = f.read()
    #for i in range(len(k)-1):
     #   if k[i] == k[i+1] == '\n':
    k = k.replace('\n','')
    k = k.replace('С составом и структурой факультетов Вы можете ознакомиться, используя левое меню.','')
    k = k.replace('Омский государственный технический университет включает в себя семь факультетов: ','')
    k = k.replace('Факультет','\nФакультет')
    k = k.replace('Аэро','\nАэро')
    k = k.replace('Худ','\nХуд')
    fF = open("fileFinal.txt", "w")
    print(k,file=fF)
    fF.close()
    print(k)
workFile()
f.close()

