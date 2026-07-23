# Project: Clustering Antarctic Penguin Species

You have been asked to support a team of researchers who have been collecting data about penguins in Antartica! The data is available in csv-Format as `penguins.csv`

**Origin of this data** : Data were collected and made available by Dr. Kristen Gorman and the Palmer Station, Antarctica LTER, a member of the Long Term Ecological Research Network.

**The dataset consists of 5 columns.**

Column | Description
--- | ---
culmen_length_mm | culmen length (mm)
culmen_depth_mm | culmen depth (mm)
flipper_length_mm | flipper length (mm)
body_mass_g | body mass (g)
sex | penguin sex

Unfortunately, they have not been able to record the species of penguin, but they know that there are **at least three** species that are native to the region: **Adelie**, **Chinstrap**, and **Gentoo**.  Your task is to apply your data science skills to help them identify groups in the dataset!

## Tasks:
Utilize your unsupervised learning skills to clusters in the penguins dataset!
* Import, investigate and pre-process the "penguins.csv" dataset.
* Perform a cluster analysis based on a reasonable number of clusters and collect the average values for the clusters. The output should be a DataFrame named stat_penguins with one row per cluster that shows the mean of the original variables (or columns in "penguins.csv") by cluster. stat_penguins should not include any non-numeric columns.

## Findings:
We have 4 clusters of penguins. 2 of the clusters are female, and 2 of the clusters are male. The main difference between each sex's 2 groups is the body mass. Group A for each sex is significantly larger than group B. These larger penguins also had longer, thinner culmens and longer flippers. Based on the visual, the groupings appear accurate and logical. The centroids are distant from one another and their bubbles hover near the centroid. Clusters 0 and 2 have a larger variation than clusters 1 and 3, suggesting that there may be a reasoning for a 5th or 6th group.
