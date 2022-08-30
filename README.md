# Sentiment Analysis using nltk

nltk is a python module that helps us in analysing sentiments\
nltk stands for Natural Language Toolkit
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install nltk.

```bash
pip install nltk
```

## Importing the library
```python
import nltk.sentiment
```
The nltk library which is installed need to be imported
## Score calculator function
```python
def get_score(input_text):
    analyzer = nltk.sentiment.SentimentIntensityAnalyzer()
```
SentimentIntensityAnalyzer is a package that is present in nltk.sentiment. Here analyzer is an object.
```python
    scores = analyzer.polarity_scores(input_text)
```
scores is a dictionary, that has keys for various scores like nagative, positive and neutral. 'compound' is the key that we consider here
```python
    sentiment_score = scores['compound']
    return sentiment_score
```
sentiment_score has values in between -1 to +1, indicating the quantity of sentiment

## Display Function
```python
def get_reaction(score):
    if(score > 0.5):
        return 'Highly Positive'
    if(score > 0):
        return 'Positive'
    if(score == 0):
        return 'Neutral'
    if(score < -0.5):
        return 'Highly Negative'
    if(score < 0):
        return 'Negative'
```
'score' that is obtained from calculator function is used to display message to the user. The scores and their respective sentiments are represented in the function.

## The main function
```python 
def main():
    input_text = input("Please enter a sentence : ")
    score = get_score(input_text)
    reaction = get_reaction(score)
    print('Sentiment score : ', score)
    print(reaction)
if __name__ == "__main__":
    main()
```
This consists of user input and calling essential functions.

## Samples (Input and Output)
![02](https://user-images.githubusercontent.com/94124126/187417838-d3da51d5-0f6b-41a8-8c24-2d488738951c.png)

![01](https://user-images.githubusercontent.com/94124126/187417823-078bbb56-75ca-4d78-aaf4-9da04116e565.png)

![03](https://user-images.githubusercontent.com/94124126/187417850-bb702e85-2b44-4dad-b9d3-7cb3d8dc4e37.png)

![04](https://user-images.githubusercontent.com/94124126/187417859-c0d35c77-643a-42ab-9df7-cf3b6773efca.png)

![05](https://user-images.githubusercontent.com/94124126/187417868-68af4a00-c794-4346-b76d-f316696c4395.png)

