from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.minimize_window()
def check_twitter(username,driver):
    try:
        driver.get("https://twitter.com/"+username)
        time.sleep(1)
        contest = driver.find_element_by_xpath("/html/body/div[2]/div/h1")
        pass
        time.sleep(1)
    except:
        print(username, "is on twitter")
def check_insta(username,driver):
    try:
        driver.get("https://instagram.com/"+username)
        time.sleep(1)
        contest = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/h1")
        print(username,"is on instagram")
        time.sleep(1)
    except:
        pass
def check_fb(username,driver):
    try:
        driver.get("https://facebook.com/"+username)
        time.sleep(1)
        contest = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[3]/div/div[1]/div/div/h1/span[1]/a')
        print(username,"is on facebook")
        time.sleep(1)
    except:
        pass
if __name__ == "__main__":
    usr = input("username : ")
    check_twitter(usr, driver)
    check_fb(usr,driver)
    check_insta(usr,driver)
    driver.quit()