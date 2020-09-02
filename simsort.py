import sys,pprint

## Sorting the output of the simweb api script.
## Separate script because I was too lazy to work with multithreading and variables

DESC = True
DICT = {}

def line_to_num(line):
    cline = line.replace("\033[1;32;48m","").replace("\033[1;37;0m","")
    return int(cline[cline.find("(")+1:cline.find(")")].replace(",",""))

def line_to_dict(line):
    DICT[line_to_num(line)] = line[:-1]


if __name__ == "__main__":
    with open(sys.argv[1],"r") as f:
        for l in f.readlines():
            line_to_dict(l)
    f.close()
    for sk in sorted(DICT.keys(),reverse=DESC):
        print(DICT[sk])
