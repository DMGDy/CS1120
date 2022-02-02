string = "some,string,split\n"

char_new_char = [];
char_sep = ""
for x in string:
    if x == "\n" or x == ",":
        new_list.append(sep);
        sep = "";
    else:
        sep += x;

print(new_list)
