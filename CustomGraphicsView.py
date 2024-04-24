from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QGraphicsView, QMenu, QAction, QFileDialog


# 自定义QGraphicsView控件，实现拖拽读取图片
class CustomGraphicsView(QGraphicsView):
    def __init__(self, parent=None):
        super(CustomGraphicsView, self).__init__(parent)
        self.path = None
        self.setScene(CenteredGraphicsScene())
        self.setAcceptDrops(True)
        # 设置 QGraphicsView 的对齐方式
        self.setAlignment(Qt.AlignCenter)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                if url.toString().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tif')):
                    event.acceptProposedAction()
                    break

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                self.path = url.toLocalFile()
                pixmap = QPixmap(self.path)
                item = QGraphicsPixmapItem(pixmap)
                self.scene().clear()
                self.scene().addItem(item)
                event.acceptProposedAction()

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            # 弹出右键菜单
            self.showContextMenu(event.pos())
        else:
            super(CustomGraphicsView, self).mousePressEvent(event)

    def showContextMenu(self, pos):
        # 创建右键菜单
        menu = QMenu()
        saveAction = QAction("保存图片", menu)
        saveAction.triggered.connect(self.saveImage)
        menu.addAction(saveAction)
        menu.exec_(self.mapToGlobal(pos))

    def saveImage(self):
        # 获取当前视图的尺寸
        width = self.width()
        height = self.height()

        # 渲染视图到 QPixmap
        pixmap = QPixmap(width, height)
        painter = QPainter(pixmap)
        self.render(painter)
        painter.end()

        # 保存 QPixmap 到文件
        filePath, _ = QFileDialog.getSaveFileName(self, "保存图片", "", "Images (*.png *.xpm *.jpg)")
        if filePath:
            pixmap.save(filePath)


# 自定义QGraphicsScene，重写addPixmap和addItem实现图像居中显示
class CenteredGraphicsScene(QGraphicsScene):
    def addPixmap(self, pixmap, *args, **kwargs):
        # 调用父类的addPixmap方法添加图片
        item = super().addPixmap(pixmap, *args, **kwargs)

        # 计算场景的中心点
        center = self.sceneRect().center()

        # 移动图片项到场景中心
        item.setPos(center - item.boundingRect().center())

        return item

    def addItem(self, item):
        # 调用父类的 addItem 方法添加项目
        super().addItem(item)

        # 确保项目在场景中居中
        self.centerItem(item)

    def centerItem(self, item):
        # 计算场景的中心点
        center = self.sceneRect().center()

        # 计算项目的中心点
        item_center = item.boundingRect().center()

        # 计算项目应该移动的距离，使其中心点与场景中心点对齐
        dx = center.x() - item_center.x()
        dy = center.y() - item_center.y()

        # 移动项目到场景中心
        item.moveBy(dx, dy)
