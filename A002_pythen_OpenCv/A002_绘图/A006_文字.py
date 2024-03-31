import cv2
from PIL import Image, ImageDraw, ImageFont  #
import numpy as np

# 假设我们有一张OpenCV格式的图像
img_cv = cv2.imread('./images/1.png')

# 将OpenCV格式的图像转换为PIL格式，注意颜色空间转换
img_pil = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)  # OpenCV默认BGR，PIL默认RGB
pil_img = Image.fromarray(img_pil)

# 定义要使用的字体和大小，这里假设你有一个名为“simhei.ttf”的中文字体文件
# 确保该字体文件存在并包含你需要的中文字符集
font_path = "./images/方正粗黑宋简体.TTF"
font_size = 20
font = ImageFont.truetype(font_path, font_size)

# 创建一个ImageDraw对象用于在PIL图像上绘制文本
draw = ImageDraw.Draw(pil_img)

# 定义中文文本、坐标位置以及颜色
text = "中文字符串"
(x_pos, y_pos) = (50, 50)  # 文本左下角的位置坐标
text_color = (0, 0, 255)  # 白色

# 在PIL图像上绘制中文文本
draw.text((x_pos, y_pos), text, fill=text_color, font=font)

# 将添加了文本的PIL图像转换回OpenCV格式
img_cv_with_text = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)  # 从RGB转换回BGR

# 最后保存或显示带有中文文本的图像
cv2.imwrite('output_image.jpg', img_cv_with_text)
# 或者显示在屏幕上
while True:
    cv2.imshow("Text on Image", img_cv_with_text)
    k=cv2.waitKey(0) & 0xFF   # 获取键盘输入
    if k==27:
        break
cv2.destroyAllWindows() # 关闭所有窗口