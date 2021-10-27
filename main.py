# python imports
from datetime import datetime as dt, timedelta
import os
import re

# third-party imports
import requests
import pdftotext
from selenium import webdriver

# local imports
from config import NAMES, CHAT_ID, BOT_TOKEN


URL = 'https://coronavirus.fortaleza.ce.gov.br/lista-vacinacao-d1.html'


def send_message(msg):
    data_post = f'{{"chat_id": "{CHAT_ID}", "text": "{msg}", "disable_notification": false"}}'

    requests.post(
        f'https://api.telegram.org/{BOT_TOKEN}/sendMessage',
        data=data_post, headers={"Content-Type": "application/json"})

    print(f'# {dt.now().strftime("%d/%m/%Y %H:%M")} -- Verificação concluída.')


def main():
    print(f'# {dt.now().strftime("%d/%m/%Y %H:%M")} -- Verificando listas...')

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)  # await for any element to load
    driver.get(URL)

    scheduled = driver.find_element_by_id('boletinsAnteriores')

    matches = list()

    for item in scheduled.find_elements_by_tag_name('li > a'):
        href = item.get_attribute('href')
        text = item.text

        if 'Gestantes e Puérperas' in text:
            continue

        try:
            date = re.search(r'\d{2}/\d{2}/\d{4}', text).group(0).replace('/', '-')
            date_obj = dt.strptime(date, '%d-%m-%Y')
        except (ValueError, AttributeError):  # wrong format of date
            continue

        week_ago = dt.now() - timedelta(days=1)

        dose = 'D1'
        if 'D2' in text:
            dose = 'D2'
        elif 'D3' in text:
            dose = 'D3'

        filename = f'agendados-{dose}-{date}.pdf'
        filepath = f'files/{filename}'

        if date_obj >= week_ago:

            if not os.path.isfile(filepath):
                pdf = requests.get(href)

                with open(filepath, 'wb') as f:
                    f.write(pdf.content)

            with open(filepath, "rb") as f:
                for page in pdftotext.PDF(f):

                    elements = page.split('\n')

                    for element in elements:

                        if re.search('[0-9]*\-[0-9]*\-[0-9]*', element):  # noqa W605

                            for name in NAMES:
                                if re.search(name, element, flags=re.IGNORECASE):
                                    matches.append(re.sub("\s\s+", " ", element))  # noqa W605

    if not matches:
        send_message("Lista de vacina: nada ainda.")
        return

    message = "Lista de vacina: uris achou!"
    for match in matches:
        message += f"\n- {match}"
    send_message(message)


if __name__ == '__main__':
    main()
