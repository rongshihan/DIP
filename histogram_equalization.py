import numpy as np
import cv2
import matplotlib.pyplot as plt


# 本类实现直方图均衡化
def histogram_equalization(img_path):
    """
    直方图均衡化
    :param img_path: 图像路径
    :return:
    """
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
    plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号
    # 读取图像
    image = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), 0)

    # 直方图均衡化
    equalized_image = cv2.equalizeHist(image)

    # 计算原图像的直方图
    hist, bins = np.histogram(image.flatten(), 256, (0, 256))
    bins_centers = 0.5 * (bins[1:] + bins[:-1])

    # 计算均衡化后图像的直方图
    hist_equalized, _ = np.histogram(equalized_image.flatten(), 256, (0, 256))

    # 创建matplotlib的Figure和Axes对象
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))

    # 在第一个Axes对象上绘制原图像
    axs[0, 0].imshow(image, cmap='gray')
    axs[0, 0].set_title('原始图像')
    axs[0, 0].axis('off')

    # 在第二个Axes对象上绘制均衡化后的图像
    axs[0, 1].imshow(equalized_image, cmap='gray')
    axs[0, 1].set_title('均衡化后的图像')
    axs[0, 1].axis('off')

    # 在第三个Axes对象上绘制原图像的直方图
    axs[1, 0].plot(bins_centers, hist, color='gray')
    axs[1, 0].set_title('原始图像的直方图')
    axs[1, 0].set_xlabel('像素强度')
    axs[1, 0].set_ylabel('频率')
    axs[1, 0].set_xlim([0, 256])
    axs[1, 0].grid(True)

    # 在第四个Axes对象上绘制均衡化后图像的直方图
    axs[1, 1].plot(bins_centers, hist_equalized, color='gray')
    axs[1, 1].set_title('均衡化后的直方图')
    axs[1, 1].set_xlabel('像素强度')
    axs[1, 1].set_ylabel('频率')
    axs[1, 1].set_xlim([0, 256])
    axs[1, 1].grid(True)

    plt.tight_layout()  # 确保子图之间不会重叠

    return equalized_image, fig


if __name__ == "__main__":
    histogram_equalization('pout.tif')
