# Project: Facial Recognition with Supervised Learning

You are a member of an elite group of data scientists, specialising in advanced facial recognition technology, this firm is dedicated to identifying and safeguarding prominent individuals from various spheres—ranging from entertainment and sports to politics and philanthropy. The team's mission is to deploy AI-driven solutions that can accurately distinguish between images of notable personalities and the general populace, enhancing the personal security of such high-profile individuals. You're to focus on Arnold Schwarzenegger, a figure whose accomplishments span from bodybuilding champion to Hollywood icon, and from philanthropist to the Governor of California. 

### **The Data**
The `data/lfw_arnie_nonarnie.csv` dataset contains processed facial image data derived from the "Labeled Faces in the Wild" (LFW) dataset, focusing specifically on images of Arnold Schwarzenegger and other individuals not identified as him. This dataset has been prepared to aid in the development and evaluation of facial recognition models. There are 40 images of Arnold Schwarzenegger and 150 of other people.

| Column Name | Description |
|-------------|-------------|
| PC1, PC2, ... PCN | Principal components from PCA, capturing key image features. |
| Label | Binary indicator: `1` for Arnold Schwarzenegger, `0` for others. |

## Tasks:
Leverage machine learning to enhance the security of influential figures by distinguishing Arnold Schwarzenegger from others.

Construct machine learning pipelines for three classification models. Store these initialized models in a dictionary named models.
* Determine the best performing model based on cross-validation scores. Save the model's name as best_model_name, its parameters as best_model_info, and its cross-validation score as best_model_cv_score.
* Evaluate the selected model and store accuracy, precision, recall, and f1 on the test set.
* Aim to achieve a minimum accuracy of 80% for at least one of the models. Save your best accuracy score as score.
As an optional step, use Matplotlib to create a confusion matrix visualization for the predictions made by your best model.

## Findings
