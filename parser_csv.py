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
