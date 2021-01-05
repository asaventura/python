import json


with open('business_data.txt') as bd:
    list_of_firms = [{}, {}]
    sum_line = 0
    num_of_firms = 0
    for file_line in bd.readlines():
        line = file_line.split()
        list_of_firms[0].update({line[0]: int(line[2]) - int(line[3])})
        if int(line[2]) - int(line[3]) > 0:
            sum_line += int(line[2]) - int(line[3])
            num_of_firms += 1
    list_of_firms[1].update({'average_profit': sum_line / num_of_firms})
    with open('business_data.json', 'w') as bd_json:
        json.dump(list_of_firms, bd_json)
