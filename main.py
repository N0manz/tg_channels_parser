
import json
def file(file_root):
    with open(file_root, 'r') as file:
        json_string = file.read()

    post_url_content = {}
    st = ''
    content = ''
    url = ''
    while json_string:
        start_index = json_string.find('{')
        if start_index == -1:
            break
        end_index = json_string.find('}', start_index)
        if end_index == -1:
            break
        st = json_string[start_index:end_index + 1]
        url = st[st.find('"url": "') + len('"url": "'): st.find('", "date"')]
        content = st[st.find('"content"') + len('"content"') + 2:st.find('"outlinks"') - 2]
        if content != 'null':
            content = content[1:-1]
            content = json.loads('"' + content + '"')
        post_url_content[content] = url

        json_string = json_string[end_index + 1:]
    return post_url_content
