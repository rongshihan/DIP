环境：PyCharm 2023、Python 3.11.5

前后端交互逻辑：PyQt5的信号与槽机制。
例如用户单击“直方图”时，QlistWidget控件发出itemClicked 信号，在主窗口类main的槽函数image_processing判断其信号为“直方图”，则执行逻辑功能实现类histogram画出直方图，并在CustomGraphicsView控件上显示处理后的图片。

前端（GUI）：PyQt5三件套
(1) Qt Designer：通过拖拽的方式放置控件可以随时查看控件效果。保存后生成.ui文件。
(2) PyUIC：将Qt Designer中设计的.ui文件转换为Python代码(.py文件)。
(3) PyRCC：将资源文件(Qt Designer中用到的图片、数据…)打包成 .py 文件的工具。

CustomGraphicsView类：重写QGraphicsView成员函数（dragEnterEvent、dragMoveEvent、dropEvent、mousePressEvent），目的是实现拖拽读取图片并获得图片的路径，以及右键菜单保存图片。

8个窗口类（由PyUIC转换对应的.ui文件而来）：
1）CLAHEWindow:
三个输入框控件QlineEdit，分别用于输入自适应直方图均衡化的参数clip_limit, tile_grid_size（第二个参数是矩阵的形式，因此有三个）；
两个按钮控件QPushButton（在鼠标单击时发出cliked信号）

2）DiagWindow:
两个输入框控件QlineEdit，分别用于输入旋转放缩的参数angle，scale，分别表示旋转的角度和缩放因子。；
两个按钮控件QPushButton（在鼠标单击时发出cliked信号）

3）FreqWindow:
一个组合框控件QComboBox，用于选择频域滤波器；
两个按钮控件QPushButton（在鼠标单击时发出cliked信号）

4）GraphWindow:
重写的CustomGraphicsView控件：用于显示直方图匹配的参照图片并获得其绝对路径。
两个按钮控件QPushButton（在鼠标单击时发出cliked信号）

5）MainWindow:
左边是QlistWidget控件：在列表中的某个项被用户点击时发出itemClicked 信号，用于选择图像处理的功能。
中间是重写的CustomGraphicsView控件，用于显示处理后的图片。
右边是QlistWidget控件：同上发出itemClicked 信号，用于列出用户之前处理过的图片。

6）NoiWindow:
一个组合框控件QComboBox（在组合框的当前索引（即当前选中的项）改变时发出currentIndexChanged信号），用于选择加噪类型；
三个输入框控件QlineEdit；
两个按钮控件QPushButton（在鼠标单击时发出cliked信号）

7）ShaWindow:
一个组合框控件QComboBox，用于选择锐化方法；
两个按钮控件QPushButton（在鼠标单击时发出cliked信号）

8）SpaWindow:
一个组合框控件QComboBox（在组合框的当前索引（即当前选中的项）改变时发出currentIndexChanged信号），用于选择空域滤波器；
两个输入框控件QlineEdit，用于输入滤波器内核大小的ksize1* ksize2
两个按钮控件QPushButton（在鼠标单击时发出cliked信号）

后端：opencv、matplotlib

8个窗口实例化类（用于实例化对应的窗口类）：
1）CLAHEMyWindow:获得自适应直方图均衡化的两个参数clip_limit, tile_grid_size，分别表示对比度限制和网格大小。实现accept和reject槽函数，接受对应窗口类发来的accept和reject信号，accept方法接受输入的数据发送给主窗口类并关闭子窗口，reject方法拒绝输入的数据并关闭子窗口，下同。

2）DiagWindow:获得旋转放缩的参数angle，scale，分别表示旋转的角度和缩放因子。实现accept和reject槽函数。

3）FrequencyWindow:获得频域方法的名称。实现accept和reject槽函数。

4）GraphViewWindow:获得直方图规定化参照图片的路径。实现accept和reject槽函数。

5）main:主窗口，实现各种逻辑的地方。
image_processing（槽函数）：接收QlistWidget控件发来的信号，调用对应的逻辑功能实现类处理图片。
set_thumbnail：将处理后图片的缩略图显示到右边的QlistWidget控件上
image_display：将右边的缩略图放大显示到中间的CustomGraphicsView控件上。
save_icon：右键菜单中“保存图片”的实现。
remove_item：右键菜单中“删除”的实现。

6）NoiseWindow:获得加噪参数amount（椒盐噪声参数，表示噪声的比例）、mean, sigma（高斯噪声参数，分别表示噪声的均值和方差）。实现on_combobox_current_index_changed槽函数，接收组合框控件QComboBox发来的信号，控制三个输入框的显示和隐藏。

7）ShapenWindow:获得锐化方法的名称。实现accept和reject槽函数。

8）SpatialWindow:获得空域方法的名称，以及滤波器内核大小的参数ksize1* ksize2。实现accept和reject槽函数。实现on_combobox_current_index_changed槽函数，接收组合框控件QComboBox发来的信号，控制三个输入框的可编辑和显示、隐藏。

9个逻辑实现类（用于实现逻辑功能）：
1、adaptive_histogram_equalization：实现自适应直方图均衡化的功能。使用OpenCV的cv2.createCLAHE(clip_limit, tile_grid_size)函数实现。

2、add_noise：加噪。
1）add_salt_and_pepper_noise：添加椒盐噪声，根据amount参数计算需要添加的噪声点数量noise_num，然后随机选择图像中的点，并将其设置为黑色（椒噪声）或白色（盐噪声）；
2）add_gaussian_noise：利用random.normal函数生成与图像尺寸相同的高斯噪声，然后将生成的高斯噪声添加到归一化后的图像上。

3、frequency_domain_filter：频域滤波
1）对灰度图像进行二维傅里叶变换（np.fft.fft2），得到图像的频域表示。
2）使用np.fft.fftshift将零频分量移动到频谱中心。
3）创建滤波器掩码：
根据输入的method参数，函数会创建不同类型的滤波器掩码：
'理想低通滤波器'：所有频率低于截止频率d0的保留，高于的设为0。
'Butterworth低通滤波器'：使用Butterworth函数平滑地过渡截止频率，使滤波效果更加平滑。
'指数低通滤波器'：使用指数函数进行滤波，效果介于理想滤波器和Butterworth滤波器之间。
4）将滤波器掩码与傅里叶变换后的图像相乘，实现频域滤波。
5）使用np.fft.ifftshift将零频分量移回原始位置。
6）对滤波后的频域图像进行逆傅里叶变换（np.fft.ifft2），得到空间域的滤波后图像。

4、histogram：直方图。使用np.histogram计算灰度图像的直方图。gray_image.flatten()将二维灰度图像转换为一维数组，这样np.histogram就可以计算每个灰度级别（0-255）的像素数量。np.histogram返回两个值：hist（每个灰度级别的像素数量）和bins（灰度级别的边界）。

5、histogram_equalization：直方图均衡化
使用OpenCV的cv2.equalizeHist函数对灰度图像进行直方图均衡化。这个函数将图像的直方图拉伸，使得像素强度的分布更加均匀，从而增强图像的对比度。

6、histogram_matching：直方图匹配
1）计算两个图像的直方图：
使用np.histogram计算原图像和参照图像的直方图。
2）计算累积分布函数(CDF)：
使用cumsum方法计算直方图的累积分布函数。
3）归一化累积分布函数：
将CDF归一化到0-255之间，这样可以在后续步骤中更容易地找到映射关系。
4）创建映射表：
创建一个大小为256的映射表，用于将原图像的灰度级别映射到参照图像的灰度级别。
对于原图像中的每个灰度级别，找到参照图像CDF中与其最接近的灰度级别，并将该灰度级别索引存储在映射表中。
5）应用映射表到源图像：
使用OpenCV的cv2.LUT函数应用映射表到原图像。

7、image_rorate：旋转放缩
1）获取图像尺寸：
通过image.shape[:2]获取图像的高度和宽度。
2）定义旋转中心：
旋转中心被设定为图像的中心点。
3）获取旋转矩阵：
使用cv2.getRotationMatrix2D函数获取旋转矩阵。
4）计算旋转后图像的大小：
计算旋转后图像可能需要的最大宽度和高度，以便为旋转后的图像分配足够的空间。
5）调整旋转矩阵：
通过调整旋转矩阵中的平移参数，确保旋转后的图像位于新的图像边界的中心。
6）执行旋转：
使用cv2.warpAffine函数应用旋转矩阵，对图像进行旋转和缩放。

8、sharpen：锐化
1）普通锐化：
将图像转换为浮点类型，并加上一个常数（通常是为了避免计算中的下溢）。
使用cv2.addWeighted对图像进行加权求和，实现锐化效果。
将结果转换回8位无符号整数，并限制其值在0到255之间。
2）拉普拉斯锐化：
使用OpenCV的cv2.Laplacian函数对图像应用拉普拉斯滤波器。
将结果转换为8位无符号整数，这是通过cv2.convertScaleAbs函数实现的，它将负值转换为正值。
3）模板锐化：
定义一个锐化模板（一个3x3的矩阵）。
使用cv2.filter2D函数将模板应用到图像上。

9、spatial_filter：空域滤波
1）中值滤波：使用cv2.medianBlur函数对图像进行中值滤波。中值滤波常用于去除噪声，尤其是“椒盐”噪声。
2）盒式滤波器：使用cv2.blur函数实现，该滤波器对图像中的每个像素点，取其邻域像素的平均值作为该点的值。
3）高斯滤波器：使用cv2.GaussianBlur函数实现，该滤波器对图像中的每个像素点，取其邻域像素的加权平均值作为该点的值，权重由高斯函数确定。
4）4-领域平均：定义一个3x3的核，其中只有4个邻域像素的值为1/4，其余为0，然后使用cv2.filter2D函数应用这个核到图像上。
5）8-领域平均：定义一个3x3的核，其中8个邻域像素的值为1/9，然后使用cv2.filter2D函数应用这个核到图像上。
6）4-领域加权平均：定义一个3x3的核，其中中心像素和邻域像素的值按照指定的权重（如1/6）分布，然后使用cv2.filter2D函数应用这个核到图像上。
7）8-领域加权平均：定义一个3x3的核，其中中心像素和邻域像素的值按照指定的权重（如1/16）分布，然后使用cv2.filter2D函数应用这个核到图像上。

收获与体会：
解决的一些bug：
1、保证在拉伸界面时保持控件大小比例，而不是大小不变。
使用布局。
2、解决路径中包含中文时opencv读取不到图片。
cv2.imread改为cv2.imdecode，同时注意调整第二个参数与cv2.imread读取方式一致。
