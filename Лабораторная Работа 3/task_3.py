# TODO  Напишите функцию count_letters
def count_letters(text):
    dict_let = {}
    text = text.lower()
    for sym in text:
        if sym.isalpha():
            dict_let[sym] = text.count(sym)
    return dict_let


# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict_let):
    for key in dict_let:
        dict_let[key] = round(dict_let.get(key) / total_sym, 2)
    return dict_let


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
total_sym = 0
for c in main_str:
    if c.isalpha():
        total_sym += 1

dict_let = count_letters(main_str)
dict_freq = calculate_frequency(dict_let)
# TODO Распечатайте в столбик букву и её частоту в тексте
for key, vol in dict_freq.items():
    print(f'{key}: {vol:.2f}')
