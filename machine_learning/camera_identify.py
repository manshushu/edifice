import cv2

# from center_crop_2 import center_crop
# from black_white_3 import black_white
# from flat_image_4 import flat_image
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("debug.h5")
if __name__ == "__main__":
    cap = cv2.VideoCapture(0)  # 打开本机的摄像头
    while True:
        flag, img = cap.read()  # flag是否读取了图片
        if flag:
            # cropped_img = center_crop(frame)
            # black_white_img = black_white(frame)
            # flattened_img = flat_image(black_white_img)
            # predicions = model.predict(flattened_img)
            img_width = img.shape[1]
            img_height = img.shape[0]
            col_start = int((img_width - img_height) / 2)
            col_end = int(col_start + img_height)
            cropped_img = img[:, col_start:col_end, :]
            gray_img = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)
            (thresh, black_white) = cv2.threshold(
                gray_img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU
            )
            black_white = cv2.bitwise_not(black_white)
            black_white = cv2.resize(black_white, (28, 28))
            black_white = black_white / 255
            black_white = black_white.reshape(-1, 28, 28, 1)
            prediction = model.predict(bla)
            status = np.argmax(prediction)
            print(status)
            cv2.putText(
                img,
                status.astype(str),
                (30, 60),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2,
            )
            cv2.imshow("number", img)
            key = cv2.waitKey(0)  # 整除，时间单位为1ms
            cv2.destroyAllWindows()
            cap.release()
