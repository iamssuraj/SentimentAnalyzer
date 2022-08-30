import nltk.sentiment
# nltk.downloader.download('vader_lexicon')

def get_score(input_text):
    #SentimentIntensityAnalyzer is a package from nltk.sentiment
    analyzer = nltk.sentiment.SentimentIntensityAnalyzer()
    # analyzer.polarity_scores is a part of nltk package
    scores = analyzer.polarity_scores(input_text)
    #sentiment_score is extracted, scores is a dictionary
    sentiment_score = scores['compound']
    #sentiment_score is value between -1 and +1
    return sentiment_score
    
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

def main():
    input_text = input("Please enter a sentence : ")
    score = get_score(input_text)
    reaction = get_reaction(score)
    print('Sentiment score : ', score)
    print(reaction)
if __name__ == "__main__":
    main()