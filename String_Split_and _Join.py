def split_and_join(line):
    y=line.split(" ")
    result="-".join(y)
    return result  
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
