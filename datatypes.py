#change elements in a list
marks =[80, 90, 75]
marks[2] = 78
print(marks)
#add elements to a list
marks = [80, 90, 75]
marks.append(85)
print(marks)
#remove elements from a list
marks = [80, 90, 75]
marks.remove(90)
print(marks)
#inset elements in list
number = [10, 20, 30]
number.insert(1,15)
print(number)
number = [10, 20, 30]
number.insert(2, 25)
print(number)
#extend elements in list
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)
#clear elements in list
numbers = [10, 20, 30]
numbers.clear()
print(numbers)
#index elements in list 
number = [10, 20, 30, 40]
print(number.index(30))
#count method
numbers =[10, 20, 30, 40 ,50]
print(number.count(10))
#sort method
numbers = [10, 20, 30, 40]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
#reverse method
numbers = [10, 20, 30, 40]
numbers.reverse()
print(numbers)
#copy method
a = [1, 2, 3]
b =a.copy()
print(b)

numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])
#tuples in python
#Tuple is a collection of multiple values that is ordered and cannot be changed
student = ("Bhargavi", 98, "python") 
print(student[0])
#access values in a tuple
student = ("Bhargavi", 21, 85.5)
print(student[0])
print(student[1])
print(student[2])
#immutable nature of tuples

#tuples are immutable, meaning they cannot be changed after
numbers = (10, 20, 20, 30, 20)
print(numbers.count(20))
numbers = (10, 20, 30, 40)
print(numbers.index(30))
numbers = (10, 20, 30, 40)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
#sets in python 
#sets is a collection of unique values that is unordered and mutable 
numbers = {10, 20, 30, 20, 10} 
print(numbers)
#why use set?
#suppose students have selected subjects
subjects = {"python", "java", "python", "SQL", "java"}
print(subjects)
#add value to a set
subjects = {"python", "java"}
subjects.add("SQL")
print(subjects)
#remove values from a set 
subjects.remove("java")
print(subjects)
#sets do not allow duplicate values 
numbers = {1, 2, 2, 3, 3, 4}
print(numbers)
