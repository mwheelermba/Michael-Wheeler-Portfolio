# Project - Predicting Insurance Charges
Dive into the heart of data science with a project that combines healthcare insights and predictive analytics. As a Data Scientist at a top Health Insurance company, you have the opportunity to predict customer healthcare costs using the power of machine learning. Your insights will help tailor services and guide customers in planning their healthcare expenses more effectively.

## Dataset Summary

Meet your primary tool: the `insurance.csv` dataset. Packed with information on health insurance customers, this dataset is your key to unlocking patterns in healthcare costs. Here's what you need to know about the data you'll be working with:

## insurance.csv
| Column    | Data Type | Description                                                      |
|-----------|-----------|------------------------------------------------------------------|
| `age`       | int       | Age of the primary beneficiary.                                  |
| `sex`       | object    | Gender of the insurance contractor (male or female).             |
| `bmi`       | float     | Body mass index, a key indicator of body fat based on height and weight. |
| `children`  | int       | Number of dependents covered by the insurance plan.              |
| `smoker`    | object    | Indicates whether the beneficiary smokes (yes or no).            |
| `region`    | object    | The beneficiary's residential area in the US, divided into four regions. |
| `charges`   | float     | Individual medical costs billed by health insurance.             |


A bit of data cleaning is key to ensure the dataset is ready for modeling. Once your model is built using the `insurance.csv` dataset, the next step is to apply it to the `validation_dataset.csv`. This new dataset, similar to your training data minus the `charges` column, tests your model's accuracy and real-world utility by predicting costs for new customers.

## Tasks:
Develop a regression model using the insurance.csv dataset to predict charges. Evaluate the model's accuracy with the R-Squared Score. Then, apply the model to estimate predicted_charges for unseen data in validation_dataset.csv.
* Build a regression model to predict charges using the insurance.csv dataset. Evaluate the R-Squared Score of your trained model and save it as a variable called r2_score. The model's success will be assessed based on its R-Squared Score, which must exceed a threshold of 0.65.
* Use the trained model to predict charges for the data in validation_dataset.csv. Store the predictions as a new column in the validation dataset called predicted_charges, saving as a pandas DataFrame called validation_data. If needed, handle any negative values by replacing them with the minimum basic charge, set at 1000.

## Findings
After preprocessing, the regression model explained 72.1% of the variance in predicting insurance charges, which surpassed the required 65%. The model then predicted the charges for each of the 50 records in the validation set. None of those predictions had a negative value or were below the minimum basic charge of 1000. 
