from selenium import webdriver
from time import sleep  # 时间模块 让浏览器等待，便于展示
from selenium.webdriver.common.by import By

'''
# 框架的切换
driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.get("file:///D:/CarTest/web/Register.html")

driver.find_element(By.ID, 'user').send_keys('admin')

driver.switch_to.frame("idframe1") # 父切子   参数用idid=‘idframe1’

driver.find_element(By.ID, 'userA').send_keys('adminA')

# 子切子必须先转回父
driver.switch_to.parent_frame()   # 子切父
driver.find_element(By.XPATH, '//*[@id="zc"]/a[1]').click()

driver.switch_to.frame("idframe2") # 父切子

driver.find_element(By.ID, 'userB').send_keys('userB')
sleep(4)
'''
# =================================================================================
'''
driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.get("file:///D:/CarTest/web/Register.html")

driver.find_element(By.ID, 'user').send_keys('admin')

driver.find_element(By.XPATH, '//*[@id="idframe1"]').click()    # 没有ID 无法使用driver.switch_to.frame("ID")的话
driver.find_element(By.XPATH, '//*[@id="userA"]').send_keys('adminA')

# driver.find_element(By.XPATH, '//*[@id="zc"]/a[1]').click()
#
# driver.find_element(By.XPATH, '//*[@id="idframe2"]').click()  # 直接点网页
# driver.find_element(By.ID, 'userB').send_keys('userB')
sleep(4)
'''

# ============================================断言
'''
driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.get("http://127.0.0.1/Discuz/upload/forum.php")

driver.find_element(By.ID, 'ls_username').send_keys('admin')  # id
driver.find_element(By.ID, 'ls_password').send_keys('123456')
driver.find_element(By.XPATH, '//*[@id="lsform"]/div/div/table/tbody/tr[2]/td[3]/button').click()  # 登录
sleep(1)
driver.find_element(By.XPATH, '//*[@id="chart"]/div/a[1]').click()

driver.find_element(By.XPATH, '//*[@id="ct"]/div[1]/div[2]/ul/li[4]/a').click()   # 发帖
sleep(1)

driver.find_element(By.XPATH, '//*[@id="block_group"]/p[2]/a').click()
sleep(1)
driver.find_element(By.XPATH, '//*[@id="block_forum"]/p/a').click()
sleep(1)
driver.find_element(By.XPATH, '//*[@id="postbtn"]').click()
sleep(1)

driver.find_element(By.XPATH, '//*[@id="subject"]').send_keys('那个明星最漂亮？')

driver.switch_to.frame('e_iframe')  # 切子
driver.find_element(By.XPATH, '/html/body[@contenteditable="true"]').send_keys('都一样都一样')
driver.switch_to.parent_frame()  # 回父

driver.find_element(By.XPATH, '//*[@id="postsubmit"]').click()

sleep(3)
driver.quit()
'''

# ========================================断言 assert 预期==实际 没问题不会报错

'''
driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.get("http://127.0.0.1/Discuz/upload/forum.php")

driver.find_element(By.ID, 'ls_username').send_keys('admin')  # id
driver.find_element(By.ID, 'ls_password').send_keys('123456')
driver.find_element(By.XPATH, '//*[@id="lsform"]/div/div/table/tbody/tr[2]/td[3]/button').click()  # 登录
sleep(1)
driver.find_element(By.XPATH, '//*[@id="chart"]/div/a[1]').click()

driver.find_element(By.XPATH, '//*[@id="ct"]/div[1]/div[2]/ul/li[4]/a').click()  # 发帖
sleep(1)

driver.find_element(By.XPATH, '//*[@id="block_group"]/p[2]/a').click()
sleep(1)
driver.find_element(By.XPATH, '//*[@id="block_forum"]/p/a').click()
sleep(1)
driver.find_element(By.XPATH, '//*[@id="postbtn"]').click()
sleep(1)

driver.find_element(By.XPATH, '//*[@id="subject"]').send_keys('那个明星最漂亮？')

driver.switch_to.frame('e_iframe')  # 切子
driver.find_element(By.XPATH, '/html/body[@contenteditable="true"]').send_keys('都一样都一样')
driver.switch_to.parent_frame()  # 回父

driver.find_element(By.XPATH, '//*[@id="postsubmit"]').click()

a = driver.find_element(By.XPATH, '//*[@id="thread_subject"]').text

sleep(1)

assert a == '那个明星最漂亮？'
'''
# -----------------------------------------------------------------------
# 登录名鹰OA系统 http://192.168.8.57:8080/QzhOA/login
# 完成  新增会议、断言、
'''driver = webdriver.Chrome()
driver.get("http://192.168.8.57:8080/QzhOA/login")

# driver.find_element(By.NAME, 'username').send_keys('admin')
# driver.find_element(By.NAME, 'password').send_keys('123456')
driver.find_element(By.ID, 'btnSubmit').click()  # 登录
sleep(1)
driver.find_element(By.XPATH, '//ul[@id="side-menu"]/li[7]/a/span[1]').click()  # 会议管理
sleep(1)
driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[7]/ul/li/a').click()
sleep(1)

driver.switch_to.frame('iframe21')  # 切子
driver.find_element(By.XPATH, '//*[@id="toolbar"]/a[1]').click()  # 新增会议
sleep(2)

driver.switch_to.frame('layui-layer-iframe1')  # 切子

driver.find_element(By.XPATH, '//*[@id="meetingTheme"]').send_keys('环保4')
driver.find_element(By.XPATH, '//*[@id="meetingAddr"]').send_keys('上海')
driver.find_element(By.XPATH, '//*[@id="form-meeting-add"]/div[4]/div/div[2]/div[3]/div[3]/p').send_keys('哈哈哈哈哈哈')

driver.switch_to.parent_frame()
driver.find_element(By.XPATH, '//*[@id="layui-layer1"]/div[3]/a[1]').click()  # 确定

sleep(2)
driver.find_element(By.XPATH, '//*[@id="notice-form"]/div/ul/li[1]/input[@name="meetingTheme"]').send_keys("环保4")
driver.find_element(By.XPATH, '//*[@id="notice-form"]/div/ul/li[7]/a[1]').click()
sleep(1)

a = driver.find_element(By.XPATH, '//*[@id="bootstrap-table"]/tbody/tr[1]/td[3]').text

print(a)
assert a == '环保4'
sleep(5)

# driver.quit()
'''
# -------------------------------------------
# 修改会议、断言

'''
driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.get("http://192.168.8.57:8080/QzhOA/login")

# driver.find_element(By.NAME, 'username').send_keys('admin')
# driver.find_element(By.NAME, 'password').send_keys('123456')
driver.find_element(By.ID, 'btnSubmit').click()  # 登录
sleep(1)
driver.find_element(By.XPATH, '//ul[@id="side-menu"]/li[7]/a/span[1]').click()  # 会议管理
sleep(1)
driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[7]/ul/li/a').click()

sleep(1)
driver.switch_to.frame('iframe21')  # 切子
sleep(1)
driver.find_element(By.XPATH, '//*[@id="bootstrap-table"]/tbody/tr[1]/td[10]/a[1]').click()  # 修改会议
sleep(2)

driver.switch_to.frame('layui-layer-iframe1')  # 切子
driver.find_element(By.XPATH, '//*[@id="meetingTheme"]').clear()
driver.find_element(By.XPATH, '//*[@id="meetingTheme"]').send_keys('东方闪电的速度2')
sleep(1)

driver.switch_to.parent_frame()
# driver.switch_to.frame('layui-layer-iframe1')  # 切子
driver.find_element(By.XPATH, '//*[@id="layui-layer1"]/div[3]/a[1]').click()  # 确定

sleep(2)
a = driver.find_element(By.XPATH, '//*[@id="bootstrap-table"]/tbody/tr[1]/td[3]').text
print(a)
assert a == '东方闪电的速度1'
sleep(3)
driver.quit()
'''
# --------------------------------
# 删除会议、断言
driver = webdriver.Chrome()
driver.get("http://192.168.8.57:8080/QzhOA/login")

# driver.find_element(By.NAME, 'username').send_keys('admin')
# driver.find_element(By.NAME, 'password').send_keys('123456')
driver.find_element(By.ID, 'btnSubmit').click()  # 登录
sleep(1)
driver.find_element(By.XPATH, '//ul[@id="side-menu"]/li[7]/a/span[1]').click()  # 会议管理
sleep(1)
driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[7]/ul/li/a').click()
# --------
driver.switch_to.frame('iframe21')  # 切子
driver.find_element(By.XPATH, '//*[@id="notice-form"]/div/ul/li[1]/input[@name="meetingTheme"]').send_keys("环保2")
driver.find_element(By.XPATH, '//*[@id="notice-form"]/div/ul/li[7]/a[1]').click()
sleep(1)


i = driver.find_element(By.XPATH, '//*[@id="bootstrap-table"]/tbody/tr[1]/td[3]').text
driver.find_element(By.XPATH, '//*[@id="bootstrap-table"]/tbody/tr[1]/td[10]/a[2]').click()  # 删除
sleep(2)

driver.find_element(By.CLASS_NAME, 'layui-layer-btn0').click()
sleep(1)
print(i)
assert i == "环保2"

sleep(5)

driver.quit()
