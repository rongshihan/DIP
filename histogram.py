import io
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from PyQt5.QtGui import QImage, QPixmap
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


# 本类实现直方图
def histogram_cv(img_path):
    """
    用opencv画直方图
    :param img_path: 图像路径
    :return:
    """
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
    plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号
    # 读取图像
    image = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), 1)

    # 如果需要，将图像转换为灰度图
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 计算直方图
    hist, bins = np.histogram(gray_image.flatten(), 256, (0, 257))

    # 设置bins的位置（中心）
    bins_centers = 0.5 * (bins[1:] + bins[:-1])

    # 创建matplotlib的Figure和Axes对象
    fig, axs = plt.subplots(1, 2, figsize=(15, 10))

    # 在第一个Axes对象上绘制原始图像
    axs[0].imshow(image, cmap='gray')
    axs[0].set_title('原图像')
    axs[0].axis('off')

    # 在第二个Axes对象上绘制直方图
    axs[1].plot(bins_centers, hist, color='gray')
    axs[1].set_title('直方图')
    axs[1].set_xlabel('像素强度')
    axs[1].set_ylabel('频率')
    axs[1].set_xlim([0, 256])
    axs[1].grid(True)

    plt.tight_layout()  # 确保子图之间不会重叠

    return hist, fig


def histogram_pil(img_path):
    """
    用Pillow画直方图
    :param img_path: 图片路径
    :return:
    """
    # 读取图像并转换为灰度
    image = Image.open(img_path).convert('L')
    gray_image = np.array(image)

    # 初始化matplotlib的Figure和Axes
    fig, ax = plt.subplots()

    # 计算直方图并绘制
    hist, bins = np.histogram(gray_image.flatten(), 256, (0, 257))
    ax.bar(bins[:-1], hist, color='gray', align='edge')

    # 设置坐标轴标签和标题
    ax.set_xlabel('Pixel Intensity')
    ax.set_ylabel('Frequency')
    ax.set_title('Grayscale Histogram')

    # # 去掉matplotlib默认的边框和工具栏
    # plt.gca().set_axis_off()
    # plt.gcf().subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    # plt.margins(0, 0)

    return fig


def matplotlib_to_qimage(fig):
    """
    先将matplotlib的图形保存为一个中间格式的图像文件（比如PNG），
    然后使用Qt的QPixmap从该文件中加载图像，并最终转换为QImage。
    这种方法涉及到在内存和磁盘之间传输数据，因此如果处理的是非常大的图像或需要高性能的场景，可能需要考虑plt_to_qimg方法
    :param fig:
    :return:
    """
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    img = QImage.fromData(buf.read())
    img = img.rgbSwapped()  # 转换颜色通道，因为matplotlib使用RGBA，而Qt使用ARGB

    return QPixmap.fromImage(img)


def plt_to_qimg(fig, height, width):
    """
    直接操作matplotlib的渲染后端以获取图像数据而不保存到文件通常涉及到使用matplotlib的FigureCanvas类，
    这个类提供了将图形渲染到不同后端的接口。对于内存中的渲染，通常使用的是Agg后端（Anti-Grain Geometry），
    它是一个高质量的渲染器，可以生成PNG、SVG、PDF等格式的输出。
    :param height:
    :param width:
    :param fig:
    :return:
    """
    # 获取FigureCanvasAgg对象，用于在内存中渲染图形
    canvas = FigureCanvas(fig)

    # 渲染图形到canvas
    canvas.draw()

    # 获取渲染后的图像数据
    image_data = np.frombuffer(canvas.tostring_rgb(), dtype=np.uint8)
    image_data = image_data.reshape(canvas.get_width_height()[::-1] + (3,))

    # 转换numpy数组到QImage
    qimage = QImage(image_data, canvas.get_width_height()[0], canvas.get_width_height()[1], QImage.Format_RGB888)

    # 如果需要，可以将QImage转换为QPixmap
    qpixmap = QPixmap.fromImage(qimage).scaled(int(qimage.width() * 0.8), int(qimage.height() * 0.8))

    return qpixmap


if __name__ == "__main__":
    histogram_cv('pout.tif')
