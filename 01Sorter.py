# Varshith Bairy

def my_sort(line):
    line_fields = line.strip().split("	")
    amount = float(line_fields[1])
    return amount

n = open("01Mapper.txt","r")  # open file, read-only
s = open("01Sorter.txt", "w") # open file, write


lines = n.readlines()
lines.sort(key = my_sort , reverse= True)
# lines.sort(key = lambda x : x[1])
# lines.sort()

for line in lines:
	s.write(line)
n.close()
s.close()
