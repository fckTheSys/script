import os

# Папка с файлами, которые нужно переименовать
source_folder_path = 'C:/Users/Fmnk/Desktop/translit-icons'

# Папка, в которую нужно сохранить переименованные файлы
target_folder_path = 'C:/Users/Fmnk/Desktop/translit-icons-renamed'

# Создание папки для сохранения переименованных файлов, если она не существует
if not os.path.exists(target_folder_path):
    os.makedirs(target_folder_path)

# Словарь транслитерации
translit_dict = {
    'а': 'a',
    'б': 'b',
    'в': 'v',
    'г': 'g',
    'д': 'd',
    'е': 'e',
    'ё': 'e',
    'ж': 'zh',
    'з': 'z',
    'и': 'i',
    'й': 'y',
    'к': 'k',
    'л': 'l',
    'м': 'm',
    'н': 'n',
    'о': 'o',
    'п': 'p',
    'р': 'r',
    'с': 's',
    'т': 't',
    'у': 'u',
    'ф': 'f',
    'х': 'h',
    'ц': 'ts',
    'ч': 'ch',
    'ш': 'sh',
    'щ': 'sch',
    'ъ': '',
    'ы': 'y',
    'ь': '',
    'э': 'e',
    'ю': 'yu',
    'я': 'ya',
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'E',
    'Ж': 'Zh',
    'З': 'Z',
    'И': 'I',
    'Й': 'Y',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'H',
    'Ц': 'Ts',
    'Ч': 'Ch',
    'Ш': 'Sh',
    'Щ': 'Sch',
    'Ъ': '',
    'Ы': 'Y',
    'Ь': '',
    'Э': 'E',
    'Ю': 'Yu',
    'Я': 'Ya'
}

# Функция транслитерации
def translit(text):
    result = []
    for char in text:
        translit_char = translit_dict.get(char, char)
        result.append(translit_char)
    return ''.join(result)

for filename in os.listdir(source_folder_path):
    # Полный путь к файлу
    file_path = os.path.join(source_folder_path, filename)

    # Если это файл (а не папка)
    if os.path.isfile(file_path):
        # Транслитерация названия файла
        translit_filename = translit(filename)

        # Полный путь к новому файлу с транслитерированным названием
        translit_file_path = os.path.join(target_folder_path, translit_filename)

        # Переименование файла
        os.rename(file_path, translit_file_path)
        print(f'Файл {filename} переименован в {translit_filename}.')
