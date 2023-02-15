from pytrends.request import TrendReq
from wordcloud import WordCloud
from collections import Counter

pytrends = TrendReq(hl='taiwan', tz=360)
trends = pytrends.trending_searches(pn='taiwan')
trends_values = trends.values.tolist()

google_trend_list = []
for value in trends_values:
    item = str(value[0])
    item = item.strip()
    google_trend_list.append(item)
print('google_trend_list = ' + str(google_trend_list))

# WordCloud parameter
font_path = './msjh.ttc'
width = 600
height = 600
bg_color = 'white'
output_file = './wordcloud.png'

word_counter = Counter(google_trend_list)
wordcloud = WordCloud(
    font_path=font_path,
    width=width,
    height=height,
    background_color=bg_color,
    colormap='spring'
).generate_from_frequencies(word_counter)
wordcloud.to_file(output_file)
