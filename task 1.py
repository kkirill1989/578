#Задание
#Условие: Добавить в наш тестовый проект шаг добавления поста после входа. Должна выполняться проверка на наличие названия поста на странице сразу после его создания.
#Совет: не забудьте добавить небольшие ожидания перед и после нажатия кнопки создания поста.
#Что ещё можно почитать:
#• Начинаем работать с Selenium в Python

import yaml
from module import Site

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)

site = Site(testdata['address'])


def test_step1(x_selector_1, x_selector_2, btn_selector, x_selector_3, expected_result_1):
    input1 = site.find_element('xpath', x_selector_1)
    input1.send_keys('test')
    input2 = site.find_element('xpath', x_selector_2)
    input2.send_keys('test')
    btn = site.find_element('css', btn_selector)
    btn.click()
    error_label = site.find_element('xpath', x_selector_3)
    result = error_label.text
    assert result == expected_result_1, 'test1 failed'


def test_step2(x_selector_1, x_selector_2, btn_selector, x_selector_3, x_selector_4,
               expected_result_1, expected_result_2):
    input1 = site.find_element('xpath', x_selector_1)
    input1.clear()
    input1.send_keys(testdata['username'])
    input2 = site.find_element('xpath', x_selector_2)
    input2.clear()
    input2.send_keys(testdata['password'])
    btn = site.find_element('css', btn_selector)
    btn.click()
    link1 = site.find_element('xpath', x_selector_4)
    result = link1.text
    site.close()
    assert result == expected_result_2, 'test2 failed'