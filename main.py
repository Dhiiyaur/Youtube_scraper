# import libraries

from selenium import webdriver
from tqdm import tqdm
import os
import pandas as pd
import time

# setting

BASE = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE + '\setting')

PATH = open('selenium_path.txt', 'r').read()
URL_PAGE = open('url.txt', 'r').read()
Total_comment = int(open('n_comment.txt', 'r').read())

# function

def loop(number_loop):
    driver.execute_script('window.scrollTo(1, document.documentElement.scrollHeight);')
    time.sleep(number_loop)
    
def check():
    name = driver.find_elements_by_xpath('//*[@id="author-text"]')
    number_of_items=len(name)
    
    return number_of_items

# main

results = []
driver = webdriver.Chrome(PATH)
driver.get(URL_PAGE)

# just scoll until comment appers
time.sleep(5)
driver.execute_script('window.scrollTo(1, 500);')
time.sleep(5)

#loop
while check() < Total_comment:
    loop(2)
    print(f'comments caught : {check()}')

comment  =   driver.find_elements_by_xpath('//*[@id="content-text"]')
name     =   driver.find_elements_by_xpath('//*[@id="author-text"]')
like     =   driver.find_elements_by_xpath('//*[@id="vote-count-middle"]')

number_of_items=len(name)    
print(f'Total comment : {number_of_items}')

for i in tqdm (range(number_of_items)):
    
    result =  {
                'user_name' : name[i].text,
                'comment' : comment[i].text,
                'likes' : like[i].text
        
                }
    results.append(result)

driver.quit()

os.chdir(BASE)
box_comment = pd.DataFrame(results, columns=['user_name', 'comment','likes'])
box_comment.to_csv('Results.csv', index=False)

print(box_comment.head(10))