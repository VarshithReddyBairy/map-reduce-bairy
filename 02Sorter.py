# Varshith Bairy

def my_sort(line):
    line_fields = line.strip().split("	")
    amount = float(line_fields[1])
    return amount

n = open("01Mapper.txt","r")  # open file, read-only
o = open("02Sorter.txt", "w") # open file, write

lines = n.readlines()

# lines.sort(key = my_sort , reverse= True)
# lines.sort(key = lambda x : x[1])
lines.sort()

for line in lines:
	o.write(line)
n.close()
o.close()
