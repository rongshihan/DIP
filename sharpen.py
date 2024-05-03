import cv2
import numpy as np
import matplotlib.pyplot as plt


def sharpen(img_path, method):
    """
    实现锐化
    :param img_path: 图片路径
    :param method: 锐化方法名称
    :return:
    """
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    # 读取图像
    image = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), 1)

    sharpened_img = None
    if method == '普通锐化':
        # 转换为浮点类型以进行数学运算
        image_float = np.float32(image) + 128.0

        # 普通锐化：简单地将图像与自身相减
        sharpened_img = cv2.addWeighted(image_float, 1.5, -image_float, 0.5, 0)

        # 转换回8位无符号整数
        sharpened_img = np.uint8(np.clip(sharpened_img, 0, 255))
    elif method == '拉普拉斯锐化':
        # 应用拉普拉斯锐化
        laplacian = cv2.Laplacian(image, cv2.CV_64F)

        # 将结果转换为8位无符号整数
        sharpened_img = cv2.convertScaleAbs(laplacian)
    elif method == '模板锐化':
        # 定义一个锐化模板
        kernel = np.array([[-1, -1, -1],
                           [-1, 9, -1],
                           [-1, -1, -1]])

        # 应用模板锐化
        sharpened_img = cv2.filter2D(image, -1, kernel)

    # 绘制子图
    fig, ax = plt.subplots(1, 2, figsize=(15, 10))
    # 绘制处理后的图像
    ax[0].imshow(image, cmap='gray')
    ax[0].set_title('原图像')
    ax[0].axis('off')
    ax[1].imshow(sharpened_img, cmap='gray')
    ax[1].set_title(method)
    ax[1].axis('off')

    plt.tight_layout()  # 确保子图之间不会重叠

    return sharpened_img, fig


if __name__ == "__main__":
    sharpen('pout.tif', '模板锐化')
