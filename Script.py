# -*- coding: utf-8 -*-
import urllib.request
import ast


import pickle

from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait
import asyncio
from telegram import Bot


from selenium.webdriver.common.by import By
import time
import logging

logging.basicConfig(filename='selenium.log', level=logging.INFO)
logging.info('Starting script')

options = webdriver.ChromeOptions()
# options.add_argument("--disable-blink-features=AutomationControlled")
a = 0
# universalnamedocument


options.add_experimental_option('excludeSwitches', ['enable-logging'])


options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)







def chrome4():
    while True:
        file = r'sana.txt'
        f = open(file, "r")
        sa=f.read()
        try:
            try:
                driver.get('https://aktualno.uz/ru')
                time.sleep(5)
                sana = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    "/html/body/div/div[2]/main/div[1]/div/div[1]/section/div[1]/div[1]/article/div[4]/span[1]"))
                )

                # Once the element is clickable, perform the click action
                sana1 = sana.text
            except Exception as exx:
                bot = Bot(token='6803537624:AAEYxZWB0UsaWNoAgfCkgYDVYJG7mMM6BJ8')

                async def send_message(chat_id, text):
                    await bot.send_message(chat_id=chat_id, text=text)

                # Run the async function
                asyncio.run(send_message(chat_id=-1002218438906, text='SITE DOWN'))

                driver.refresh()
                chrome4()
            try:
                if str(sana1)==str(sa):
                    time.sleep(2)
                    driver.refresh()



                else:

                    submit = WebDriverWait(driver, 4).until(
                        EC.presence_of_element_located(
                            (By.XPATH, '/html/body/div/div[2]/main/div[1]/div/div[1]/section/div[1]/div[1]/article/div[2]/a')))

                    submit.click()
                    time.sleep(2)


                    try:
                        zagalovok = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH,
                                                        "/html/body/div/div[2]/div/div[1]/div[1]/main/div[1]/article/h1"))
                        )

                        # Once the element is clickable, perform the click action
                        zagalovoktext=zagalovok.text

                    except:
                        print('zagalovok')
                    try:
                        # t = WebDriverWait(driver, 10).until(
                        #     EC.presence_of_element_located((By.XPATH,
                        #                                 "/html/body/div/div[2]/div/div[1]/div[1]/main/div[1]/article/div[3]"))
                        # )
                        #
                        # # Once the element is clickable, perform the click action
                        # text=t.text
                        url=driver.current_url
                        print(f'url:{url}')
                    except:
                        print('zagalovok')
                    try:
                        textareabutton680 = WebDriverWait(driver, 70).until(
                            EC.presence_of_element_located(
                                (By.XPATH, '/html/body/div/div[2]/div/div[1]/div[1]/main/div[1]/article/div[1]/div/picture/img'))
                        )
                        src = textareabutton680.get_attribute('src')
                        print('src', src)
                        # download the image
                        urllib.request.urlretrieve(src, "img.png")

                    except Exception as exx:
                        print(111)
                    except:
                        print('auto false')


                    driver.get('https://www.facebook.com')

                    # phone = WebDriverWait(driver, 70).until(
                    #     EC.presence_of_element_located(
                    #         (By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input')))
                    #
                    # phone.send_keys("+998996556503")
                    #
                    # passport = WebDriverWait(driver, 70).until(
                    #     EC.presence_of_element_located(
                    #         (By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input')))
                    # passport.send_keys("20121999Fda1")
                    #
                    # facebooksubmit = WebDriverWait(driver, 70).until(
                    #     EC.presence_of_element_located(
                    #         (By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')))
                    # facebooksubmit.click()
                    # time.sleep(15)
                    # pickle.dump(driver.get_cookies(),open('facebook_cookies.pkl','wb'))
                    #
                    for cookie in pickle.load(open("facebook_cookies1.pkl", "rb")):
                        cookie['domain']='.facebook.com'
                        try:
                            driver.add_cookie(cookie)
                        except Exception as exx:
                            print('cokiee')
                    time.sleep(2)
                    driver.refresh()


                    public = WebDriverWait(driver, 4).until(
                        EC.presence_of_element_located(
                            (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[2]')))


                    public.click()
                    write = WebDriverWait(driver, 14).until(
                        EC.presence_of_element_located(
                            (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div[1]')))
                    write.send_keys(f'{zagalovoktext}\n\nВы можете прочитать полную информацию здесь:\n{url}')
                    photo = WebDriverWait(driver, 4).until(
                        EC.presence_of_element_located(
                            (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div/input')))
                    photo.send_keys("D:/aktualno/img.png")
                    time.sleep(2)
                    submitfacebook = WebDriverWait(driver, 4).until(
                        EC.presence_of_element_located(
                            (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div/div'))).click()

                    time.sleep(2)
                    submitfacebook2 = WebDriverWait(driver, 4).until(
                        EC.presence_of_element_located(
                            (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[2]/div/div/div[2]/div[5]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div')))
                    submitfacebook2.click()
                    time.sleep(2)


                    submitfacebook3 = WebDriverWait(driver, 4).until(
                        EC.presence_of_element_located(
                            (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[2]/div/div/div[2]/div[6]/div/div')))
                    submitfacebook3.click()

                    with open(file, 'w') as f:
                        f.write(str(sana1))

                    time.sleep(4)
                    print('done')
            except Exception as exx:
                print('alert')
        except Exception as exx:
            print(exx)




chrome4()
