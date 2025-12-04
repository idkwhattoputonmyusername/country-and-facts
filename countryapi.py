import requests
def get_country_information(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}?fullText=true"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json() 
    except requests.exceptions.RequestException as e:
        print(f"Помилка при виконанні запиту до API restcountries.com: {e}")
        return
    if not data:
        print(f"Інформацію про країну '{country_name}' не знайдено.")
        return
    country = data[0]
    official_name = country['name']['official']
    capital = country['capital'][0] if 'capital' in country and country['capital'] else 'Немає даних'
    flag_emoji = country['flag']
    population = country['population']
    formatted_population = f"{population:,}".replace(",", " ")
    if 'latlng' in country and len(country['latlng']) == 2:
        latitude, longitude = country['latlng']
    else:
        latitude, longitude = 'Немає даних', 'Немає даних'
    print("\n*** ІНФОРМАЦІЯ ПРО КРАЇНУ ***")
    print(f"Офіційна назва: [{official_name}]")
    print(f"Столиця: [{capital}]")
    print(f"Прапор: {flag_emoji}")
    print(f"Населення: [{formatted_population}] осіб")
    print("\n--- Географічне положення ---")
    print(f"{official_name} розташована приблизно на широті [{latitude}] та довготі [{longitude}].")
def get_cat_fact():
    url = "https://catfact.ninja/fact"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get('fact', 'Не вдалося отримати факт про кота.')
    except requests.exceptions.RequestException as e:
        return f"Помилка при запиті до catfact.ninja: {e}"
def get_random_quote():
    url = "https://zenquotes.io/api/random"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data and isinstance(data, list) and 'q' in data[0]:
            quote = data[0]['q']
            author = data[0].get('a', 'Невідомий автор')
            return f"«{quote}» - {author}"
        return 'Не вдалося отримати цитату.'
    except requests.exceptions.RequestException as e:
        return f"Помилка при запиті до zenquotes.io: {e}"
search_country = "guatemala" 
get_country_information(search_country)
cat_fact = get_cat_fact()
random_quote = get_random_quote()
print("\n=== ВИПАДКОВИЙ ФАКТ ДЛЯ РОЗВАГИ ===")
print(f"Факт про кота: {cat_fact}")
print(f"Цитата дня: {random_quote}")