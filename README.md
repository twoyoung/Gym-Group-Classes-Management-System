# Gym Group Classes Management System

This is the design of a system to manage group exercise classes in a gym using object oriented programming.

The goal is to create a system that efficiently manages class enrolments, tracks attendance, and calculatespayments for gym members participating in group exercise sessions. 

## Classes definition

- The GroupExercise Class groupExercise:
  - Attributes:
```
  def __init__(self, name, maximumCapacity):
        self.__name = name
        self.__maximumCapacity = maximumCapacity
        self.__fee = 0 # Initialize the fee to 0
        self.__trainer = None # Initialize the trainer to None
        self.__enrolledMemberList = [] # Initialize as empty list
        self.__waitlist = [] # Initialize as empty list
        self.__checkedInMemberList = [] # Initialize as empty list
```


    - The name of the group exercise class.
    - The trainer assigned to conduct the class (an object of the Trainer class).
    - The maximum capacity of the class.
    - A list of participants (objects of the Member class) who have enrolled in the class.
    - A list of gym members who are on the waitlist for the class.
    - The fee amount for the class.
    - A list of gym members (objects of the Member class) who have checked-in for the class.
  - Methods:
    - Enrols a gym member into the group exercise class. If the class is full, the member will be added to the waitlist.
    - Removes a gym member from the enrolled list.
    - Displays all gym members currently enrolled in the group exercise class.
    - Assigns a trainer to conduct the group exercise class.
    - Returns the number of gym members currently enrolled in the class.
    - Returns the number of available slots for enrolment in the class.
    - Sets the fee amount for the class.
    - Calculates and returns the total payment received for the group exercise class based on the number of enrolled members and the class fee.
    - Marks a gym member's attendance for the class.
    - Calculates and returns the attendance percentage for the class, representing the ratio of members checked-in to the total number of enrolled members.

- The Member Class:
```
def __init__(self, name, memberNumber):
        self.__name = name
        self.__memberNumber = memberNumber
        self.__enrolledGroupClass = [] # Initialize as emply list
```

  - Attributes:
    - The full name of the gym member.
    - A unique membership number for the gym member.
    - A list of group exercise classes (objects of the GroupExercise class) in which the member is enrolled.
  - Methods:
    - Books enrolment in a group exercise class. If the class is already full, the member will be added to the waitlist.
    - Cancels enrolment in a group exercise class.
    - Displays all booked group exercise classes.

- The Trainer Class:
```
class trainer:
    def __init__(self, name, expertise):
        self.__name = name
        self.__expertise = expertise
        self.__groupClass = []
```

  - Attributes:
    - The full name of the trainer.
    - The specialisation or expertise of the trainer.
    - A list of group exercise classes (objects of the GroupExercise class) assigned to the trainer.
  - Methods:
    - Displays the list of group exercise classes assigned to the trainer.
    - Adds a group exercise class to the list of classes assigned to the trainer.
