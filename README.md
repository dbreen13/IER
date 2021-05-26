# IER; Living situation of students; the effect on the perception of the importance of a sufficient amount of physical activity.

## Table of contents
* [General info](#general-info)
* [Software](#software)
* [License](#license)
* [Acknowledgement](#acknowledgement)

## General info
Recent studies have shown that there is a correlationbetween  parental  support  and  the  amount  of  physical  activityconducted by their children. The question is whether this parentalsupport or more the lack of parental support when moving outwill result in a change in the perception of the first year’s studentsat  Erasmus  University.  Thus  the  research  question  is:  To  whatextent does the perception of the importance of sufficient exerciseof the first year Erasmus students living on their own differ fromthe  perception  of  first-year  Erasmus  students  living  with  theirparents?  For  this  research  a  t-test  has  been  performed  on  thedata, collected through the IPAQ questionnaire and the Omronfitness tracker, to show whether there was a significant differencebetween the perception of the importance of a sufficient amountof  exercise  between  students  living  on  their  own  or  with  theirparents. 

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
