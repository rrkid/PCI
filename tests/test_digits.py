import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

import string_parser_pro as string_parser

uppercase_string = "ОДИН ДВА ТРИ STRING"
uppercase_string_res = "1 2 3 string"

uppercase_mixed_string = "ОдИН два ТРИ чЕТЫРЕ"
uppercase_mixed_string_res = "1 2 3 4"

odd_spaces_string = "один    два три     четыре"
odd_spaces_string_res = "1 2 3 4"
odd_spaces_on_right = "пять шесть семь восемь        "
odd_spaces_on_right_res = "5 6 7 8"
odd_spaces_on_left = "           восемь девять"
odd_spaces_on_left_res = "8 9"
odd_spaces_everywhere = "        один         два              "
odd_spaces_everywhere_res = "1 2"

odd_delimeters = "один, два, три, четыре"
odd_delimeters_res = "1 2 3 4"
odd_symbols = "!!!!од%ин 'два' $три &четыре||"
odd_symbols_res = "1 2 3 4"

odd_symbols_and_spaces = "один два          , , , , , ,        три       !!!"
odd_symbols_and_spaces_res = "1 2 3"

digits_delimeters = "6  !  '''' ' ' ' ' ' ' 7          8 4    !!! "
digits_delimeters_res = "6 7 8 4"

russian_words = 'Звонить 89425546881'
russian_words_res = '89425546881'

more_russian = '-1300р. Xerjoff Esquel ... Xerjoff Modoc ... ранний выпуск,шикааарный глубоокий и многогранный!!!'
more_russian_res = '-1300. xerjoff esquel ... xerjoff modoc ...'

if (string_parser.prepareString(uppercase_string) == uppercase_string_res):
    print("TEST uppercase_string 1/10 - OK")
else:
    print("TEST uppercase_string 1/10 - Failed")

if (string_parser.prepareString(uppercase_mixed_string) == uppercase_mixed_string_res):
    print("TEST uppercase_mixed 2/10 - OK")
else:
    print("TEST uppercase_mixed 2/10 - Failed")
    
if (string_parser.prepareString(odd_spaces_string) == odd_spaces_string_res):
    print("TEST odd_spaces_string 3/10 - OK")
else:
    print("TEST odd_spaces_string 3/10 - Failed")

if (string_parser.prepareString(odd_spaces_on_right) == odd_spaces_on_right_res):
    print("TEST odd_spaces_on_right 4/10 - OK")
else:
    print("TEST odd_spaces_on_right 4/10 - Failed")

if (string_parser.prepareString(odd_spaces_on_left) == odd_spaces_on_left_res):
    print("TEST odd_spaces_on_left 5/10 - OK")
else:
    print("TEST odd_spaces_on_left 5/10 - Failed")

if (string_parser.prepareString(odd_spaces_everywhere) == odd_spaces_everywhere_res):
    print("TEST odd_spaces_everywhere 6/10 - OK")
else:
    print("TEST odd_spaces_everywhere 6/10 - Failed")

if (string_parser.prepareString(odd_delimeters) == odd_delimeters_res):
    print("TEST odd_delimeters 7/10 - OK")
else:
    print("TEST odd_delimeters 7/10 - Failed")
    
if (string_parser.prepareString(odd_symbols) == odd_symbols_res):
    print("TEST odd_symbols 8/10 - OK")
else:
    print("TEST odd_symbols 8/10 - Failed")

if (string_parser.prepareString(odd_symbols_and_spaces) == odd_symbols_and_spaces_res):
    print("TEST odd_symbols_and_spaces 9/10 - OK")
else:
    print("TEST odd_symbols_and_spaces 9/10 - Failed")

if (string_parser.prepareString(digits_delimeters) == digits_delimeters_res):
    print("TEST digits_delimeters 10/10 - OK")
else:
    print("TEST digits_delimeters 10/10 - Failed")

if (string_parser.prepareString(russian_words) == russian_words_res):
    print("TEST russian_words 11/11 - OK")
else:
    print("TEST russian_words 11/11 - Failed")

if (string_parser.prepareString(more_russian) == more_russian_res):
    print("TEST more_russian 12/12 - OK")
else:
    print("TEST more_russian 12/12 - Failed")

if __name__ == '__main__':
     pass
