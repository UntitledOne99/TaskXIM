import re
from pdfminer.high_level import extract_text


def extractor(document='test_task.pdf'):
    """Получение файла и разбиение его на части. Получил нулевое значение длиной в три
     элемента и поэтому вынес его в отдельный список. Также последние два элемента разделились поэтому объединил в один"""
    text = (extract_text(document).lstrip().rstrip('\t')).rstrip('\x0c').split("\n")
    res = text[1:-3]
    last = [text[-4], text[-3]]
    final_list = [["Title:", text[0]]]
    result ={}

    """Разбиение внутренних списков по разделителю ':' чтобы получить подобие ключ - значение"""
    for item in range(len(res[1:])):
        if len(res[item]) > 1 and res[item] != ' ':
            final_list.append(res[item].split(":"))
    final_list.append(last)

    """Финальное преобразование результирующего списка final-list в словарь result"""
    keys = [x[0] for x in final_list]
    for _ in range(1, len(final_list[0])):
        values = [row[_] for row in final_list]
        result = dict(zip(keys, values))
    print(result) #return(result)

if __name__ == "__main__":
    extractor()
