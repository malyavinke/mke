import MapReduce
import sys
import json

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order number
    key = record[1]

    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    # key: order number

    order = ""
    order_items = []
    for record in list_of_values:

        if 'line_item' in record:
            order_items.append(record)
        else:
            order = record

    for item in order_items:
        join_record = order[:]
        for word in item:
            join_record.append(word)
        mr.emit(join_record)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
