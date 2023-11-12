import math


def length(vector):
    return math.sqrt(sum([x ** 2 for x in vector]))


def normalize_vector(vector):
    # magnitude = math.sqrt(sum([x ** 2 for x in vector]))
    magnitude = length(vector)
    if magnitude == 0:
        return vector
    return [x / magnitude for x in vector]


# Пример использования
# vector = [3, 4, 0]
vector = (3, 4, 0)
normalized_vector = normalize_vector((3, 4, 0))
print(normalized_vector)
normalized_vector = normalize_vector((0, 3, 4))
print(normalized_vector)
