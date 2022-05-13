from os.path import abspath
from requests import get
from bs4 import BeautifulSoup

""" 
https://es.wikwik.org/todaspalabrastam.htm

https://es.wikwik.org/todaspalabrastampagina2.htm

https://es.wikwik.org/todaspalabrastampagina3.htm

https://es.wikwik.org/todaspalabrastampagina4.htm

etc..

total paginas 1855
 """


def ExtractTextValue(url_: str) -> list:
    getUrl = get(url=url_)
    bsterminal = BeautifulSoup(getUrl.content, "html.parser")
    result = bsterminal.find_all('p', class_='mm')[0].findChildren()
    return [i.text for i in result]


def DocumentSave(nameDoc: str, filterList: list):
    with open(abspath(f'./dict/{nameDoc}.txt'), 'a') as openSaveList:
        for i in filterList:
            openSaveList.write(f'{i}\n')
        else:
            openSaveList.close()


def SaveSumDict():

    namedocument = 'holamundo'
    temporal1 = ExtractTextValue(
        url_='https://es.wikwik.org/todaspalabrastam.htm')
    DocumentSave(nameDoc=namedocument, filterList=temporal1)

    counter = 2
    while True:
        try:
            temporalURL = f'https://es.wikwik.org/todaspalabrastampagina{counter}.htm'
            temporal1 = ExtractTextValue(url_=temporalURL)
            DocumentSave(nameDoc=namedocument, filterList=temporal1)
        except:
            counter = 2
            break
        counter += 1


if __name__ == '__main__':
    SaveSumDict()
