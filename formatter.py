from datetime import datetime
import preferences
import requests

def format_summary(user_id):
    plus, minus = preferences.get_prefs(user_id)
    news = __filter_news(plus, minus)
    holidays = __get_holidays()

    lines = []
    today = datetime.today().strftime('%d/%m/%Y')
    lines.append(f"🗞️ *Noticias destacadas – {today}*")
    if plus:
        lines.append(f"\n🎯 *Temas incluidos:* {', '.join(plus)}")
    if minus:
        lines.append(f"\n🚫 *Temas excluidos:* {', '.join(minus)}")

    grouped = {}
    for n in news:
        topic = n['source']
        grouped.setdefault(topic, []).append(n)

    for topic, items in grouped.items():
        lines.append(f"\n*{topic.title()}*")
        for i in items:
            lines.append(f"- [{i['title']}]({i['link']})")

    if holidays:
        lines.append("\n🗓️ *Feriados y no laborables*")
        for h in holidays:
            lines.append(f"- {h['date']}: {h['name']} ({h['type']})")

    lines.append("\n_Usá +tema o -tema para personalizar tus noticias_")
    return '\n'.join(lines)

def __filter_news(plus, minus):
    from feeds import get_news
    items = get_news()
    result = []
    for n in items:
        text = (n['title'] + ' ' + n['source']).lower()
        if plus and not any(p.lower() in text for p in plus):
            continue
        if minus and any(m.lower() in text for m in minus):
            continue
        result.append(n)
    return result

def __get_holidays():
    url = 'https://nolaborables.com.ar/api/v2/feriados/' + datetime.today().strftime('%Y')
    try:
        r = requests.get(url, timeout=10)
        data = r.json()
        today = datetime.today().strftime('%Y-%m-%d')
        result = [h for h in data if h['fecha'] == today or h['fecha'] > today]
        return result[:5]
    except:
        return []
