import configparser  # импортируем библиотеку

config = configparser.ConfigParser()  # создаём объекта парсера
config.read("options.ini")  # читаем конфиг

print(config["Work"]["start"])  # обращаемся как к обычному словарю!