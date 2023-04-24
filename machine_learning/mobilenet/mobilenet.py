import cv2
import tensorflow as tf

# 加载预训练模型
model = tf.keras.applications.MobileNetV2(weights='imagenet')

# 加载图像
image = cv2.imread('./yolo/image.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = cv2.resize(image, (224, 224))
image = tf.keras.preprocessing.image.img_to_array(image)
image = tf.keras.applications.mobilenet_v2.preprocess_input(image)

# 运行预测
predictions = model.predict(image.reshape(1, 224, 224, 3))

# 解析预测结果
results = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=5)[0]
for result in results:
    print(result[1], result[2])

# 在图像上标注检测到的物体
for result in results:
    label = result[1]
    score = result[2]
    if score > 0.5:
        (startX, startY, endX, endY) = (0, 0, 0, 0) # 需要根据模型输出调整矩形框位置和大小
        cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
        cv2.putText(image, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# 显示带有标注的图像
cv2.imshow('Object Detection', image)
cv2.waitKey(0)