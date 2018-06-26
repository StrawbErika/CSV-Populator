
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

def readCSV():
    file = open("book32listing.csv", "r") 
    book = file.readlines() 
    fileList = []

    for x in range(0, len(book)):
        lineList = book[x].split(",")
        fileList.append(lineList)
    return fileList

def getFirst200OfCategory(data):
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


bookList = readCSV()
deleteUnnecessaryData(bookList)
save_file(bookList, "officialBookList")

import pymysql


for x in range(0, len(bookList)):
    bid = bookList[x][0]
    title = bookList[x][1]
    author = bookList[x][2] 
    category = bookList[x][-1]
    connectionObject = pymysql.connect(host='localhost',
                                user='root',
                                password='tomhiddleston',
                                db='library',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        cursorObject= connectionObject.cursor()                                     
        cursorObject.execute("""INSERT INTO book(bid, title, author, category) VALUES (%s,%s,%s, %s)""", (bid, title, author, category))
    except Exception as e:
        print("Exeception occured:{}".format(e))
    finally:
        connectionObject.close()

    print(str(x) +" Done!")
