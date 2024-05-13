def custom_split(text, delimiter):
  result = []
  start = 0
  for i in range(len(text)):
    char = text[i]
    if char == delimiter:
      result.append(text[start:i])
      start = i + 1
  result.append(text[start:])
  return result


def tulis_csv(filename, data):
  with open(filename, 'w', newline='') as file:
    for row in data:
      csv_row = ""
      for index, element in enumerate(row):
                csv_row += str(element)
                if index < len(row) - 1:
                    csv_row += ';'
      csv_row += '\n'
      file.write(csv_row)


def baca_csv(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            if line[len(line)-1] == '\n':
                line = line[:len(line)-1]
            row = custom_split(line, ";")
            data.append(row)
    return data