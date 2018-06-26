def deleteUnnecessaryData(data):
    for num in range(0, len(data)):
        del data[num][1:3]

def save_file(data, name):
    file = open(name + ".txt","w") 
    num = 0
    while(num != len(data)):
        file.write(str(data[num])+"\n")
        num = num + 1        
    file.close() 

def getFirst200OfCategory():
    file = open("book32listing.csv", "r") 
    book = file.readlines() 
    fileList = []

    for x in range(0, len(book)):
        lineList = book[x].split(",")
        fileList.append(lineList)

    categoryList = []
    officialList = []
    x = 0

    count = 0
    while(x<len(fileList)):
        category = fileList[x][-1]
        try:
            number=categoryList.index(category)
        except ValueError:
            count = count + 1
            inList = 'false'
        else:
            inList = 'true'
        if((categoryList == 0) or (inList == 'false')):
            categoryList.append(category)
            y = 0 
            for y in range(x, x+201):
                if(fileList[y][-1] != category):
                    break;
                else:
                    officialList.append(fileList[y])
            category = fileList[y][-1]
            x = x + 200
        x = x + 1    

    return officialList
bookList = getFirst200OfCategory()
deleteUnnecessaryData(bookList)
save_file(bookList, "officialBookList")

    

# "Amazon Index","Filename","Image","Title","Author","Category ID","Category"
# 0                 1         2        3      4          5