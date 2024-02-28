import re

#1
def match_ab(s):
    pattern = r'^ab*'
    if re.match(pattern, s):
        return "Match found"
    else:
        return "Match not found"
    
#2 
def match_abb(s):
    pattern = r'^ab{2,3}'
    if re.match(pattern, s):
        return "Match found"
    else:
        return "Match not found"

#3
def find_sequences(s):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, s)

#4
def find_uppercase_sequences(s):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, s)

#5
def match_a_anything_b(s):
    pattern = r'^a.*b$'
    if re.match(pattern, s):
        return "Match found"
    else:
        return "Match not found"

#6
def replace_with_colon(s):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', s)

#7
def snake_to_camel(s):
    components = s.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

#8
def split_at_uppercase(s):
    pattern = r'(?=[A-Z])'
    return re.split(pattern, s)[1:]

#9
def insert_spaces(s):
    pattern = r'(?<=[a-z])(?=[A-Z])'
    return re.sub(pattern, ' ', s)

#10
def camel_to_snake(s):
    pattern = r'(?<=\w)([A-Z])'
    return re.sub(pattern, r'_\1', s).lower()

