from selenium import webdriver
from time import sleep  # 时间模块 让浏览器等待，便于展示
from selenium.webdriver.common.by import By

# Chrome("webdriver驱动绝对路径")  和谷歌浏览器放在一起
# driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")
# driver.get("https://www.baidu.com/")

# ---------------------------------------------------------------------------------------
# 伪装
# from selenium import webdriver
#
# option = webdriver.ChromeOptions()
# Chrome_driver = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
# option.add_experimental_option('excludeSwitches', ['enable-automation'])
# option.add_experimental_option('useAutomationExtension', False)
# driver = webdriver.Chrome(Chrome_driver, options=option)
# driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
#                        {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})
# url = "https://www.baidu.com"
# driver.get(url)
# =========================================================================================

from selenium import webdriver
from time import sleep  # 时间模块 让浏览器等待，便于展示
from selenium.webdriver.common.by import By

#
driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.get("file:///C:/Users/admin/Desktop/mingying.html")
# 对元素操作   优先使用id,name,XPATH
# driver.find_element(By.ID, 'input_01').send_keys('admin')    # id
# driver.find_element(By.NAME, 'input_02').send_keys('123456')   # name
# driver.find_element(By.CLASS_NAME, 'sk').click()           # class
# driver.find_element(By.TAG_NAME, 'p').click()           # tag 通过标签定义元素 <p></p>
# driver.find_element(By.LINK_TEXT, '百度一下').click()           # 链接的所有文本，不能少  <a>百度一下</a>
# driver.find_element(By.PARTIAL_LINK_TEXT, '百度').click()           # 链接的部分文本 <a>百度一下</a>
'''
driver.find_element(By.XPATH, '/html/body/select/option[3]').click()    # XPATH 绝对路径
driver.find_element(By.XPATH, '//select/option[2]').click()    # XPATH 相对路径
driver.find_element(By.XPATH, '//div[@id="su"]/input[@name="01"]').click()    # XPATH 相对路径加标签属性    //input[@属性='值']
# XPATH 模糊定位starts-with:id=input_01   '//标签[starts-with(@属性，值)]'
driver.find_element(By.XPATH, '//input[starts-with(@id,input)]').send_keys('eeeee')
# XPATH 模糊定位contains:id=input_01      //标签[contains(@属性，"值")]
driver.find_element(By.XPATH, '//input[contains(@id,"input")]').send_keys('wwww')
# XPATH 模糊定位contains:text()      //标签[contains(text()，"值")]
driver.find_element(By.XPATH, '//a[contains(text(),"百度一下")]').click()

# driver.find_element(By.NAME, 'input_02').clear()   # 清空
'''

# sleep(5)   # 等待5秒再操作
# 对网页的操作
# driver.quit() # 退出当前网页
# driver.close() # 关闭浏览器

# =========================================================================

# 定位一组元素
str1 = driver.find_elements(By.XPATH, '//select/option')
str1[2].click()  # 再选择元素操作
print(str1[2])

# =========================================================================

# 切窗口

sleep(2)  # 等待一下
driver.window_handles  # 获取所有窗口句柄
sleep(2)
winh = driver.current_window_handle  # 获取当前窗口句柄
print(winh)
driver.switch_to.window(winh[1])  # 切换到指定句柄窗口 索引的方式切
3
# ========================================================等待
# 强制等待  写在操作里
sleep()

# 隐式等待
driver.implicitly_wait(10)  # 写在开头 每个操作10秒

# 显式等待  写在开头
# 整个这句话的意思是，在5秒时间内，每隔0.5秒去定位一次元素(id="kw"的元素)。
# 如果5秒内能定位到，则继续执行；定位失败，则报错
WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, "kw")))


