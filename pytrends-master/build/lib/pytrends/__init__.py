from pytrends import pytrends
trends = pytrends()

keywords = ["Vale S.A."]
titles = ["Interest over time","Related queries"]
time = "all"
for title in titles:
  print(trends.download_report(keywords, title, time))