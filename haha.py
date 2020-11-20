from appium import webdriver
import time
import redis
red = redis.Redis(host='94.191.56.13',port=6379,db=8,password='123123')
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = '8bb70'
desired_caps['appPackage'] = 'com.eg.android.AlipayGphone'
desired_caps['appActivity'] = '.AlipayLogin'
desired_caps['noReset'] = 'true'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element_by_id('com.alipay.android.phone.wealth.home:id/tab_description').click()
zhangdan = driver.find_element_by_xpath(
    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TabHost/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[5]/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout')
zhangdan.click()
def get_data():
    driver.swipe(300, 400, 300, 900,1000)   #下拉刷新
    time.sleep(0.5)
    datas = driver.find_elements_by_id("com.alipay.mobile.bill.list:id/listItem")
    for data in datas:
        data.click()
        info = driver.find_elements_by_class_name('android.view.View')
        payer = info[4].text
        paymoney = info[5].text
        paystate = info[6].text
        paytime = info[17].text
        paynumber = info[20].text
        list = [paynumber,paymoney,payer,paytime,paystate]
        sl = ",".join(list)
        print(sl)

        time.sleep(1)
        driver.back()
        red.sadd("zhifubaole",sl)
        if red.sismember("zhifubaole",sl):  #如果集合里面有这个元素直接跳出循环重新刷新索引页
            break
while True:
    get_data()
    time.sleep(2)
