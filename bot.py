from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

# Here Chrome  will be used
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(input("filepath tp your chrome driver")

url ='https://www.instagram.com/'


driver.get(url)
time.sleep(3)
driver.find_element_by_name("username").send_keys(input("Username:"))
driver.find_element_by_name("password").send_keys(input("password:"))


time.sleep(0.5)
button_login = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
button_login.click()
time.sleep(3)

search = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(input("account name:"))

time.sleep(3)
s2 = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a")
s2.click()
time.sleep(3)
n_posts = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span")
print(n_posts.text)
p1 = driver.find_element_by_class_name("_9AhH0")
p1.click()   # clicks on the first picture

def like_pic():
    time.sleep(2)
    like = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button")

    # you can find the like button using class name too
    time.sleep(0.5)
    like.click()

def next_picture():
    time.sleep(1)
    nex = driver.find_element_by_tag_name("body").send_keys(Keys.ARROW_RIGHT)
    time.sleep(1)

    return nex



def continue_liking():

    for x in range(int(n_posts.text)):
        like_pic()
        next_picture()




continue_liking()
driver.quit()
