def int_main(void):
    #opening file for reading, if not found, main is terminated
    file_name = input('What file do you want to parse?: ')
    try:
        with open(file_name) as my_file:
            list_of_all_lines = my_file.readlines()
    except:
        print('File not found.')
        return 1;

    #obtaining list of all unique regions
    all_regions = unique_regions(list_of_all_lines);

    #outputting information for each region 
    for region in all_regions:
        diff_langs, most_common = list_of_all_languages(region,list_of_all_lines);
        print(f"Name of continent: {region}\nPopulation: {population_count_for_a_region(region,list_of_all_lines)}\nArea: {area_count_for_a_region(region,list_of_all_lines)}");
        print(f"List of all Languages : {diff_langs}\nMost spoken Language: {most_common}\n");

    return 0;

def break_apart(my_string, my_delimiter):
    #initializing empty list and empty string to add char to
    new_list, list_entry = [], str("");

    #for each char not equal to delimiter and ',', added to empty string until loop iterates through it
    for char in range(len(my_string)):
        if (my_string[char] == my_delimiter or my_string[char] == ','):
            new_list.append(list_entry)
            list_entry = str("");
        else:
            list_entry += str(my_string[char]);

    return new_list;

def most_frequent(List): 
    #for each element duplicate add to count, if greater than max count, that word becomes most frequent
    max_count, most_freq_elem = int(0), None;

    for element in range(len(List)):
        count = 1;
        for duplicate in range(len(List)):
            if(List[duplicate] == List[element]):
                count += 1;
                if (count > max_count):
                    most_freq_elem = List[duplicate];
                    max_count = count;

    return most_freq_elem;

def unique_regions(list_of_all_countries_with_data):
    aux_list, Regions, holder = [], [], [];

    #for each element, break the list down, and append the 4th index
    for element in range(len(list_of_all_countries_with_data)):
        aux_list = break_apart(list_of_all_countries_with_data[element], "\n");
        holder.append(aux_list[4]);

    #add element if element does not already exist
    for x in range(len(holder)):
        dupe = False;
        for y in range(len(Regions)):
            if (holder[x] == Regions[y]):
                dupe = True;
        if(dupe == False):
            Regions.append(holder[x]);
    #making regions sorted in alphabetical order
    Regions.sort()

    return Regions;

def population_count_for_a_region(region,list_of_all_countries_with_data):
    holder, aux_list, total_pop = [], [], 0;

    #Break appart list and add the element of population to another list
    for element in range(len(list_of_all_countries_with_data)):
        aux_list = break_apart(list_of_all_countries_with_data[element], "\n");
        holder.append(aux_list);
    #if regions are the same to the new list, add the value of population
    for x in range(len(holder)):
        if(region == holder[x][4]):
            total_pop += int(holder[x][1]);

    return total_pop;

def area_count_for_a_region(region,list_of_all_countries_with_data):
    #same as previous function except using a differnt index that holds the element with area
    holder, aux_list, total_area = [], [], int(0);

    for element in range(len(list_of_all_countries_with_data)):
        aux_list = break_apart(list_of_all_countries_with_data[element], "\n");
        holder.append(aux_list);
    for x in range(len(holder)):
        if(region == holder[x][4]):
            total_area += int(holder[x][2]);

    return total_area;

def list_of_all_languages(region,list_of_all_countries_with_data):
    holder, aux_list, repeated_langs, Langs, most_common_lang = [], [], [], [], None;

    #break appart by creating 2d array with region and language
    for element in range(len(list_of_all_countries_with_data)):
        aux_list = break_apart(list_of_all_countries_with_data[element], "\n");
        holder.append(aux_list);
    for x in range(len(holder)):
        if(region == holder[x][4]):
            repeated_langs.append(holder[x][3]);

    most_common_lang = most_frequent(repeated_langs);

    #same procedure to find repeated regions used here
    for x in range(len(repeated_langs)):
        dupe = False;
        for y in range(len(Langs)):
            if (repeated_langs[x] == Langs[y]):
                dupe = True;
        if(dupe == False):
            Langs.append(repeated_langs[x]);

    return Langs,most_common_lang;

void = None;
int_main(void);
