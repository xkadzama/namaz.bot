import requests
import bs4



CONC_ = '%D0%BB%D0%B0%D0%BC%D0%B0%D0%B7%D0%B0%D0%BD-%D1%85%D0%B5%D0%BD%D0%B0%D1%88-%D0%B2%D1%80%D0%B5%D0%BC%D1%8F-%D0%BC%D0%BE%D0%BB%D0%B8%D1%82%D0%B2#'
responce = requests.get('https://govzalla.com/' + CONC_)


pars_file = bs4.BeautifulSoup(responce.text, 'html.parser')

time_file = pars_file.find_all('h4')
description = pars_file.find_all('div', class_='label')




# ЗАПОЛНЯЮ СПИСОК ОПИСАНИЕМ НАМАЗА
def namaz_clean(description: 'html') -> list:
    desc = []
    for i in description:
        desc.append(i.get_text().replace(' ', '').replace('\n', '')) #УДАЛЯЮ ПРОБЕЛЫ И СНОСКИ. МЕТОДОМ GET_TEXT ОТБРАСЫВАЮ ТЭГИ
    return desc



# ЗАПОЛНЯЮ СПИСОК ВРЕМЕНАМИ НАМАЗА
def time_clean(time_file: 'html') -> list:
    time = []
    for j in time_file:
        time.append(j.get_text())
    return time



# СОЕДИНЯЮ ОПИСАНИЕ И ВРЕМЯ НАМАЗА В СЛОВАРЕ | КЛЮЧИ:ЗНАЧЕНИЕ
# ПО ИДЕИ ПРОХОЖУ ДЛИНУ ОДНОГО СПИСКА, НО ЗНАЧЕНИЯ БЕРУ СРАЗУ С ДВУХ. МАГИЯ ПИТОНА

def concat_nt() -> dict:
    desc_and_key = {}
    for k in range(len(desc)):
        desc_and_key[desc[k].lower()] = time[k]
    # output = desc_and_key[search.lower()]
    # return output
    return desc_and_key



''' Передал функциям распарсенные данные, чтобы они в свою очередь 
обработали их и привели в нужный вид, возвращаемые данные использую уже для функции CONCAT_NT
без аргументов ибо сама функция видит их как глобальные. 
После я могу вызывать функцию CONCAT без передачи в неё аргументов '''

desc = namaz_clean(description)
time = time_clean(time_file)



