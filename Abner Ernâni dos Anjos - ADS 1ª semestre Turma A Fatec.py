'''
Essa código faz a raspagem de dois sites um com o nome das estrelas e outro
com o nome das constelações em latim
'''

import requests
from bs4 import BeautifulSoup

# a função título deixa o texto em destaque
def titulo(a):
    x= '===' + a + '==='
    print('\n',x,'\n')

# get_urlsoup recebe um url e retorna uma sopa
def get_urlsoup(a):
    page = requests.get(a)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

#findall recebe uma sopa e um parâmetro string e retorna uma lista
def findall(b,a):
    x= b.find_all(a)
    return x

titulo('Astronomia')
print('HR => cúmulo globular\nHD => espectroscópica\n')

titulo('Nome de Estrelas mais próximas')
soup = get_urlsoup('http://www.astro.wisc.edu/~dolan/constellations/starname_list.html')
lista = findall(soup,'a')

nomes= []# adiciona os nomes das estrelas a um vetor
for k in lista:
    nomes.append(k)

lengh= len(nomes) - 1

#retira os três últimos nomes que são desnecessários
for i in [lengh, lengh - 1, lengh - 2]:
    nomes.remove(nomes[i])

urls= []# adiciona os urls da página da informação de cada estrela
for i in nomes:
    a= ' '.join(str(i)).split(' ')
    index= []
    for j in a:
        if j in '1234567890':
            index.append(j)
            if len(index) == 8:
                url = 'http://www.astro.wisc.edu/~dolan/constellations/hr/' + str(''.join(index)) + '.html'
                urls.append(url)

#abre cada url e transforma em uma sopa    
for g in urls:
    x= get_urlsoup(g)
    y= findall(x,'ul')
    z= x.find('h1')
    print(titulo(z.get_text()))
    for h in y:
        caract= h.find('li').get_text()
        print(caract)

titulo('Nome de Todas as 88 constelações em Latim')
html= get_urlsoup('http://www.galeriadometeorito.com/p/constelacoes.html')
s= html.findAll('div',{'class':'MsoNormal'})

#Raspa os nomes das constelações
for i in s:
    x= i.find('b')
    if x != None:
        y= x.find('span')
        print(y.get_text())
