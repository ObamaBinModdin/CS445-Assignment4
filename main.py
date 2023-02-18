import string
import plotly.graph_objects as go
from wordcloud import WordCloud
import pandas as pd

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
                                                       'it', 'but', 'this', 'as', 'was']]
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

# Initialize figure
fig = go.Figure()

# Bar graph for 10 words.
fig.add_trace(go.Bar(x=df['Frequency'], y=df['Word'].head(10), orientation='h', visible=True, hoverinfo='x+y')). \
    update_layout(yaxis=dict(autorange='reversed'), yaxis_title='Word', xaxis_title='Frequency')

# Bar graph for 30 words.
fig.add_trace(go.Bar(x=df['Frequency'], y=df['Word'].head(30), orientation='h', visible=False, hoverinfo='x+y')). \
    update_layout(yaxis=dict(autorange='reversed'), yaxis_title='Word', xaxis_title='Frequency')

# Bar graph for 50 words.
fig.add_trace(go.Bar(x=df['Frequency'], y=df['Word'].head(50), orientation='h', visible=False, hoverinfo='x+y')). \
    update_layout(yaxis=dict(autorange='reversed'), yaxis_title='Word', xaxis_title='Frequency')

# WordCloud for 100 words.
wordcloud100 = WordCloud(background_color='white', width=1000, height=1000, max_words=100, relative_scaling=0.5). \
    generate_from_frequencies(wordCount)

# WordCloud for 150 words.
wordcloud150 = WordCloud(background_color='white', width=1000, height=1000, max_words=150, relative_scaling=0.5). \
    generate_from_frequencies(wordCount)

# WordCloud for 200 words.
wordcloud200 = WordCloud(background_color='white', width=1000, height=1000, max_words=200, relative_scaling=0.5). \
    generate_from_frequencies(wordCount)

# WordCloud for 250 words.
wordcloud250 = WordCloud(background_color='white', width=1000, height=1000, max_words=250, relative_scaling=0.5). \
    generate_from_frequencies(wordCount)

# Adding WordClouds as traces to fig.
fig.add_trace(go.Image(z=wordcloud100, visible=False, hoverinfo='none'))
fig.add_trace(go.Image(z=wordcloud150, visible=False, hoverinfo='none'))
fig.add_trace(go.Image(z=wordcloud200, visible=False, hoverinfo='none'))
fig.add_trace(go.Image(z=wordcloud250, visible=False, hoverinfo='none'))

# Buttons
fig.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    label='10 Words Bar',
                    method='update',
                    args=[{'visible': [True, False, False, False, False, False, False]},
                          {'title': '10 Most Frequent Words in Tweets'}]
                ),
                dict(
                    label='30 Words Bar',
                    method='update',
                    args=[{'visible': [False, True, False, False, False, False, False]},
                          {'title': '30 Most Frequent Words in Tweets'}]
                ),
                dict(
                    label='50 Words Bar',
                    method='update',
                    args=[{'visible': [False, False, True, False, False, False, False]},
                          {'title': '50 Most Frequent Words in Tweets'}]
                ),
                dict(
                    label='100 WordCloud',
                    method='update',
                    args=[{'visible': [False, False, False, True, False, False, False]},
                          {'title': '100 Most Frequent Words in Tweets'}]
                ),
                dict(
                    label='150 WordCloud',
                    method='update',
                    args=[{'visible': [False, False, False, False, True, False, False]},
                          {'title': '150 Most Frequent Words in Tweets'}]
                ),
                dict(
                    label='200 WordCloud',
                    method='update',
                    args=[{'visible': [False, False, False, False, False, True, False]},
                          {'title': '200 Most Frequent Words in Tweets'}]
                ),
                dict(
                    label='250 WordCloud',
                    method='update',
                    args=[{'visible': [False, False, False, False, False, False, True]},
                          {'title': '250 Most Frequent Words in Tweets'}]
                )
            ])
        )
    ]
)

# Set title
fig.update_layout(title_text='10 Most Frequent Words in Tweets')

# Disabling zooming.
fig.layout.xaxis.fixedrange = True
fig.layout.yaxis.fixedrange = True

# Show graphs.
fig.show()
