from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
# Initialize the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Example texts for sentiment analysis
df = pd.read_csv('/Users/mackmorgan/Desktop/test_reddit_data.csv')
neighborhood_score = {}
local_counts = []
local = 0
for index, row in df.iterrows():
    sentiment = analyzer.polarity_scores(str(row[1]))
    if row[0] in neighborhood_score.keys():
        neighborhood_score[row[0]] += sentiment['compound']
        local_counts[local - 1] += 1
    else:
        neighborhood_score[row[0]] = 0
        neighborhood_score[row[0]] += sentiment['compound']
        local_counts.append(0)
        local += 1
local = 0

#print(local_counts)
for k in neighborhood_score:
    if local_counts[local] == 0:
        pass
    else:
        neighborhood_score[k] /= local_counts[local]
    local+=1

neighborhood_score = dict(sorted(neighborhood_score.items(), key=lambda item: item[1], reverse=True))
print(neighborhood_score)    

neighborhood_score = dict(sorted(neighborhood_score.items(), key=lambda item: item[1], reverse=True))

# Convert the dictionary to a DataFrame for exporting
df_output = pd.DataFrame(list(neighborhood_score.items()), columns=['Neighborhood', 'SentimentScore'])

# Export the DataFrame to a CSV file
output_csv_path = '/Users/mackmorgan/Desktop/test_sentiment_scores.csv'
df_output.to_csv(output_csv_path, index=False)

print("Sentiment scores exported to:", output_csv_path)