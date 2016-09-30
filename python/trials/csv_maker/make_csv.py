from pprint import pprint

l_users_num = 10
m_users_num = 500
l_starting_index = 3000


def make_n_entries_for_csv_filename(filename,
                                    start_id=20001,
                                    num_entries=100000,
                                    heading_row=True
                                    ):
    num_med = 0
    num_long = 0
    med_li = []
    long_li = []

    output_csv_li = []
    output_csv_li.append("BigLT_All_IDs,BigLT_All_Passwords")

    # Sprinkle medium and large users too from time to time
    long_interval = num_entries / l_users_num
    med_interval = num_entries / m_users_num

    l_index = 121000
    m_index = 120500

    for i in range(start_id, start_id + num_entries):
        next_str = str(i)
        email_id = "ltuser+" + next_str + "+i@enfold.com"
        password = "Enfold*" + next_str
        output_csv_li.append(",".join([email_id, password]))

        if (i-l_starting_index) % long_interval == 0:
            long_li.append(i)
            l_str = str(l_index)
            email_id = "ltuser+" + l_str + "+l@enfold.com"
            password = "Enfold*" + l_str
            output_csv_li.append(",".join([email_id, password]))
            num_long += 1
            l_index += 1
        if i % med_interval == 0:
            med_li.append(i)
            m_str = str(m_index)
            email_id = "ltuser+" + m_str + "+md@enfold.com"
            password = "Enfold*" + m_str
            output_csv_li.append(",".join([email_id, password]))
            num_med += 1
            m_index += 1

    with open(filename, 'w') as fw:
        fw.write("\r\n".join(output_csv_li))

    print("Num med -%d, num long - %d " % (num_med, num_long))
    pprint("Num med -%s, num long - %s " % (med_li, long_li))


if __name__ == "__main__":
    num_entries = 100000
    make_n_entries_for_csv_filename(
        str(num_entries) + "_users.csv",
        num_entries=num_entries
    )
