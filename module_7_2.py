from pprint import pprint


def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    number_string = 1
    for string_write in strings:
        byte_string = file.tell()
        file.write(string_write + '\n')
        strings_positions[number_string, byte_string] = string_write
        number_string += 1
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    "Because there are 2 languages!",
    "Спасибо!"
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
