import re

info_list = "sama zare +989177655948"

find_number = re.findall(r"\+\d+", info_list)
print(f"is this {find_number} your number?")