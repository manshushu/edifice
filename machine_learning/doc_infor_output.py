import os
import pandas as pd
from PIL import Image

# 定义需要获取信息的文件夹路径
folder_path = 'C:/Users/m0815/Downloads/dogs-vs-cats/train/train'

# 获取所有文件名
file_names = os.listdir(folder_path)

# 创建空的DataFrame
file_info_df = pd.DataFrame(columns=['filename', 'path', 'extension', 'size', 'channels', 'width', 'height'])

# 遍历所有文件
for file_name in file_names:
    # 获取文件路径
    file_path = os.path.join(folder_path, file_name)
    
    # 获取文件扩展名
    extension = os.path.splitext(file_name)[1]
    
    # 获取文件大小
    size = os.path.getsize(file_path)
    
    # 如果是图片，获取图片信息
    if extension.lower() in ['.jpg', '.jpeg', '.png', '.bmp']:
        with Image.open(file_path) as img:
            channels = len(img.getbands())
            width, height = img.size
    else:
        channels, width, height = None, None, None
    
    # 将文件信息添加到DataFrame
    file_info_df = file_info_df.append({'filename': file_name,
                                        'path': file_path,
                                        'extension': extension,
                                        'size': size,
                                        'channels': channels,
                                        'width': width,
                                        'height': height}, ignore_index=True)

# 将DataFrame保存为csv文件
file_info_df.to_csv('file_info.csv', index=False)
