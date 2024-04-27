import cv2
import matplotlib.pyplot as plt
import numpy as np


def frequency_domain_filter(img_path, method):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    # 读取图像并转换为灰度

    image = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), 0)

    # 获取图像尺寸
    rows, cols = image.shape

    # 进行傅里叶变换
    f = np.fft.fft2(image)
    f_shift = np.fft.fftshift(f)

    # 设定截止频率D0
    d0 = 30
    # 创建理想低通滤波器的掩码
    [x, y] = np.meshgrid(np.arange(-cols // 2, cols // 2), np.arange(-rows // 2, rows // 2))
    d = np.sqrt(x ** 2 + y ** 2)
    mask = d <= d0

    # 滤波器掩码
    filter_mask = None
    if method == '理想低通滤波器':
        # 应用滤波器
        filter_mask = np.zeros_like(f_shift, dtype=np.complex64)
        filter_mask[mask] = f_shift[mask]

    elif method == 'Butterworth低通滤波器':
        # Butterworth滤波器的n值，n越大过渡带越陡
        n = 2

        filter_mask = 1 / (1 + (d / d0) ** (2 * n))
        filter_mask = f_shift * filter_mask

    elif method == '指数低通滤波器':
        # 创建指数低通滤波器的掩码
        filter_mask = np.exp(-(d / d0) ** 2)
        filter_mask = f_shift * filter_mask

    # 逆傅里叶变换
    f_i_shift = np.fft.ifftshift(filter_mask)
    img_filter = np.fft.ifft2(f_i_shift)
    img_filter = np.abs(img_filter)

    # 绘制子图
    fig, ax = plt.subplots(1, 2, figsize=(15, 10))
    # 绘制处理后的图像
    ax[0].imshow(image, cmap='gray')
    ax[0].set_title('原图像')
    ax[0].axis('off')
    ax[1].imshow(img_filter, cmap='gray')
    ax[1].set_title(method)
    ax[1].axis('off')

    plt.tight_layout()  # 确保子图之间不会重叠

    # 归一化到0-255范围
    img_filter = (img_filter / np.max(img_filter) * 255).astype(np.uint8)

    plt.show()

    return img_filter, fig


if __name__ == "__main__":
    frequency_domain_filter('pout.tif', '理想低通滤波器')
