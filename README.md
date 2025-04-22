#  Chronic Kidney Disease (CKD) Detection Project

##  Overview
This project aims to detect and classify Chronic Kidney Disease (CKD) stages using machine learning and deep learning techniques. It involves exploratory data analysis (EDA), preprocessing, modeling, evaluation, and model persistence for real-world usage.

## Team Collaboration
> [**Anish Paul**]
> Data Preprocessing & Augmentation
> (Handled missing values, feature encoding, scaling, and applied SMOTE augmentation)

> [**Akash Mitra**]
>Neural Network Design & Model Training
> (Built and trained the neural network architecture, optimized hyperparameters)

> [**Ekra Bintay Ismail**]
> Data Analysis, Evaluation & Documentation
> (Analyzed results, compared performance, and documented the entire project)



## Dataset Information

This project dataset:
- `CKD_dataset_AbuDhabi.csv`

Each dataset contains clinical and laboratory features with a corresponding target column (`stage`, `ckd_stage`, or `CKD_stage`) representing the CKD stage.




1. Data Loading:
   The dataset "ChronicKidneyDisease_EHRs_from_AbuDhabi.csv" was loaded into a Pandas DataFrame to facilitate structured data manipulation and analysis within the Python environment.

2. Data Exploration:
   An exploratory data analysis was conducted to understand the overall structure and composition of the dataset. This included identifying numerical and categorical features, examining the distribution of values,
   checking for the presence of missing data, and confirming the data types of each column. Based on this analysis, suitable augmentation techniques were selected according to the nature of the data.

3. Data Preparation:
   To prepare the dataset for augmentation:
   - Missing values were handled appropriately, either by imputation or removal, depending on the context and importance of the feature.
   - Categorical features, if present, were encoded using label encoding or one-hot encoding to convert them into numerical form, suitable for machine learning models.
   - Numerical features were scaled as needed to ensure consistency across the dataset and to improve model training stability.

4. Data Augmentation:
   To enhance the dataset and support model generalization, the dataset size was increased by 30% using augmentation techniques:
   - SMOTE (Synthetic Minority Over-sampling Technique) was employed for augmenting numerical features, especially to balance class distributions if imbalance was detected.
   - Random oversampling was considered for categorical features (if any were found) to improve the representation of underrepresented classes.
   Given the medical nature of the data, caution was exercised to ensure that the augmented data remained realistic and medically plausible.
   avoiding the introduction of noise that could compromise the integrity of the analysis.

5. Data Analysis:
   Finally, a comparative analysis was performed between the original and augmented datasets using descriptive statistics such as mean, standard deviation, and distribution plots. This step was essential to confirm that the augmentation process preserved the core characteristics of the original dataset and did not introduce unintended bias or distortion.

6. The average accuracy, precision, recall, and F1 score for your neural network model evaluated using 5-fold cross-validation

# Results and Performance
Average accuracy across 5 folds: 98.24% ,
Average precision across 5 folds: 97.00% ,
Average recall across 5 folds: 98.15% ,
Average F1 score across 5 folds: 97.57%

# References
https://www.kaggle.com/datasets/davidechicco/chronic-kidney-disease-ehrs-abu-dhabi?resource=download
