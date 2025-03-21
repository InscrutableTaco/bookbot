def count_words(source_text):
    count = len(source_text.split())
    return count

def count_chars(source_text):
    unsorted_dict = {}
    for char in source_text.lower():
        if char in unsorted_dict:
            unsorted_dict[char] += 1
        else:
            unsorted_dict[char] = 1
    return unsorted_dict

def sort_alpha(source_dict):
    sorted_keys = sorted(source_dict.keys())
    alpha_dict = {key: source_dict[key] for key in sorted_keys}
    return alpha_dict

def sort_on(dict):
    return dict["count"]

def sort_freq(source_dict):
    dict_list = []
    char_freq_list = []
    char_freq_str = ""
    for item in source_dict:
        if item.isalpha():
            dict_list.append({"char":item, "count":source_dict[item]})
    dict_list.sort(reverse=True, key=sort_on)

    #return dict_list

    for dict in dict_list:
        for key in dict:
            char_freq_list.append(dict[key])

    #return char_freq_list


    for item in char_freq_list:
        if type(item) == int:
            char_freq_str += str(item) + "\n"
        else:
            char_freq_str += item +": "

    return char_freq_str
