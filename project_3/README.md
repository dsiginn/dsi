# Project 3: Web APIs & Classification

### Goals:
1. Using Reddit's API, you'll collect posts from two subreddits of your choosing.
2. You'll then use NLP to train a classifier on which subreddit a given post came from. This is a binary classification problem.

### Subreddits of choice!
[**Famliy**](https://www.reddit.com/r/family) | [**JustNoMotherinlaw Subreddit**](https://www.reddit.com/r/JUSTNOMIL)

### Problem Statement

We will be using Natural Language Progamming to train a classifier model on which subreddit a given post came from.

### Executive Summary
- Data collection
- Data cleaning 
- Preprocessing and Modelling
- Evaluation
- Conlusion

### Data Gathering
As we are classifing using NLP, data gathering was a challenge as urls links, memes/gif are popular ways of how users submit post in Reddit. We chose Family and JustnoMotherinlaw as subreddit choices becuase subreddit users values privacy and will have a higher tendecy to post text content. To gather the data for this research, I used Jupyter Notebook to scrape Reddit's API. I collected the text from the recent 1000 posts from each respective topic. EDA included removing null values and tokenizing using Regex to remove punctuation, url components, and HTML formatted character codes

### Preprocessing and Modelling/ Evaluation

Pre-processing includes lemmatizing, vectorizing with Count Vectorizer and TF-IDF (Term Frequency-Inverse Document Frequency) to enhance modeling response. We did a train-test spilt and begin modelling. Using pipeline, we include GridsearchCV for Model optimization, Multinomial Naive Bayes and Logistic Regression in the modelling process.


### Conclusion
Logistic Regression out perform Mutinomial NB model.

