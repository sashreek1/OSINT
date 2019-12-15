from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.minimize_window()
def check_twitter(username,driver):
    try:
        driver.get("https://twitter.com/"+username)
        time.sleep(1)
        contest = driver.find_element_by_xpath("/html/body/div[2]/div/h1")
    except:
        print(username, "is on twitter")
def check_insta(username,driver):
    try:
        driver.get("https://instagram.com/"+username)
        time.sleep(1)
        contest = driver.find_element_by_xpath("/html/body/div/div[1]/div/div/h2")
    except:
        print(username, "is on instagram")
        time.sleep(1)
def check_fb(username,driver):
    try:
        driver.get("https://facebook.com/"+username)
        time.sleep(1)
        contest = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/h2')
    except:
        print(username, "is on facebook")
        time.sleep(1)
if __name__ == "__main__":
    usr = input("username : ")
    check_twitter(usr, driver)
    check_fb(usr,driver)
    check_insta(usr,driver)
    driver.close()
    driver.quit()
