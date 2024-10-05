# import math
#
# EARTH_RADIUS = 6371210  # Радиус Земли в метрах
# DISTANCE = 5000  # Интересующее нас расстояние в метрах (10 км)
#
#
# # Функция для перевода градусов в радианы
# def deg2rad(degrees):
#     return degrees * math.pi / 180
#
#
# # Функция для вычисления длины одного градуса по широте
# def compute_latitude_delta():
#     return EARTH_RADIUS * math.pi / 180
#
#
# # Функция для вычисления длины одного градуса по долготе
# def compute_longitude_delta(latitude):
#     return EARTH_RADIUS * math.pi / 180 * math.cos(deg2rad(latitude))
#
#
# def find_offer_by_location(latitude, longitude):
#     delta_lat = compute_latitude_delta()  # Дельта по широте
#     delta_lon = compute_longitude_delta(latitude)  # Дельта по долготе
#
#     # Вычисляем диапазоны координат
#     min_latitude = latitude - (DISTANCE / delta_lat)
#     max_latitude = latitude + (DISTANCE / delta_lat)
#     min_longitude = longitude - (DISTANCE / delta_lon)
#     max_longitude = longitude + (DISTANCE / delta_lon)
#
#     # Формируем списки долготы и широты
#     longitude_range = [min_longitude, max_longitude]
#     latitude_range = [min_latitude, max_latitude]
#
#     return [longitude_range, latitude_range]
#
#
# # Пример использования
# latitude = 40.4667725  # Координаты широты 40.4667725,71.6919271
# longitude = 71.6919271  # Координаты долготы
# range_coordinates = find_offer_by_location(latitude, longitude)
# print(range_coordinates)  # [[min_longitude, max_longitude], [min_latitude, max_latitude]]
#
# # 40.376843303641564,71.5737209113588
# # 40.376843303641564,71.8101332886412
# # 40.55670169635843,71.5737209113588
# # 40.55670169635843,71.8101332886412
import math


def km_to_degrees(latitude):
    # 1 км по широте в градусах
    degrees_per_km_latitude = 1 / 111.32  # км

    # Длина одного градуса по долготе (в км)
    km_per_degree_longitude = 111.32 * math.cos(math.radians(latitude))  # км

    # 1 км по долготе в градусах
    degrees_per_km_longitude = 1 / km_per_degree_longitude  # градусы

    return degrees_per_km_latitude, degrees_per_km_longitude


def calculate_delta_for_1_km(latitude, longitude):
    lat_delta, lon_delta = km_to_degrees(latitude)

    # Возвращаем, сколько нужно добавить к текущей широте и долготе для перемещения на 1 км
    return {
        "latitude_plus": lat_delta,  # на сколько добавить к широте
        "latitude_minus": -lat_delta,  # на сколько отнять от широты
        "longitude_plus": lon_delta,  # на сколько добавить к долготе
        "longitude_minus": -lon_delta  # на сколько отнять от долготы
    }


# Пример использования
latitude = 40.4667725  # Ваша широта 40.4667725,71.6919271
longitude = 71.6919271  # Ваша долгота

deltas = calculate_delta_for_1_km(latitude, longitude)
print(f"Добавить к широте для 1 км: {deltas['latitude_plus']}°")
print(f"Добавить к долготе для 1 км: {deltas['longitude_plus']}°")
print(latitude+deltas['latitude_plus'])
