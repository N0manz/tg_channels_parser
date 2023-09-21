import pandas as pd
import json
import codecs

with open(r'D:\python_projects\parser_tg_project\rybar.json', 'r') as file:
    json_string = file.read()
posts_arr = []
content_arr = []
while json_string:
    start_index = json_string.find('{')
    if start_index == -1:
        break
    end_index = json_string.find('}', start_index)
    if end_index == -1:
        break
    st = json_string[start_index:end_index + 1]
    content = st[st.find('"content"') + len('"content"') + 2:st.find('"outlinks"') - 2]
    if content != 'null':
        content = content[1:-1]
        content = json.loads('"' + content + '"')
    content_arr.append(content)

    posts_arr.append(json_string[start_index:end_index + 1])
    json_string = json_string[end_index + 1:]


for content in content_arr:
    print(content)

