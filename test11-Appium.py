from time import sleep  # 时间模块 让浏览器等待，便于展示
import selenium
from appium import webdriver
from appium.webdriver.common.appiumby import By
from appium.webdriver.common.appiumby import AppiumBy

'''# 初始化参数
desired_caps = {
    'platformName': 'Android',  # 手机系统
    'platformVersion': '7.1.2',  # 系统版本号
    'deviceName': '127.0.0.1:5554',  # 设备名，可以通过adb devices命令获取
    'appPackage': 'com.android.settings',  # 要测试的APP的Package名称(包名)
    'appActivity': '.Settings'
    # 'appPackage': 'com.android.launcher3',  # 要测试的APP的Package名称(包名)
    # 'appActivity': '.Launcher'
    # 'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
    # 'noReset': True,
    # 'newCommandTimeout': 6000,
}

# 输入中文无效，在前置代码添加以下两行
# desired_caps['unicodeKeyboard'] = True
# desired_caps['resetKeyboard'] = True

# 和web自动化一样的设置驱动，会自动打开模拟器到指定页面   ip和端口看自己连接的
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(10)

# driver.find_element(AppiumBy.ID, 'android.widget.FrameLayout').click() # 点击文件夹
#
# driver.find_element(By.CLASS_NAME, 'android.widget.TextView').click() # 点设置

# driver.start_activity("com.sky.jisuanji",".JisuanjizixieActivity")
#

driver.find_element(AppiumBy.ID, 'com.android.settings:id/search').click()  # 点搜索框
sleep(1)

driver.find_element(AppiumBy.ID, 'android:id/search_src_text').send_keys('百年')  # 搜索
'''


'''# 初始化参数
desired_caps = {
    'platformName': 'Android',  # 手机系统
    'platformVersion': '7.1.2',  # 系统版本号
    'deviceName': '127.0.0.1:5554',  # 设备名，可以通过adb devices命令获取
    # 'appPackage': 'com.android.settings',  # 要测试的APP的Package名称(包名)
    # 'appActivity': '.Settings'
    'appPackage': 'com.android.launcher3',  # 要测试的APP的Package名称(包名)
    'appActivity': '.Launcher'
    # 'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
    # 'noReset': True,
    # 'newCommandTimeout': 6000,
}

# 输入中文无效，在前置代码添加以下两行
# desired_caps['unicodeKeyboard'] = True
# desired_caps['resetKeyboard'] = True

# 和web自动化一样的设置驱动，会自动打开模拟器到指定页面   ip和端口看自己连接的
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(10)

driver.find_element(AppiumBy.name, '高德地图').click()


# driver.start_activity("com.sky.jisuanji",".JisuanjizixieActivity")
#
'''


# 初始化参数
desired_caps = {
    'platformName': 'Android',  # 手机系统
    'platformVersion': '7.1.2',  # 系统版本号
    'deviceName': '127.0.0.1:5554',  # 设备名，可以通过adb devices命令获取
    'appPackage': 'com.autonavi.minimap',  # 要测试的APP的Package名称(包名)
    'appActivity': 'com.autonavi.map.activity.SplashActivity',
    'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
    # 'noReset': True,
    # 'newCommandTimeout': 6000,
}

# 输入中文无效，在前置代码添加以下两行
# desired_caps['unicodeKeyboard'] = True
# desired_caps['resetKeyboard'] = True

# 和web自动化一样的设置驱动，会自动打开模拟器到指定页面   ip和端口看自己连接的
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(10)

driver.find_element(By.ID, 'com.autonavi.minimap:id/agree').click()


driver.find_element(By.ID, 'com.autonavi.minimap:id/enter_amap').click()

# driver.start_activity("com.sky.jisuanji",".JisuanjizixieActivity")
#
# =================================================================



