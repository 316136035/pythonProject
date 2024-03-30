from selenium import webdriver
from time import sleep

f = webdriver.Chrome()
f.get("https://passport.jd.com/uc/login")

# 让浏览器保持打开直到手动关闭
input("Press Enter to quit...")
# 或者等待一段时间
# sleep(10)

# 最后记得正常关闭浏览器以释放资源
# f.quit()