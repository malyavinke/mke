import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: 
    # value: 
    m = record[0]
    i = record[1]
    j = record[2]
    value = record[3]

    if m == 'a':
        for x in range(5):
            mr.emit_intermediate((i, x), ((i,j),value))
    if m == 'b':
        for x in range(5):
            mr.emit_intermediate((x, j), ((x,i),value))

def reducer(key, list_of_values):
    dict = {}
    for rec in list_of_values:
        row_col = rec[0]
        value = rec[1]
        dict.setdefault(row_col, [])
        dict[row_col].append(value)
    dot_pr = 0
    for list in dict.itervalues():
        if len(list) > 1:
            dot_pr = dot_pr + list[0] * list[1]
    mr.emit((key[0],key[1], dot_pr))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
