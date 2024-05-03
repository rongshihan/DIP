import cv2
import numpy as np
import matplotlib.pyplot as plt


def adaptive_histogram_equalization(img_path, clip_limit, tile_grid_size):
    """
    实现自适应直方图均衡化
    :param img_path: 图片路径
    :param clip_limit: (对比度限制)： 这是用来限制对比度的参数。
    其值越大，对比度的增加越明显，但可能会导致噪声放大。默认值通常是 40。
    :param tile_grid_size: (网格大小)： 这是将图像分割成的小块（或称为“tiles”）的大小。
    每个小块都会单独进行直方图均衡化。tileGridSize 是一个元组，例如 (8, 8)，表示图像被分割成 8x8 的小块。
    选择较大的网格大小会增加处理速度，但可能会降低局部对比度增强的效果；反之，选择较小的网格大小会增加局部对比度增强的效果，但可能会增加处理时间。
    :return:
    """
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    # 创建CLAHE对象
    clahe = cv2.createCLAHE(clip_limit, tile_grid_size)

    # 读取图像
    image = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), 0)

    # 绘制子图
    fig, ax = plt.subplots(1, 2, figsize=(15, 10))

    ax[0].imshow(image, cmap='gray')
    ax[0].set_title('原图像')
    ax[0].axis('off')

    # 应用CLAHE
    clahe_img = clahe.apply(image)

    # 绘制处理后的图像
    ax[1].imshow(clahe_img, cmap='gray')
    ax[1].set_title('对比度限制:' + str(clip_limit) + ',网格大小:' + str(tile_grid_size))
    ax[1].axis('off')

    return clahe_img, fig


if __name__ == "__main__":
    # 添加高斯噪声
    adaptive_histogram_equalization('2.tif', 25.0, (257, 257))
