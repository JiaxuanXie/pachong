from selenium import webdriver
import time #控制程序休眠时间
import csv
import study

def search_product(key):
    # 搜索商品
    driver.get('https://www.tmall.com//')
    driver.find_element_by_id('mq').send_keys(key)
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[2]/form/fieldset/div/button').click()
    driver.implicitly_wait(10)  # 隐式等待10s，等待页面渲染
    driver.maximize_window()  # 最大化浏览器
    time.sleep(3)
    # # 多选品牌
    # driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/form/div/div[1]/div/div[2]/div[2]/a[1]').click()
    # time.sleep(1)
    # driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/form/div/div[1]/div/div[2]/ul/li[1]/a').click()
    # time.sleep(1)
    # driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/form/div/div[1]/div/div[2]/ul/li[2]/a').click()
    # time.sleep(1)
    # driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/form/div/div[1]/div/div[2]/ul/li[3]/a').click()
    # time.sleep(1)
    # driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/form/div/div[1]/div/div[2]/ul/li[4]/a').click()
    # time.sleep(1)
    # driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/form/div/div[1]/div/div[2]/ul/li[5]/a').click()
    # time.sleep(1)
    # driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/form/div/div[1]/div/div[2]/ul/li[7]/a').click()
    # time.sleep(1)
    # driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/form/div/div[1]/div/div[2]/ul/li[8]/a').click()
    # time.sleep(1)
    # driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/form/div/div[1]/div/div[2]/ul/li[9]/a').click()
    # time.sleep(1)
    # driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/form/div/div[1]/div/div[2]/div[3]/a[1]').click()
    # time.sleep(1)

    # # 解决登录
    # driver.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys(study.USERNAME)
    # time.sleep(2)
    # driver.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys(study.PASSWORD)
    # time.sleep(2)
    # driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[1]/div/div[2]/div/form/div[4]/button').click()
    # driver.implicitly_wait(10)

    # driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[4]/a[4]').click()
    # time.sleep(1)

def get_data():
    divs = driver.find_elements_by_xpath('//div[@id="J_ItemList"]/div[@class="product  "]/div[@class="product-iWrap"]')
    #print(divs)
    for div in divs:
        pic_link1 = div.find_element_by_xpath('.//div[@class="productImg-wrap"]/a[@class="productImg"]/img').get_attribute('src')
        info = div.find_element_by_xpath('.//p[@class="productTitle"]/a').text
        pic_link2 = div.find_element_by_xpath('.//div[@class="productImg-wrap"]/a[@class="productImg"]/img').get_attribute('data-ks-lazyload')
        price = div.find_element_by_xpath('.//p[@class="productPrice"]/em').text
        sales = div.find_element_by_xpath('.//p[@class="productStatus"]/span/em').text
        shop = div.find_element_by_xpath('.//div[@class="productShop"]/a').text
        pro_link = div.find_element_by_xpath('.//div[@class="productImg-wrap"]/a[@class="productImg"]').get_attribute('href')
        print(pic_link1, info, pic_link2, price, sales, shop, pro_link, sep='|')
        time.sleep(1)
        with open('basketball_shoes2.csv', mode='a+', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow([pic_link1, info, pic_link2, price, sales, shop, pro_link])

'''def main():'''

if __name__ == '__main__':
    driver = webdriver.Firefox()
    keyword = input('请输入你要搜索的商品名字：')
    search_product(keyword)
    get_data()
    time.sleep(2)

    page_num = 1
    while page_num != 3:
        print('*' * 100)
        print('正在爬取第{}页数据'.format(page_num + 1))
        print('*' * 100)
        driver.get('https://list.tmall.com/search_product.htm?&brand=20578,3329161,20579,3424764,20581,20592,20069292,31840&s={}&q=%C0%BA%C7%F2%D0%AC&sort=d'.format(page_num * 60))
        driver.implicitly_wait(10)
        get_data()
        time.sleep(2)
        page_num += 1

