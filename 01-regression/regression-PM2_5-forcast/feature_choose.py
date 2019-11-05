import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 获得测试集数据
train_data = pd.read_csv('Dataset/train.csv')
train_data.drop(['Date','stations','observation'], axis=1, inplace=True)

# 种类数
ItemNum = 18

#训练样本features集合
X_Train=[]
#训练样本目标PM2.5集合
Y_Train=[]

for i in range(int(len(train_data)/ItemNum)):
    oneday_all_data = train_data[i*ItemNum:(i+1)*ItemNum]
#     print(oneday_all_data,'\n')
    for j in range(15):
        x = oneday_all_data.iloc[:,j-24:j+9-24] # 将一天的数据分为15份
        y = int(oneday_all_data.iloc[9,j+9-24])
        
        # 存储分割好的数据
        X_Train.append(x) 
        Y_Train.append(y)
# print(len(Y_Train))
# print(len(X_Train[0].iloc[10]))

def Transform(data):
    if(data != 'NR'):
        return float(data)
    else:
        return 0.

def GetAverage(pandas_serise):
    sum = 0.
    for i in range(len(pandas_serise)):
        sum += Transform(pandas_serise[i])
    sum /= len(pandas_serise)
    return sum;

x_AMB=[]
x_CH4=[]
x_CO=[]
x_NMHC=[]

x_NO=[]
x_NO2=[]
x_NOX=[]
x_O3=[]

x_PM10=[]
x_PM2Dot5=[]
x_RAINFALL=[]
x_RH=[]

x_SO2=[]
x_THC=[]
x_WD_HR=[]
x_WIND_DIREC=[]

x_WIND_SPEED=[]
x_WS_HR=[]

y = []

for i in range(len(Y_Train)):
    y.append(Y_Train[i])
    x_AMB.append(GetAverage(X_Train[i].iloc[0]))
    x_CH4.append(GetAverage(X_Train[i].iloc[1]))
    x_CO.append(GetAverage(X_Train[i].iloc[2]))
    x_NMHC.append(GetAverage(X_Train[i].iloc[3]))

    x_NO.append(GetAverage(X_Train[i].iloc[4]))
    x_NO2.append(GetAverage(X_Train[i].iloc[5]))
    x_NOX.append(GetAverage(X_Train[i].iloc[6]))
    x_O3.append(GetAverage(X_Train[i].iloc[7]))

    x_PM10.append(GetAverage(X_Train[i].iloc[8]))
    x_PM2Dot5.append(GetAverage(X_Train[i].iloc[9]))
    x_RAINFALL.append(GetAverage(X_Train[i].iloc[10]))
    x_RH.append(GetAverage(X_Train[i].iloc[11]))

    x_SO2.append(GetAverage(X_Train[i].iloc[12]))
    x_THC.append(GetAverage(X_Train[i].iloc[13]))
    x_WD_HR.append(GetAverage(X_Train[i].iloc[14]))
    x_WIND_DIREC.append(GetAverage(X_Train[i].iloc[15]))

    x_WIND_SPEED.append(GetAverage(X_Train[i].iloc[16]))
    x_WS_HR.append(GetAverage(X_Train[i].iloc[17]))

# 绘制散点图
plt.figure(num = '1',figsize=(10,180))
# x_AMB
plt.subplot(9,2,1)
plt.title('x_AMB')
plt.scatter(x_AMB,y)
# x_CH4
plt.subplot(9,2,2)
plt.title('x_CH4')
plt.scatter(x_CH4,y)
# x_CO
plt.subplot(9,2,3)
plt.title('x_CO')
plt.scatter(x_CO,y)
# x_NMHC
plt.subplot(9,2,4)
plt.title('x_NMHC')
plt.scatter(x_NMHC,y)

# x_NO
plt.subplot(9,2,5)
plt.title('x_NO')
plt.scatter(x_NO,y)
# x_NO2
plt.subplot(9,2,6)
plt.title('x_NO2')
plt.scatter(x_NO2,y)
# x_NOX
plt.subplot(9,2,7)
plt.title('x_NOX')
plt.scatter(x_NOX,y)
# x_O3
plt.subplot(9,2,8)
plt.title('x_O3')
plt.scatter(x_O3,y)

# x_PM10
plt.subplot(9,2,9)
plt.title('x_PM10')
plt.scatter(x_PM10,y)
# x_PM2Dot5
plt.subplot(9,2,10)
plt.title('x_PM2Dot5')
plt.scatter(x_PM2Dot5,y)
# x_RAINFALL
plt.subplot(9,2,11)
plt.title('x_RAINFALL')
plt.scatter(x_RAINFALL,y)
# x_RH
plt.subplot(9,2,12)
plt.title('x_RH')
plt.scatter(x_RH,y)

# x_SO2
plt.subplot(9,2,13)
plt.title('x_SO2')
plt.scatter(x_SO2,y)
# x_THC
plt.subplot(9,2,14)
plt.title('x_THC')
plt.scatter(x_THC,y)
# x_WD_HR
plt.subplot(9,2,15)
plt.title('x_WD_HR')
plt.scatter(x_WD_HR,y)
# x_WIND_DIREC
plt.subplot(9,2,16)
plt.title('x_WIND_DIREC')
plt.scatter(x_WIND_DIREC,y)

# x_WIND_SPEED
plt.subplot(9,2,17)
plt.title('x_WIND_SPEED')
plt.scatter(x_WIND_SPEED,y)
# x_WS_HR
plt.subplot(9,2,18)
plt.title('x_WS_HR')
plt.scatter(x_WS_HR,y)
plt.show()
