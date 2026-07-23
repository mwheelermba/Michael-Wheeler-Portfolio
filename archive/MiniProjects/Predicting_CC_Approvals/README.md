# Project - Predicting Credit Card Approvals

Commercial banks receive _a lot_ of applications for credit cards. Many of them get rejected for many reasons, like high loan balances, low income levels, or too many inquiries on an individual's credit report, for example. Manually analyzing these applications is mundane, error-prone, and time-consuming (and time is money!). Luckily, this task can be automated with the power of machine learning and pretty much every commercial bank does so nowadays. In this workbook, you will build an automatic credit card approval predictor using machine learning techniques, just like real banks do.

### The Data

The data is a small subset of the Credit Card Approval dataset from the UCI Machine Learning Repository showing the credit card applications a bank receives. This dataset has been loaded as a `pandas` DataFrame called `cc_apps`. The last column in the dataset is the target value.

## Tasks:
Use supervised learning techniques to automate the credit card approval process for banks.
* Preproccess the data and apply supervised learning techniques to find the best model and parameters for the job. Save the accuracy score from your best model as a numeric variable, best_score. Aim for an accuracy score of at least 0.75. The target variable is the last column of the DataFrame.

## Findings
The Random Forest ensemble mmodel performs best on this data set, producing an accuracy score of 87.58% on the training set and 84.06% on the testing set, well above the required 75% for the project. It performs strongly for correctly predicting approvals and rejections equally. Its accuracy, precision, recall, and f1 score on the test set are all at 84%.
