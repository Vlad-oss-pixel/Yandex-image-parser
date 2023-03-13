import requests
import csv
import json

def search_image_yandex(query):
    api_key = "your_api_key"
    url = "https://yandex.ru/images/search"
    params = {
        "format": "json",
        "request": {"text": query, "lang": "ru"},
        "sort": "relevance",
        "max_size": "medium",
        "apikey": api_key,
        "num": 1,
    }


    try:
        response = requests.post(url, json=params)
        response.raise_for_status()
        data = response.json()

        if "items" in data:
            for item in data["items"]:
                if "preview" in item and "url" in item["preview"]:
                    return item["preview"]["url"]

        return None
    except (requests.exceptions.RequestException, json.decoder.JSONDecodeError):
        return None

with open('input.csv', 'r') as input_file, open('output.csv', 'w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    for row in reader:
        articul = row[0]
        query = f"Товар {articul}"
        image_url = search_image_yandex(query)

        if image_url:
            row.append(image_url)
        else:
            row.append("")

        writer.writerow(row)