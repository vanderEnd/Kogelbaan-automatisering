import time
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 

'variabelen worden gedefinieerd wordt gedefinieerd' 
start = None
eind = None

#%%
'Tijdverschil wordt uitgerekend tussen twee pieken' 
def tijd_verschil(x1,x2): 
    global start,eind,tijden    
    if start == None and x1 >= 3:      
        start = time.time()
    if x2 >= 3 and eind == None and start != None:
        eind = time.time()
        print(round((eind - start),5))  
    if start != None and eind != None:
        start = None 
        eind = None
#%%
'Standaard plot word gegenereerd' 
def plot(y,x1,xlabel,ylabel):
    plt.plot(y,x1,'.b')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend([ylabel])
    plt.legend(loc=0)
    plt.grid(color='#AAAAAA', linestyle='--', linewidth=1)
    plt.show()
    return
#%%
'inlezen van de data' 
def inlezen(filename):    
    data = pd.read_csv(filename,sep=',',header=None,names=['tijd','ch1','ch2','ch3','ch4'])
#data uit csv bestand wordt ingelezen in lijsten 
    tijd = np.array(data['tijd'])
    ch1 = np.array(data['ch1']) #ch1 staat voor Channel 1 ch2 voor Channel 2 etc.
    ch2 = np.array(data['ch2'])
    ch3 = np.array(data['ch3'])
    ch4 = np.array(data['ch4'])
    return tijd,ch1,ch2,ch3,ch4
#%%
#Bit sensor/converter
#Range tot welk voltage gaat converter
#gaat de sensor/converter tot negatieve waarden
def data_converter(data,bit,Range,polariteit):
    counts = 2**bit
    if polariteit == True:
        data = data*2
    data = Range*data/counts
    print(data)

'TO Do'
'data plotten die ingelezen is gaat nog niet goed' 
    
        
    
    

