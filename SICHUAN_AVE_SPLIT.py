import csv;
import pandas as pd 

index=0
header_row = ['','id','en','entime','ex','extime','path','link','time_inter','speed','count','length','shike']
filename = "E:\\LEARN\\PAPER_PROCEDURE\\k_shoretest_path\\TEST_NEW1.txt"
#最后的结果集
all=[]
with open(filename) as f:
    reader = csv.reader(f)
    list2=list(reader)
#    print(list2)
    #添加第一行
    all.append(header_row)

    for index1 in range(len(list2)):
        #第一行不写入
        if(index1!=0):
            row=list2[index1]
            #范围list ['101', '104', '105']
            scales=list(row[6].replace("[","").replace("]","").replace(" ","").replace("'","").split(","))
            scales1=list(row[12].replace("[","").replace("]","").replace("'","").split(","))
            scales2=list(row[7].replace("[","").replace("]","").split(","))
            for num in range(len(scales)-1):
                insertList=[]
                #复制列表
                for everyElement in row:
                    insertList.append(everyElement)

                insertList[0]=index
                index=index+1

                insertList[2]=int(scales[num])
                insertList[4]=int(scales[num+1])
#            for num1 in range(len(scales1)-1):
                insertList[3]=(scales1[num])
                insertList[5]=(scales1[num+1])
                insertList[7]=(scales2[num])
                    
                all.append(insertList)
#            if (index1!=0):
#                row=list2[index1]
#                num=list(row[12].replace("[","").replace("]","")..replace("'","").split(","))
#                for i in range(len(num)-1):
#                    inserList1=[]
#                    for everyElement in row:
#                        inserList.append(everyElement)
#                    insertList1
#print(all)
all1=pd.DataFrame(all,columns=['','id','en','entime','ex','extime','path','link','time_inter','speed','count','length','shike'])
result=all1[['id','en','entime','ex','extime','link','time_inter','speed','count','length']]
result=result[1:]
#result.to_csv('E:\\LEARN\\PAPER_PROCEDURE\\k_shoretest_path\\TEST_NEW2.txt')
print(result)

'''
for resultrow in all:
    print(resultrow)
    
with open('E:\\LEARN\\PAPER_PROCEDURE\\k_shoretest_path\\hhhhhh1.txt', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(all)
'''