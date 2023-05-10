# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:03:41 2017

@author: Xinyu Zhang
"""
import numpy as np
import pandas as pd
import TR_03_data_pict_0904 as Pict
from sklearn import neighbors
import TR_03_data_pict_0904 as PICT

def Data_pic(data,ss):
    """ Mapping and data analysis results: distribution, Hist, CDF, and planar distribution """
    for i in range(0,len(data.columns)):
        tn=data.columns[i]
        t=data[tn]
        
        Pict.Data_Distribution(t,tn+ss)
        Pict.Data_Hist(t,tn+ss)
        Pict.Data_CDF(t,tn+ss)
        Pict.Data_Map(data.X,data.Y,t,tn+ss)
        
    return()

def DesAna_pro(data,ss):
    """ Statistical analysis, and output analysis results """
    data_describe=data.describe()
    data_describe.to_excel('%s\Record\Describe_%s.xlsx'%(Pro_path,ss))
    
    return()

def Data_input():
    """  Input data and process the track header """
    AA=pd.ExcelFile('Hc_data.xlsx')
    BB=AA.parse('Sheet1')
    data=BB
    
    assert len(data), 'The file is empty !'
    
    data.insert(2,'ID',(data.index+1))
    
    data['xd']=data['X']
    data['yd']=data['Y']
    
    print('The Hc points are %s'%len(data))
    
#    DesAna_pro(data['data'],'hc_raw')
    
#    Pict.Data_Distribution(data['data'],'hc_raw')
#    Pict.Data_Hist(data['data'],'hc_raw')
#    Pict.Data_CDF(data['data'],'hc_raw')
#    Pict.Data_Map(data.X,data.Y,data['data'],'hc_raw')
    
    return(data)

def Data_clear(data):
    """ processing null value, c outlier, and normalization """
    datan=data.dropna()
    
    datan=datan.drop_duplicates()
    print('the point_num is %s/%s'%(len(datan),len(data)))
    
    ppv1=datan['data'][datan['data']>0].quantile(0.95)
    datan['data'][datan['data']>ppv1]=ppv1 
    
    ppv2=datan['data'][datan['data']<0].quantile(0.05)
    datan['data'][datan['data']<ppv2]=ppv2  
    
    for i in range(3,6):
        tn=datan.columns[i] 
        t_max=datan[tn].max()
        t_min=datan[tn].min()
        datan[tn]=(datan[tn]-t_min)/(t_max-t_min)
    
#    DesAna_pro(data,'norm')
        
   # Pict.Data_Distribution(datan['data'],'hc_pro')
    Pict.Data_Map(datan.X,datan.Y,datan['data'],'hc_pro')
    
    return(datan)

def Data_att(data):
    func=['mean','median','min','max','var','std','skew']
    data=data['data'].agg(func)
    
    for i in range(0,len(data.columns)):
        tn=data.columns[i] 
        t_max=data[tn].max()
        t_min=data[tn].min()
        data[tn]=(data[tn]-t_min)/(t_max-t_min)
    
#    DesAna_pro(data,'hc_norm')
        
#    Data_pic(data['data'],'hc_norm')
    
    return(data)

#########     ################      ################      ################ 

def Sample_input():
    AA=pd.ExcelFile('sample_data.xlsx')
    BB=AA.parse('Sheet1')
    data=BB
    
    data=data.reset_index(drop=True)    
        
    data=data.dropna()
    
    return(data)

def Samp_data(geo_data,hc_data):
    """  According to the geological point data, filter the geochemical data 
    as the key parameters of the central sample for cluster analysis, 
    dist is the sample search range  """
    dist=100
    
    t1=pd.DataFrame()
    data=pd.DataFrame()
    
    for i in geo_data.index:
        t1=hc_data[abs(hc_data['X']-geo_data['X'][i])<dist]
        t1=t1[abs(t1['Y']-geo_data['Y'][i])<dist]
        t1['Mapping Unit']=geo_data['data'][i]
        data=data.append(t1,ignore_index=True)
        data=data.drop_duplicates()
        
    return(data)

def Knn(hc_data,sample):
    
    data=hc_data.drop(['ID','X','Y'],axis=1)
    
    train_data=sample.drop(['ID','X','Y','Mapping Unit'],axis=1)
    labels=sample['Mapping Unit']    
    
    x = np.array(data)
    y=np.array(labels)

    '''get knn classifier ''' 
    clf = neighbors.KNeighborsClassifier(weights='distance',n_neighbors=10)
    
    ''' model training '''
    clf.fit(train_data, y)
    
    ''' data prediction  '''
    result = clf.predict(data)
    
#    test_pro=clf.predict_proba(x)
    test_neighbor_dis,test_neighbor=clf.kneighbors(x,12,True)  
    
    '''output results '''
    result_data=pd.DataFrame() 
    result_data['X']=hc_data['X']
    result_data['Y']=hc_data['Y']
    result_data['data']=result
    
    result_data.to_excel('result_data.xlsx')
    
    PICT.Data_Map(result_data['X'],result_data['Y'],result_data['data'],'result_hc_100')

    return(result_data) 

##############################################################################




#########     ################      ################      ################ 

#Pro_path=r'E:\Geology_test'   
Rawdata=Data_input()
#
Hc_data=Data_clear(Rawdata)
#
#'''input Geological point data '''
Sample_data=Sample_input()

Sample=Samp_data(Sample_data,Hc_data)

result_data=Knn(Hc_data,Sample)

result_all=pd.concat([Sample_data,result_data])
result_all.to_excel('result_all.xlsx')

PICT.Data_Map(result_all['X'],result_all['Y'],result_all['data'],'result_hc_all_100')
PICT.Data_Map(Sample_data['X'],Sample_data['Y'],Sample_data['data'],'sample_data_100')

    



















