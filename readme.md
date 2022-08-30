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
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
