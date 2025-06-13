import feedparser

RSS_FEEDS = {
    'infobae': 'https://www.infobae.com/rss/america/',
    'clarin': 'https://www.clarin.com/rss/',
    'lanacion': 'https://www.lanacion.com.ar/rss/',
    'ambito': 'https://www.ambito.com/rss/',
    'télam': 'https://www.telam.com.ar/rss/feed/',
    'lpo': 'https://www.lapoliticaonline.com/rss/',
    'ole': 'https://www.ole.com.ar/rss/',
    'lcapital': 'https://www.lacapital.com.ar/rss/',
}

def get_news():
    items = []
    for source, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)
        for e in feed.entries[:5]:
            items.append({
                'source': source,
                'title': e.title,
                'link': e.link
            })
    return items
