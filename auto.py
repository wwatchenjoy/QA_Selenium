import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.asos.com/ru/men/')

# TК-005	Проверка функции поиск по сайту
search_box = driver.find_element(By.XPATH,
                                 '//*[@id="chrome-search"]')
search_box.send_keys('Рубашка')
time.sleep(1)
search_button = driver.find_element(By.XPATH,
                                    '//*[@id="chrome-sticky-header"]/div[1]/div/div/div/form/div/button')
search_button.click()

answer = driver.find_element(By.XPATH, '//*[@id="search-term-banner"]/p[2]')

if answer.text != u'рубашка':
    print("Ожидаемый ответ верен =  %r" % answer.text)
else:
    print("Ожидаемый ответ ", answer.text, " не найден")

time.sleep(3)
# driver.quit()


# TК-006	Проверка функции сортировки товара
sort_button = driver.find_element(By.XPATH,
                                  '//*[@id="plp"]/div/div[2]/div/div/div/div[1]/ul/li[3]/div/button')
time.sleep(1)
sort_button.click()
time.sleep(1)
man_sort = driver.find_element(By.XPATH,
                               '//*[@id="plp"]/div/div[2]/div/div/div/div[1]/ul/li[3]/div/div/div/ul/li[1]/div/label/div')
man_sort.click()
time.sleep(1)
print('Сортировка по полу успешна')


# TК-004	Проверка функции добавление товара в Избранное

sell_box = driver.find_element(By.XPATH,
                               '//*[@id="product-20774938"]/a')

sell_box.click()
time.sleep(1)
wish_button = driver.find_element(By.XPATH,
                                  '//*[@id="product-save"]/div/button')
wish_button.click()
time.sleep(1)
wish_list_button = driver.find_element(By.XPATH,
                                       '//*[@id="chrome-sticky-header"]/div[1]/div/ul/li[2]/a')
wish_list_button.click()

print('Товар добавлен в список желаемого')
time.sleep(1)



