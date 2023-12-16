import os
from PIL import Image

# 设置您要转换图像的文件夹路径
folder_path = 'compare'

# 遍历文件夹
for subdir, dirs, files in os.walk(folder_path):
    for file in files:
        # 检查文件是否为图像
        if file.lower().endswith(('.png', '.bmp', '.jpeg', '.gif')):
            # 构建完整的文件路径
            file_path = os.path.join(subdir, file)
            # 打开图像
            with Image.open(file_path) as img:
                # 删除alpha通道
                if img.mode in ('RGBA', 'LA'):
                    fill_color = 'white'  # 或者是你想要的任何颜色
                    background = Image.new(img.mode[:-1], img.size, fill_color)
                    background.paste(img, img.split()[-1])
                    img = background
                # 转换图像为JPEG
                rgb_im = img.convert('RGB')
                # 构建新的文件名和路径
                new_file_path = os.path.splitext(file_path)[0] + '.jpg'
                # 保存转换后的文件
                rgb_im.save(new_file_path, 'JPEG')
                # 如果你想删除原始文件，取消注释下面的行
                # os.remove(file_path)



