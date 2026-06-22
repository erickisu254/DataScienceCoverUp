# Data

import re

data = {
    "Name": [
        "@Sarah Jones", "David Miller ", "mavis Jokie", "1Mavis Jones", "Mary John ", "Taylor macey", "John Doe", "Barry Allen#", "tisler mary", "@Wilfred Gondy"
        ],
        "Age": [
        23, 45, 67, 23, 54, 24, 42, 16, 53, 36
        ],
        "Countrty of residence": [
        "KE", "UG", "TZ", "US", "FR", "EG", "SA", "KE", "TZ", "ER"
        ],
        "GPA":[
        12, 32, 26, 36, 74, 12, 53, 74, 26, 102
        ]}


Names_list = data["Name"]

Names_l =[]
for elem in Names_list:
    Clean_Name = re.sub(r'[^a-zA-Z\s]', '', elem)
    Clean_Name = Clean_Name.strip()
    Clean_Name = Clean_Name.title()

    Names_l.append(Clean_Name)



print(Names_l)

