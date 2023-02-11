import json
from time import sleep

from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def hello(request):
    return HttpResponse('Test')


def article_detail(request):
    # id = request.GET.get('id', None)
    query = request.GET.get('name')
    return HttpResponse(query)

def getreport(request):
    body = request.body.decode('utf-8')
    data = json.loads(body)
    # url = data["url"].replace('"', "")


    # selenium
    # create an instance of Chrome options
    options = Options()

    # set the option to run Chrome in headless mode
    options.headless = True
    options.add_argument("--headless=chrome")

    # else uncomment this
    # options.add_experimental_option("detach", True)

    # create a new Chrome browser instance with the options
    browser = webdriver.Chrome(options=options)
    # url = "https://ais.zzotk.ba:9443/tuzla/Startup?ST_ACTION=102723.do&K.ID=Perfrm&K.1=12026142&I1=XML.FOP.FORCED&AUTOLOGIN_USER=cust&AUTOLOGIN_TS=2023-02-02T13:48:00.000Z&AUTOLOGIN_TOKEN=494733DE304CB150498185626A9FC8422122DA8B218243FD97CAA8CBB53E3C6CB6BC3A646AF16770AC1E26B4F16F03C50D110227884AF46E5AB7B77D7F9A3824"

    url = "https://ais.zzotk.ba:9443/tuzla/Startup?ST_ACTION=102723.do&K.ID=Perfrm&K.1=12026142&I1=XML.FOP.FORCED&AUTOLOGIN_USER=cust&AUTOLOGIN_TS=2023-02-06T15:32:31.000Z&AUTOLOGIN_TOKEN=55C593B12A16C069A9F5D223BA90BE890EEE3422A52A2F3057D866AFF24C6C85D5863337E404FAB00825A2E06703E73889F849A9AA18CA3C4E40B5E90A935EBF"


    browser.get(url)

    # Wait for the new window to load
    current_window_handle = browser.current_window_handle

    windows = browser.window_handles
    for window in windows:
        if window != current_window_handle:
            # print('change tab')
            browser.switch_to.window(window)
            break

    sleep(6)
    # Switch to the alert
    alert = browser.switch_to.alert

    # Close the alert
    alert.dismiss()

    # switch to frame
    iframe = browser.find_element(By.NAME, "loginFrm")
    # switch to selected iframe
    browser.switch_to.frame(iframe)

    browser.find_element(By.ID, "PWD").send_keys("PanonikA")
    buttons = browser.find_elements(By.CLASS_NAME, "button")
    buttons[0].click()

    # getByAttribute
    pdfWindow = browser.find_element(By.NAME, "FH0").get_attribute("src")
    browser.get(pdfWindow)

    pdfUrl = browser.find_element(By.ID, "save_pdf_a").get_attribute("href")
    # print(pdfUrl)


    return HttpResponse(pdfUrl)