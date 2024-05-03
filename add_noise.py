import cv2
import numpy as np
import random
import matplotlib.pyplot as plt


def add_salt_and_pepper_noise(img_path, amount):
    """
    给图像添加椒盐噪声
    :param img_path: 图片路径
    :param amount: 表示噪声的比例
    :return:
    """
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    # 读取图像
    image = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), 1)

    # 绘制子图
    fig, ax = plt.subplots(1, 2, figsize=(15, 10))

    ax[0].imshow(image, cmap='gray')
    ax[0].set_title('原图像')
    ax[0].axis('off')

    noise_img = image.copy()
    noise_num = int(amount * image.shape[0] * image.shape[1])
    for i in range(noise_num):
        randx = random.randint(0, image.shape[0] - 1)
        randy = random.randint(0, image.shape[1] - 1)
        if random.randint(0, 1) == 0:
            noise_img[randx, randy] = 0  # 椒噪声，设置为黑色
        else:
            noise_img[randx, randy] = 255  # 盐噪声，设置为白色

    # 绘制处理后的图像
    ax[1].imshow(noise_img, cmap='gray')
    ax[1].set_title('添加椒盐噪声')
    ax[1].axis('off')

    return noise_img, fig


def add_gaussian_noise(img_path, mean, sigma):
    """
    给图像添加高斯噪声
    :param img_path:
    :param mean: 噪声的均值
    :param sigma: 噪声的方差
    :return:
    """
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    # 读取图像
    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # 绘制子图
    fig, ax = plt.subplots(1, 2, figsize=(15, 10))

    ax[0].imshow(image, cmap='gray')
    ax[0].set_title('原图像')
    ax[0].axis('off')

    noise_img = image.copy() / 255.0  # 归一化到[0, 1]范围
    rows, cols = noise_img.shape
    gauss = np.random.normal(mean, sigma, (rows, cols))  # 生成高斯噪声
    gauss = gauss.reshape(rows, cols)
    noise_img = noise_img + gauss
    noise_img = np.clip(noise_img, 0, 1)  # 防止像素值超出[0, 1]范围
    noise_img = (noise_img * 255).astype(np.uint8)  # 还原到[0, 255]范围

    # 绘制处理后的图像
    ax[1].imshow(noise_img, cmap='gray')
    ax[1].set_title('添加高斯噪声')
    ax[1].axis('off')

    plt.tight_layout()  # 确保子图之间不会重叠

    return noise_img, fig


if __name__ == "__main__":
    # 添加高斯噪声
    noisy_image = add_gaussian_noise('pout.tif', 0, 25)
