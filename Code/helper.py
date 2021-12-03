
def sorted(sort_by):
    with open('inventory.txt', 'r') as f:
        lines = f.read().split('\n')
        lines = filter(None, lines)
        items = [tuple(line.split(',')) for line in lines]
        if sort_by != 1:
            items.sort(key=lambda x: x[sort_by])
        else:
            # if sorting by quantity, first parse it into integer
            items.sort(key=lambda x: int(x[sort_by]))
        print(len(items[0]))
        print('but this does print')
        return items

def create_string(arr):
    s = ''
    print(len(arr[0]))
    for name, amount, date in arr:
        s += name + ',' + amount + ',' + date + ';'

    if len(s) > 0:
        s = s[:-1]
    return s

def create_string_1(name, amount, date):
    s = ''
    
    s += name + "," + amount + "," + date
    return s

def updated(name, newq):
    with open('inventory.txt', 'r') as f:
        lines = f.read().split('\n')
        for line in lines:
            print(line)
    with open('inventory.txt', 'w') as f:
        flag = False
        print("changes are abbout to be made \n")
        for line in lines:
            fields = line.split(',')
            if fields[0] == name:
                flag = True
                new_item = create_string_1(fields[0], newq, fields[2])
                f.write(new_item + "\n") 
            else:
                f.write(line + "\n")
        if flag == True:
            return 'Response\nsuccess'
        else:
            return 'Response\nerror\nUnable to find Item' + name
            
def delete(name):
    with open('inventory.txt', 'r') as f:
        lines = f.read().split('\n')
        for line in lines:
            print(line)
    with open('inventory.txt', 'w') as f:
        flag = False
        print("changes are about to be made \n")
        for line in lines:
            fields = line.split(',')
            if fields[0] == name:
                flag = True
                #f.write(new_item + "\n") 
            else:
                f.write(line + "\n")
        if flag == True:
            return 'Response\nsuccess'
        else:
            return 'Response\nerror\nUnable to find Item ' + name

# print('test')
# items = sorted(0)
# # items = [','.join(x) for x in items]
# print(create_string(items))