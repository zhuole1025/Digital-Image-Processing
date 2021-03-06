# 图像分割
* 图像分割是指将图像细分为构成它的子区域或物体
* 本章算法基于灰度值的两个基本性质之一：不连续性和相似性

## 点、线和边缘检测
* 就像局部平均平滑一幅图像那样，假设平均处理类似于积分，对于灰度的突变，局部变化可以用微分来检测
* 使用空间滤波器来计算图像中每个像素位置处的一阶导数和二阶导数
* 一阶导数和二阶导数的特点
    * 一阶导数通常在图像中产生较粗的边缘
    * 二阶导数对精细细节，如细线、孤立点和噪声有较强的响应
    * 二阶导数在灰度斜坡和灰度台阶过渡处会产生双边缘响应
    * 二阶导数的符号可用于确定边缘的过渡是从亮到暗还是从暗到亮
* 孤立点的检测
    * 点的检测应以二阶导数为基础，即使用拉普拉斯算子
    * 如果在某个点处，该模板的响应的绝对值超过了指定的阈值，则在 (x,y) 处的点已被检测到。在输出图像中，该点标为1，否则为0
* 线检测
    * 对于线检测，二阶导数将导致更强的响应，产生比一阶导数更细
的线。我们可以使用拉普拉斯模板，但要处理双线效应
    * 当把3×3滤波器居中放在一条宽为5个像素的恒定灰度线上时，其
  响应将为零，这样就产生了双线效应
    * 点检测的拉普拉斯算子是各向同性的，因此其响应与方向无关 (相对于该3×3拉普拉斯目标的4个方向:垂直方向、水平方向和两个对角方向)
    * 所有模板的系数之和为0，这表明恒定灰度区域中的响应为0
* 边缘模型
    * 边缘检测是基于灰度突变来分割图像的常用方法
    * 边缘模型根据它们的灰度剖面来分类。有台阶边缘、斜坡边缘和 “屋顶”边缘等
    * 一阶导数的幅度可用于检测图像中的某个点处是否存在一个边缘
    * 二阶导数的符号用于确定一个边缘像素是位于该边缘的暗侧还是位于该边缘的亮侧
        * 对图像中的每条边缘，二阶导数生成两个值(一个不希望的特点)
        * 二阶导数的零交叉点可用于定位粗边缘的中心
    * 微弱的可见噪声严重影响检测边缘所用的一阶导数和二阶导数，二阶导数比一阶导数更为敏感
    * 因此执行边缘检测的三个基本步骤是:
        * 为降噪图像进行平滑处理
        * 边缘点的检测。这是一个局部操作，从一幅图像中提取所有边缘点的潜在候选者
        * 边缘定位。这一步的目的是从候选边缘点中选择组成边缘点集合的真实成员
* 基本边缘检测
    * 梯度向量、幅度和方向角
    * 图像边缘方向与边缘上点的梯度向量正交
    * 梯度算子：Roberts, Prewitt, Sobel（抑制噪声）
    * 在计算梯度前对图像进行平滑处理，边缘检测可做更多的选择。
    * 实现相同基本目标的另一种方法是，对梯度图像进行阈值处理。
        * 阈值处理后的图像边缘更少，并且图像中的边缘要清晰得多
        * 另一方面，许多边缘被断开了
* 更先进的边缘检测技术
    * 用于边缘检测的算子应有两个特点
        * 能计算图像中每一个点处的一阶导数或二阶导数的数字近似的微分算子
        * 能被“调整”以便在任何期望的尺寸上起作用，因此大算子也可用于检测模 糊边缘，小算子可用于检测锐度集中的精细细节
    * Marr-Hildreth边缘检测器（马尔算子）
        * 高斯拉普拉斯（LoG）
        * 特点
            * 算子的高斯部分会模糊图像
            * 尽管一阶导数可用于检测灰度突变，但它们是有方向的算子。另一方面，拉普拉斯有各向同性的优点，符合人的视觉系统特性
        * 步骤
            * 用一个2-D的高斯平滑模板与源图象卷积
            * 计算卷积后图象的拉普拉斯值
            * 检测拉普拉斯图象中的零交叉作为边缘点
                * 寻找零交叉的方法是用以p为中心的一个3x3的邻域，p点处零交叉意味着至少有两个相对的邻域像素的符号不同；如果进行阈值处理，那么不仅相对邻域的符号不同，它们的数值差的绝对值还必须超过这个阈值
                * 使用零交叉检测边缘的另一个好处是可以得到一个像素宽的边缘，简化了诸如边缘连接的后续阶段的处理
        * 使用高斯差分(DoG)来近似LoG滤波器
    * 坎尼边缘检测器
