# -*- coding: utf-8 -*-
"""
xwq
 
2020/2/11
"""

import matplotlib.pyplot as plt 
import math
import numpy as np
r = 0.85
D_Sm = 1.7
D_Nd = 2.4
Sm_O = 8.0
Nd_O = 38.0
Sm_A = 7.0
Nd_A = 36.0
Sm_Nd_O = 0.1271
Nd_Nd_O = 0.512141 
Sm_Nd_A = 0.1172 
Nd_Nd_A = 0.511876 
sample_SmNd=[0.1301, 0.1445, 0.1514, 0.1720, 0.1695, 0.1792, 0.1800, 0.1678 ]
sample_NdNd=[0.512136, 0.512112, 0.512113, 0.512108, 0.512095, 0.512061, 0.512031, 0.511997 ]
x=[]
y=[]
x1=[]
y1=[]
point=[0.85,0.91,0.93,0.95,0.97,0.99,0.2]
for F in np.linspace(0,1,1000):
    #Sm/Nd
    f_Sm = F **((D_Sm+r-1)/(1-r))
    COCL_Sm=1/(f_Sm+Sm_A*r*(1-f_Sm)/(Sm_O*(D_Sm+r-1)))
    Sm_Nd_L=Sm_Nd_O+(Sm_Nd_A-Sm_Nd_O)*(1-f_Sm*COCL_Sm)
    x.append(Sm_Nd_L)
    #Nd/Nd
    f_Nd = F **((D_Nd+r-1)/(1-r))
    COCL_Nd=1/(f_Nd+Nd_A*r*(1-f_Nd)/(Nd_O*(D_Nd+r-1)))
    Nd_Nd_L=Nd_Nd_O+(Nd_Nd_A-Nd_Nd_O)*(1-f_Nd*COCL_Nd)
    y.append(Nd_Nd_L)    
for F in point:
    #Sm/Nd
    f_Sm = F **((D_Sm+r-1)/(1-r))
    COCL_Sm=1/(f_Sm+Sm_A*r*(1-f_Sm)/(Sm_O*(D_Sm+r-1)))
    Sm_Nd_L=Sm_Nd_O+(Sm_Nd_A-Sm_Nd_O)*(1-f_Sm*COCL_Sm)
    x1.append(Sm_Nd_L)
    #Nd/Nd
    f_Nd = F **((D_Nd+r-1)/(1-r))
    COCL_Nd=1/(f_Nd+Nd_A*r*(1-f_Nd)/(Nd_O*(D_Nd+r-1)))
    Nd_Nd_L=Nd_Nd_O+(Nd_Nd_A-Nd_Nd_O)*(1-f_Nd*COCL_Nd)
    y1.append(Nd_Nd_L)
plt.text(x1[-1]+0.002, y1[-1]+0.000001, 'F:%.2f'%point[-1],fontsize=10)
for i in range(0,len(point)-1):
    print(x1[i],y1[i],point[i])
    plt.text(x1[i]-0.005, y1[i]+0.000005, '%.2f'%point[i],fontsize=10)
plt.plot(x,y,linewidth=2,color='black')
plt.scatter(x1,y1, s=30,color='orangered') 
#plt.plot(sample_SmNd,sample_NdNd,".")
plt.scatter(sample_SmNd,sample_NdNd, s=30,color='olive') 
#设置图表标题，并给坐标轴加上标签 
plt.title("AFC", fontsize=24) 
plt.xlabel("$\mathregular{^1}{^4}^7$Sm/$\mathregular{^1}{^4}^4$Nd", fontsize=14)
plt.ylabel("$\mathregular{^1}{^4}^3$Nd/$\mathregular{^1}{^4}^4$Nd", fontsize=14) 
plt.legend(['$\mathregular{C_L}$','F',"Sample"])
plt.savefig("AFC.png",dpi=100)
plt.show()
