import cv2
import numpy as np
import pytesseract

# 设置识别语言为英文
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
custom_config = r'-l eng --oem 3 --psm 6'

def plate_detection(image):
    # 转换为灰度图像
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 提取水平和垂直方向上的图像边缘
    dx = cv2.Sobel(gray_img, cv2.CV_32F, 1, 0)
    dy = cv2.Sobel(gray_img, cv2.CV_32F, 0, 1)
    
    # 取绝对值
    dx = cv2.convertScaleAbs(dx)
    dy = cv2.convertScaleAbs(dy)
    
    # 结合水平方向和垂直方向的边缘
    edge_img = cv2.addWeighted(dx, 0.5, dy, 0.5, 0)
    
    # 使用二值化处理，生成二值图像
    _, threshold_img = cv2.threshold(edge_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # 膨胀操作，提升连通性
    kernel = np.ones((3, 3), np.uint8)
    morph_img = cv2.morphologyEx(threshold_img, cv2.MORPH_DILATE, kernel)
    
    # 在图像中查找指定形状的轮廓，这里是一个矩形
    contours, hierarchy = cv2.findContours(morph_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # 定位最大轮廓区域，即车牌所在的位置。因为矩形面积是宽*高，因此定位最大矩形区域即定位车牌位置
    max_area = 0
    plate_rect = None
    
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            plate_rect = cv2.boundingRect(contour)
    
    # 返回车牌位置矩形框
    return plate_rect

def segment_characters(image, plate_rect):
    # 裁剪出车牌区域
    x, y, w, h = plate_rect
    plate_image = image[y:y+h, x:x+w]
    
    # 将车牌进行腐蚀操作
    kernel = np.ones((3,3), np.uint8)
    eroded_plate_image = cv2.erode(plate_image, kernel, iterations=1)
    
    # 将车牌转换为灰度图像
    gray_img = cv2.cvtColor(eroded_plate_image, cv2.COLOR_BGR2GRAY)
    
    # 使用二值化处理，生成二值图像
    _, threshold_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # 使用开操作去除噪点
    kernel = np.ones((3,3), np.uint8)
    opening_img = cv2.morphologyEx(threshold_img, cv2.MORPH_OPEN, kernel)
    
    # 查找图像中轮廓
    contours, hierarchy = cv2.findContours(opening_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # 裁剪并保存识别出的字符
    segments = []
    for contour in contours:
        contour_rect = cv2.boundingRect(contour)
        x1, y1, w1, h1 = contour_rect
        aspect_ratio = w1 / h1
        if 0.2 < aspect_ratio < 1.0:
            segment = opening_img[y1:y1+h1, x1:x1+w1]
            segments.append(segment)
    
    #返回字符片段
    return segments

def recognize_characters(segments):
    # 识别每个字符
    characters = []
    for segment in segments:
        character = pytesseract.image_to_string(segment, config=custom_config).strip()
        characters.append(character)
    
    # 返回所有字符
    return characters

def recognize_color(image):
    #将图像从BGR颜色空间转换到HSV颜色空间
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # 设置HSV颜色阈值上下限值
    lower_blue = np.array([100, 43, 46])
    upper_blue = np.array([124, 255, 255])
    
    # 筛选符合指定颜色范围的像素点
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # 计算符合条件像素点的数量，设定数量阈值以确定车牌颜色
    pixel_count = cv2.countNonZero(mask)
    
    # 如果符合条件像素点的数量大于设定阈值，则返回蓝色车牌，否则返回黄色车牌
    if pixel_count > 2000:
        return 'blue'
    else:
        return 'yellow'

def recognize_plate(image):
    # 定位车牌位置
    plate_rect = plate_detection(image)
    
    # 分割字符
    segments = segment_characters(image, plate_rect)
    
    # 识别字符
    characters = recognize_characters(segments)
    
    # 识别车牌颜色
    color = recognize_color(image)
    
    # 将字符和车牌颜色组合起来得到最终的车牌号码
    plate_number = ''.join(characters) + ' ' + color
    
    return plate_number

# 读入图像
image = cv2.imread('car1.jpg')

# 显示OpenCV版本
print('OpenCV version:', cv2.__version__)

# 车牌识别
plate_number = recognize_plate(image)

# 显示识别结果
print('车牌号码为：', plate_number)
