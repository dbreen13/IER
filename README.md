# Living situation of students; the effect on the perception of the importance of a sufficient amount of physical activity.

## Table of contents
* [General info](#general-info)
* [Methodology] (#methodology)
* [Files] (#Files)
* [Software](#software)
* [License](#license)
* [Acknowledgement](#acknowledgement)

## General info
Recent studies have shown that there is a correlationbetween  parental  support  and  the  amount  of  physical  activityconducted by their children. The question is whether this parentalsupport or more the lack of parental support when moving outwill result in a change in the perception of the first year’s studentsat  Erasmus  University.  Thus  the  research  question  is:  To  whatextent does the perception of the importance of sufficient exerciseof the first year Erasmus students living on their own differ fromthe  perception  of  first-year  Erasmus  students  living  with  theirparents?  For  this  research  a  t-test  has  been  performed  on  thedata, collected through the IPAQ questionnaire and the Omronfitness tracker, to show whether there was a significant differencebetween the perception of the importance of a sufficient amountof  exercise  between  students  living  on  their  own  or  with  theirparents. 

## Methodology
The data used for this research was collected by other students and thus this secondary data was provided as a CSV file. This data was collected through a questionnaire and by gathering data from a fitness tracker without intervening. This same research was done in 2019 and 2020. 94 first-year students (both in 2020 and 2019) of the Erasmus University, located in Rotterdam, were asked to provide the following information and data when partitioning in the research: 
* Reported prior to the measuring of physical activity
  * Specifications about the demographics, containing gender, BMI (body mass index) and their living situation; living with their parents or moved out of the parental house.
  * Their perceived physical; How many steps they thought they took daily, whether they thought they got enough exercise (0=I do not agree at all --- 7=I completely agree) and the estimate of their level of physical activities (0=Very low --- 7=Very high).
  *  Questions on the attitude towards physical activity.
* Completed prior and after the measuring of the physical activity
  * A shortened International Physical Activity Questionnaire (IPAQ). The IPAQ questionnaire estimates the energy used during a full week as a result of physical activity. Thus a week without any PA will result in a score of zero.  
* The physical activity measurement:
  * The physical activity measured with the Omron fitness tracker.
  * The physical activity measured with the Omron app.
  * A check whether the students used the fitness tracker in the right way and for which amount of time they wore it. 

After the data was collected, a t-test was performed on the data to see whether there were significantly differences between the students that had moved out and that still lived with their parents. 
For this t-test some assumptions were made about the data samples used and were also proven to be correct (see code):
* The observations in each sample are independent. This is true for this data set since no individual in the group 'living with their parents' is also in the group 'moved out'. This is the case for both 2020 and 2019 because the students in the 2020 group are different from the ones in the 2019 group.\
* The observations in each sample are normally distributed.
* The observations in each sample have the same variance. This is proven using  Levene's test.

## Files
* The IPAQ questionnaire used for this research can be found in the file called: IPAQ Questionnaire.pdf
* The python code used for this research can be found in the file called: Data_analysis.py
## Software 
For this data analysis, different Python libraries were used. The version of Python that was used was Python 3.8: 
* [Pandas](https://pandas.pydata.org/) was used to open and manipulate the data. The version used is 1.0.5.
* [Matplotlib.pyplot](https://matplotlib.org/stable/index.html) was used to create the plots. The version used is 3.2.2.
* [Scipy.tests](https://docs.scipy.org/doc/scipy/reference/stats.html) was used to perform the t-test,  Levene's test and the normality test. The version used is 1.5.0.
* [Tableone](https://pypi.org/project/tableone/) was used to generate the Table 1 of the demographics of the research. The version used is 0.7.10.

Most of the above packages are already installed in Python 3.8 except Tableone, to install follow these instructions
```
$pip install tableone
```
## License
This project is licensed under MIT- see LICENCE.md for details about the license

## Ackowledgement
I would like to thank Heike Vallery, Angeniet Kam, Karin van Nispen, Yasemin Turkyilmaz and Lisa Hoogendam for the support during this research.
