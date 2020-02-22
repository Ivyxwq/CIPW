# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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
Nd_Nd_O =0.512141- Sm_Nd_O*230*6.54/1000000
Sm_Nd_A = 0.1172 
Nd_Nd_A = 0.511876 - Sm_Nd_A*230*6.54/1000000
sample_Sm=np.array([7.86,6.19 ,4.72 ,2.60 ,2.53 ,2.51 ,2.43 ,2.35 ])
sample_Nd=np.array([36.54 ,25.93 ,18.86 ,9.15 ,9.00 ,8.51 ,8.22 ,8.47 ])
sample_Sm_Nd=sample_Sm/sample_Nd
sample_SmNd=np.array([0.1301, 0.1445, 0.1514, 0.1720, 0.1695, 0.1792, 0.1800, 0.1678 ])
sample_NdNd=np.array([0.512136, 0.512112, 0.512113, 0.512108, 0.512095, 0.512061, 0.512031, 0.511997 ])
initial_NdNd= sample_NdNd-sample_SmNd*230*6.54/1000000
#print(initial_NdNd)
x=[]
y=[]
x1=[]
y1=[]
point=[0.85,0.88,0.91,0.92,0.93,0.95,0.97,0.99,0.2]
for F in np.linspace(0,1,1000):
    #Sm/Nd
    f_Sm = F **((D_Sm+r-1)/(1-r))   
    f_Nd = F **((D_Nd+r-1)/(1-r))
    CL_Sm=Sm_O*(f_Sm+Sm_A*r*(1-f_Sm)/(Sm_O*(D_Sm+r-1)))
    CL_Nd=Nd_O*(f_Nd+Nd_A*r*(1-f_Nd)/(Nd_O*(D_Nd+r-1)))
    CL_Sm_Nd=CL_Sm/CL_Nd
    x.append(CL_Sm_Nd)
    #Nd/Nd
    COCL_Nd=1/(f_Nd+Nd_A*r*(1-f_Nd)/(Nd_O*(D_Nd+r-1)))
    Nd_Nd_L=Nd_Nd_O+(Nd_Nd_A-Nd_Nd_O)*(1-f_Nd*COCL_Nd)
    y.append(Nd_Nd_L) 
    

for F in point:
    #Sm/Nd
    f_Sm = F **((D_Sm+r-1)/(1-r))   
    f_Nd = F **((D_Nd+r-1)/(1-r))
    CL_Sm=Sm_O*(f_Sm+Sm_A*r*(1-f_Sm)/(Sm_O*(D_Sm+r-1)))
    CL_Nd=Nd_O*(f_Nd+Nd_A*r*(1-f_Nd)/(Nd_O*(D_Nd+r-1)))
    CL_Sm_Nd=CL_Sm/CL_Nd
    x1.append(CL_Sm_Nd)
    #Nd/Nd
    COCL_Nd=1/(f_Nd+Nd_A*r*(1-f_Nd)/(Nd_O*(D_Nd+r-1)))
    Nd_Nd_L=Nd_Nd_O+(Nd_Nd_A-Nd_Nd_O)*(1-f_Nd*COCL_Nd)
    y1.append(Nd_Nd_L) 
   
plt.text(x1[-1]-0.005, y1[-1]+0.000005, 'F:%.2f'%point[-1],fontsize=10)
plt.text(x1[0]-0.008, y1[0]-0.000004, point[0],fontsize=10)
for i in range(1,len(point)-1):
    #print(x1[i],y1[i],point[i])
    plt.text(x1[i]+0.001, y1[i]+0.000003, '%.2f'%point[i],fontsize=10)
plt.plot(x,y,linewidth=2,color='black')
plt.scatter(x1,y1, s=30,color='orangered') 
#plt.plot(sample_SmNd,sample_NdNd,".")
plt.scatter(sample_Sm_Nd,initial_NdNd, s=30,color='olive') 

plt.text(sample_Sm_Nd[0]+0.000003,initial_NdNd[0]+0.000004, 'S1',fontsize=10)
plt.text(sample_Sm_Nd[1]+0.000003,initial_NdNd[1]-0.000012, 'S2',fontsize=10)
plt.text(sample_Sm_Nd[2]+0.000003,initial_NdNd[2]+0.000004, 'S3',fontsize=10)
plt.text(sample_Sm_Nd[3]+0.000003,initial_NdNd[3]+0.000004, 'S4',fontsize=10)
plt.text(sample_Sm_Nd[5]+0.000003,initial_NdNd[5]+0.000004, 'S6',fontsize=10)
plt.text(sample_Sm_Nd[6]+0.000003,initial_NdNd[6]+0.000004, 'S7',fontsize=10)
plt.text(sample_Sm_Nd[7]+0.000003,initial_NdNd[7]+0.000004, 'S8',fontsize=10)
plt.text(0.28,initial_NdNd[4]+0.000006, 'S5',fontsize=10)
#设置图表标题，并给坐标轴加上标签 
plt.title("AFC", fontsize=24) 
plt.xlabel("Sm/Nd", fontsize=14)
plt.ylabel("$\mathregular{^1}{^4}^3$Nd/$\mathregular{^1}{^4}^4$Nd", fontsize=14) 
plt.legend(['$\mathregular{C_L}$','F',"Sample"])
plt.savefig("AFC.png",dpi=400,bbox_inches = 'tight')
plt.show()