# 数字图像基础
#### 人眼感知视觉
* 锥状体（亮视觉）+ 杆状体（暗视觉）
* 人的视觉系统感知的亮度是进入人眼光强的**对数函数**
* 亮度适应现象： 视觉系统不能同时在一个范围内工作，而通过改变其整个灵敏度来实现
---

#### 光与电磁波谱
* 可见光波长范围：0.43微米-0.79微米
* 单色光的唯一属性是强度，也称灰度
* 彩色光属性：发光强度、光通量和亮度
---

#### 图像感知与获取
* 滤光器 + 传感器（光二极管）
* $f(x, y) = i(x, y) r(x, y)$，其中 $i(x, y)$ $r(x, y)$ 分别为入射分量和反射分量
---

#### 图像取样与量化
* 目的：将连续的图像转换为数字形式
* 对坐标值进行数字化为取样；对幅值数字化称为量化
* 量化的精度依赖于所用的离散级数和取样信号的噪声
* 数字图像表示
    * 显示成灰度阵列
    * 显示为二维数字阵列
* 离散灰度级
    * 为了便于储存，常取2的整数次幂
    * 动态范围：系统中最大可度量灰度与最小可检测灰度之比
        * 上限取决于饱和度，下限取决于噪声
    * 对比度：图像中最高与最低灰度级间的灰度差
    * k 比特图像：图像有 $2^k$ 个灰度级，需要 $M\times N\times k$ 比特来储存
* 空间分辨率
    * 度量方法：每单位距离线对数和每单位距离像素数
* 灰度分辨率
    * 定义：用于量化灰度的比特数，一般为8比特
* 图像内插
    * 基本的图像重取样方法，通过内插来调整图像的大小
    * 最邻近内插：会导致某些直边缘的严重失真
    * 双线性内插：$v(x,y)=ax+by+cxy+d$ 
    * 双三次内插：$v(x,y)=\sum^3_{i=0}\sum^3_{j=0}a_{i,j}x^iy^j$
* 像素间基本关系
    * 相邻像素（4邻域）：$(x+1,y),(x-1,y),(x,y+1),(x,y-1)$
    * 对角相邻像素（与相邻像素共称为8邻域）：$(x-1,y+1),(x+1,y+1),(x-1,y-1),(x+1,y-1)$
    * 邻接性、连通性、区域与边界
        * 4邻接、8邻接、m邻接
        * 闭合通路、连通分量、联通集
        * 内边界、外边界
        * 一个有限区域的边界形成一条闭合通路
* 距离度量
    * 距离或度量必须满足三个条件：
        * $D(p,q)≥0$，$D(p,q)=0$ 当且仅当$p=q$
        * $D(p,q)=D(q,p)$
        * $D(p,z)≤D(p,q)+D(q,z)$
    * 欧式距离：$D_e(p,q)=[(x-s)^2+(y-t)^2)]^{\frac{1}{2}}$
    * $D_4$（城市街区距离）：$D_4(p,q)=|x-s|+|y-t|$
        * 其中 $D_4 = 1$ 的像素是 $(x,y)$ 的4邻域
    * $D_8$ （棋盘距离）：$D_8(p,q)=max(|x-s|,|y-t|)$
        * 其中 $D_8 = 1$ 的像素是 $(x,y)$ 的8邻域
* 数学工具
    * 阵列与矩阵操作
    * 线性操作与非线性操作
    * 算术操作：对应像素间的加减乘除
        * 对含噪声图片进行图像平均
        * 增强差别的图像相减
        * 使用图像相乘或相除来矫正阴影
        * 图像标准化操作（0-K）：$f_m=f-min(f);\ f_s=K[f_m/max(f_m)]$
    * 集合与逻辑操作
        * 灰度图像的补集：$A^c=\{(x,y,K-z|(x,y,z)\in A\}$
        * 灰度图像的并集：$A\bigcup B=\{max_z(a,b)|a\in A,b \in B\}$
    * 空间操作
        * 单像素操作：以灰度为基础直接改变单个像素的值，$s=T(z)$
         邻域操作：如取平均，$g(x,y)=\frac{1}{mn}\sum _{(r,c)\in S_{xy}}f(r,c)$
        * 几何空间变换与图像配准：仿射变换
    * 向量与矩阵操作
    * 图像变换：对输入图像进行变换，在变换域执行指定的任务，再用反变换返回空间域
        * 二维线性变换  
            $T(u,v)=\sum^{M-1}_{u=0}\sum^{N-1}_{v=0}f(x,y)r(x,y,u,v)$  
            $f(x,y)=\sum^{M-1}_{u=0}\sum^{N-1}_{v=0}T(u,v)s(x,y,u,v)$  
            其中，$r(x,y,u,v)$ 称为正变换核，$s(x,y,u,v)$ 称为反变换核
    * 概率方法  
        令 $z_i,i=0，1，2，…L-1$ 表示一幅 $M×N$ 大小数字图像中所有可能的灰度值
        * 灰度级 $z_k$ 出现的概率：$p(z_k)=\frac{n_k}{MN}$
        * 平均灰度：$m=\sum^{L-1}_{k=0}p(z_k)=1$
        * 灰度的方差：$\sigma^2=\sum^{L-1}_{k=0}(z_k-m)^2p(z_k)$
