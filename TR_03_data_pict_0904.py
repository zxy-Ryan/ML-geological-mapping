# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 10:16:01 2018

@author: Xinyu Zhang
"""
from matplotlib import pyplot as plt
from scipy import stats
import numpy as np

fsize=(20,20) 
fwsize=25   
flsize=6    
ftb=10      
fdpi=100   

mpsize=[400]  
msize=(22,20) 
mwsize=25
mdpi=100

"""
    def Picture_att(file_name):
    def Data_Distribution(data,name):  
    def Data_Hist(data,name):
    def Data_CDF(data,name):
    def Sample_Map(X_cor,Y_cor,Z_data):  
    def Data_Map(X_cor,Y_cor,Z_data,data_name):  
    def Img_Colorbar(gca,Col_label):
    def Data_zone_dist_Map(X_cor,Y_cor,Z_data,data_name):  
    def KM_Stat(data,km_num):
    def KM_Map(data,km_num):
"""

####### plot data distribution
def Picture_att(file_name):
    plt.tick_params(labelsize=mwsize)
    plt.xlabel('X coordinat',fontsize=mwsize)
    plt.ylabel('Y coordinat',fontsize=mwsize)   
    plt.title(file_name, fontsize=mwsize)
    plt.savefig(file_name, bbox_inches='tight') 
    return()


def Data_Distribution(data,name):    
    plt.figure(num='%s' %name,figsize=fsize,dpi=fdpi)
    data.plot(style='r*')
    
    plt.tick_params(labelsize=fwsize)
    plt.grid('on')
    plt.title('%s' %name,fontsize=fwsize)
    plt.savefig('%s' %name,bbox_inches='tight') 
    return()


def Data_Hist(data,name):
    """ plot data distribution: histogram  """
    plt.figure(num='Histogram of %s' %name,figsize=fsize,dpi=fdpi)
    data.hist(bins=30,rwidth=0.8,align='mid',normed=True)
    data.plot(kind='kde',style='r--',linewidth =flsize)
    
    plt.tick_params(labelsize=fwsize)
    plt.ylabel('probability',fontsize=fwsize)
    plt.grid('on')
    plt.title('Histogram of %s' %name,fontsize=fwsize)
    plt.savefig('Histogram of %s' %name,bbox_inches='tight') 
    return()


def Data_CDF(data,name):
    """ plot data distribution: cumulative distribution function plot  """
    plt.figure(num='CDF of %s' %name,figsize=fsize,dpi=fdpi)
    data.hist(bins=30,normed=True,histtype='step',cumulative=True,linewidth =flsize)
    
    plt.tick_params(labelsize=fwsize)
    plt.ylabel('CDF',fontsize=fwsize)
    plt.grid('on')
    plt.title('CDF of %s' %name,fontsize=fwsize)
    plt.savefig('CDF of %s' %name,bbox_inches='tight') 
    return()

 
def Sample_Map(X_cor,Y_cor,Z_data):  
    """ distribution map of sample points in the work area  """
    plt.figure(num='Data distribution map',figsize=msize,dpi=mdpi)
    s=mpsize*len(Z_data)    
    plt.scatter(X_cor,Y_cor,s,Z_data,marker='.',cmap='jet')     
   
    plt.tick_params(labelsize=mwsize)
    plt.xlabel('X coordinat',fontsize=mwsize)
    plt.ylabel('Y coordinat',fontsize=mwsize)    
    plt.title('Data distribution map', fontsize=mwsize)
    plt.savefig('Data distribution map', bbox_inches='tight') 
    return() 

 
def Data_Map(X_cor,Y_cor,Z_data,data_name):  
    """ element distribution map of the work area """
    plt.figure(num='Map of %s' %data_name,figsize=msize,dpi=mdpi)
    s=mpsize*len(Z_data)    
    plt.scatter(X_cor,Y_cor,s,Z_data,marker='.',cmap='jet') 
    
    plt.tick_params(labelsize=mwsize)
    plt.xlabel('X coordinat',fontsize=mwsize)
    plt.ylabel('Y coordinat',fontsize=mwsize)  
    plt.colorbar()
    plt.title('Map of %s' %data_name, fontsize=mwsize)
    plt.savefig('Map of %s' %data_name, bbox_inches='tight') 
    return() 


def Img_Colorbar(gca,Col_label):
    
    Cor_labelt=Col_label.tolist()
    cbar = plt.colorbar(gca)  
    cbar.ax.set_yticks(Col_label)  
    cbar.ax.set_yticklabels(Cor_labelt,fontsize=mwsize) 
    return()

##### regional distribution map
def Data_zone_dist_Map(X_cor,Y_cor,Z_data,data_name):   
    colors_v = ['#000080', '#0000FF', '#6495ED',
              '#FFD700', '#F08080', '#FF0000', '#800000']    
    plt.figure(num='TR %s zone dis map' %data_name,figsize=msize,dpi=mdpi)
    s=mpsize*len(Z_data) 
    gca=plt.scatter(X_cor,Y_cor,s,Z_data,marker='*',cmap=plt.cm.jet)     

    plt.tick_params(labelsize=mwsize)
    Col_label=np.linspace(0,6000,7)
    Img_Colorbar(gca,Col_label)
    plt.xlabel('X coordinat',fontsize=mwsize)
    plt.ylabel('Y coordinat',fontsize=mwsize)    
    plt.title('TR %s zone dis map' %data_name, fontsize=mwsize)
    plt.savefig('TR %s zone dis map' %data_name, bbox_inches='tight') 
    return() 

####### draw KMeans results statistical distribution map
def KM_Stat(data,km_num):
    plt.figure(num='KMeans Result Statistics --%d'%km_num,figsize=fsize,dpi=fdpi)
    plt.plot(data.index,data,'ro',markersize=ftb)
    plt.plot(data.index,data,'b-',linewidth =flsize)
    plt.grid('on')
    plt.savefig('KMeans Result Statistics --%d' %km_num,bbox_inches='tight')  
    return()

def KM_Map(data,km_num):
    plt.figure(num='KMeans Result Image--%d' %km_num,figsize=msize,dpi=mdpi)
    for name, group in data.groupby('labels'):
        plt.plot(group['Xcor'], group['Ycor'], '.',markersize=mwsize,label=name)
    plt.legend(loc='best',fontsize=mwsize)
    plt.tick_params(labelsize=mwsize)
    plt.xlabel('X coordinat',fontsize=mwsize)
    plt.ylabel('Y coordinat',fontsize=mwsize)    
    plt.title('KMeans Result Image--%d' %km_num, fontsize=mwsize)
    plt.savefig('KMeans Result Image--%d' %km_num,bbox_inches='tight')
    return()

