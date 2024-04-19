
# CS 412 - Group Project, Spring 2024

## Group Members: Aamir Merchant, Benjamin Caulfield, Krenar Banushi, Matias Garcia, and Shiladitya Singh Bhati

### Directory:

-> ReadMe.md - has directory information and dataset information.

-> Dataset python import.py - imports the data set from source (ucimlrepo) via python.

-> Project Oultine.txt - General project development information, to be iteratively updated.

-> LR SVM KNN notebook - import data, split train and test, model Logistic Regression, SVM, and KNN.


### Dataset Name: Predict Students' Dropout and Academic Success; 
Link: https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success

Dataset Description: A dataset created from a higher education institution (acquired from several disjoint databases) related to students enrolled in different undergraduate degrees, such as agronomy, design, education, nursing, journalism, management, social service, and technologies. The dataset includes information known at the time of student enrollment (academic path, demographics, and social-economic factors) and the students' academic performance at the end of the first and second semesters. The data is used to build classification models to predict students' dropout and academic success. The problem is formulated as a three category classification task, in which there is a strong imbalance towards one of the classes.

Dataset Citation: Realinho,Valentim, Vieira Martins,Mónica, Machado,Jorge, and Baptista,Luís. (2021). Predict Students' Dropout and Academic Success. UCI Machine Learning Repository. https://doi.org/10.24432/C5MC89.

Dataset information: 
N(students) instances = 4424, Num_features = 36

Features:
                                              name     role         type  
0                                   Marital Status  Feature      Integer   
1                                 Application mode  Feature      Integer   
2                                Application order  Feature      Integer   
3                                           Course  Feature      Integer   
4                       Daytime/evening attendance  Feature      Integer   
5                           Previous qualification  Feature      Integer   
6                   Previous qualification (grade)  Feature   Continuous   
7                                      Nacionality  Feature      Integer   
8                           Mother's qualification  Feature      Integer   
9                           Father's qualification  Feature      Integer   
10                             Mother's occupation  Feature      Integer   
11                             Father's occupation  Feature      Integer   
12                                 Admission grade  Feature   Continuous   
13                                       Displaced  Feature      Integer   
14                       Educational special needs  Feature      Integer   
15                                          Debtor  Feature      Integer   
16                         Tuition fees up to date  Feature      Integer   
17                                          Gender  Feature      Integer   
18                              Scholarship holder  Feature      Integer   
19                               Age at enrollment  Feature      Integer   
20                                   International  Feature      Integer   
21             Curricular units 1st sem (credited)  Feature      Integer   
22             Curricular units 1st sem (enrolled)  Feature      Integer   
23          Curricular units 1st sem (evaluations)  Feature      Integer   
24             Curricular units 1st sem (approved)  Feature      Integer   
25                Curricular units 1st sem (grade)  Feature      Integer   
26  Curricular units 1st sem (without evaluations)  Feature      Integer   
27             Curricular units 2nd sem (credited)  Feature      Integer   
28             Curricular units 2nd sem (enrolled)  Feature      Integer   
29          Curricular units 2nd sem (evaluations)  Feature      Integer   
30             Curricular units 2nd sem (approved)  Feature      Integer   
31                Curricular units 2nd sem (grade)  Feature      Integer   
32  Curricular units 2nd sem (without evaluations)  Feature      Integer   
33                               Unemployment rate  Feature   Continuous   
34                                  Inflation rate  Feature   Continuous   
35                                             GDP  Feature   Continuous   
36                                          Target   Target  Categorical   

