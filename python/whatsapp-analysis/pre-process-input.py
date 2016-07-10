import re
import json

SEP = "::"


def build_no_to_name_map(file_name):
    obj = {}
    with open(file_name) as fp:
        for line in fp.readlines():
            num, name = line.strip().split(',')
            obj[num] = name
    return obj

if __name__ == "__main__":
    no_to_name_map = build_no_to_name_map("ignore_dir/num_to_name.txt")

    file_name = "ignore_dir/whatsapp_stats.txt"
    with open(file_name) as fp:
        file_contents = fp.read()

    # parsing the file inputs
    date_split_re = r'(?:^|\n)(\d+\/\d+\/\d+\s*,\s*.*?\-)'
    content_list = re.split(date_split_re, file_contents)[1:]

    # cleaning the content_list
    data_list = []
    for i in xrange(0, len(content_list), 2):
        j = i+1
        obj = {}
        obj["date"] = content_list[i].strip(" -")
        dialog_components = content_list[j].split(":", 1)
        dialog_components = map(str.strip, dialog_components)
        if len(dialog_components) > 1:
            dialog_type = "default"
            author, dialog = dialog_components
            # Cleaning up the author
            author = author.strip("\xe2\x80\xaa\xe2\x80\xac")
            author = no_to_name_map.get(author, author)
            if author in no_to_name_map.keys():
                author = no_to_name_map[author]
        else:
            author = ''
            dialog_type = "heading"
            dialog = dialog_components[0]

        obj['dialog_type'] = dialog_type
        obj['dialog'] = dialog
        obj['author'] = author

        data_list.append(obj)

    with open('ignore_dir/whatsapp_stats.json', 'w') as fw:
        json.dump(data_list, fw)
