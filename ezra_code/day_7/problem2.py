'''
A program to return a dictionary of all the names that start with S
how many times they appear in the dictionary
'''

def first_s(list):
    tracker = 0
    s_name_dict = {}
    for name in list:
        #divide the s names from the other names in the list
        if name[0] == 'S':
            #Tracker to keep track of the number of times the name has appeared
            tracker = list.count(name)
            #Append name to a dictionary plus the counter
            s_name_dict[name] = tracker
            #Reset tracker
            tracker = 0


    #return the dictionary
    return s_name_dict

test = ["Joseph", "Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]

print(first_s(test))
