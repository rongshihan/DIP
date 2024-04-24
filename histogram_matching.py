import cv2
import matplotlib.pyplot as plt
import numpy as np


# 本类实现直方图规定化
def histogram_matching(origin_path, reference_path):
    """
    直方图规定化
    :param origin_path: 原图像路径
    :param reference_path: 参照图像路径
    :return:
    """
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
    plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

    # 读取原图像和参照图像
    # 读取图像
    org_img = cv2.imdecode(np.fromfile(origin_path, dtype=np.uint8), 1)
    ref_img = cv2.imdecode(np.fromfile(reference_path, dtype=np.uint8), 1)

    # 计算两个图像的直方图
    org_hist, bins = np.histogram(org_img.flatten(), 256, (0, 256))
    ref_hist, bins = np.histogram(ref_img.flatten(), 256, (0, 256))

    # 计算累积分布函数(cdf)
    org_cdf = org_hist.cumsum()
    ref_cdf = ref_hist.cumsum()

    # 归一化累积分布函数到0-255之间
    org_cdf = (org_cdf / org_cdf[-1]) * 255
    ref_cdf = (ref_cdf / ref_cdf[-1]) * 255

    # 创建一个映射表，将源图的亮度值映射到参照图的亮度值
    histogram_map = np.zeros(256, dtype=np.uint8)
    for i in range(256):
        closest_value_index = np.abs(ref_cdf - org_cdf[i]).argmin()
        histogram_map[i] = closest_value_index

    # 应用映射表到源图像
    mat_img = cv2.LUT(org_img, histogram_map)

    # 绘图展示
    fig, axs = plt.subplots(2, 3, figsize=(15, 10))  # 修改为2x3子图布局

    # 原始图像
    axs[0, 0].imshow(org_img, 'gray')
    axs[0, 0].set_title('原始图像')
    axs[0, 0].axis('off')

    # 参照图像
    axs[0, 1].imshow(ref_img, 'gray')
    axs[0, 1].set_title('参照图像')
    axs[0, 1].axis('off')

    # 规定化后的图像
    axs[0, 2].imshow(mat_img, 'gray')
    axs[0, 2].set_title('规定化后的图像')
    axs[0, 2].axis('off')

    # 原始图直方图
    axs[1, 0].plot(cv2.calcHist([org_img], [0], None, [256], [0, 256]), color='gray')
    axs[1, 0].set_title('原始图像的直方图')
    axs[1, 0].set_xlabel('像素强度')
    axs[1, 0].set_ylabel('频率')
    axs[1, 0].grid(True)

    # 参照图直方图
    axs[1, 1].plot(cv2.calcHist([ref_img], [0], None, [256], [0, 256]), color='gray')
    axs[1, 1].set_title('参照图像的直方图')
    axs[1, 1].set_xlabel('像素强度')
    axs[1, 1].set_ylabel('频率')
    axs[1, 1].grid(True)

    # 规定化后的直方图
    axs[1, 2].plot(cv2.calcHist([mat_img], [0], None, [256], [0, 256]), color='gray')
    axs[1, 2].set_title('规定化后的直方图')
    axs[1, 2].set_xlabel('像素强度')
    axs[1, 2].set_ylabel('频率')
    axs[1, 2].grid(True)

    plt.tight_layout()  # 确保子图之间不会重叠

    return mat_img, fig


if __name__ == "__main__":
    histogram_matching('pout.tif', '1.png')
