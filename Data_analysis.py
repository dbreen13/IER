# -*- coding: utf-8 -*-
"""
Created on Thu May 13 17:02:52 2021

@author: demibreen
"""
#include the libraries
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
from scipy.stats import normaltest
from scipy.stats import levene
from tableone import TableOne

#read datafile
data1=pd.read_csv("Data_analysis_Data_IER.csv", sep=",", encoding='cp1252')

#Sort the data in the right samples
data1.sort_values(by=['year'], inplace=True)
df_1_t=data1.iloc[:94,:] #all the samples of 2019
df_2=data1.iloc[95:,:] #all the samples of 2020
#drop_indices = np.random.choice(df_2_t.index, 3, replace=False) # make the sample sizes of 2020 and 2019 same length by deleting three random entries
#df_2=df_2_t.drop(drop_indices)
df_1=df_1_t.drop(57) #drop the nan data sample
df_1.sort_values(by=['living'], inplace=True) #sort by living situation
df_2.sort_values(by=['living'], inplace=True) #sort by living situation

#make table 1
columns=['year', 'gender', 'bmi', 'living']
mytable = TableOne(data1, columns=columns, pval=False)
print(mytable.tabulate(tablefmt = "fancy_grid"))
mytable.to_csv('mytable.csv')

#split the data samples in living with their parents and moved out for 2020 and calculate means
grouped1=df_1.groupby(df_1.living)
Moved_out_2019=grouped1.get_group("Moved_out")
mean1=Moved_out_2019["attitu_2"].mean()
Parents_2019=grouped1.get_group("Living_with_parents")
mean2=Parents_2019["attitu_2"].mean()
#split the data samples in living with their parents and moved out for 2019 and calculate means
grouped2=df_2.groupby(df_2.living)
Moved_out_2020=grouped2.get_group("Moved_out")
mean3=Moved_out_2020["attitu_2"].mean()
Parents_2020=grouped2.get_group("Living_with_parents")
mean4=Parents_2020["attitu_2"].mean()

#plot in a figure the perception values 
plt.figure()
fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True)
Moved_out_2020["attitu_2"].plot.hist(ax=axes[0,0])
axes[0,0].set_title('MO 2020')
Parents_2020["attitu_2"].plot.hist(ax=axes[0,1])
axes[0,1].set_title('Parents 2020')
Moved_out_2019["attitu_2"].plot.hist(ax=axes[1,0])
axes[1,0].set_title('MO 2019')
Parents_2019["attitu_2"].plot.hist(ax=axes[1,1])
axes[1,1].set_title('Parents 2019')
plt.tight_layout()
plt.savefig('all.eps', format='eps')

#plot in a histogram the values of perception of 2020
plt.figure()
Parents_2020["attitu_2"].plot.hist(alpha=0.5, label='Living with the parents')
Moved_out_2020["attitu_2"].plot.hist(alpha=0.5, label='Moved out')
plt.legend(loc='upper left')
plt.title('Difference bewteen the perception of year 2020')
plt.savefig('2020.eps', format='eps')

#plot in a histogram the values of the perception of 2019 
plt.figure()
Parents_2019["attitu_2"].plot.hist(alpha=0.5, label='Living with the parents')
Moved_out_2019["attitu_2"].plot.hist(alpha=0.5, label='Moved out')
plt.legend(loc='upper left')
plt.title('Difference bewteen the perception of year 2019')
plt.savefig('2019.eps', format='eps')

#calculate the mean values for the amount of activity of parents (1) and friends (2)
mean5=Moved_out_2020["soc_omg_1"].mean()
mean6=Moved_out_2020["soc_omg_2"].mean()

mean7=Parents_2020["soc_omg_1"].mean()
mean8=Parents_2020["soc_omg_2"].mean()

mean9=Moved_out_2019["soc_omg_1"].mean()
mean10=Moved_out_2019["soc_omg_2"].mean()

mean11=Parents_2019["soc_omg_1"].mean()
mean12=Parents_2019["soc_omg_2"].mean()


#perform t-test to see whether mean values of the different livingsituations are of significant difference

stat1, p1 = ttest_ind(Moved_out_2020["attitu_2"], Parents_2020["attitu_2"])
print('stat=%.3f, p=%.3f' % (stat1, p1))
if p1 > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')
    
stat2, p2 = ttest_ind(Moved_out_2019["attitu_2"], Parents_2019["attitu_2"])
print('stat=%.3f, p=%.3f' % (stat2, p2))
if p2 > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')

#perform t-test to see whether mean values of estimates of activity of friends and parents is significant

stat5, p5 = ttest_ind(Moved_out_2020["soc_omg_1"], Moved_out_2020["soc_omg_2"])
print('stat=%.3f, p=%.3f' % (stat5, p5))
if p5 > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')
stat6, p6 = ttest_ind(Moved_out_2019["soc_omg_1"], Moved_out_2019["soc_omg_2"])
print('stat=%.3f, p=%.3f' % (stat6, p6))
if p6 > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')
    
stat7, p7 = ttest_ind(Parents_2020["soc_omg_1"], Parents_2020["soc_omg_2"])
print('stat=%.3f, p=%.3f' % (stat7, p7))
if p7 > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')
    
stat8, p8 = ttest_ind(Parents_2019["soc_omg_1"], Parents_2019["soc_omg_2"])
print('stat=%.3f, p=%.3f' % (stat8, p8))
if p8 > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')



#Test all the assumptions


#test whether normal distributions

stat, p = normaltest(Moved_out_2020["attitu_2"])
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably Gaussian')
else:
	print('Probably not Gaussian')
    
stat3, p3 = normaltest(Parents_2020["attitu_2"])
print('stat=%.3f, p=%.3f' % (stat3, p3))
if p3 > 0.05:
	print('Probably Gaussian')
else:
	print('Probably not Gaussian')   

stat9, p9 = normaltest(Moved_out_2019["attitu_2"])
print('stat=%.3f, p=%.3f' % (stat9, p9))
if p9 > 0.05:
	print('Probably Gaussian')
else:
	print('Probably not Gaussian')
    
stat10, p10 = normaltest(Parents_2019["attitu_2"])
print('stat=%.3f, p=%.3f' % (stat10, p10))
if p10 > 0.05:
	print('Probably Gaussian')
else:
	print('Probably not Gaussian')

stat11, p11 = normaltest(Parents_2019["soc_omg_1"])
print('stat=%.3f, p=%.3f' % (stat11, p11))
if p11 > 0.05:
	print('Probably Gaussian')
else:
	print('Probably not Gaussian')
stat12, p12 = normaltest(Parents_2019["soc_omg_2"])
print('stat=%.3f, p=%.3f' % (stat12, p12))
if p12 > 0.05:
	print('Probably Gaussian')
else:
	print('Probably not Gaussian')
    
stat13, p13 = normaltest(Moved_out_2019["soc_omg_1"])
print('stat=%.3f, p=%.3f' % (stat13, p13))
if p13 > 0.05:
	print('Probably Gaussian')
else:
	print('Probably not Gaussian')
    
stat14, p14 = normaltest(Moved_out_2019["soc_omg_2"])
print('stat=%.3f, p=%.3f' % (stat14, p14))
if p14 > 0.05:
	print('Probably Gaussian')
else:
	print('Probably not Gaussian')
    
stat15, p15 = normaltest(Parents_2020["soc_omg_1"])
print('stat=%.3f, p=%.3f' % (stat15, p15))
if p15 > 0.05:
	print('Probably Gaussian')
else:
	print('Probably not Gaussian')
stat16, p16 = normaltest(Parents_2020["soc_omg_2"])
print('stat=%.3f, p=%.3f' % (stat16, p16))
if p16 > 0.05:
	print('Probably Gaussian')
else:
	print('Probably not Gaussian')
    
stat17, p17 = normaltest(Moved_out_2020["soc_omg_1"])
print('stat=%.3f, p=%.3f' % (stat17, p17))
if p17 > 0.05:
	print('Probably Gaussian')
else:
	print('Probably not Gaussian')
    
stat18, p18 = normaltest(Moved_out_2020["soc_omg_2"])
print('stat=%.3f, p=%.3f' % (stat18, p18))
if p18 > 0.05:
	print('Probably Gaussian')
else:
	print('Probably not Gaussian')   
    
    

#Test the variance with Levene
stat4, p4=levene(Moved_out_2020["attitu_2"], Parents_2020["attitu_2"])
print('stat=%.3f, p=%.3f' % (stat4, p4))
if p4 > 0.05:
	print('Probably same varience')
else:
	print('Probably different varience') 

stat19, p19=levene(Moved_out_2019["attitu_2"], Parents_2019["attitu_2"])
print('stat=%.3f, p=%.3f' % (stat19, p19))
if p19 > 0.05:
	print('Probably same varience')
else:
	print('Probably different varience') 

stat20, p20=levene(Moved_out_2020["soc_omg_1"], Moved_out_2020["soc_omg_2"])
print('stat=%.3f, p=%.3f' % (stat20, p20))
if p20 > 0.05:
	print('Probably same varience')
else:
	print('Probably different varience') 
    
stat21, p21=levene(Moved_out_2019["soc_omg_1"], Moved_out_2019["soc_omg_2"])
print('stat=%.3f, p=%.3f' % (stat21, p21))
if p21 > 0.05:
	print('Probably same varience')
else:
	print('Probably different varience') 

stat22, p22=levene(Parents_2020["soc_omg_1"], Parents_2020["soc_omg_2"])
print('stat=%.3f, p=%.3f' % (stat22, p22))
if p22 > 0.05:
	print('Probably same varience')
else:
	print('Probably different varience') 

stat23, p23=levene(Parents_2019["soc_omg_1"], Parents_2019["soc_omg_2"])
print('stat=%.3f, p=%.3f' % (stat23, p23))
if p23 > 0.05:
	print('Probably same varience')
else:
	print('Probably different varience') 


