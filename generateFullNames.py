# last names as keys, and a list of employee first names as values. 
# The function generates a new list that contains each employees’ full
# name (First_name Last_Name). For example, the key "Garcia" with the 
# values ["Maria", "Hugo", "Lucia"] should be converted to a list 
# that contains ["Maria Garcia", "Hugo Garcia", "Lucia Garcia"].
def generate_fullnames(employee_dict):
    full_names = []
    for lastname, firstnames in employee_dict.items():
        for firstname in firstnames:
            full_names.append(firstname +' '+lastname)
    return full_names
print(generate_fullnames({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}))