import csv
f=open("day6\students.csv","r")
f1=open("day6\student_details.txt","w")
k=csv.reader(f)
for i in k:
    f1.write(",".join(i)+"\n")
f.close()
f1.close()
