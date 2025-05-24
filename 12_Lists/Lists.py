# IN LIST WE CAN STORE MULTIPLE DATATYPE
# LIST IS MUTABLE AS COMPARE TO STRINGS MEANS WE CAN CHANGE LIST DIRECTLY

marks = [50,43,76,21]

mixed_marks = ["Kaif",54,8.9,True]

print(marks)
print(mixed_marks)

# STRING SLICING IS ALSO WORK IN LIST
print(marks[1:3])
print(mixed_marks[0:3])

# CONVERTING IN LIST
mark = str(marks)
print(mark,"\n",type(mark))