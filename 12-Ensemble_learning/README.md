# Ensemble learning

* 主要学习了三种集成学习的方法：voting、boosting、Random forest(随机森林)、Extra trees(极其随机森林)、stacking

## Voting
* 1、分为hard and soft，soft具有更好的效果，只需在使用<u>VotingClassifier</u>类时设置voting参数即可
* 2、使用该类是，需要设置estimators参数，即分类器

## bagging & pasting
* 1、__bagging__ 和 __pasting__ 的使用，bagging值放回取样，pasting指不放回取样
* 2、使用<u>BaggingClassifier</u>，需要设置分类器，子模块个数，每次取样个数，bootstrap=True等参数
* 3、oob_score_的使用，可以省去对原始数据的split

## RandomForest & ExtraTrees
* 1、RandomForest(随机森林)使用方法大致与bagging相同
* 2、ExtraTrees(极其随机森林)使用时不需要设置estimators，内部直接设置为decision tree
* 3、ExtraTrees做法：选取随机特征，随机阈值；效果：抑制过拟合，但增大了Bias，训练速度更快

## boosting
* 1、Ada boosting，不能使用oob_score
* 2、Gradient boosting，不能使用oob_score

## stacking
* 可以理解为神经网络的前身

## 学习的sklearn中的类

> from sklearn.ensemble import VotingClassifier

> from sklearn.ensemble import BaggingClassifier

> from sklearn.ensemble import RandomForestClassifier

> from sklearn.ensemble import ExtraTreesClassifier

> from sklearn.ensemble import AdaBoostClassifier

> from sklearn.ensemble import GradientBoostingClassifier
