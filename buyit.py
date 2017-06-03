#!/usr/bin/env python
# encoding: utf-8
from selenium import webdriver
import datetime
import time
import getpass

def do_process(chrome_driver, process):
    if process == "Add Item":
        try:
            chrome_driver.find_element_by_link_text("加入购物车").click()
            return True
        except:
            print("No correspond text label found")
            return False

    if process == "Go Checkout":
        try:
            chrome_driver.find_element_by_link_text("去购物车结算").click()
            return True
        except:
            print("No correspond text label found")
            try:
                chrome_driver.find_element_by_link_text("去结算").click()
                return True
            except:
                print("No correspond text label found")
                try:
                    chrome_driver.find_element_by_id("GotoShoppingCart").click()
                    return True
                except:
                    print("No correspond element found")
                    return False

    if process == "Checkout":
        try:
            chrome_driver.find_element_by_link_text("去结算").click()
            return True
        except:
            print("No correspond text label found")
            try:
                chrome_driver.find_element_by_link_text("去购物车结算").click()
                return True
            except:
                print("No correspond text label found")
                try:
                    chrome_driver.find_element_by_class_name("submit-btn").click()
                    return True
                except:
                    print("No correspond class name found")
                    return False

    if process == "Place Order":
        try:
            chrome_driver.find_element_by_link_text("提交订单").click()
            return True
        except:
            print("No correspond text label found")
            try:
                chrome_driver.find_element_by_id("order-submit").click()
                return True
            except:
                print("No correspond id found")
                try:
                    chrome_driver.find_element_by_class_name("checkout-submit").click()
                    return True
                except:
                    print("No correspond class name found")
                    return False


def login(usr, pwd, chrome_driver):
    chrome_driver.get("http://www.jd.com")
    if chrome_driver.find_element_by_link_text("你好，请登录"):
        chrome_driver.find_element_by_link_text("你好，请登录").click()
    if chrome_driver.find_element_by_link_text("账户登录"):
        chrome_driver.find_element_by_link_text("账户登录").click()
    if chrome_driver.find_element_by_name("loginname"):
        chrome_driver.find_element_by_name("loginname").send_keys(usr)
    if chrome_driver.find_element_by_name("nloginpwd"):
        chrome_driver.find_element_by_name("nloginpwd").send_keys(pwd)
    if chrome_driver.find_element_by_id("loginsubmit"):
        chrome_driver.find_element_by_id("loginsubmit").click()
    time.sleep(1)
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))

def buy_on_time(chrome_driver, buytime):
    chrome_driver.get("https://item.jd.com/3888216.html")
    while True:
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
            while not do_process(chrome_driver, "Add Item"):
                time.sleep(0.1)
            while not do_process(chrome_driver, "Go Checkout"):
                time.sleep(0.1)
            while not do_process(chrome_driver, "Checkout"):
                time.sleep(0.1)
            while not do_process(chrome_driver, "Place Order"):
                time.sleep(0.1)


if __name__ == '__main__':
    username = input("Type in User name here: ")
    password = getpass.getpass("Type in Password here ")
    str_time = input("Type in Start time here, the format is yyyy-mm-dd HH:MM:SS ")
    now = datetime.datetime.now()
    print('Program lauched:', now.strftime('%Y-%m-%d %H:%M:%S'))
    date_time = datetime.datetime.strptime(str_time, "%Y-%m-%d %H:%M:%S")
    ahead_time = (date_time-now).seconds
    # 1 minutes ahead preparation
    time.sleep(ahead_time-60)
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    login(username,password,driver)
    buy_on_time(driver,str_time)
    # buy_on_time('2017-06-03 16:44:05', driver)
