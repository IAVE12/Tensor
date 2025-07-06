import requests
import time
from datetime import datetime


def task1():
    url = "https://yandex.com/time/sync.json?geo=213"

    deltas = []

    for i in range(5):
        local_time_before = time.time()
        response = requests.get(url)
        data = response.json()


        if i == 0:
            print(data)
            print()


        timestamp = data['time'] / 1000
        human_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        timezone = data['clocks']['213']['offsetString']

        if i == 0:
            print("'Человекопонятный' формат и временная зона:")
            print(f"время: {human_time}")
            print(f"временная зона: {timezone}")
            print()


        server_time = timestamp
        local_time_after = time.time()
        delta = (local_time_before + local_time_after) / 2 - server_time

        deltas.append(abs(delta))

        print(f"Дельта для запроса номер {i + 1}: {delta:.6f} секунд")

    average_delta = sum(deltas) / len(deltas)
    print()
    print(f"Средняя дельта за 5 запросов: {average_delta:.6f} секунд")





if __name__ == "__main__":
    task1()