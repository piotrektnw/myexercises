sampleStr = "Emma is good developer. Emma is a writer"
cnt = sampleStr.count("Emma")
print(cnt)

# or without using any string function 

def count_jhon(statement):
    print("Given String: ", statement)
    count = 0
    for i in range(len(statement) - 1):
        count += statement[i: i + 4] == 'Emma'
    return count

count = count_jhon("Emma is good developer. Emma is a writer")
print("Emma appeared ", count, "times")
