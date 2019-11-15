# Decision Tree

* 主要学习了Decision tree的判别标准，entropy(信息熵) 和 gini(基尼系数).
~~~
* 属性：
1、非参数学习算法；
2、可以解决分类问题；
3、天然可以解决多酚类问题；
4、当然也可以解决回归问题；
5、有非常好的解释性

* 目标：
在某一维度上寻找某一阈值使得其entropy或gini最小

* 局限性：
1、决策边界总是横平竖直的
2、对单个样本比较敏感
3、非参数的学习方法，非常容易过拟合
~~~
* entropy(信息熵)：代表随机变量的不确定度的度量
* 其值越大，数据的不确定度越高；反之，越低

* gini(基尼系数)：其值越大，数据的不确定度越高；反之，越低

## 学习的sklearn中的类

> from sklearn.tree import DecisionTreeClassifier


* 类中参数：

|   parameter name  |      comment   
|    -----------    |     -----
| min_samples_splt  |   最小分离样本数
| min_samples_leaf  |   子叶最小样本数
| min_weight_fraction_leaf  |   [0，0.5]
| max_depth  |   最大层数
| max_leaf_nodes  |   最大树叶节点   
| min_features  |    最小特征数


