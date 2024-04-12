single_quotes_text = 'single quotes!'
double_quotes_text = "Paris rabbit got your back :)! Yay!"
number_text = '1975'
escape_text_1 = 'doesn\'t'
escape_text_2 = "\"Yes,\" they said."
no_escape_text = "doesn't"
new_line_text_1 = 'First line.\nSecond line.'
new_line_text_2 = "C:\\some\name"
raw_text = r"C:\some\name"
tab_text = "\tABC"

print("single_quotes_text: " + single_quotes_text)
print("double_quotes_text: " + double_quotes_text)
print("number_text: " + number_text)
print("escape_text_1: " + escape_text_1)
print("escape_text_2: " + escape_text_2)
print("no_escape_text: " + no_escape_text)
print("new_line_text_1: " + new_line_text_1)
print("new_line_text_2: " + new_line_text_2)
print("raw_text: " + raw_text)
print("tab_text: " + tab_text)
print("-----------------------------")

'''
This is output result

single_quotes_text: single quotes!
double_quotes_text: Paris rabbit got your back :)! Yay!
number_text: 1975
escape_text_1: doesn't
escape_text_2: "Yes," they said.
no_escape_text: doesn't
new_line_text_1: First line.
Second line.
new_line_text_2: C:\some
ame
raw_text: C:\some\name
tab_text: 	ABC
'''

multiple_lines_text = """
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""
repeated_text = 3 * "Abc"
concatenated_text = single_quotes_text + " - " + double_quotes_text
character_text = single_quotes_text[0]
last_character_text = single_quotes_text[-1]
substring_text = single_quotes_text[0:3]
single_quotes_text_length = len(single_quotes_text)
number_to_string_text = str(1234)

print("multiple_lines_text: " + multiple_lines_text)
print("repeated_text: " + repeated_text)
print("concatenated_text: " + concatenated_text)
print("character_text: " + character_text)
print("last_character_text: " + last_character_text)
print("substring_text: " + substring_text)
print("single_quotes_text_length: " + str(single_quotes_text_length))
print("number_to_string_text: " + number_to_string_text)

'''
This is output result

multiple_lines_text: 
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to

repeated_text: AbcAbcAbc
concatenated_text: single quotes! - Paris rabbit got your back :)! Yay!
character_text: s
last_character_text: !
substring_text: sin
single_quotes_text_length: 14
number_to_string_text: 1234
'''