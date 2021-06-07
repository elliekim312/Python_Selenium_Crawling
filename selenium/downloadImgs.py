# Call the Selenium Libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import getopt
import sys
import urllib.request


def startCrawling(keyword):

    # Use Chromedriver which under selenium folder
    driver = webdriver.Chrome()

    # Move to the Site
    driver.get("https://www.google.com/imghp?hl=en&ogbl")

    # Find search input box
    elem = driver.find_element_by_name("q")

    # My keyword to search input box
    elem.send_keys(keyword)

    # Enter!
    elem.send_keys(Keys.RETURN)

    # Load multiple items and download
    SCROLL_PAUSE_TIME = 1

    # Get scroll height with run javascript to place all images
    last_height = driver.execute_script("return document.body.scrollHeight")

    keep_running = True
    while keep_running == True:
        # Scroll down to bottom
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:  # the end
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height

        images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

        count = 1
        for img in images:
            try:
                img.click()
                time.sleep(3)
                imgUrl = driver.find_element_by_xpath(
                    "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img").get_attribute("src")
                urllib.request.urlretrieve(
                    imgUrl, "img/google_" + keyword + "_" + str(count) + ".png")
                count = count+1
            except:
                pass

    driver.close()


# Get Arguments from command line
def main(sysArgv):
    imgCount = ""

    fullCmdArguments = sysArgv
    fileName = fullCmdArguments[0]
    argumentList = fullCmdArguments[1:]

    if argumentList:
        shortOption = "hk:i:"
        longOption = ["help", "keyword="]

        try:
            arguments, values = getopt.getopt(
                argumentList, shortOption, longOption)

        except getopt.GetoptError:
            print(
                fullCmdArguments[0], '--keyword=<keyword> OR --k=<keyword>')
            sys.exit(2)

        for arg, val in arguments:
            if arg in ("--h", "--help"):
                print(
                    fullCmdArguments[0], '--keyword=<keyword> OR --k=<keyword>')
                sys.exit()

            elif arg in ("--k", "--keyword"):
                keyword = val

        startCrawling(keyword)

    else:
        print(
            fullCmdArguments[0], '--keyword=<keyword> OR --k=<keyword>')


if __name__ == "__main__":
    main(sys.argv)
