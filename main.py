def open_file(filename):
    return open(filename,"r", encoding = "UTF-8")

def generate_frequency_map(filename):
    dictionary = {} 
    DictFile = open_file(filename)

    if not DictFile:
        print("invalid file")
        return None
    
    while True:
        read_content = DictFile.read(1)
        if not read_content:
            break
        # for content in read_content:
        if read_content in dictionary:
            dictionary[read_content]+=1
        else:
            dictionary[read_content] = 1

    return dictionary

print(generate_frequency_map("135-0.txt"))