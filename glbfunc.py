#globally used function goes here. e.g : csv read, parse, etc.


# csv reader
def csv_reader(file_name):
    return open(file_name, 'r')

# csv parser
def csv_parser(file_name, separator, column, row):
    new_string = 0
    new_list = ['' for i in range (row)]; new_list_counter = 0
    new_new_list = [['' for j in range (row)] for i in range (column)]; new_new_list_counter = 0
    for i in range(row):
        for j in range(i):
            if j != separator and j != '\n':
                new_string += j
            elif j == separator:
                new_list[new_list_counter] = new_string
                new_list_counter += 1
                new_string = ''
            else:
                new_list[new_list_counter] = new_string
                new_new_list[new_new_list_counter] = new_list
                new_string = ''
                new_list = ['' for i in range (row)]
                new_list_counter = 0
                new_new_list_counter += 1
    return new_new_list

#F05 - Nakeisha
#def csv_monster(file_name, separator, column, row):
#    list_monster = csv_parser(file_name, separator, column, row)
#    while True :
        



def fsplit(text, separator): # penggunaan split manual
    var_kosong = []
    index_mulai = 0
    for i, char in enumerate(text):
        if char == separator:
            var_kosong.append(text[index_mulai:i])
            index_mulai = i + 1
    var_kosong.append(text[index_mulai:])
    return var_kosong



def custom_split(text, delimiter):
    parts = []
    current_part = ''
    for char in text:
        if char != delimiter:
            current_part += char
        else:
            parts.append(current_part)
            current_part = ''
    parts.append(current_part)  # Append the remaining part
    return parts


def read_csv(file_path, delimiter):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            row = custom_split(line, delimiter)
            data.append(row)
    return data

def potion (hpx, monsterl) :
    strength_potion = atk_power + (atk_power * 0.05)
    resilience_potion = def_power + (def_power * 0.05)
    if hpx > hp :
        healing_potion = hp + (hp *0.25)
    else :
        healing_potion = hpx + (hpx *0.25)
    return strength_potion, resilience_potion, healing_potion


def search_monster(data, monster_id):
    for item in data:
        if str(item[0]) == str(monster_id): # skip kolom pertama
            return item
            break   


def search_monster_inventory(data, user_id) :
    arr = []
    for item in data:
        if str(item[0]) == str(user_id) :
            arr.append(item)
            continue
    return arr
    
def search_item_inventory(data, user_id) :
    arr = []
    for item in data:
        if str(item[0]) == str(user_id) :
            arr.append(item)
            continue
    return arr

def search_item_shop(data, ftype) :
    for item in data:
        if str(item[0]).lower() == str(ftype).lower(): # skip kolom pertama
            return item
            break       

def search_monster_shop(data, monster_id) :
    for item in data:
        if str(item[0]) == str(ftype): # skip kolom pertama
            return item
            break       

def search_user(data, user_id) :
    for item in data:
        if str(item[0]) == str(user_id): # skip kolom pertama
            return item
            break    

def search_list_inventory(data_inventory, no_urut) :
    for item in data_inventory:
        if str(item[0]) == str(no_urut): # skip kolom pertama
            return item
            break    

def ket_potion(source) :
    type_posion=''
    if source == "strength" :
        type_posion = "ATK"
    elif source== "resilience" :
        type_posion = "DEF"
    elif source == "healing" :
        type_posion = "Heal"
    return type_posion