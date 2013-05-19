import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: 
    # value: 
    key = record[0]
    value = record[1]
    trimed = value[:-10]
    mr.emit_intermediate(trimed, 1)

def reducer(key, list_of_values):
    # key: 
    # value: 
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
