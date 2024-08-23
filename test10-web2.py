# 论坛系统课堂及其课后练习题库
#
from selenium import webdriver
from time import sleep  # 时间模块 让浏览器等待，便于展示
from selenium.webdriver.common.by import By

'''
# 一、自动登录
# 1、点击登录按钮 # 2、输入用户名，密码，（使用id属性）# 3、点击登录
driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.get("http://127.0.0.1/Discuz/upload/forum.php")

driver.find_element(By.ID, 'ls_username').send_keys('admin')  # id
driver.find_element(By.ID, 'ls_password').send_keys('123456')
driver.find_element(By.XPATH, '//*[@id="lsform"]/div/div/table/tbody/tr[2]/td[3]/button').click()  # 登录
'''

# -----------------
# 二、设置用户的真实姓名   # 1、登录    2、点击设置超链接   3、输入用户名    4、点击保存

'''
driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.get("http://127.0.0.1/Discuz/upload/forum.php")

driver.find_element(By.ID, 'ls_username').send_keys('admin')  # id
driver.find_element(By.ID, 'ls_password').send_keys('123456')
driver.find_element(By.XPATH, '//*[@id="lsform"]/div/div/table/tbody/tr[2]/td[3]/button').click()  # 登录
sleep(1)
driver.find_element(By.XPATH, '//*[@id="um"]/p[1]/strong/a').click()

sleep(1)  # 等待一下
driver.current_window_handle      # 获取当前窗口句柄
win = driver.window_handles
print(win)
driver.switch_to.window(win[1])        # 切换到指定句柄窗口 索引的方式切

sleep(1)  # 等待一下
driver.find_element(By.XPATH, '//*[@id="pcd"]/div/ul[1]/li[4]/a').click()
sleep(1)

driver.find_element(By.XPATH, '//*[@id="td_realname"]/input').send_keys('小王')
driver.find_element(By.XPATH, '//*[@id="profilesubmitbtn"]').click()  # 
'''
# ----------------
# 三、单个注册与连续注册多个  1、点击立即注册  2、输入四个输入框  3、提交  4、实现连续注册10个账号
'''
user = ['aa1121', 'aa1a', 'aa1aa', 's1s1', 'ss1s', 's1sss']
pad = ['123', '12134', '123451', '1234156', '123412', '1213123']
email = ['12111213@qq.com', '12314@qq.com', '123145@qq.com', '1231456@qq.com', '123412@qq.com', '1231123@qq.com']

for i in range(0, 6):
    driver.get("http://127.0.0.1/Discuz/upload/forum.php")
    driver.find_element(By.XPATH, '//*[@id="lsform"]/div/div/table/tbody/tr[2]/td[4]/a').click()  #
    driver.find_element(By.XPATH, '//*[@id="FMjM6T"]').send_keys(user[i])
    driver.find_element(By.XPATH, '//*[@id="RD3S6a"]').send_keys(pad[i])
    driver.find_element(By.XPATH, '//*[@id="2XxNnK"]').send_keys(pad[i])
    driver.find_element(By.XPATH, '//*[@id="5uzNiN"]').send_keys(email[i])
    driver.find_element(By.XPATH, '//*[@id="registerformsubmit"]').click()  #
    sleep(5)
    driver.find_element(By.XPATH, '//*[@id="um"]/p[1]/a[4]').click()  # 退出
    continue
'''
# -----------------------------

'''
# 四、完善个人信息  # 1、登录  # 2、点击设置
# 3、基本资料栏位依次输入内容性别、生日、出生地、居住地、情感状态、交友目的、血型     4、所有信息后的下拉框设置为保密  5、保存
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.get("http://127.0.0.1/Discuz/upload/forum.php")

driver.find_element(By.ID, 'ls_username').send_keys('admin')  # id
driver.find_element(By.ID, 'ls_password').send_keys('123456')  # name
driver.find_element(By.XPATH, '//*[@id="lsform"]/div/div/table/tbody/tr[2]/td[3]/button').click()  # 登录
sleep(1)
driver.find_element(By.XPATH, '//*[@id="um"]/p[1]/a[1]').click()  #
driver.find_element(By.XPATH, '//*[@id="td_realname"]/input').send_keys('小王2')
driver.find_element(By.XPATH, '//*[@id="gender"]/option[2]').click() #性别
driver.find_element(By.XPATH, '//*[@id="birthyear"]/option[45]').click() #生日
driver.find_element(By.XPATH, '//*[@id="birthmonth"]/option[7]').click()
driver.find_element(By.XPATH, '//*[@id="birthday"]/option[19]').click()

driver.find_element(By.XPATH, '//*[@id="td_birthcity"]/a').click() # 修改
sleep(1)
driver.find_element(By.XPATH, '//*[@id="birthprovince"]/option[@did="17"]').click()  #出生地
sleep(1)
driver.find_element(By.XPATH, '//*[@id="birthcity"]/option[@did="267"]').click()
sleep(1)
driver.find_element(By.XPATH, '//*[@id="birthdist"]/option[@did="2890"]').click()
sleep(1)
driver.find_element(By.XPATH, '//*[@id="birthcommunity"]/option[@did="26249"]').click()
sleep(1)

driver.find_element(By.XPATH, '//*[@id="td_residecity"]/a').click()   # 修改
sleep(1)
driver.find_element(By.XPATH, '//*[@id="resideprovince"]/option[@did="10"]').click()  #居住地
sleep(1)
driver.find_element(By.XPATH, '//*[@id="residecity"]/option[@did="166"]').click()
sleep(1)
driver.find_element(By.XPATH, '//*[@id="residedist"]/option[@did="2072"]').click()
sleep(1)
driver.find_element(By.XPATH, '//*[@id="residecommunity"]/option[@did="14283"]').click()

driver.find_element(By.XPATH, '//*[@id="td_affectivestatus"]/input').send_keys('单') #情感状态
driver.find_element(By.XPATH, '//*[@id="td_lookingfor"]/input').send_keys('一起打游戏') #交友目的
driver.find_element(By.XPATH, '//*[@id="td_bloodtype"]/select/option[3]').click()  #血型

driver.find_element(By.XPATH, '//*[@id="tr_realname"]/td[2]/select/option[3]').click()
driver.find_element(By.XPATH, '//*[@id="tr_gender"]/td[2]/select/option[3]').click()
driver.find_element(By.XPATH, '//*[@id="tr_birthday"]/td[2]/select/option[3]').click()
driver.find_element(By.XPATH, '//*[@id="tr_birthcity"]/td[2]/select/option[3]').click()
driver.find_element(By.XPATH, '//*[@id="tr_residecity"]/td[2]/select/option[3]').click()
driver.find_element(By.XPATH, '//*[@id="tr_affectivestatus"]/td[2]/select/option[3]').click()
driver.find_element(By.XPATH, '//*[@id="tr_lookingfor"]/td[2]/select/option[3]').click()
driver.find_element(By.XPATH, '//*[@id="tr_bloodtype"]/td[2]/select/option[3]').click()

sleep(1)
driver.find_element(By.XPATH, '//*[@id="profilesubmitbtn"]').click()  # 保存

'''
