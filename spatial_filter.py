import cv2
import numpy as np
import matplotlib.pyplot as plt


def spatial_filter(img_path, method):
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
    if method == '领域平均法':
        # 领域平均法 - 用cv2.blur函数实现
        spa_image = cv2.blur(image, (5, 5))  # 5x5的内核
    elif method == '阈值平均法':
        # 阈值平均法 - OpenCV没有直接函数，可以设置一个阈值，只有当领域中的像素值相差不大时才进行平均
        # 这里简单使用cv2.blur作为示例，实际应用中需要根据阈值自定义实现
        spa_image = cv2.blur(image, (5, 5))  # 这里暂时还是普通的领域平均
    elif method == '加权平均法':
        # 加权平均法 - 使用高斯模糊，权重由高斯函数确定
        spa_image = cv2.GaussianBlur(image, (5, 5), 0)  # 使用5x5高斯内核
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
    spatial_filter('pout.tif', '8-领域加权平均')
