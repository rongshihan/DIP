import sys

from PyQt5.QtCore import QSize, Qt, QPoint
from PyQt5.QtGui import QPixmap, QTransform, QIcon, QMouseEvent, QImage
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QGraphicsPixmapItem, QListWidgetItem, QFileDialog, \
    QAction, QMenu

from DialogWindow import MyDialog
from GraphViewWindow import MyGraphView
from MainWindow import Ui_MainWindow
from FrequencyWindow import MyFreqWindow
from SpatialWindow import MySpaWindow
from SharpenWindow import MyShaWindow
from NoiseWindow import MyNoiWindow
from CLAHEMyWindow import MyCLAHEWindow

from histogram import histogram_cv, plt_to_qimg
from histogram_equalization import histogram_equalization
from histogram_matching import histogram_matching
from sharpen import sharpen
from spatial_filter import spatial_filter
from frequency_domain_filter import frequency_domain_filter
from add_noise import add_salt_and_pepper_noise, add_gaussian_noise
from image_rorate import image_rotate, cv_to_q_image
from adaptive_histogram_equalization import adaptive_histogram_equalization


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.scene = None
        self.setupUi(self)
        self.retranslateUi(self)

        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.screenheight = self.screenRect.height()
        self.screenwidth = self.screenRect.width()

        self.resize(int(self.screenwidth * 0.8), int(self.screenheight * 0.8))

        wid = self.listWidget1.width() * 2

        self.listWidget1.setIconSize(QSize(wid, wid))
        # 设置该窗口是一个顶级窗口并去除窗口的框架和标题栏，使窗口无边框
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        # 设置窗口的背景为半透明
        self.setAttribute(Qt.WA_TranslucentBackground)
        # 设置窗口在关闭时自动销毁（delete）
        self.setAttribute(Qt.WA_DeleteOnClose)
        # 设置其他窗口无法与之交互，直到该模态窗口关闭
        self.setWindowModality(Qt.ApplicationModal)

        self.m_bPressed = False
        self.m_point = QPoint()

        self.listWidget1.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listWidget1.customContextMenuRequested.connect(self.show_context_menu)

    def show_context_menu(self, pos):
        # 获取被点击的 QListWidgetItem
        item = self.listWidget1.itemAt(pos)
        if not item:
            return

            # 创建右键菜单
        menu = QMenu(self)

        # 添加 "保存图片" 选项
        save_icon_action = QAction("保存图片", self)
        save_icon_action.triggered.connect(lambda: self.save_icon(item))
        menu.addAction(save_icon_action)

        remove_item_action = QAction("删除", self)
        remove_item_action.triggered.connect(lambda: self.remove_item())
        menu.addAction(remove_item_action)

        # 显示菜单
        menu.exec_(self.listWidget1.viewport().mapToGlobal(pos))

    def save_icon(self, item):
        # 获取 QListWidgetItem 的图标
        icon = item.icon()
        pixmap = icon.pixmap(256, 256)  # 可以根据需要调整大小

        # 保存为文件
        file_path, _ = QFileDialog.getSaveFileName(self, "保存图片", "", "PNG Files (*.png);;JPG Files (*.jpg)")
        if file_path:
            pixmap.save(file_path)

    def remove_item(self):
        current_item = self.listWidget1.currentItem()
        row = self.listWidget1.row(current_item)
        self.listWidget1.takeItem(row)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.m_bPressed = True
            self.m_point = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.m_bPressed:
            self.move(event.globalPos() - self.m_point)

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.m_bPressed = False

    def closeEvent(self, event):
        # 在关闭窗口时销毁（delete）该窗口
        self.deleteLater()
        # 调用父类的 closeEvent 方法，以确保窗口的正常关闭
        super().closeEvent(event)

    def image_processing(self, item):
        """
        listWidget的槽函数
        :param item:
        :return:
        """
        img_path = self.graphicsView.path

        if img_path is None:
            QMessageBox.information(QMainWindow(), "提示框", "图呢？你让我处理什么？",
                                    QMessageBox.Yes | QMessageBox.No,
                                    QMessageBox.Yes)
        else:
            # 获取 QGraphicsView 的 QGraphicsScene
            self.scene = self.graphicsView.scene()
            self.scene.clear()
            # 获得单击的选项名称
            text = item.text()
            if text == '直方图':
                # 画直方图
                hist, fig = histogram_cv(img_path)

                # plt转Qimage
                matplotlib_to_qimage = plt_to_qimg(fig, self.graphicsView.height(), self.graphicsView.width())

                item = QGraphicsPixmapItem(matplotlib_to_qimage)

                # 将 pixmap_item 添加到场景中
                self.scene.addItem(item)

                # 将缩略图显示到右边
                self.set_thumbnail(matplotlib_to_qimage)
            elif text == '直方图均衡化':
                # 直方图均衡化
                equalized_image, fig = histogram_equalization(img_path)

                # plt转QImage
                matplotlib_to_qimage = plt_to_qimg(fig, self.graphicsView.height(), self.graphicsView.width())

                item = QGraphicsPixmapItem(matplotlib_to_qimage)

                pixmap = QPixmap.fromImage(cv_to_q_image(equalized_image))

                self.scene.addItem(item)

                # 将缩略图显示到右边
                self.set_thumbnail(pixmap)
                self.set_thumbnail(matplotlib_to_qimage)
            elif text == '自适应直方图均衡化':
                # 实例化子窗口类
                window = MyCLAHEWindow()
                # 显示子窗口
                window.exec()

                text1 = window.lineEdit_1.text().strip()

                if text1 == '':
                    clip_limit = 40.0
                else:
                    clip_limit = float(text1)

                text2 = window.lineEdit_2.text().strip()

                if text2 == '':
                    tile_grid_size1 = 8
                else:
                    tile_grid_size1 = float(text2)

                text3 = window.lineEdit_3.text().strip()

                if text3 == '':
                    tile_grid_size2 = 8
                else:
                    tile_grid_size2 = float(text3)

                # 直方图均衡化
                image, fig = adaptive_histogram_equalization(img_path, clip_limit, (tile_grid_size1, tile_grid_size2))

                # plt转QImage
                matplotlib_to_qimage = plt_to_qimg(fig, self.graphicsView.height(), self.graphicsView.width())

                item = QGraphicsPixmapItem(matplotlib_to_qimage)

                pixmap = QPixmap.fromImage(cv_to_q_image(image))

                self.scene.addItem(item)

                # 将缩略图显示到右边
                self.set_thumbnail(pixmap)
                self.set_thumbnail(matplotlib_to_qimage)
            elif text == '直方图规定化':
                # 原图path
                org_img_path = img_path
                # 实例化子窗口类
                my_graphview = MyGraphView()
                # 显示子窗口
                my_graphview.exec()
                # 参考图path
                ref_img_path = my_graphview.get_path()

                # 直方图规定化
                mat_img, fig = histogram_matching(org_img_path, ref_img_path)

                # plt转QImage
                matplotlib_to_qimage = plt_to_qimg(fig, self.graphicsView.height(), self.graphicsView.width())

                item = QGraphicsPixmapItem(matplotlib_to_qimage)

                pixmap = QPixmap.fromImage(cv_to_q_image(mat_img))

                self.scene.addItem(item)

                # 将缩略图显示到右边
                self.set_thumbnail(pixmap)
                self.set_thumbnail(matplotlib_to_qimage)
            elif text == '水平翻转':
                # 获取第一个 QGraphicsView 的内容
                pixmap = QPixmap(img_path)

                # 对 QPixmap 进行水平和垂直翻转
                transform = QTransform().scale(-1, 1)
                transform.translate(-pixmap.width(), -pixmap.height())
                flipped_pixmap = pixmap.transformed(transform)

                # 将翻转后的图片添加到 QGraphicsView 上
                self.scene.addPixmap(flipped_pixmap)

                self.set_thumbnail(flipped_pixmap)

            elif text == '垂直翻转':
                pixmap = QPixmap(img_path)

                # 对 QPixmap 进行水平和垂直翻转
                transform = QTransform().scale(1, -1)
                transform.translate(-pixmap.width(), -pixmap.height())
                flipped_pixmap = pixmap.transformed(transform)

                # 将翻转后的图片添加到 QGraphicsView 上
                self.scene.addPixmap(flipped_pixmap)

                self.set_thumbnail(flipped_pixmap)
            elif text == '旋转放缩':
                # 实例化子窗口类
                self.my_dialog = MyDialog()
                # 显示子窗口
                self.my_dialog.exec()

                # 获得对话框的输入内容
                text = self.my_dialog.lineEdit.text().strip()

                if text == '':
                    angle = 180
                else:
                    angle = float(text)

                # 获得对话框的输入内容
                text1 = self.my_dialog.lineEdit_2.text().strip()

                if text1 == '':
                    scale = 1.0
                else:
                    scale = float(text1)

                self.my_dialog.close()
                # 旋转图像
                img_rorate = image_rotate(img_path, angle, scale)

                # 创建 QPixmap 和 QGraphicsPixmapItem
                pixmap = QPixmap.fromImage(cv_to_q_image(img_rorate))
                pixmap_item = QGraphicsPixmapItem(pixmap)

                # 创建 QGraphicsScene 并添加 pixmap_item
                self.scene.addItem(pixmap_item)

                # 将缩略图显示到右边
                self.set_thumbnail(pixmap)

            elif text == '空域平滑':
                # 实例化子窗口类
                window = MySpaWindow()
                # 显示子窗口
                window.exec()
                # 获得对话框的输入内容
                text = window.comboBox.currentText()
                # 空域滤波
                spa_filter, fig = spatial_filter(img_path, text)

                # plt转QImage
                matplotlib_to_qimage = plt_to_qimg(fig, self.graphicsView.height(), self.graphicsView.width())

                item = QGraphicsPixmapItem(matplotlib_to_qimage)

                pixmap = QPixmap.fromImage(cv_to_q_image(spa_filter))

                self.scene.addItem(item)

                # 将缩略图显示到右边
                self.set_thumbnail(pixmap)
                self.set_thumbnail(matplotlib_to_qimage)

            elif text == '频域平滑':
                # 实例化子窗口类
                window = MyFreqWindow()
                # 显示子窗口
                window.exec()
                # 获得对话框的输入内容
                text = window.comboBox.currentText()
                # 频域滤波
                fre_filter, fig = frequency_domain_filter(img_path, text)

                # plt转QImage
                matplotlib_to_qimage = plt_to_qimg(fig, self.graphicsView.height(), self.graphicsView.width())

                item = QGraphicsPixmapItem(matplotlib_to_qimage)

                pixmap = QPixmap.fromImage(cv_to_q_image(fre_filter))

                self.scene.addItem(item)

                # 将缩略图显示到右边
                self.set_thumbnail(pixmap)
                self.set_thumbnail(matplotlib_to_qimage)
            elif text == '锐化':
                # 实例化子窗口类
                window = MyShaWindow()
                # 显示子窗口
                window.exec()
                # 获得对话框的输入内容
                text = window.get_data()
                # 锐化
                sharpen_img, fig = sharpen(img_path, text)

                # plt转QImage
                matplotlib_to_qimage = plt_to_qimg(fig, self.graphicsView.height(), self.graphicsView.width())

                item = QGraphicsPixmapItem(matplotlib_to_qimage)

                pixmap = QPixmap.fromImage(cv_to_q_image(sharpen_img))

                self.scene.addItem(item)

                # 将缩略图显示到右边
                self.set_thumbnail(pixmap)
                self.set_thumbnail(matplotlib_to_qimage)
            elif text == '加噪':
                # 实例化子窗口类
                window = MyNoiWindow()
                # 显示子窗口
                window.exec()

                noise = window.comboBox.currentText()

                text1 = window.lineEdit_1.text().strip()

                if text1 == '':
                    amount = 0.05
                else:
                    amount = float(text1)

                text2 = window.lineEdit_2.text().strip()

                if text2 == '':
                    mean = 0
                else:
                    mean = float(text2)

                text3 = window.lineEdit_3.text().strip()

                if text3 == '':
                    sigma = 0.05
                else:
                    sigma = float(text3)

                window.close()
                if noise == '椒盐噪声':
                    add_noise_image, fig = add_salt_and_pepper_noise(img_path, amount)
                else:
                    add_noise_image, fig = add_gaussian_noise(img_path, mean, sigma)

                # plt转QImage
                matplotlib_to_qimage = plt_to_qimg(fig, self.graphicsView.height(), self.graphicsView.width())

                item = QGraphicsPixmapItem(matplotlib_to_qimage)

                pixmap = QPixmap.fromImage(cv_to_q_image(add_noise_image))

                self.scene.addItem(item)

                # 将缩略图显示到右边
                self.set_thumbnail(pixmap)
                self.set_thumbnail(matplotlib_to_qimage)

            else:
                QMessageBox.information(QMainWindow(), "提示框", "点个屁啊没实现呢",
                                        QMessageBox.Yes | QMessageBox.No,
                                        QMessageBox.Yes)

    def set_thumbnail(self, pixmap):
        item = QListWidgetItem()
        icon = QIcon()
        icon.addPixmap(QPixmap(pixmap), QIcon.Normal, QIcon.Off)

        item.setIcon(icon)
        self.listWidget1.addItem(item)

    def image_display(self, item):
        # 获取图标并转换为 QPixmap
        icon = item.icon()
        # 设置你想要的尺寸
        pixmap = icon.pixmap(self.graphicsView.height(), self.graphicsView.width())

        # 创建 QGraphicsPixmapItem 并添加到场景中
        pixmap_item = QGraphicsPixmapItem(pixmap)

        # 获取 QGraphicsView 的 QGraphicsScene
        self.scene = self.graphicsView.scene()
        self.scene.clear()
        self.scene.addItem(pixmap_item)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindow()
    # 展示窗口
    w.show()

    app.exec()
