from dtree import *
from id3 import *
import sys
import math
import csv as csv


def get_file():
    """
    Tries to extract a filename from the command line.  If none is present, it
    prompts the user for a filename and tries to open the file.  If the file 
    exists, it returns it, otherwise it prints an error message and ends
    execution. 
    """
    # Get the name of the data file and load it into 
    if len(sys.argv) < 2:
        # Ask the user for the name of the file
        print "Filename: ", 
        filename = sys.stdin.readline().strip()
    else:
        filename = sys.argv[1]
    return filename
    try:
        fin = open(filename, "r")
    except IOError:
        print "Error: The file '%s' was not found on this system." % filename
        sys.exit(0)

    return fin

def get_data(csv_file_object, new_attributes, attr_list):
    data=[] #Creat a variable called 'data'
    for row in csv_file_object: #Skip through each row in the csv file
        data.append(row) #adding each row to the data variable
#        data = np.array(data) #Then convert from a list to an array    

#    return
# Create a list of all the lines in the data file
#    lines = [line.strip() for line in fin.readlines()]

    # Remove the attributes from the list of lines and create a list of
    # the attributes.
  #  lines.reverse()


#    attributes = [attr.strip() for attr in lines.pop(0).split(",")]
#    print attributes
 #   lines.reverse()

    # Create a list of the data in the data file
    train_data = []
    for line in data:
        values = []
        i = -1
        for datum in line:
            i = i + 1
            if i in attr_list:
#                if not datum: values.append('C')
#                else: 
                values.append(datum.strip())
#        data.append(dict(zip(attributes,
#                             [datum.strip() for datum in line.split(",")])))

        train_data.append(dict(zip(new_attributes, values)))
        
    # Copy the data list into the examples list for testing
#    print train_data

    return train_data
    examples = train_data[:]
    print train_data


def get_test_data(csv_file_object, new_attributes, attr_list):
    data=[] #Creat a variable called 'data'
    for row in csv_file_object: #Skip through each row in the csv file
        data.append(row) #adding each row to the data variable
#        data = np.array(data) #Then convert from a list to an array    

#    return
# Create a list of all the lines in the data file
#    lines = [line.strip() for line in fin.readlines()]

    # Remove the attributes from the list of lines and create a list of
    # the attributes.
  #  lines.reverse()


#    attributes = [attr.strip() for attr in lines.pop(0).split(",")]
#    print attributes
 #   lines.reverse()

    # Create a list of the data in the data file
    train_data = []
    for line in data:
        values = [""]
        i = -1
        for datum in line:
            i = i + 1
            if i in attr_list:
                values.append(datum.strip())
#        data.append(dict(zip(attributes,
#                             [datum.strip() for datum in line.split(",")])))

        train_data.append(dict(zip(new_attributes, values)))
        
    # Copy the data list into the examples list for testing
#    print train_data

    return train_data
    examples = train_data[:]
    print train_data


def run_test(fin):
    """
    This function creates a list of exmaples data (used to learn the d-tree)
    and a list of samples (for classification by the d-tree) from the
    designated file.  It then creates the d-tree and uses it to classify the
    samples.  It prints the classification of each record in the samples list
    and returns the d-tree.
    """
    csv_file_object = csv.reader(open(fin, 'rb')) #Load in the csv file
    attributes = csv_file_object.next() #Skip the fist line as it is a header
#    print attributes
    new_attributes = [attributes[0], attributes[1], attributes[3], attributes[5], attributes[6],attributes[10]]
#    print new_attributes


    target_attr = attributes[0]


    
    # Create the decision tree
    tree = create_decision_tree(get_data(csv_file_object, new_attributes, [0,1,3,5,6,10]), new_attributes, target_attr, gain)

    # Classify the records in the examples list
    
    csv_file_object = csv.reader(open('test.csv', 'rb')) #Load in the csv file
    attributes = csv_file_object.next() #Skip the fist line as it is a header
#    print attributes
#    new_attributes = [attributes[0], attributes[2], attributes[4], attributes[9]]
#    print new_attributes


#    target_attr = attributes[0]



    classification = classify(tree, get_test_data(csv_file_object,new_attributes, [0,2,4,5,9]))

    # Print out the classification for each record
    for item in classification:
        print item

    return tree

def print_tree(tree, str):
    """
    This function recursively crawls through the d-tree and prints it out in a
    more readable format than a straight print of the Python dict object.  
    """
    if type(tree) == dict:
        print "%s%s" % (str, tree.keys()[0])
        for item in tree.values()[0].keys():
            print "%s\t%s" % (str, item)
            print_tree(tree.values()[0][item], str + "\t")
    else:
        print "%s\t==>\t%s" % (str, tree)
        

if __name__ == "__main__":
    fin = get_file()
    print "------------------------\n"
    print "--   Classification   --\n"
    print "------------------------\n"
    print "\n"    
    tree = run_test(fin)
#    print "\n"
#    print "------------------------\n"
#    print "--   Decision Tree    --\n"
#    print "------------------------\n"
#    print "\n"
#    print_tree(tree, "")
#    fin.close()
