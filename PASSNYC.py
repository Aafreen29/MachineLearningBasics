# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 09:17:01 2018

@author: Aafreen Dabhoiwala
"""

#------ Step by Step EDA (Exploratory Data Analysis) ANALYSIS----------------------------

# import the necessary module for data manipulation and data visualization.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as matplot
import seaborn as sns
%matplotlib


from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly import tools
import plotly.plotly as py

#opening the file
df = pd.read_csv('C:/Users/Aafreen Dabhoiwala/Documents/Kaggle/2016 School Explorer- PASSNYC.csv')
df.head(3)
df.shape

#preprocessing some data
#creating the function to convert the percentage into flot value

def p2f(x):
    return float(x.strip('%'))/100

df['Percent of Students Chronically Absent']=df['Percent of Students Chronically Absent'].astype(str).apply(p2f)
df['Rigorous Instruction %'] = df['Rigorous Instruction %'].astype(str).apply(p2f)
df['Collaborative Teachers %'] = df['Collaborative Teachers %'].astype(str).apply(p2f)
df['Supportive Environment %'] = df['Supportive Environment %'].astype(str).apply(p2f)
df['Effective School Leadership %'] = df['Effective School Leadership %'].astype(str).apply(p2f)
df['Strong Family-Community Ties %'] = df['Strong Family-Community Ties %'].astype(str).apply(p2f)
df['Trust %'] = df['Trust %'].astype(str).apply(p2f)
df['Student Attendance Rate'] = df['Student Attendance Rate'].astype(str).apply(p2f)

#ECONOMIC NEED INDEX distribution of the New York on it map

df['School Income Estimate'] = df['School Income Estimate'].str.replace(',', '')
df['School Income Estimate'] = df['School Income Estimate'].str.replace('$', '')
df['School Income Estimate'] = df['School Income Estimate'].str.replace(' ', '')
df['School Income Estimate'] = df['School Income Estimate'].astype(float)

df['School Income Estimate'] = df['School Income Estimate'].fillna(0)
df['Economic Need Index'] = df['Economic Need Index'].fillna(0)

#Statistic View of the above trend

df.plot(kind="scatter", x="Longitude", y="Latitude",
    s=df['School Income Estimate']/1400, c="Economic Need Index", cmap=plt.get_cmap("jet"),
        label='Schools', title='New York School Population Map',colorbar=True, alpha=0.4, figsize=(15,7))


#Findings from the above analyis:
# Schools that are located in the Upper and central New York Area have Higher econommic need


#-------Percentage of schools having black students in New York
df['Percent Asian'] = df['Percent Asian'].apply(p2f)
df['Percent Black'] = df['Percent Black'].apply(p2f)
df['Percent Hispanic'] = df['Percent Hispanic'].apply(p2f)
df['Percent White'] = df['Percent White'].apply(p2f)
df['Percent Black / Hispanic'] = df['Percent Black / Hispanic'].apply(p2f)

df.plot(kind="scatter", x="Longitude", y="Latitude",
    s=df['School Income Estimate']/4500, c="Percent Black", cmap=plt.get_cmap("jet"),
        label='Schools', title='New York School Black Ratio',colorbar=True, alpha=0.4, figsize=(15,7))

# Findings from the above analysis:
# Majority of black population are living in Central New York.

#----------Percentage of schools having hispanic students in New York

df.plot(kind="scatter", x="Longitude", y="Latitude",
    s=df['School Income Estimate']/4500, c="Percent Hispanic", cmap=plt.get_cmap("jet"),
        label='Schools', title='New York School Hispanic Ratio',colorbar=True, alpha=0.4, figsize=(15,7))

#Findings from the above analysis:
# Majority of Hispanic population are living in Upper New York.
# Black and Hispanic are isolated from each other.

#-------Percentage of schools having Asian students in New York
df.plot(kind="scatter", x="Longitude", y="Latitude",
    s=df['School Income Estimate']/4500, c="Percent Asian", cmap=plt.get_cmap("jet"),
        label='Schools', title='New York School Asian Ratio',colorbar=True, alpha=0.4, figsize=(15,7))

#Findings from the above statistics:
# Asian population are mostly living in Central New York

#---- Percentage of schools having White studnets in New York
df.plot(kind="scatter", x="Longitude", y="Latitude",
    s=df['School Income Estimate']/4500, c="Percent White", cmap=plt.get_cmap("jet"),
        label='Schools', title='New York School Asian Ratio',colorbar=True, alpha=0.4, figsize=(15,7))

#Findings from the above statistics:
#White population are mostly in lower and edge parts of New York


#----- RACE DISTRIBUTION FROM SCHOOLS

#---------WHITE AND ASIAN DISTRIBUTION--------------------------------
# Set up the matplotlib figure
f, axes = plt.subplots(ncols=2, figsize=(15, 6))

# Graph 
sns.distplot(df['Percent Asian'], kde=False, color="g", ax=axes[0], bins=25).set_title('% Asian Distribution')

axes[0].set_ylabel('School Count')

# Graph
sns.distplot(df['Percent White'], kde=False, color="r", ax=axes[1], bins=25).set_title('% White Distribution')

axes[1].set_ylabel('school count')


#----------BLACK AND HISPANIC DISTRIBUTION------------------------------
f, axes = plt.subplots(ncols=2, figsize=(15, 6))

#Graph
sns.distplot(df['Percent Black'], kde=False, color="g", ax=axes[0], bins=25).set_title('% Black Distribution')

axes[0].set_ylabel('School Count')

#Graph
sns.distplot(df['Percent Hispanic'], kde=False, color="b", ax=axes[1], bins=25).set_title('% Hipanic Distribution')

axes[0].set_ylabel('School Count')

# Findings from the above statistics
# Black and Hispanic represents majority of the school's population
# White and Asians are representing approx 15% of the school's population

#-------------ECONOMIC NEED INDEX and RACE DISTRIBUTION RELATION-----------------
f, axes= plt.subplots(2, 2, figsize=(19, 9))

#Graph
sns.regplot(x=df["Economic Need Index"], y=df["Percent Asian"], color='purple', ax=axes[0, 0], line_kws={"color": "black"})
sns.regplot(x=df["Economic Need Index"], y=df["Percent White"], color='g', ax=axes[0, 1], line_kws={"color": "black"})
sns.regplot(x=df["Economic Need Index"], y=df["Percent Black"], color='b', ax=axes[1, 0], line_kws={"color": "black"})
sns.regplot(x=df["Economic Need Index"], y=df["Percent Hispanic"], color='r', ax=axes[1, 1], line_kws={"color": "black"})

# Findings from the above analysis
# schools with higher white and asian have approximately LOWER ECONOMIC NEED SCORE
# schools with higher black and hispanic have HIGHER ECONOMIC NEED SCORE

#---- SCHOOL AND SCHOOL ATTENDANCE-----------------------------

print(df['Percent of Students Chronically Absent'].mean())

# from the above analysis the AVERAGE ABSENT RATE is 21%----

#--------create a data frame of schools with an absent rate of 30% or more-----
absent_30 = df[df['Percent of Students Chronically Absent']>=.30]

#-------Create a dataframe of schools with an absent rate of 11% or less.
absent_11 = df[df['Percent of Students Chronically Absent']<=.11]

#Exploring absent rate 

df['Percent of Students Chronically Absent'].describe()


#----- Average Economic Need and School Income Estimate of 30% Absent Ratio
print(absent_30['Economic Need Index'].mean())

print(absent_30['School Income Estimate'].mean())

# From the above analysis, 
# Average Economic Need Index at 84% and Average school income rate is $25000

absent_30.iloc[:,[15,16,17,23,19,20,21,22]].describe()

# from the above analysis, it shows that Asians and white make up to 5% of the students
# And Black and Hispanic make up to 95% of the students

print(absent_11['Economic Need Index'].mean())

print(absent_11['School Income Estimate'].mean())

# From the above analysis, 
# Average Economic Need Index at 44% and Average school income rate is $45000

absent_11.iloc[:,[3,15,16,17,23,19,20,21,22]].describe()

# from the above analysis, it shows that Black and Hispanic make up to approx 52% of the students
# And Asians and White make up to aprrox 48% of the students

#-- LOCATION OF HIGH AND LOW ABSENT RATE SCHOOLS

absent_30.plot(kind="scatter", x="Longitude", y="Latitude",
    s=absent_30['School Income Estimate']/4500, c="Economic Need Index", cmap=plt.get_cmap("jet"),
        label='Schools', title='New York School with 30% Absent Ratio',colorbar=True, alpha=0.4, figsize=(15,7))

# From the above analysis, it shows that schools with 30% of absent rate are more concentrated 
# in the CENTRAL AND UPPER regions of New York

absent_11.plot(kind="scatter", x="Longitude", y="Latitude",
    s=absent_11['School Income Estimate']/4500, c="Economic Need Index", cmap=plt.get_cmap("jet"),
        label='Schools', title='New York School with 10% Absent Ratio',colorbar=True, alpha=0.4, figsize=(15,7))

# From the above analysis, it shows that schools with 10% of absent rate are dispersed all
# around New York


#------- Student ELA and MATH Performance By Race-----------------

# Display the Mean ELA and Math Scores for Black/Hispanic Dominant Schools
df[df['Percent Black / Hispanic'] >= .70][['Average ELA Proficiency','Average Math Proficiency']].mean()

# Display the Mean ELA and Math Scores for White/Asian Dominant Schools
df[df['Percent Black / Hispanic'] <= .30][['Average ELA Proficiency','Average Math Proficiency']].mean()


#--------Math Test Performance By Race----------------

asian_math = []
asian_math.append(sum(df['Grade 3 Math 4s - Asian or Pacific Islander']))
asian_math.append(sum(df['Grade 4 Math 4s - Asian or Pacific Islander']))
asian_math.append(sum(df['Grade 5 Math 4s - Asian or Pacific Islander']))
asian_math.append(sum(df['Grade 6 Math 4s - Asian or Pacific Islander']))
asian_math.append(sum(df['Grade 7 Math 4s - Asian or Pacific Islander']))
asian_math.append(sum(df['Grade 8 Math 4s - Asian or Pacific Islander']))


white_math = []
white_math.append(sum(df['Grade 3 Math 4s - White']))
white_math.append(sum(df['Grade 4 Math 4s - White']))
white_math.append(sum(df['Grade 5 Math 4s - White']))
white_math.append(sum(df['Grade 6 Math 4s - White']))
white_math.append(sum(df['Grade 7 Math 4s - White']))
white_math.append(sum(df['Grade 8 Math 4s - White']))

black_math = []
black_math.append(sum(df['Grade 3 Math 4s - Black or African American']))
black_math.append(sum(df['Grade 4 Math 4s - Black or African American']))
black_math.append(sum(df['Grade 5 Math 4s - Black or African American']))
black_math.append(sum(df['Grade 6 Math 4s - Black or African American']))
black_math.append(sum(df['Grade 7 Math 4s - Black or African American']))
black_math.append(sum(df['Grade 8 Math 4s - Black or African American']))

hispanic_math = []
hispanic_math.append(sum(df['Grade 3 Math 4s - Hispanic or Latino']))
hispanic_math.append(sum(df['Grade 4 Math 4s - Hispanic or Latino']))
hispanic_math.append(sum(df['Grade 5 Math 4s - Hispanic or Latino']))
hispanic_math.append(sum(df['Grade 6 Math 4s - Hispanic or Latino']))
hispanic_math.append(sum(df['Grade 7 Math 4s - Hispanic or Latino']))
hispanic_math.append(sum(df['Grade 8 Math 4s - Hispanic or Latino']))


# Create dataframe of math scores
race_mathscores = pd.DataFrame({'Asian Math':asian_math,'Black Math':black_math,'White Math':white_math, 'Hispanic Math':hispanic_math})
race_mathscores['Grade'] = [3,4,5,6,7,8]
race_mathscores

#--- From the above analysis, it shows that White and Asians have higher counts of 4s 
#-- on their  MATH Test

# Black and Hispanic have lower count of 4s on their MATH Test

#------ ELA Test Performance by Race-------

# Create the math scores for each race
asian_ELA = []
asian_ELA.append(sum(df['Grade 3 ELA 4s - Asian or Pacific Islander']))
asian_ELA.append(sum(df['Grade 4 ELA 4s - Asian or Pacific Islander']))
asian_ELA.append(sum(df['Grade 5 ELA 4s - Asian or Pacific Islander']))
asian_ELA.append(sum(df['Grade 6 ELA 4s - Asian or Pacific Islander']))
asian_ELA.append(sum(df['Grade 7 ELA 4s - Asian or Pacific Islander']))
asian_ELA.append(sum(df['Grade 8 ELA 4s - Asian or Pacific Islander']))

white_ELA = []
white_ELA.append(sum(df['Grade 3 ELA 4s - White']))
white_ELA.append(sum(df['Grade 4 ELA 4s - White']))
white_ELA.append(sum(df['Grade 5 ELA 4s - White']))
white_ELA.append(sum(df['Grade 6 ELA 4s - White']))
white_ELA.append(sum(df['Grade 7 ELA 4s - White']))
white_ELA.append(sum(df['Grade 8 ELA 4s - White']))

black_ELA = []
black_ELA.append(sum(df['Grade 3 ELA 4s - Black or African American']))
black_ELA.append(sum(df['Grade 4 ELA 4s - Black or African American']))
black_ELA.append(sum(df['Grade 5 ELA 4s - Black or African American']))
black_ELA.append(sum(df['Grade 6 ELA 4s - Black or African American']))
black_ELA.append(sum(df['Grade 7 ELA 4s - Black or African American']))
black_ELA.append(sum(df['Grade 8 ELA 4s - Black or African American']))

hispanic_ELA = []
hispanic_ELA.append(sum(df['Grade 3 ELA 4s - Hispanic or Latino']))
hispanic_ELA.append(sum(df['Grade 4 ELA 4s - Hispanic or Latino']))
hispanic_ELA.append(sum(df['Grade 5 ELA 4s - Hispanic or Latino']))
hispanic_ELA.append(sum(df['Grade 6 ELA 4s - Hispanic or Latino']))
hispanic_ELA.append(sum(df['Grade 7 ELA 4s - Hispanic or Latino']))
hispanic_ELA.append(sum(df['Grade 8 ELA 4s - Hispanic or Latino']))


# Create dataframe of ELA scores
race_ELA = pd.DataFrame({'Asian ELA':asian_ELA,'Black ELA':black_ELA,'White ELA':white_ELA, 'Hispanic ELA':hispanic_ELA})
race_ELA['Grade'] = [3,4,5,6,7,8]
race_ELA


# from the above analysis, it shows that Asians and white dominates in ELA too in 4s on their ELA test 

#---------KEY NOTES FROM ALL OF THE ABOVE EDA (EXPLORATORY DATA ANALYSIS)--------------------------------
# 1>>>>>  Central and Upper New York schools are mostly in Need. 
# 2>>>>> Central and Upper New York contains more underperforming students.
# 3>>>>> Mojority of Black are in Central New york
# 4>>>>> Majority of HIspanic are in Upper NEw york
# 5>>>>> Schools with 30% or more Absent Rate have an average of 95% Black/Hispanic Dominated Schools
# 6>>>>> On average, Black/Hispanic have a lower ELA & Math Performance Scores than White/Asian
# 7>>>>> Overall, Asians received the most 4s in ELA and Math Performance.