# Binary Classification 
 Binary classification of the data ```train.txt``` and test the performance on ```test.txt```
# Install
 - Anaconda3 distribution for  Python3 https://www.anaconda.com/distribution/
and install requirment.txt
```
pip install -r requirment.txt
```
 - or use python 3 and install this requirment.txt using the above command also 
- jupyter notebook (for better understanding of the steps and how i made these decisions).

# Overview 

- ## Preprocessing Notebook Or preprocessing.py 
  - Both have the same code but the notebook have also data exploration code of the data sets and how i came up with these decision. 
  - ### Preprocessing steps

    - Read Data correctly (read variable2,3,8 14,15,17 and 19 correctly as numeric values)
    - imputation of variable1,4,5,6,7 with mode value (because they are categorial variables)
    - imputation of variable2,14,17 with mean value (because they are numeric variables)
    - Remove variable18 columns (because its have null values greater than 50% and also has strong correlation with variable10)
    - Remove variable5 because it is totally correlated with variable4
    - Remove variable17 because it is totally correlated with variable14
    - Remove variable19 because it can lead to missclassification (totally correlated with Class label in train data set but not in test data set)
    - Because the data train is unbalanced and this can led to high FalsePositive or high FalseNegative so we will use SMOTE technique to generate synthetic samples
    - Because the data have many categorial features and we must encode them to number so i will encode them using oneHotencoding technique (better than label encoding because the categorial data we have don't have order relationship)
 