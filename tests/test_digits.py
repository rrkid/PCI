import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

import string_parser

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

odd_delimeters = "один, два, три, четыре."
odd_delimeters_res = "1 2 3 4"
odd_symbols = "!!!!од%ин 'два' $три &четыре||."
odd_symbols_res = "1 2 3 4"

odd_symbols_and_spaces = "один два          , , , , , ,        три       !!!"
odd_symbols_and_spaces_res = "1 2 3"

digits_delimeters = "6  !  '''' ' ' ' ' ' ' 7          8 4    !!! "
digits_delimeters_res = "6 7 8 4"


if (string_parser.prepareString(uppercase_string) == uppercase_string_res):
    print("TEST 1/10 - OK")
else:
    print("TEST 1/10 - Failed")

if (string_parser.prepareString(uppercase_mixed_string) == uppercase_mixed_string_res):
    print("TEST 2/10 - OK")
else:
    print("TEST 2/10 - Failed")
    
if (string_parser.prepareString(odd_spaces_string) == odd_spaces_string_res):
    print("TEST 3/10 - OK")
else:
    print("TEST 3/10 - Failed")

if (string_parser.prepareString(odd_spaces_on_right) == odd_spaces_on_right_res):
    print("TEST 4/10 - OK")
else:
    print("TEST 4/10 - Failed")

if (string_parser.prepareString(odd_spaces_on_left) == odd_spaces_on_left_res):
    print("TEST 5/10 - OK")
else:
    print("TEST 5/10 - Failed")

if (string_parser.prepareString(odd_spaces_everywhere) == odd_spaces_everywhere_res):
    print("TEST 6/10 - OK")
else:
    print("TEST 6/10 - Failed")

if (string_parser.prepareString(odd_delimeters) == odd_delimeters_res):
    print("TEST 7/10 - OK")
else:
    print("TEST 7/10 - Failed")
    
if (string_parser.prepareString(odd_symbols) == odd_symbols_res):
    print("TEST 8/10 - OK")
else:
    print("TEST 8/10 - Failed")

if (string_parser.prepareString(odd_symbols_and_spaces) == odd_symbols_and_spaces_res):
    print("TEST 9/10 - OK")
else:
    print("TEST 9/10 - Failed")

if (string_parser.prepareString(digits_delimeters) == digits_delimeters_res):
    print("TEST 10/10 - OK")
else:
    print("TEST 10/10 - Failed")


if __name__ == '__main__':
    pass
