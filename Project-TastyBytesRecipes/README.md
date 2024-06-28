# Tasty Bytes Recipe Popularity Prediction
Welcome to the Tasty Bytes Recipe Popularity Prediction project! Our main objective is to predict recipes that will boost our website's traffic and ensure that these selections are correct 80% of the time.

## Background
Founded in 2020, Tasty Bytes emerged during the Covid Pandemic as a beacon for food enthusiasts. Initially introduced as a recipe search engine, it later transitioned into a comprehensive culinary platform offering tailored meal plans. With the right recipe displayed on the homepage, we've seen traffic boosts of up to 40%, leading to higher subscription rates. Your role? Use data science magic to predict these traffic-boosting recipes!

## Challenge
Predict recipes that lead to high traffic. Aim for 80% accuracy in these predictions. Craft and showcase a presentation with your findings and recommendations for the product team. Compile a detailed report capturing your analytical journey, including the code, thought process, and decision-making narrative. Currently, recipe selection is based on heuristics and domain knowledge. While this can still produce hit recipes, it is not as reliable as a predictive model could be.

## Methods:
* Logistic regression is used as the baseline.
* K-Neighbors Classifier and Decision Tree Classifier are both used as well.
* Metrics used include accuracy, precision, recall, and f1 scores.
* The metric of interest is **precision**.

## Results:
* Logistic Regression with a parameter of C=0.201 produced the highest precision score of the three models at 82.24%.

