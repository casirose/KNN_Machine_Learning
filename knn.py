import pandas as pd
from tqdm import tqdm
import time


test = pd.read_csv('test_set.csv')
training = pd.read_csv('training_set.csv')


test_copy = test


del test_copy[test_copy.columns[0]]
test_copy.head()


num_of_train = len(training.axes[1])

df = pd.DataFrame()
col_name = 0


for (columnName, columnData) in tqdm(test_copy.iteritems(),desc="Loading…",ascii=False, ncols=75):#loops 6009 times
    x = columnName# get the column name 
    dis_test_train = []
    col_name += 1 #for naming the distance dataframe
    for j in range(1,num_of_train):# loops 14833 times
        y = 'train' + str(j) # for looping through the training data set
        def ed(x,y):
                
                diff = 0
                for i in range(0,len(x)):#loops 85 times
                    diff = diff + ((x[i]-y[i])**2)
                dis = diff**0.5
                dis_test_train.append(dis)
        ed(test[x],training[y]) 
    df.loc[:,'dis_test_train'+str(col_name)] = dis_test_train