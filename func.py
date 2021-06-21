import requests
from bs4 import BeautifulSoup
import re


def all_car_brands(result):
    global li
    li = []
    cars = []
    page = requests.get('https://bama.ir/')

    soup = BeautifulSoup(page.content, 'html.parser')
    for a in soup.find_all('a', href=True):
        if a['href'].startswith('/car/'):
            li.append(a['href'])
            cars.append((a['href'].split('/')[2]).strip())

    cars = list(set(cars))
    cars.sort()
    return cars


def car_brands(result):
    if result == '':
        return None
    brands_cars = []
    for item in li:
        if item.startswith(f'/car/{result}'):
            if len(item.split('/')) > 3:
                brands_cars.append((item.split('/')[3]).strip())
    brands_cars = list(set(brands_cars))
    brands_cars.sort()
    return list(set(brands_cars))


def get_car_title(car,brand,from_year,to_year,price,installment,replacement,list_car):
    page = 1
    global list_car_detail
    list_car_detail = []
    if not brand: brand = 'all-models'
    while True:
        url = update_url(car,brand,from_year,to_year,price,installment,replacement,page)
        soup = BeautifulSoup(url.content, 'html.parser')
        # result = soup.find_all("a",{"class":"cartitle cartitle-mobile"})
        result = soup.find_all("a",{"itemprop":"url"})
        for a in result:
            list_car_detail.append({re.sub("\s*","",(a.text.strip())):a['href']})

        next_page = soup.find('a',{'rel':'next'})
        if next_page:
            page+=1
        else:
            break

    for i in range(len(list_car_detail)):
        for key,value in list_car_detail[i].items():
            list_car.insert(i,key)


def update_url(car,brand,from_year,to_year,price,installment,replacement,page):
    if not from_year and not to_year:
        if price or installment or replacement:
            if price and installment:
                url = requests.get(f'https://bama.ir/car/{car}/{brand}/all-trims?hasprice=true&instalment=1&page={page}')
            elif price and replacement:
                url = requests.get(f'https://bama.ir/car/{car}/{brand}/all-trims?hasprice=true&hastrade=true&page={page}')
            elif price:
                url = requests.get(f'https://bama.ir/car/{car}/{brand}/all-trims?hasprice=true&instalment=0&page={page}')
            elif replacement:
                url = requests.get(f'https://bama.ir/car/{car}/{brand}/all-trims?hastrade=true&instalment=0&page={page}')
            elif installment:
                url = requests.get(f'https://bama.ir/car/{car}/{brand}/all-trims?instalment=1&page={page}')
        else:
            url = requests.get(f'https://bama.ir/car/{car}/{brand}/all-trims?page={page}')

    elif from_year and to_year:
        if price or installment or replacement:
            if price and installment:
                url = requests.get(f'https://bama.ir/car/{car}/{brand}/all-trims?hasprice=true&instalment=1&year={from_year}-{to_year}&page={page}')
            elif price and replacement:
                url = requests.get(f'https://bama.ir/car/{car}/{brand}/all-trims?hasprice=true&hastrade=true&year={from_year}-{to_year}&page={page}')
            elif price:
                url = requests.get(f'https://bama.ir/car/{car}/{brand}/all-trims?hasprice=true&year={from_year}-{to_year}&page={page}')
            elif replacement:
                url = requests.get(f'https://bama.ir/car/{car}/{brand}/all-trims?hastrade=true&instalment=0&year={from_year}-{to_year}&page={page}')
            elif installment:
                url = requests.get(f'https://bama.ir/car/{car}/{brand}/all-trims?instalment=1&year={from_year}-{to_year}&page={page}')
        else:
            url = requests.get(f'https://bama.ir/car/{car}/{brand}/all-trims?year={from_year}-{to_year}&page={page}')
        
    elif from_year or to_year:
        if from_year:
            if price or installment or replacement:
                if price and installment:
                    url = requests.get(f'https://bama.ir/car/{car}/{brand}/all-trims?hasprice=true&instalment=1&year={from_year}&page={page}')
                elif price and replacement:
                    url = requests.get(f'https://bama.ir/car/{car}/{brand}/all-trims?hasprice=true&hastrade=true&year={from_year}&page={page}')
                elif price:
                    url = requests.get(f'https://bama.ir/car/{car}/{brand}/all-trims?hasprice=true&instalment=0&year={from_year}&page={page}')
                elif replacement:
                    url = requests.get(f'https://bama.ir/car/{car}/{brand}/all-trims?hastrade=true&instalment=0&year={from_year}&page={page}')
                elif installment:
                    url = requests.get(f'https://bama.ir/car/{car}/{brand}/all-trims?instalment=1&year={from_year}&page={page}')
            else:
                url = requests.get(f'https://bama.ir/car/{car}/{brand}/all-trims?year={from_year}&page={page}')
        else:
            if price or installment or replacement:
                if price and installment:
                    url = requests.get(f'https://bama.ir/car/{car}/{brand}/all-trims?hasprice=true&instalment=1&year=0-{to_year}&page={page}')
                elif price and replacement:
                    url = requests.get(f'https://bama.ir/car/{car}/{brand}/all-trims?hasprice=true&hastrade=true&year=0-{to_year}&page={page}')
                elif price:
                    url = requests.get(f'https://bama.ir/car/{car}/{brand}/all-trims?hasprice=true&instalment=0&year=0-{to_year}&page={page}')
                elif replacement:
                    url = requests.get(f'https://bama.ir/car/{car}/{brand}/all-trims?hastrade=true&instalment=0&year=0-{to_year}&page={page}')
                elif installment:
                    url = requests.get(f'https://bama.ir/car/{car}/{brand}/all-trims?instalment=1&year=0-{to_year}&page={page}')
            else:
                url = requests.get(f'https://bama.ir/car/{car}/{brand}/all-trims?year=0-{to_year}&page={page}')
 
    return url


def get_car_detail(index,detail_list):
    for key,value in list_car_detail[index].items():
        detail_list.insert(0,value)
        link = value
    
    url = requests.get(link)
    soup = BeautifulSoup(url.content, 'html.parser')

    result = soup.find(class_ = "prdinfo")
    
    detail = soup.find(class_ = "removeEmoji")
    if detail:
        detail_list.insert(0,detail.text.strip())

    info = soup.find_all('p',result)
    info = info[:-4]
    for i in range(len(info)):
        info[i] = re.sub("\t*\n*\r*","",((info[i]).text.strip()))
        detail_list.insert(i,info[i])
 


