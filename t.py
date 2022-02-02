def break_apart(my_string, my_delimiter):
    '''
    This is for 10 points extra credit.
    This function receives a string and returns a list back.
    It receives something like "Azerbaijan,9552500,86600,az,Asia\n" and a delimiter i.e. ','
    should return something like ['Azerbaijan', '9552500', '86600', 'az', 'Asia']
    '''
    new_list = [];
    list_entry = "";
    for  char in my_string:
        if (char == my_delimiter):
            new_list.append(list_entry);
            list_entry = "";
        else:
            list_entry += char;

    return new_list;

list_of_all_countries_with_data = ["Australia,23696900,7692024,en,Oceania\n", "Austria,8527230,83871,de,Europe\n", "Azerbaijan,9552500,86600,az,Asia\n","Bulgaria,7245677,110879,bg,Europe\n"]
aux_list = [];
Regions = []
print(list_of_all_countries_with_data[0])
for element in range(len(list_of_all_countries_with_data)):
    print(list_of_all_countries_with_data[element])
    aux_list = break_apart(list_of_all_countries_with_data[element], ",");
    print(aux_list)
