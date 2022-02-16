import numpy as np

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    #задаем интервал чисел от 0 до 100
    min, max = 1, 101
    while True:
        count += 1
        #находим середину интервала
        predict_number = (min + max)//2 
        # Если предполагаемое число  больше загаданного, устанавливаем его наибольшим значением интервала
        if predict_number > number:
            max = predict_number
        # Если предполагаемое число  меньше загаданного, устанавливаем его наименьшим значением интервала
        elif predict_number < number:
            min = predict_number
        else:
            break
    return(count)

print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)