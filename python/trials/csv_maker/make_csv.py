def make_n_entries_for_csv_filename(filename,
                                    start_id=20001, num_entries=10000):
    output_csv_li = []
    for i in range(start_id, start_id + num_entries):
        next_str = str(i)
        email_id = "ltuser+" + next_str + "+i@enfold.com"
        password = "Enfold*" + next_str
        output_csv_li.append(",".join([email_id, password]))

    with open(filename, 'w') as fw:
        fw.write("\n".join(output_csv_li))

if __name__ == "__main__":
    make_n_entries_for_csv_filename(
        "10k_users.csv"
    )
