import csv

class Person(object):
    def __init__(self, id, person_dict):
        self.id = id
        self.category = person_dict.pop('Category')
        self.first_name = person_dict.pop('First Name')
        self.last_name = person_dict.pop('Last Name')
        for (day, seat_assignment)  in person_dict.iteritems():
            setattr(self, day, seat_assignment)

def people_objects(filename):
    reader = csv.DictReader(open(filename,"rwU"))
    people = [row for row in reader]
    current_id = 1
    people_list = []
    days = days_list(filename)
    for p in people: 
        person = Person(current_id, p)
        people_list.append(person)
        current_id += 1
    return people_list

class Table(object):
    def __init__(self, name, day, capacity):
        self.name = name
        self.day = day
        self.capacity = capacity
        self.people = []

def table_objects(filename):
    '''
    Creates a list of objects, 1 for each table
    '''
    reader = csv.DictReader(open(filename,"rwU"))
    temp_tables = [row for row in reader]
    days = days_list(filename)
    tables = []
    for table in temp_tables:
        name = table['Table Name']
        for day in days:
            capacity = table[day]
            table_object = Table(name, day, capacity)
            tables.append(table_object)
    return tables

def days_list(filename):
    reader = csv.reader(open(filename, "rwU"))
    header = reader.next()
    days_list = [day for day in header if day not in 
                 ['Table Name', 'Category', 'First Name', 'Last Name']]
    return days_list

def tables_to_people(tables_list):
    all_people = []
    people_dicts = []
    for table in tables_list:
        all_people.extend(table.people)
    unique_people = set(all_people)
    for person in unique_people:
        people_dicts.append(person.__dict__)
    return people_dicts

def write_to_csv(tables, filename):
    people = tables_to_people(tables)
    fieldnames = ['id','category', 'last_name', 'first_name', 
                  'Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    output_file = open(filename,'wb')
    csvwriter = csv.DictWriter(output_file, delimiter=',', fieldnames=fieldnames)
    csvwriter.writerow(dict((fn,fn) for fn in fieldnames))
    for p in people:
        csvwriter.writerow(p)
    output_file.close()