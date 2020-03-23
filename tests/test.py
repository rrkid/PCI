import src.string_parser as string_parser

uppercase_string = "TEST STRING TEST STRING"
uppercase_string_res = "test string test string"

uppercase_mixed_string = "TeST string TEST sTRING"
uppercase_mixed_string_res = "test string test string"

odd_spaces_string = "test    string for     tests"
odd_spaces_string_res = "test string for tests"
odd_spaces_on_right = "test string for tests        "
odd_spaces_on_right_res = "test string for tests"
odd_spaces_on_left = "           test string"
odd_spaces_on_left_res = "test string"
odd_spaces_everywhere = "        test         string              "
odd_spaces_everywhere_res = "test string"

odd_delimeters = "test, test, test, string."
odd_delimeters_res = "test test test string"
odd_symbols = "!!!!str%ing 'test' $for &tests||."
odd_symbols_res = "string test for tests"

odd_symbols_and_spaces = "test test          , , , , , ,        test       !!!"
odd_symbols_and_spaces_res = "test test test"

all_mixed = "TEST  !  '''' ' ' ' ' ' ' string          for testS    !!! "
all_mixed_res = "test string for tests"

cyrillic_all_mixed = "тест строКА     !!! с     ....   кириЛЛицей !!       %%       "
cyrillic_all_mixed_res = "тест строка кириллицей"

if (string_parser.prepareString(uppercase_string) == uppercase_string_res):
    print("TEST 1/11 - OK")
else:
    print("TEST 1/11 - Failed")

if (string_parser.prepareString(uppercase_mixed_string) == uppercase_mixed_string_res):
    print("TEST 2/11 - OK")
else:
    print("TEST 2/11 - Failed")
    
if (string_parser.prepareString(odd_spaces_string) == odd_spaces_string_res):
    print("TEST 3/11 - OK")
else:
    print("TEST 3/11 - Failed")

if (string_parser.prepareString(odd_spaces_on_right) == odd_spaces_on_right_res):
    print("TEST 4/11 - OK")
else:
    print("TEST 4/11 - Failed")

if (string_parser.prepareString(odd_spaces_on_left) == odd_spaces_on_left_res):
    print("TEST 5/11 - OK")
else:
    print("TEST 5/11 - Failed")

if (string_parser.prepareString(odd_spaces_everywhere) == odd_spaces_everywhere_res):
    print("TEST 6/11 - OK")
else:
    print("TEST 6/11 - Failed")

if (string_parser.prepareString(odd_delimeters) == odd_delimeters_res):
    print("TEST 7/11 - OK")
else:
    print("TEST 7/11 - Failed")
    
if (string_parser.prepareString(odd_symbols) == odd_symbols_res):
    print("TEST 8/11 - OK")
else:
    print("TEST 8/11 - Failed")

if (string_parser.prepareString(odd_symbols_and_spaces) == odd_symbols_and_spaces_res):
    print("TEST 9/11 - OK")
else:
    print("TEST 9/11 - Failed")

if (string_parser.prepareString(all_mixed) == all_mixed_res):
    print("TEST 10/11 - OK")
else:
    print("TEST 10/11 - Failed")

if (string_parser.prepareString(cyrillic_all_mixed) == cyrillic_all_mixed_res):
    print("TEST 11/11 - OK")
else:
    print("TEST 11/11 - Failed")
