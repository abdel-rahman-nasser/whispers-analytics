import re


def string_to_folder_name(string):
    s = ''.join(e for e in string if e.isalnum()
                or e == ' ').lower()
    return re.sub(' +', ' ', s).replace(' ', '_')
