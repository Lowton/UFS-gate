import requests, log
from bs4 import BeautifulSoup
from lxml import html

site = 'https://bulbapedia.bulbagarden.net'
url = '/wiki/Bulbasaur_(Pok%C3%A9mon)'

def page_parce(url):
    url = site + url
    log.log.info(url)
    page = requests.get(url) # получаем страничку
    soup = BeautifulSoup(page.text, 'html.parser') # пропарсим и распределим

    pokename = soup.find('span', {'class':'mw-headline','id':'Name_origin'})
    pokenum = soup.find('th', {'width':'25%','class':'roundy','style':'background:#FFF;'})

    poketitle = pokename.previous_element
    en_pokename = pokename.next_element.next_element.next_element
    jp_pokename = pokename.next_element.next_element.next_element.next_sibling
    if jp_pokename != '\n':
        jp_pokename = jp_pokename.prettify()

    #print(pokename.previous_element, en_pokename, jp_pokename)
    pokenumber = pokenum.next_element.next_element.next_element.string
    pokemon = soup.title.string.replace(' (Pokémon) - Bulbapedia, the community-driven Pokémon encyclopedia','')
    poketitle.string = pokenumber + ' ' + pokemon

    pokedata = poketitle.prettify() + en_pokename.prettify() + jp_pokename

    with open('pokemon.html', 'ba') as htmlfile:
        htmlfile.write(str(pokedata).encode('utf8'))

    # выдёргиваем ссылку на следующую страницу
    tablo = soup.find('table')
    next_url = tablo.find_all('a')[5]['href']
    with open('href.html', 'ba') as htmlfile:
        htmlfile.write(str(tablo.prettify()).encode('utf8'))

    return next_url

pokenumber = 0

while int(pokenumber) < 807:
    turl = url
    url = page_parce(turl)
