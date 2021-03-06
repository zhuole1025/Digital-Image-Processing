# 彩色图像处理
## 彩色基础
* 人类感知一个物体的颜色是由物体反射光的性质决定的
* 描述彩色光源的基本量：
    * 辐射：是从光源流出能量的总量，用瓦特来度量
    * 光强：给出观察者从光源感知的能量总和的度量，用流明来度量
    * 亮度：是主观描绘子，不可度量，体现了无色的强度的概念
* 三原色：蓝色 = 435.8nm，绿色 = 546.1nm，红色 = 700nm
    * 错误概念：三原色以各种强度比混合在一起时，就可以产生所有的可见彩
    * 原色相加可以产生二次色
    * 区别光的原色和颜料的原色：
        * 颜料的三原色为 MCY ，满足减色原理，混合后为黑色
        * 光的三原色为 RGB ，满足加色原理，混合后为白色
        <div align="center"><img src="img/img1.png" alt="Image" style="zoom:69%;" /></div>
* 区别不同颜色特性的特征：
    * 亮度：Intensity，表达无色的强度概念
    * 色调：Hue，是光波混合中与主波长有关的属性，表示观察者感知的主要颜色
    * 饱和度：Saturation，指相对的纯净度，或一种颜色混合白光的数量（饱和度与白光数量成反比）
    * 色调和饱和度一起成为色度，形成任何特殊彩色的红、绿、蓝的数量称为三色值
    * CIE 色度图：以红和绿的函数表示颜色的组成
        * 等能量点表示白光的 CIE 标准
        * 色度图边界上的点为全饱和颜色
        * 色度图中连接任意两点的直线段定义了所有不同颜色的变化，这些颜色可以由这两种颜色相加组合得到
<div align="center"><img src="img/img2.png" alt="Image" style="zoom:60%;" /></div>

---

## 彩色模型
目的：在某些标准下用通常可以接受的方式方便地对彩色加以说明
* RGB 彩色模型
    <div align="center"><img src="img/img3.png" alt="Image" style="zoom:80%;" /></div>

    * 面向硬件，常用于彩色摄像机
    * 在 RGB 彩色模型中表示的图像由3个分量图像组成，每种原色一幅分量图像
    * 像素深度：用于表示每个像素的比特数
    * 稳定色：与观察者无关，共216种，每种都由3个十六进制数构成，如 FFFFFF 为白色，000000 为黑色
<div align="center"><img src="img/img4.png" alt="Image" style="zoom:69%;" /></div>

* CMY 和 CMYK 彩色模型
    * 青色、深红色、黄色是光的二次色，是颜料的原色
    * 大多数在纸上沉积彩色颜料的设备，如彩色打印机和复印机，要求输入 CMY 数据或在内部进行 RGB 到 CMY 的转换
    * RGB -> CMY： $\left[\begin{array}{rcl}C\\M\\Y\end{array} \right]=\left[\begin{array}{rcl}1\\1\\1\end{array} \right]-\left[\begin{array}{rcl}R\\G\\B\end{array} \right]$
    * CMYK 模型加上了黑色
* HSI 彩色模型
    * 更符合人描述和解释颜色的方式
    * 形成 HSI 空间所要求的色调、饱和度和强度值可以通过 RGB 彩色立方体得到，也就是说可以将任何 RGB 点转换为对应 HSI 彩色模型中的点
    * 与红轴的夹角给出了色调，向量的长度是饱和度，强度由垂直强度轴上的平面的位置决定
    <div align="center"><img src="img/img5.png" alt="Image" style="zoom:50%;" /></div>

    * RGB -> HSI：
        * $H= \left\{\begin{array}{rcl}\theta, & & B\leq G\\360-G,&  & B\geq G\end{array}\right.$  
          其中，$\theta=arccos\{\frac{\frac{1}{2}[(R-G)+(R-B)]}{[(R-G)^2+(R-B)(G-B)]^{1/2}}\}$
        * $S=1-\frac{3}{(R+G+B)}[minR,G,B)]$
        * $I=\frac{1}{3}(R+G+B)$
    * HSI -> RGB：
        * 若在 RG 扇区内（$0^\circ\leq H<120^\circ$）  
              $\begin{array}{l}B=I(1-S)\\R=I[1+\frac{ScosH}{cos(60^\circ-H)}]\\G=3I-(R+B)\end{array}$  
        * 若在 GB 扇区内（$120^\circ\leq H<240^\circ$）  
              $\begin{array}{l}H=H-120^\circ\\R=I(1-S)\\G=I[1+\frac{ScosH}{cos(60^\circ-H)}]\\B=3I-(R+B)\end{array}$  
        * 若在 RB 扇区内（$240^\circ\leq H<360^\circ$）  
              $\begin{array}{l}H=H-240^\circ\\G=I(1-S)\\B=I[1+\frac{ScosH}{cos(60^\circ-H)}]\\R=3I-(R+B)\end{array}$
* HSV 模型
    * 一般用六棱锥表示
    * H 同 HSI 模型
    * RGB -> HSV：  
        $\begin{array}{l}S=\frac{max(R,G,B)-min(R,G,B)}{max(R+G+B)}\\V=\frac{max(R,G,B)}{255}\end{array}$

---

## 伪彩色图像处理
伪彩色图像处理是指基于一种指定的规则对灰度值赋以颜色的处理
* 灰度分层
    <div align="center"><img src="img/img6.png" alt="Image" style="zoom:60%;" /></div>

    * 用一些平行于图像的坐标平面的平面来切割图像，对被切割的不同部分赋以不同的颜色
* 灰度到彩色的变换
    <div align="center"><img src="img/img7.png" alt="Image" style="zoom:60%;" /></div>

    * 对任何输入的像素灰度执行三个独立的变换，将三个变换结果分别送入彩色监视器的红、绿、蓝通道，产生一副合成图像
    * 多光谱图像处理
<div align="center"><img src="img/img8.png" alt="Image" style="zoom:60%;" /></div>

---

## 全彩色图像处理
* 第一种方法是将彩色图像看作三幅分量图像的组合体，县分别单独处理，再将结果合成
* 第二种方法是将彩色图像中的每个像素看作一个向量，用对向量的表达方法进行处理* 两种方法等价的条件
    * 处理必须对向量和标量都可用
    * 对向量的每个分量的操作对其他分量必须是独立的

---

## 彩色变换
* 变换公式
    * $g(x,y)=T(f(x,y)]$
    * 理论上，任何变换都可在任何彩色模型中执行。但实际上，某些操作对特定的模型比较适用(简洁)
* 补色
    * 在彩色环上，与色调直接相对的另一端被称为补色
    * 补色对于增强嵌在彩色图像暗区的细节很有用
<div align="center"><img src="img/img9.png" alt="Image" style="zoom:70%;" /></div>

* 彩色分层
    * 突出图像中某个特定彩色区域，对从周围分离出目标物体很有用
    * 彩色变换函数比灰度变换函数复杂得多，故采用把某些感兴趣区域之外的彩色映射为不突出的无确定性质的颜色（制定一个中心点和一个范围）
        * $s_i=\left\{\begin{array}{rl}0.5 &,[|r_j-a_j|>\frac{W}{2}]_{1\leq j\leq n}\\r_i&,others\end{array}\right. i=1, 2, ...,n$
        * $s_i=\left\{\begin{array}{rl}0.5 &,\sum^n_{j=1}(r_j-a_j)^2>R_0^2\\r_i&,others\end{array}\right. i=1, 2, ...,n$
* 色调和彩色矫正
    * 一幅图像的色调范围是指颜色强度的基本分布，高主调图像的多数信息集中在高强度处，低主调图像的颜色主要位于低亮度处
    * 色调变换
        * 概念：实验性地调整图像亮度和对比度，以便在合适的灰度范围内提供最多的细节
        * 彩色本身并不改变，在 RGB 和 CMY(k) 空间中，这意味着使用相同的变换函数映射所有的3个（或4个）彩色分量；在 HSI 彩色空间中，则改进了亮度分量
    * 彩色平衡
        * 在调整一幅图像的彩色分量时，要认识到每个操作都会影响到图像的全部彩色平衡
        * 基于彩色环可以预测一个彩色分量如何影响其他彩色分量
        * 任何颜色的比例都可以通过减小图像中相对色的数量来增大
* 直方图处理
    * 单独对彩色图像的分量进行直方图均衡通常是不明智的，会产生不正确的彩色，而应当均匀地展开这种彩色灰度，保持色调不变
    * 而有时虽然没有改变图像的色调以及饱和度的值，但是会影响图像的整体颜色感观

---

## 平滑和锐化
* 彩色图像平滑
    * 灰度图像平滑可以推广到彩色图像处理上
    * 邻域平滑可以在每个彩色平面的基础上分别执行，其结果与使用 RGB 彩色向量执行平均是相同的
    * 通过对 HSI 模型中的亮度分量执行平均得到不同的结果
* 彩色图像锐化
    * 与灰度图像一样，同样采取拉普拉斯变换方法对图像进行锐化
    * 同样可对 RGB 模型分量或 HSI 模型分量进行锐化，得到不同的结果

---

## 基于彩色的图像分割
* HSI 彩色空间的分割
    * 一般为了在色调图像中分离出感兴趣的孤立区域，将饱和度用做一幅模版图像
    <div align="center"><img src="img/img10.png" alt="Image" style="zoom:80%;" /></div>
* RGB 向量空间中的分割
    * 给定感兴趣的有代表性彩色的样点集，得到平均彩色用$a$表示
    * 相似性度量，比较空间任一点$z$与$a$的距离
        * 欧式距离（轨迹是球体）：$D(z,a)=||z-a||$
        * 马氏距离（轨迹是椭球体）：$D(z,a)=[(z-a)^TC^{-1}(z-a)]^{\frac{1}{2}}$
        * 边界盒（避免开方运算）：$D(z,a)=z-a$
<div align="center"><img src="img/img11.png" alt="Image" style="zoom:80%;" /></div>

* 彩色边缘检测
    * 单独处理 RGB 三个分量的梯度图像再合成可能会导致错误的结果
    * 对于标量函数，梯度是坐标点指向 f 的最大变化率的方向
    * $u=\frac{\partial R}{\partial x}r+\frac{\partial G}{\partial x}g+\frac{\partial B}{\partial x}b, v=\frac{\partial R}{\partial y}r+\frac{\partial G}{\partial y}g+\frac{\partial B}{\partial y}b$
    * $\begin{array}{l}g_{xx}=u\cdot u=u^Tu=|\frac{\partial R}{\partial x}|^2+|\frac{\partial G}{\partial x}|^2+|\frac{\partial B}{\partial x}|^2\\g_{yy}=v\cdot v=v^Tv=|\frac{\partial R}{\partial y}|^2+|\frac{\partial G}{\partial y}|^2+|\frac{\partial B}{\partial y}|^2\\g_{xy}=u\cdot v=u^Tv=\frac{\partial R}{\partial x}\frac{\partial R}{\partial y}+\frac{\partial G}{\partial x}\frac{\partial G}{\partial y}+\frac{\partial B}{\partial x}\frac{\partial B}{\partial y}\end{array}$
    * 可以证明 $c(x, y)$ 方向上的最大变化率的值由以下角度给出  
        $\theta(x,y)=\frac{1}{2}arctan[\frac{2g_{xy}}{g_{xx}-g_{yy}}]$
    * 且在该角度方向上的变化率的值由下式给出  
        $F_{\theta}(x,y)=\{\frac{1}{2}[(g_{xx}+g_{yy}+)+(g_{xx}-g_{yy})cos2\theta(x,y)+2g_{xy}sin2\theta(x,y)]\}^{\frac{1}{2}}$ 

---

## 彩色图像中的噪声
* 通常，彩色图像的噪声内容在每个彩色通道中具有相同的特性，但噪声对不同彩色通道所造成的影响不同；不同的噪声水平像是由每个彩色通道的相对照射强度的差异造成的
* 将 RGB 三个通道均匀带噪图像转换为 HSI 模型后可以看出噪声图像的色调与饱和度分量明显降质了，这分别是由转换函数中求余弦与取最小值操作的非线性造成的；而强度分量比 3 个带噪声的 RGB 分量图像中的任何一个都要平滑一些，这是由亮度图像是RGB图像的平均这一事实造成的
<div align="center"><img src="img/img12.png" alt="Image" style="zoom:60%;" /></div>

* 在仅有一个 RGB 通道受噪声影响的情况下，到 HSI 的转换才将噪声扩散到所有 HSI 分量图像

---

## 彩色图像压缩
* 压缩是减少或消除冗余和不相干数据的处理
*  因为描述彩色所要求的比特数比描述灰度级所要求的比特数大 3 ~ 4 倍，所以数据压缩在存储和传输彩色图像中起着核心的作用

