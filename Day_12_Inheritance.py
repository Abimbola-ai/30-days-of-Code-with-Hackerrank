class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
        
    def __init__(self, firstName, lastName, idNumber,scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores
   
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(total_scores):
        ave = int(sum(scores)//len(scores))
        if 90 <= ave <= 100:
            return("O")
        elif 80 <= ave < 90:
            return("E")
        elif 70 <= ave < 80:
            return("A")
        elif 55 <= ave <70:
            return("P")
        elif 40 <= ave < 55:
            return("D")
        elif ave < 40:
            return("T")