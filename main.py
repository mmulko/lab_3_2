import requests
import pprint

base_url = "https://api.twitter.com/"

access_token = "AAAAAAAAAAAAAAAAAAAAALGUMwEAAAAAmILu6iQzNkREUy4mdleOVgRy%2FC8%3DX099gZ94kyEdZuws41gPTZiQKDCRQ3AoCHXspvHPgw1Rr9E6wk"

search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

search_params = {
    'screen_name': '@ManaByte',
}

search_url = '{}1.1/friends/list.json'.format(base_url)

response = requests.get(search_url, headers=search_headers, params=search_params)

json_response = response.json()


def get_list_keys(dct):
    lst = []
    for key in dct.keys():
        lst.append(key)
    return lst


print(get_list_keys(json_response))
pprint.pprint(json_response)
