

def make_n_entries_for_csv_filename(filename,
                                    start_id=20001,
                                    num_entries=10000,
                                    heading_row=True
                                    ):
    output_csv_li = []
    output_csv_li.append("BigLT_All_IDs,BigLT_All_Passwords")
    for i in range(start_id, start_id + num_entries):
        next_str = str(i)
        email_id = "ltuser+" + next_str + "+i@enfold.com"
        password = "Enfold*" + next_str
        output_csv_li.append(",".join([email_id, password]))

    with open(filename, 'w') as fw:
        fw.write("\r\n".join(output_csv_li))

if __name__ == "__main__":
    num_entries = 50000
    make_n_entries_for_csv_filename(
        str(num_entries) + "_users.csv",
        num_entries=num_entries
    )
