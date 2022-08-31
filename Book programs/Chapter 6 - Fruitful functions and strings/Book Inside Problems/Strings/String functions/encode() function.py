# encode() function
# """The encode() function returns the encoded version of the given string
# SYNTAX : string.encode(encoding='UTF-8', errors='strict')
# where 1) encoding - Specifies the string type to be encoded. The default one is 'UTF-8'
#       2) errors - response when the encoding fails . There are 6 types of error responses
#             a) strict - default response which raise UnicodeDecodeError exception on failure
#             b) ignore - ignores the unencodable characters from the result
#             c) xmlcharrefreplace - inserts XML character reference instead of unencodable unicode
#             d) namereplace - inserts a \N{...} escape sequence instead of unencodable unicode"""

string = input("Enter a string : ")
print(f'The string ({string}) before encoding : {string}')
# error - strict
print(f'The string ({string}) after encoding using (strict) : {string.encode(encoding="ascii", errors="strict")}')
# error - ignore
print(f'The string ({string}) after encoding using (ignore) : {string.encode(encoding="ascii", errors="ignore")}')
# error - replace
print(f'The string ({string}) after encoding using (replace) : {string.encode(encoding="ascii", errors="replace")}')
# error - xmlcharrefreplace
print(f'The string ({string}) after encoding using (xmlcharrefreplace) : {string.encode(encoding="ascii", errors="xmlcharrefreplace")}')
# error - backslashreplace
print(f'The string ({string}) after encoding using (backslashreplace) : {string.encode(encoding="ascii", errors="backslashreplace")}')
# error - namereplace
print(f'The string ({string}) after encoding using (namereplace) : {string.encode(encoding="ascii", errors="namereplace")}')
