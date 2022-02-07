










def main():
    #getting input file to read, if not found exit program


    return 0;

def create_map_find_path(file_name):



    return 0;



def find_path(current_pos, dest,pos):
    while weight[1][3][0] == "inf":





    return 0;



def print_path(path):



    return 0;


def less_bloated_split(my_string, my_delimiter):
    #initializing empty list and empty string to add char to
    new_list, list_entry = [], str("");

    #for each char not equal to delimiter and ',', added to empty string until loop iterates through it
    for char in range(len(my_string)):
        if (my_string[char] == my_delimiter or my_string[char] == "\n"):
            new_list.append(list_entry)
            list_entry = str("");
        else:
            list_entry += str(my_string[char]);

    return new_list;
#file_name = input('What file do you want to parse?: ')
try:
    with open("sample.txt") as my_file:
        map_text = my_file.readlines()
except:
    print('File not found.')
    exit()

weight, map_h, temp, map_info= [], [], [], [];

for line in range(len(map_text)):
    temp = less_bloated_split(map_text[line]," ");
    map_info.append(temp);
print(map_info)
n = int(map_info[0][0])
Map = [[ [] for i in range(n)] for j in range(n)]
weight = [[ [] for i in range(n)] for j in range(n)]
for x in range(n):
    map_h.append(map_info[3+x])
for j in range(n):
    for k in range(n):
        Map[j][k].append(map_h[j][0][k])
for i in range(n):
    for j in range(n):
        if Map[i][j][0] != "1":
            weight[i][j].append("inf");
        elif Map[i][j][0] == "1":
            weight[i][j].append(-1)
for row in Map:
    print(*row, sep="")
weight[7][3][0] = 0
for row in weight:
    print(*row, sep="")

