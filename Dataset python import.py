# -*- coding: utf-8 -*-
"""CS 412 Group Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1G43K99pr3tJ-9Ijrx1gOmM9I4OFtXh5z
"""

#
# CS 412 - Group Project
#

#
# Author: Shiladitya
#

#
# Importing Dataset: Predict Students' Dropout and Academic Success
# Link: https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success

#
# Dataset Description: A dataset created from a higher education institution (acquired from several disjoint databases)
# related to students enrolled in different undergraduate degrees, such as agronomy, design, education, nursing, journalism,
# management, social service, and technologies. The dataset includes information known at the time of student enrollment
# (academic path, demographics, and social-economic factors) and the students' academic performance at the end of the first
# and second semesters. The data is used to build classification models to predict students' dropout and academic sucess.
# The problem is formulated as a three category classification task, in which there is a strong imbalance towards one of the classes.
#

# Dataset Citation: Realinho,Valentim, Vieira Martins,Mónica, Machado,Jorge, and Baptista,Luís. (2021). Predict Students' Dropout and Academic Success. UCI Machine Learning Repository. https://doi.org/10.24432/C5MC89.

#
# N(students) instances = 4424, Num_features = 36
#


# Importing...

!pip install ucimlrepo

from ucimlrepo import fetch_ucirepo

# fetch dataset
predict_students_dropout_and_academic_success = fetch_ucirepo(id=697)

# data (as pandas dataframes)
X = predict_students_dropout_and_academic_success.data.features
y = predict_students_dropout_and_academic_success.data.targets

# metadata
print(predict_students_dropout_and_academic_success.metadata)

# variable information
print(predict_students_dropout_and_academic_success.variables)