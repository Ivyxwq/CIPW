# -*- coding: utf-8 -*-
"""
xuwenqiao 2020/2/9

CIPW
"""
import xlwt
import numpy as np
import xlrd
from datetime import date,datetime
def CIPW(data):
    #SiO2,TiO2,Al2O3,Fe2O3,FeO,MnO,MgO,CaO,Na2O,K2O,P2O5分子量
    MolWt=np.array([60,80,102,160,72,71,40,56,62,94,142])
    #重量百分数除以分子量，得到分子数
    MolNum=data/MolWt*1000
    Mol_keys=['SiNum','TiNum','AlNum','Fe3Num','Fe2Num','MnNum','MgNum','CaNum','NaNum','KNum','PNum']
    Mol=dict(zip(Mol_keys,MolNum))
    #print(Mol)
    SiO2=0
    #print("氧化物分子数",MolNum)
    #将MnO加到FeO step 1  none_Mn_P
    Mol['Fe2Num']=Mol['Fe2Num']+Mol['MnNum']
    Mol['MnNum'] =0
    Mol['CaNum'] = Mol['CaNum']- 3.33*Mol['PNum']
    print('磷灰石Ap 3CaO.P2O5.0.33CaF2',Mol['PNum'])
    Mol['PNum']= 0
    #step 2 none_Ti(Ca)
    if Mol['Fe2Num']>Mol['TiNum']:
        print ('钛铁矿Il FeO.TiO2',Mol['TiNum'])
        Mol['Fe2Num'] =Mol['Fe2Num'] - Mol['TiNum']   
        Mol['TiNum'] = 0
        sp = 0 
        cnt = 0
    else:
        cnt = 1
        print ('钛铁矿Il FeO.TiO2',Mol['Fe2Num'])
        Mol['TiNum']=Mol['TiNum']-Mol['Fe2Num']
        if Mol['CaNum'] > Mol['TiNum']:
            sp = Mol['TiNum']
           # print('榍石 CaTiSiO4O' ,Mol['TiNum'])
            SiO2 =SiO2 + Mol['TiNum']           
            Mol['TiNum'] = 0
            Mol['CaNum'] =Mol['CaNum'] -Mol['TiNum']
 
        else:
            #print('榍石 CaTiSiO4O' ,Mol['CaNum'])
            sp = Mol['CaNum']
            SiO2 =SiO2 + Mol['CaNum']  
            Mol['CaNum'] = 0
            Mol['TiNum'] = Mol['TiNum'] -Mol['CaNum']
            print ('金红石 TiO2',Mol['TiNum'])
            Mol['TiNum'] = 0
    # step 3 none_K
    print('正长石Or K2O.Al2O3.6SiO2',Mol['KNum'])
    SiO2 =SiO2 + Mol['KNum']*6 
    Mol['AlNum'] =Mol['AlNum'] -Mol['KNum']
    Mol['KNum'] = 0
    # step 4 none_Na_Al(Ca)
    if Mol['AlNum'] > Mol['NaNum']:
        NaNum=Mol['NaNum']
       # print ('钠长石 Na2O.Al2O3.6SiO2',Mol['NaNum'])
        SiO2 =SiO2 + Mol['NaNum']*6
        Mol['AlNum'] =Mol['AlNum'] -Mol['NaNum']
        Mol['NaNum'] = 0 
       
        if Mol['AlNum'] > Mol['CaNum'] :
            print('钙长石An CaO.Al2O3.2SiO2',Mol['CaNum'])
            SiO2 =SiO2 + Mol['CaNum']*2
            Mol['AlNum']= Mol['AlNum'] -Mol['CaNum']
            Mol['CaNum']= 0
            print('刚玉C Al2O3',Mol['AlNum'])
            Mol['AlNum']= 0
        else:
            print('钙长石An CaO.Al2O3.2SiO2',Mol['AlNum'])
            SiO2 =SiO2 + Mol['AlNum']*2
            Mol['CaNum']=Mol['CaNum']- Mol['AlNum'] 
            Mol['AlNum']= 0
          #  print('硅灰石',Mol['CaNum'])
           # Mol['CaNum']= 0
       
    else: 
        NaNum=Mol['AlNum']
        #print ('钠长石 Na2O.Al2O3.6SiO2',Mol['AlNum'])
        SiO2 =SiO2 + Mol['AlNum']*6
        Mol['NaNum'] =Mol['NaNum'] -Mol['AlNum']
        Mol['AlNum'] = 0 
        if Mol['Fe3Num'] >Mol['NaNum']:
            print ('锥辉石Ac Na2O.Fe2O3.4SiO2',Mol['NaNum'])
            SiO2 =SiO2 + Mol['NaNum']*4
            Mol['Fe3Num'] =Mol['Fe3Num'] -Mol['NaNum']
            Mol['NaNum'] = 0 
    # step 4-5
    if Mol['Fe3Num']>Mol['Fe2Num']:
        print ('磁铁矿Mt FeO.Fe2O3',Mol['Fe2Num'])
        Mol['Fe3Num'] =Mol['Fe3Num'] -Mol['Fe2Num']
        Mol['Fe2Num'] = 0 
        print('赤铁矿He Fe2O3',Mol['Fe3Num'])
        Mol['Fe3Num']=0
    else :
        print ('磁铁矿Mt FeO.Fe2O3',Mol['Fe3Num'])
        Mol['Fe2Num'] =Mol['Fe2Num'] -Mol['Fe3Num']
        Mol['Fe3Num'] = 0 
        print('Mg/Fe',Mol['MgNum']/Mol['Fe2Num'])
        ratio=Mol['MgNum']/Mol['Fe2Num']
     #step 5
    if  Mol['CaNum'] > ( Mol['Fe2Num'] + Mol['MgNum'] ):
         print ('透辉石 FeO.SiO2(Fs)\MgO.SiO2(En)\CaO.SiO2(Wo)',Mol['Fe2Num'],Mol['MgNum'])
         SiO2 =SiO2 + Mol['Fe2Num']+Mol['MgNum']+Mol['CaNum']
         #Mol['CaNum'] =Mol['CaNum']-Mol['Fe2Num']-Mol['MgNum']
         Mol['Fe2Num'] =0
         Mol['MgNum'] =0
         print('硅灰石 CaO.SiO2(Wo)',Mol['CaNum'])
         Mol['CaNum']= 0
         flag = 0
    else :
         print ('透辉石 FeO.SiO2(Fs)\MgO.SiO2(En)\CaO.SiO2(Wo)',Mol['CaNum']/(1+ratio),Mol['CaNum']-Mol['CaNum']/(1+ratio),Mol['CaNum'])
         SiO2 =SiO2 + Mol['Fe2Num']+Mol['MgNum']+Mol['CaNum'] 
         M = Mol['Fe2Num']+Mol['MgNum']-Mol['CaNum']#FeO和MgO的分子数
         flag=1
  
         Mol['CaNum']= 0 

         
    #step 6
   # print('11',Mol['SiNum']-SiO2)
    if SiO2< Mol['SiNum']:
        if flag ==1:
            print ('紫苏辉石 FeO.SiO2(Fs)\MgO.SiO2(En)',  M/(1+ratio),M-M/(1+ratio))
            Mol['Fe2Num'] =0    
            Mol['CaNum']= 0 
            Mol['MgNum'] =0 
        if cnt ==1:
            print ('榍石 CaTiSiO4O' ,sp )
        print ('钠长石Ab Na2O.Al2O3.6SiO2',NaNum)
        print('石英Q SiO2', Mol['SiNum']-SiO2)    
    else: 
         S= Mol['SiNum']-SiO2 +M #可用的SiO2
         #print('S,M',S,M)
         x =2*S-M
         y =M-x
         if x<0:
              print ('橄榄石 2FeO.SiO2(Fa)\ 2MgO.SiO2(Fo)', M/(1+ratio)/2,(M-M/(1+ratio))/2)
              Mol['Fe2Num'] =0    
              Mol['MgNum'] =0
              short_SiO2=M/2 - S
              if sp > short_SiO2:
                  print ('钠长石Ab Na2O.Al2O3.6SiO2',NaNum)
                  print ('钙钛矿 CaO.TiO2',  short_SiO2)
                  print ('榍石 CaTiSiO4O' ,sp - short_SiO2)
              else:
                  if cnt ==1:
                      print ('钙钛矿 CaO.TiO2', sp)
                      short_SiO2 = short_SiO2 -sp
                  S=NaNum*6-short_SiO2
                  x= (S-2*NaNum)/4
                  y= NaNum - x
                  if x> 0:
                      print ('钠长石Ab Na2O.Al2O3.6SiO2',x)
                      print ('霞石Ne Na2O.Al2O3.2SiO2',y)
                  else:
                      print ('霞石Ne Na2O.Al2O3.2SiO2',NaNum)
                      short_SiO2=short_SiO2-NaNum*4
                      print("short_SiO2",short_SiO2)
                  
         else: 
             if cnt ==1:
                 print ('榍石 CaTiSiO4O' ,sp )
             Mol['Fe2Num'] =0    
            
             Mol['MgNum'] =0
             print ('钠长石Ab Na2O.Al2O3.6SiO2',NaNum)
             print ('紫苏辉石 FeO.SiO2(Fs)\MgO.SiO2(En)', x/(1+ratio),x-x/(1+ratio))
             print ('橄榄石 2FeO.SiO2(Fa)\ 2MgO.SiO2(Fo)', y/(1+ratio)/2,(y-y/(1+ratio))/2)
   # print(Mol)

file = r'C:\Users\ivy\Documents\Tencent Files\326306955\FileRecv\2019test.xls'

def read_excel(i):

    wb = xlrd.open_workbook(filename=file)#打开文件
    sheet1 = wb.sheet_by_index(0)#通过索引获取表格

    cols = sheet1.col_values(i)[7:18]#获取列内容
   # print(round(cols[0],6))
    return cols

#data = eval(input("输入SiO2,TiO2,Al2O3,Fe2O3,FeO,MnO,MgO,CaO,Na2O,K2O,P2O5重量百分数："))
for i in range(8,9):
    print(i)
    data = read_excel(i)
    print(data)
    CIPW(data)


 
