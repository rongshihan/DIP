import cv2
import numpy as np
import matplotlib.pyplot as plt


def spatial_filter(img_path, ksize1, ksize2, method):
    """
    实现空域滤波
    :param img_path: 图片路径
    :param ksize1: 滤波器核大小
    :param ksize2: 滤波器核大小
    :param method: 空域滤波器名称
    :return:
    """
    # 设置matplotlib绘图时的中文显示问题
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
    plt.rcParams['axes.unicode_minus'] = False  # 处理负号问题

    # 读取图片
    image = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), 1)

    # 绘制子图
    fig, ax = plt.subplots(1, 2, figsize=(15, 10))
    # 绘制处理后的图像
    ax[0].imshow(image, cmap='gray')
    ax[0].set_title('原图像')
    ax[0].axis('off')

    spa_image = None
    if method == '中值滤波':
        # 应用中值滤波
        # 这里的 5 是滤波器的大小，它必须是正奇数，比如 3, 5, 7 等
        spa_image = cv2.medianBlur(image, ksize1)
    elif method == '盒式滤波器':
        # 领域平均法 - 用cv2.blur函数实现
        spa_image = cv2.blur(image, (ksize1, ksize2))  # 5x5的内核
    elif method == '高斯滤波器':
        # 加权平均法 - 使用高斯模糊，权重由高斯函数确定
        spa_image = cv2.GaussianBlur(image, (ksize1, ksize2), 0)  # 使用5x5高斯内核
    elif method == '4-领域平均':
        # 4-领域平均 (使用自定义核)
        kernel_4_neighbour = np.array([[0, 1, 0],
                                       [1, 0, 1],
                                       [0, 1, 0]], np.float32) / 4
        spa_image = cv2.filter2D(image, -1, kernel_4_neighbour)
    elif method == '8-领域平均':
        # 8-领域平均 (使用自定义核)
        kernel_8_neighbour = np.array([[1, 1, 1],
                                       [1, 1, 1],
                                       [1, 1, 1]], np.float32) / 9
        spa_image = cv2.filter2D(image, -1, kernel_8_neighbour)
    elif method == '4-领域加权平均':
        # 4-领域加权平均 (使用自定义核，中心权重大)
        kernel_4_neighbour_weighted = np.array([[0, 1, 0],
                                                [1, 2, 1],
                                                [0, 1, 0]], np.float32) / 6
        spa_image = cv2.filter2D(image, -1, kernel_4_neighbour_weighted)
    elif method == '8-领域加权平均':
        # 8-领域加权平均 (使用自定义核，中心权重大)
        kernel_8_neighbour_weighted = np.array([[1, 2, 1],
                                                [2, 4, 2],
                                                [1, 2, 1]], np.float32) / 16
        spa_image = cv2.filter2D(image, -1, kernel_8_neighbour_weighted)

    ax[1].imshow(spa_image, cmap='gray')
    ax[1].set_title(method)
    ax[1].axis('off')

    plt.tight_layout()  # 确保子图之间不会重叠

    return spa_image, fig


if __name__ == "__main__":
    spatial_filter('pout.tif', 8, 8, '盒式滤波器')
