# Python String Functions/ Methods

"""
String Methods in Python

Function Name     | Description/Purpose                                            | Example
------------------|---------------------------------------------------------------|-----------------------------------------------------------------
len()             | Returns the length of the string                              | len("Hello") This returns 5
lower()           | Converts the string to lowercase                              | "Hello".lower() This returns "hello"
upper()           | Converts the string to uppercase                              | "Hello".upper() This returns "HELLO"
capitalize()      | Capitalizes the first character of the first word in a string | "hello".capitalize() This returns "Hello"
title()           | Capitalizes the first character of each word in the string    | "hello world".title() This returns "Hello World"
count()           | Returns the number of occurrences of a substring              | "Hello, Hello, Hello".count("Hello") This returns 3
replace()         | Replaces a substring (and all its copies) with another substring | "Hello, World".replace("Hello", "Hi") This returns, "Hi, World"
split()           | Splits the string into a list of substrings. By default, breaks the string wherever there is a whitespace. | "Hello, World".split(",") This returns ['Hello', ' World']
join()            | Joins elements of a list into a string using a separator.     | ", ".join(['Apple', 'Banana', 'Orange']) This returns "Apple, Banana, Orange"
strip()           | Removes leading and trailing whitespace                       | " Hello ".strip() This returns "Hello"
splitlines()      | Splits a multiline string into a list of lines/strings        | multi_line = "Apple\nBanana\nOrange"\nSplit_list = multi_line.splitlines() This returns a list of individual strings.
startswith()      | Check if the string starts with a given string/character digit | str1 = "How are you doing?"\nprint("Starts with 'How':", str1.startswith('How')) The result will be True.
endswith()        | Check if the string ends with a given string/character digit  | str1 = "How are you doing?"\nprint("Ends with '?':", str1.endswith('?')) The result will be True.
removeprefix()    | Removes a given prefix from the string                        | str2 = "Please, will you do this??"\nstr2_prefix = str2.removeprefix("Please, ") This will remove "Please" and space from the string.
removesuffix()    | Removes a given suffix from the string                        | str2 = "Will you do this??"\nstr2_suffix = str2.removesuffix("?") This will remove one question mark.
"""

#
# Escape Characters & Python Strings


| **Escape Sequence** | **Description**                                                            |
|---------------------|----------------------------------------------------------------------------|
| `\\`                | Backslash (escaped character representing a single backslash)              |
| `\'`                | Single quote                                                               |
| `\"`                | Double quote                                                               |
| `\n`                | Newline (line break)                                                       |
| `\t`                | Tab                                                                        |
| `\b`                | Backspace                                                                  |
| `\r`                | Carriage return (moves the cursor to the beginning of the line)            |
| `\f`                | Form feed (moves the cursor to the next page or clears the screen)         |
| `\v`                | Vertical tab                                                               |
| `\a`                | Bell (produces a beep sound)                                               |
| `\uXXXX`            | Unicode character (16-bit hexadecimal)                                     |
| `\UXXXXXXXX`        | Unicode character (32-bit hexadecimal)                                     |
| `\xXX`              | Hexadecimal value of a character (ASCII)                                   |
