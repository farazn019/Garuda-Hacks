import requests

def list_places(city, country, currency, locale):


    country = str(country)
    currency = str(currency)
    locale = str(locale)
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UK/GBP/en-GB/"

    querystring = {"query":city}

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': "915f3ed9fbmsha6957c677d44e14p1f10f3jsn323641387393"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    return(response.text)

#list_places("Stockholm")