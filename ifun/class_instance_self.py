# Know more from 'class', 'self', 'instance', '__variable'
# any 'def' in 'class' should include 'self' in the parameter, to point the created instance
class Student(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score = score
	def print_porperty(self):
		print('%s:%d'%(self.__name, self.__score))

	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__score
	def reset_name(self, change_name):
		self.__name = change_name
	def reset_score(self, change_score):
		self.__score = change_score

student = Student('hanry', 99)
student.print_porperty()
name = student.get_name()

name = student.get_name()
score = student.get_score()
print('%s:%d' %(name, score))

# When using '__name' or store variable to the name with '__', other outside function cannot 
# call the '__name', but can return the '__name'
# the problem only appear when call 'print'

# when seeing '__xxx__', means to 'particular value', we can visit the 'particular value'
# directly.
class Student(object):
	def print_self(self):
		print(self)
		print(self.__class__)

student = Student()
student.print_self()
# 'self' is the instance of class, 'self.__class__' is a truly 'class' instead

class Teacher(object):
	def __init__(self, teacher):
		self.teacher = teacher
		print(self.teacher)
	def print_self(self):
		print(self)

class Student(object):
	def __init__(self, student):
		self.student = student
		print(self.student)
	def print_self_1(self):
		print(self)
teacher = Teacher('hensry')
student = Student('simona')
student.print_self1()
student.print_self()
# when define 'class', it's better to add 'self' in the parameter of 'class'
# when inherit, the last two line would output the same result
# because the 'self' is the same as the last given value -> the same 'self'
