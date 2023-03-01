import os
from typing import List


def get_file_name(file_list: List[str]) -> List[str]:
    max_len: int = max(len(os.path.splitext(name)[0]) for name in file_list)
    used_chars: dict = {}  # словарь для отслеживания уже использованных символов
    for i in range(len(file_list)):
        file_name, ext = os.path.splitext(file_list[i])  # разделение имени файла и расширения
        new_name: str = ""
        for c in file_name:
            if c not in used_chars:
                new_name += c
                used_chars[c] = True  # помечаем символ как использованный
        if len(new_name) < max_len:
            new_name += "_" * (max_len - len(new_name))
        file_list[i] = new_name + ext  # обновление имени файла в списке
        used_chars = {}  # очистка словаря использованных символов
    return file_list


file_list = ['file1.txt', 'longer_file_name2.doc', 'file3.png']
