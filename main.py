import string
import plotly.graph_objects as go
from wordcloud import WordCloud
import pandas as pd
from plotly.subplots import make_subplots

# Reads CSV from GitHub and converts it into a dataframe.
df = pd.read_csv('https://github.com/ObamaBinModdin/CS445-Assignment4/raw/main/TweetsElonMusk.csv')

# Converts type of column "tweet" to string.
df['tweet'] = df['tweet'].astype('string')

# Dropping all column except "tweet".
df = df['tweet']

# Dictionary to count occurrences.
wordCount = {}

# Iterates through each tweet.
for tweet in df:
    tweetAsList = tweet.lower().translate(str.maketrans('', '', string.punctuation)).split()

    # Removes common filler words.
    tweetAsList = [i for i in tweetAsList if i not in ['the', 'that', 'an', 'a', 'for', 'in', 'be', 'by', 'or', 'and',
                                                       'with', 'to', 'is', 's', 'of', 'but', 'are', 'at', 'so', 'on',
                                                       'it', 'but', 'this', 'as', 'was', 'i', 'we', 'you', 'not', 'have'
                                                       , 'just', 'my', 'from', "it\'s", 'than', 'yes', 'no', 'if',
                                                       'should', 'would', 'about', 'there', 'has', 'much', "...", 'our'
                                                       , 'too', 'also', 'what', 'also', 'very', 'your', 'which']]
    # Adds the word to the dictionary 'wordCount' if not present. Otherwise, increment count.
    for word in tweetAsList:
        wordCount[word] = wordCount.get(word, 0) + 1

# Converts dictionary to dataframe and name the column 'Frequency'.
df = pd.Series(wordCount).to_frame('Frequency')

# Sort data so most frequent words show up at the top.
df = df.sort_values(by=['Frequency'], ascending=False)

# Reset index column to counting up.
df = df.reset_index()

# Rename 'index' column to 'Word'.
df = df.rename({'index': 'Word'}, axis=1)

# Initialize part one figure.
figPartOne = make_subplots(rows=1, cols=2)

# Bar graph for 10 words.
figPartOne.add_trace(go.Bar(x=df['Frequency'], y=df['Word'].head(10), orientation='h', visible=True, hoverinfo='x+y'),
                     row=1, col=1). \
    update_layout(yaxis=dict(autorange='reversed'), yaxis_title='Word', xaxis_title='Frequency')

# Word cloud 10 words.
figPartOne.add_trace(
    go.Image(z=WordCloud(background_color='white', width=1000, height=1000, max_words=10, relative_scaling=0.5). \
             generate_from_frequencies(wordCount), visible=True, hoverinfo='none'), row=1, col=2)

# Bar graph for 30 words.
figPartOne.add_trace(go.Bar(x=df['Frequency'], y=df['Word'].head(30), orientation='h', visible=False, hoverinfo='x+y'),
                     row=1, col=1). \
    update_layout(yaxis=dict(autorange='reversed'), yaxis_title='Word', xaxis_title='Frequency')

# Word cloud 30 words.
figPartOne.add_trace(
    go.Image(z=WordCloud(background_color='white', width=1000, height=1000, max_words=30, relative_scaling=0.5). \
             generate_from_frequencies(wordCount), visible=False, hoverinfo='none'), row=1, col=2)

# Bar graph for 50 words.
figPartOne.add_trace(go.Bar(x=df['Frequency'], y=df['Word'].head(50), orientation='h', visible=False, hoverinfo='x+y'),
                     row=1, col=1). \
    update_layout(yaxis=dict(autorange='reversed'), yaxis_title='Word', xaxis_title='Frequency')

# Word cloud 50 words.
figPartOne.add_trace(
    go.Image(z=WordCloud(background_color='white', width=1000, height=1000, max_words=50, relative_scaling=0.5). \
             generate_from_frequencies(wordCount), visible=False, hoverinfo='none'), row=1, col=2)

# Creating figure for part two.
figPartTwo = go.Figure()

# WordCloud for 100 words.
figPartTwo.add_trace(
    go.Image(z=WordCloud(background_color='white', width=1000, height=1000, max_words=100, relative_scaling=0.5). \
             generate_from_frequencies(wordCount), visible=True, hoverinfo='none'))

# WordCloud for 150 words.
figPartTwo.add_trace(
    go.Image(z=WordCloud(background_color='white', width=1000, height=1000, max_words=150, relative_scaling=0.5). \
             generate_from_frequencies(wordCount), visible=False, hoverinfo='none'))

# WordCloud for 200 words.
figPartTwo.add_trace(
    go.Image(z=WordCloud(background_color='white', width=1000, height=1000, max_words=200, relative_scaling=0.5). \
             generate_from_frequencies(wordCount), visible=False, hoverinfo='none'))

# WordCloud for 250 words.
figPartTwo.add_trace(
    go.Image(z=WordCloud(background_color='white', width=1000, height=1000, max_words=250, relative_scaling=0.5). \
             generate_from_frequencies(wordCount), visible=False, hoverinfo='none'))

# Buttons for part one.
figPartOne.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    label='10 Words Bar',
                    method='update',
                    args=[{'visible': [True, True, False, False, False, False]},
                          {'title': '10 Most Frequent Words in Tweets'}]
                ),
                dict(
                    label='30 Words Bar',
                    method='update',
                    args=[{'visible': [False, False, True, True, False, False]},
                          {'title': '30 Most Frequent Words in Tweets'}]
                ),
                dict(
                    label='50 Words Bar',
                    method='update',
                    args=[{'visible': [False, False, False, False, True, True]},
                          {'title': '50 Most Frequent Words in Tweets'}]
                )
            ])
        )
    ]
)

# Buttons for part two.
figPartTwo.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    label='100 WordCloud',
                    method='update',
                    args=[{'visible': [True, False, False, False]},
                          {'title': '100 Most Frequent Words in Tweets'}]
                ),
                dict(
                    label='150 WordCloud',
                    method='update',
                    args=[{'visible': [False, True, False, False]},
                          {'title': '150 Most Frequent Words in Tweets'}]
                ),
                dict(
                    label='200 WordCloud',
                    method='update',
                    args=[{'visible': [False, False, True, False]},
                          {'title': '200 Most Frequent Words in Tweets'}]
                ),
                dict(
                    label='250 WordCloud',
                    method='update',
                    args=[{'visible': [False, False, False, True]},
                          {'title': '250 Most Frequent Words in Tweets'}]
                )
            ])
        )
    ]
)

# Set titles
figPartOne.update_layout(title_text='10 Most Frequent Words in Tweets')
figPartTwo.update_layout(title_text='100 Most Frequent Words in Tweets')

# Disabling zoom.
figPartOne.update_layout(xaxis2=dict(fixedrange=True), yaxis2=dict(fixedrange=True))
figPartOne.update_layout(xaxis=dict(fixedrange=True), yaxis=dict(fixedrange=True))
figPartTwo.update_layout(xaxis=dict(fixedrange=True), yaxis=dict(fixedrange=True))

# Disabling labels for word clouds.
figPartOne.update_xaxes(showticklabels=False, row=1, col=2)
figPartOne.update_yaxes(showticklabels=False, row=1, col=2)
figPartTwo.update_xaxes(showticklabels=False)
figPartTwo.update_yaxes(showticklabels=False)

# Show graphs.
figPartOne.show()
figPartTwo.show()
