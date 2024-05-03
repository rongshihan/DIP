import cv2
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtGui import QImage


# 本类实现图像选择缩放和opencv转QImage
def image_rotate(img_path, angle, scale):
    """
    实现图像旋转缩放
    :param img_path: 图片路径
    :param angle: 旋转角度
    :param scale: 缩放因子（1.0表示不缩放）
    :return:
    """
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    # 读取图像
    image = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), 1)

    # 获取图像尺寸
    (h, w) = image.shape[:2]

    # 定义旋转中心为图像中心
    center = (w / 2, h / 2)

    # 获取旋转矩阵
    m = cv2.getRotationMatrix2D(center, angle, scale)

    # 计算旋转后图像的大小
    cos = np.abs(m[0, 0])
    sin = np.abs(m[0, 1])

    # 新的图像边界
    n_w = int((h * sin)) + int((w * cos))
    n_h = int((h * cos)) + int((w * sin))

    # 调整旋转矩阵以考虑平移
    m[0, 2] += (n_w / 2) - center[0]
    m[1, 2] += (n_h / 2) - center[1]

    # 执行旋转
    rotated = cv2.warpAffine(image, m, (n_w, n_h), borderValue=(255, 255, 255))

    # 将旋转后的图像转换为RGB格式，以便在matplotlib中正确显示
    rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)

    return rotated_rgb


def cv_to_q_image(image):
    # 将BGR图像转换为RGB图像
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # 转换为 QImage
    height, width, channel = rgb_image.shape
    bytes_per_line = 3 * width
    qt_img = QImage(rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)

    return qt_img


if __name__ == "__main__":
    image_rotate('pout.tif', 45, 0.2)
