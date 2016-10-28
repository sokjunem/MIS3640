from nltk.sentiment.vader import SentimentIntensityAnalyzer

sentence = 'I am so happy that movie was so bad. horrible'

score = SentimentIntensityAnalyzer().polarity_scores(sentence)
print(score)

input()
