from random import shuffle
used_words = []
letters_dict = {
    "а": 8,
    "б": 2,
    "в": 4,
    "г": 2,
    "д": 4,
    "е": 8,
    "ё": 1,
    "ж": 1,
    "з": 2,
    "и": 5,
    "й": 1,
    "к": 4,
    "л": 4,
    "м": 3,
    "н": 5,
    "о": 10,
    "п": 4,
    "р": 5,
    "с": 5,
    "т": 5,
    "у": 4,
    "ф": 1,
    "х": 1,
    "ц": 1,
    "ч": 1,
    "ш": 1,
    "щ": 1,
    "ъ": 1,
    "ы": 2,
    "ь": 2,
    "э": 1,
    "ю": 1,
    "я": 2
}


def convert_dict_to_list(dict_: dict) -> list:
    """
    Конвертирует словарь букв в список
    """
    list_ = []

    for letter, count in dict_.items():
        for i in range(count):
            list_.append(letter)

    return list_


list_of_letters = convert_dict_to_list(letters_dict)


def get_random_letters(player: list, count: int):
    """
    Добавляет рандомные буква во входной список извлекая из основного
    """
    if len(list_of_letters) == 0:
        print("В мешочке не осталось буковок... :(")
        return
    shuffle(list_of_letters)
    count = min(len(list_of_letters), count)
    some_letters = []

    [some_letters.append(list_of_letters[i]) for i in range(count)]
    [list_of_letters.pop(0) for i in range(count)]
    player += some_letters


def start_game() -> list:
    """
    Приветствует игрока, спрашивает имя
    """
    print("Привет.\nМы начинаем играть в Scrabble!\n")
    while True:
        name1 = input("Введите имя первого игрока: ").strip()
        if name1 == "":
            print("Ну пожалуйста... :(")
            continue
        else:
            break
    while True:
        name2 = input("Введите имя второго игрока: ").strip()
        if name1 == "":
            print("Ну пожалуйста... :(")
            continue
        else:
            break
    print(f"\n{name1} vs {name2}\n(раздаю случайные буквы)\n")
    return [name1, name2]


def is_word_exist(word: str) -> bool:
    """
    Проверяет строку на наличие его в файле со словами
    """
    with open('russian_word.txt', encoding="UTF-8") as file:
        for row in file:
            if word == row.strip():
                return True
        return False


def get_word_from_letters(word: str, letters: list) -> bool:
    """
    Удаляет буквы слова из списка если все они есть в этом списке
    """
    tmp = []
    tmp.extend(letters)
    try:
        for letter in word:
            tmp.remove(letter)
        letters.clear()
        letters.extend(tmp)
        return True
    except:
        return False


def count_points(word: str) -> int:
    """
    Считает заработанные очки
    """
    len_ = len(word)
    if len_ <= 3:
        points = len_
    else:
        points = len_ + 2
    return points


def game_turn(name:str, player: list) -> int:
    """проигрывает один кон, возвращает количество заработанных за ход очков"""
    print(f"Ходит {name}")
    player_word = input("Введите слово: ").strip().lower()
    while player_word in used_words:
        player_word = input("Уже было...\nВведите новое слово: ").strip().lower()
    if player_word == "stop":
        return None
    if is_word_exist(player_word):
        if get_word_from_letters(player_word, player):
            points = count_points(player_word)
            print(f"Хороший ход!\nВаш счёт увеличивается на {points}!\n")
            get_random_letters(player, len(player_word) + 1)
            used_words.append(player_word)
            return points
        else:
            print("Не собрать такое слово\n")
    else:
        print("Нет такого слова\n")
    get_random_letters(player, 1)
    return 0


def print_result(name1, score1, name2, score2):
    """
    Выводит на экран результат игры
    """
    if score1 > score2:
        print(f"Победитель: {name1}!!!\nСчёт: {score1}:{score2}")
    elif score2 > score1:
        print(f"Победитель: {name2}!!!\nСчёт: {score2}:{score1}")
    else:
        print("НИЧЬЯ!!!")


if __name__ == "__main__":
    name1, name2 = start_game()
    score1 = score2 = 0
    turn = 0
    player1 = []
    player2 = []
    get_random_letters(player1, 7)
    get_random_letters(player2, 7)

    while True:
        print(f"{name1} - {player1}\n{name2} - {player2}\n")
        turn += 1
        if turn % 2 == 1:
            try:
                score1 += game_turn(name1, player1)
            except:
                break
        else:
            try:
                score2 += game_turn(name2, player2)
            except:
                break

    print_result(name1, score1, name2, score2)