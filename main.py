"""lol"""
import json


def get_json_dict(json_file: str):
    """
    This function takes json file and if file is in list, coverts it to dict
    """
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        if type(data) is list:
            return data[0]
        else:
            return data


def get_list_keys(dct: dict):
    """
    This function gets all keys of inputted dict
    """
    lst = []
    for key in dct.keys():
        lst.append(key)
    return lst


def border_msg(msg: str):
    """
    This function creates boarders in the top and bottom of text
    """
    row = len(msg)
    h = ''.join(['+'] + ['-' * row] + ['+'])
    return h + "\n" + msg + "\n" + h


def navigate_json(file):
    """
    This function with the help of recursion help to navigate through json file
    """
    key_list = get_list_keys(file)
    print("Choose your way:")
    f_str = ""
    count = 0
    for key in key_list:
        if len(key_list) > 4:
            if count > 0:
                if count % 3 == 0:
                    f_str += "[" + key + "]" + "\n"
                    count += 1
                else:
                    f_str += "[" + key + "]" + " "
                    count += 1
            else:
                f_str += "[" + key + "]" + " "
                count += 1
        else:
            f_str += "[" + key + "]" + " "
            count += 1
    print(border_msg(f_str))
    req = input("Input: ")
    if type(file[req]) is dict:
        return navigate_json(file[req])
    elif type(file[req]) is list:
        if len(file[req]) > 0:
            req_2 = input("Choose index between 0 and " + str(len(file[req]) - 1) + ": ")
            if type(file[req][int(req_2)]) is dict:
                return navigate_json(file[req][int(req_2)])
            else:
                return file[req][int(req_2)]
        else:
            return file[req]
    else:
        return file[req]


if __name__ == "__main__":
    print(border_msg("Enter .json file name"))
    print("IMPORTANT: FILE MUST BE IN THE SAME FOLDER AS PROGRAM")
    path = input("Input: ")
    print("\n")
    json_response = get_json_dict(path)
    print("RESULT: " + str(navigate_json(json_response)))
    print("You have reached one of many ends of the file. Please, restart!")

