import re
SEP = "::"

if __name__ == "__main__":
    file_name = "whatsapp_stats.txt"
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
        obj["date"] = content_list[i].strip()

        dialog = content_list[j].strip()

        dialog_type = "default"
