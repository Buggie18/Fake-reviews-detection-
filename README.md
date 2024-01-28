# Fake-Reviews-Detection

## Problem Statement
In the realm of e-commerce, a pervasive issue that erodes user trust and hinders informed decision-making is the prevalence of fake reviews. Fake reviews can mislead consumers by providing false information about products or services.

This deceptive practice impacts user trust, as individuals rely on reviews to make purchasing decisions. Identifying and mitigating the influence of fake reviews is crucial for maintaining the integrity of the online marketplace and ensuring that users can make well-informed choices based on genuine feedback.

## Description

 Description: The generated fake reviews dataset, containing 20k fake reviews and 20k real product reviews. OR = Original reviews (presumably human created and authentic); CG = Computer-generated fake reviews. 
 
## Python Libraries and Packages Used
 
 <ul>
  <li>Numpy</li>
  <li>Pandas</li>
  <li>Matplotlib.pyplot</li>
  <li>Seaborn</li>
  <li>Warnings</li>
  <li>nltk</li>
  <li>nltk.corpus</li>
  <li>String</li>
  <li>sklearn.naive_bayes</li>
  <li>sklearn.feature_extraction</li>
  <li>sklearn.model_selection</li>
  <li>sklearn.ensemble</li>
  <li>sklearn.tree</li>
  <li>sklearn.linear_model</li>
  <li>sklearn.svc</li>
  <li>sklearn.neighbors</li>
</ul>

## Techniques Used for Text Preprocessing

<ul>
  <li>Removing punctuation character</li>
  <li>Transforming text to lower case</li>
  <li>Eliminating stopwords</li>
  <li>Stemming</li>
  <li>Lemmatizing</li>
  <li>Removing digits</li>
</ul>

## Transformers Used for Text Vectorization, Weighting and Normalization

<ul>
  <li>CountVectorizer Bag of Words Transformer</li>
  <li>TFIDF(Term Frequency-Inverse Document Frequency) Transformer</li>
</ul>

## Machine Learning Algorithms Used

<ol>
  <li>Logistic Regression</li>
  <li>K Nearest Neighbors</li>
  <li>Support Vector Classifier</li>
  <li>Decision Tree Classifier</li>
  <li>Random Forests Classifier</li>
  <li>Multinomial Naive Bayes</li>
</ol>

## Performance Overview of ML Models Leveraged

<p>Among the algorithms tested for identifying fake reviews, Support Vector Machines (SVM) had the highest accuracy rate at slightly over 88%, closely trailed by Logistic Regression at just over 86%. Random Forests and Multinomial Naive Bayes followed closely behind, each achieving around 84% accuracy. However, Decision Trees lagged significantly behind with an accuracy just over 73%. K Nearest Neighbors (KNN) performed the worst among the algorithms, achieving an accuracy of nearly 58%.</p>

