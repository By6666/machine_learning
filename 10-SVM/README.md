# SVM(support vector machine)

* 主要学习了hard-svm、soft-svm、polynomial-svm、kernel

~~~
* 属性：
1、可以解决 Classifier 和 Regression
2、通过OVR or OVO 方法可以解决 multi-Classifier
3、需要对数据进行归一化处理

* 目标：
寻找一个最优边界，即最大化margin(一个距离值)

* hard-svm：
1、假设问题是标准的二分类问题；
2、通过设置参数C，当C很大时，相当于一个hard-svm

* soft-svm：
1、允许svm存在一定的错误，但尽可能使错误尽可能小
2、通过设置参数C，当C很小时，相当于一个soft-svm

* 正则化：
L1 正则项 和 L2 正则项

* 多分类：
OVR or OVO，OVR速度更快、OVO效果更好

* 添加多项式特征的SVM
1、使用PipeLine(LinearSVC)
2、使用sklearn中的SVC / SVR

* kenel
SVC中RBF核(高斯核函数)，效果明显
~~~

## 学习的sklearn中的类

> from sklearn.svm import LinearSVC / LinearSVR

> from sklearn.svm import SVC / SVR 

* 类中参数：

|   parameter name  |      comment   |    tip 
|    -----------    |     -----      |  ---------
| C  |   正则化参数 | C越大允许的错误越小
| multi-class  |   多分类参数 | 使用的方法OVO / OVR
| penalty  |   正则化参数 | 可选方法 l1 / l2
| kernel  | 核函数参数  | SVC/SVR类中才可设置 
| gamma  |   当设置Kernel = "rbf"时  | gamma越大对应得模型越复杂，反之越简单
| degree |   当设置Kernel = "poly"时 | 相当于添加多项式项


