import requests
import pprint
import json
import os


def get_json_dict(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        if type(data) is list:
            return data[0]
        else:
            return data


# base_url = "https://api.twitter.com/"
# access_token = "AAAAAAAAAAAAAAAAAAAAALGUMwEAAAAAmILu6iQzNkREUy4mdleOVgRy%2FC8%3DX099gZ94kyEdZuws41gPTZiQKDCRQ3AoCHXspvHPgw1Rr9E6wk"
# search_headers = {
#     'Authorization': 'Bearer {}'.format(access_token)
# }
# search_params = {
#     'screen_name': '@ManaByte',
# }
# search_url = '{}1.1/friends/list.json'.format(base_url)
# response = requests.get(search_url, headers=search_headers, params=search_params)
# json_response = response.json()


def get_list_keys(dct):
    lst = []
    for key in dct.keys():
        lst.append(key)
    return lst


def border_msg(msg):
    row = len(msg)
    h = ''.join(['+'] + ['-' *row] + ['+'])
    # result = h + '\n'"|"+msg+"|"'\n' + h
    return h + "\n" + msg + "\n" + h


def navigate_json(file):
    key_list = get_list_keys(file)
    print("Choose your way:")
    f_str = ""
    count = 0
    for key in key_list:
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
    print(border_msg(f_str))
    req = input("Input: ")
    if type(file[req]) is dict:
        return navigate_json(file[req])
    elif type(file[req]) is list:
        if len(file[req]) > 0:
            req_2 = input("Choose index between 0 and " + str(len(file[req]) - 1) + ": ")
            if type(file[req][int(req_2)]) is dict:
                res = file[req][int(req_2)]
                return navigate_json(file[req][int(req_2)])
            else:
                return file[req][int(req_2)]
        else:
            return file[req]
    else:
        return file[req]


# pprint.pprint(json_response)

if __name__ == "__main__":
    print(border_msg("Enter .json file name"))
    print("IMPORTANT: FILE MUST BE IN THE SAME FOLDER AS PROGRAM")
    path = input("Input: ")
    print("\n")
    json_response = get_json_dict(path)
    print(navigate_json(json_response))

