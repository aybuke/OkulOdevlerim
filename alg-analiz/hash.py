def insert(h,k,v):
    index = hash(k)%100
    found_pair = False

    for pairs in h[index]:
        if k == pairs[0]:
            pairs[1] = v 
            found_pair = True

    if not found_pair:
        h[index].append([k,v])

    return h
     
def get(h,k):
    index = hash(k)%100

    for pairs in h[index]:
        if k == pairs[0]:
            return pairs[1]

    return 0

def main():
    hash_list = range(100)
    hash_list = [[] for i in hash_list]
    # print hash_list
    keep_going = "y"

    # prompts user for a key-value pair
    while keep_going.lower() == 'y':
        key = raw_input("key: ")
        value = raw_input("value: ")
        keep_going = raw_input("Want to add more? ('y' or 'n') ")

        hash_list = insert(hash_list,key,value)
        print hash_list

    key_to_find_value = raw_input("Find value of: ")
    found_value = get(hash_list,key_to_find_value)
    
    print found_value
    # print hash_list


main()
