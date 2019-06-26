import requests

user = "xavier_v_tandova"
url = 'https://www.instagram.com/' + user
r = requests.get(url).text

start = '"edge_followed_by":{"count":'
end = '},"followed_by_viewer"'
# str_string = 'staaart'
# str_start = 'taa'
# str_end = 'rt'

print(len(start))
print(r.find(start)+len(start))
print(r.rfind(end))
print(r[r.find(start)+len(start):r.rfind(end)]) 
 
# print(start[len(start)/2:(len(start)/2)+1])
# print(str_string.find(str_start))
# print(str_string.find(str_end[0]))
# print(str_string[str_string.find(str_start)+len(str_start):str_string.find(str_end[0])])