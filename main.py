# Below is the definition of classes:

# groupExercise class definition
class groupExercise:
    def __init__(self, name, maximumCapacity):
        self.__name = name
        self.__maximumCapacity = maximumCapacity
        self.__fee = 0 # Initialize the fee to 0
        self.__trainer = None # Initialize the trainer to None
        self.__enrolledMemberList = [] # Initialize as empty list
        self.__waitlist = [] # Initialize as empty list
        self.__checkedInMemberList = [] # Initialize as empty list
    #getter
    @property
    def name(self):
        return self.__name
    @property
    def maximumCapacity(self):
        return self.__maximumCapacity
    @property
    def fee(self):
        return self.__fee
    @property
    def trainer(self):
        return self.__trainer
    @property
    def enrolledMemberList(self):
        return self.__enrolledMemberList
    @property
    def waitlist(self):
        return self.__waitlist
    @property
    def checkedInMemberList(self):
        return self.__checkedInMemberList
    #setter
    @name.setter
    def name(self, name):
        if name:
            self.__name = name
    @maximumCapacity.setter
    def maximumCapacity(self,number):
        self.__maximumCapacity = number
    @fee.setter
    def fee(self, amount):
        self.__fee = amount
    @trainer.setter
    def trainer(self, trainer):
        self.__trainer = trainer

    def __str__(self):
        return ("Group Exercise: {}\nMaximum Capacity: {}\nFee: {}\nTrainer: {}\n".format(self.__name, self.__maximumCapacity, \
        self.__fee, self.__trainer))
    
    # Enrols a gym member into the group exercise class. 
    def enrolMember(self, member):
        if len(self.__enrolledMemberList) < self.__maximumCapacity:
            self.__enrolledMemberList.append(member)
            member.enrolledGroupClass.append(self) # update member's class list
        else:
            self.__waitlist.append(member) # If the class is full, the member will be added to the waitlist.
    
    # Removes a gym member from the enrolled list. 
    def removeMember(self, member):
        if member in self.__enrolledMemberList: # If member in enrolled list, delete it
            self.__enrolledMemberList.remove(member)
            member.enrolledGroupClass.remove(self) # Update member's enrolled class list
        elif member in self.__waitlist: # If member in wait list, delete it
            self.__waitlist.remove(member)
        else: 
            print("Error: member not in enrolled list or wait list.")
    
    # Displays all gym members currently enrolled in the group exercise class.
    def displayEnrolledMembers(self):
        print("Enrolled Members for {}:\n".format(self.name))
        for member in self.__enrolledMemberList:
            print(member)
    
    # Assigns a trainer
    def assignTrainer(self, trainer):
        # if there's already another trainer, delete the exercise from the old trainer's class list
        if self.trainer:
            trainer.groupClass.remove(self)
        self.__trainer = trainer
        trainer.groupClass.append(self)

    # Returns the number of gym members currently enrolled in the class
    def numberOfEnrolledMembers(self):
        return len(self.__enrolledMemberList)

    # Returns the number of available slots for enrolment in the class.
    def numberOfAvailableSlots(self):
        return self.__maximumCapacity - len(self.__enrolledMemberList)
    
    # Sets the fee amount for the class.
    def setFee(self, amount):
        self.__fee = amount
    
    # Returns the total payment received for the group exercise class
    def totalPayment(self):
        return self.__fee * len(self.__enrolledMemberList)
    
    # Marks a gym member's attendance for the class. Add the member to the checked in list.
    def checkInClass(self, member):
        if member in self.__enrolledMemberList:
            self.__checkedInMemberList.append(member)
        else:
            print("Error. Couldn't mark this member's attendance. This member isn't enrolled.\n")
    
    # Returns the attendance percentage for the class
    def attendancePercentage(self):
        if len(self.__enrolledMemberList) > 0:
            return len(self.__checkedInMemberList)/len(self.__enrolledMemberList)


# member class definition 
class member:
    def __init__(self, name, memberNumber):
        self.__name = name
        self.__memberNumber = memberNumber
        self.__enrolledGroupClass = [] # Initialize as emply list
    # getter
    @property
    def name(self):
        return self.__name
    @property
    def memberNumber(self):
        return self.__memberNumber
    @property
    def enrolledGroupClass(self):
        return self.__enrolledGroupClass
    #setter
    @name.setter
    def name(self, name):
        if name:
            self.__name = name
    def __str__(self):
        return ("#{} {}\n".format(self.__memberNumber, self.__name))
    
    # Displays all booked group exercise classes.
    def displayBookedClass(self):
        for groupClass in self.__enrolledGroupClass:
            print(groupClass.name)

    # Cancels enrolment in a group exercise class. 
    def cancelClass(self, groupClass):
        groupClass.removeMember(self)

    # Books enrolment in a group exercise class.
    def bookClass(self, groupClass):
        groupClass.enrolMember(self)


# trainer class definition
class trainer:
    def __init__(self, name, expertise):
        self.__name = name
        self.__expertise = expertise
        self.__groupClass = []
    # getter
    @property
    def name(self):
        return self.__name
    @property
    def expertise(self):
        return self.__expertise
    @property
    def groupClass(self):
        return self.__groupClass
    # setter
    @name.setter
    def name(self, name):
        if name:
            self.__name = name
    @expertise.setter
    def expertise(self, expertise):
        if expertise:
            self.__expertise = expertise
    def __str__(self):
        return ("{} expertise in {}\n".format(self.__name, self.__expertise))
    
    # Displays the list of group exercise classes assigned to the trainer. 
    def displayClass(self):
        for groupClass in self.__groupClass:
            print(groupClass.name)

    # Adds a group exercise class to the list of classes assigned to the trainer.
    def addClass(self, groupClass):
        groupClass.assignTrainer(self)

# definition of classes end
# Below is the driver program:

# create groupExercise objects
groupExercise1 = groupExercise('Pilates', 15)
groupExercise2 = groupExercise('Yoga', 18)

# create member objects
member1 = member('David Brown',1)
member2 = member('Bob Marley',2)
member3 = member('Carol Keith',3)
member4 = member('Eve Green',4)
member5 = member('Alice Smith',5)

# create trainer objects
trainer1 = trainer('Michael Taylor','Pilates')
trainer2 = trainer('Leo White','Yoga')

# assign trainer to groupExercise objects
groupExercise1.assignTrainer(trainer1)
groupExercise2.assignTrainer(trainer2)

# set fee for groupExercise objects
groupExercise1.setFee(20.5)
groupExercise2.setFee(18.95)


# book classes for members
member1.bookClass(groupExercise1)
member1.bookClass(groupExercise2)
member2.bookClass(groupExercise1)
member3.bookClass(groupExercise2)
member4.bookClass(groupExercise2)
member5.bookClass(groupExercise2)

# cancel class for a member
member5.cancelClass(groupExercise2)

# record check in
groupExercise1.checkInClass(member1)

# display enrolled participants
groupExercise1.displayEnrolledMembers()
groupExercise2.displayEnrolledMembers()

# display the waitlist of a group exercise class
print("Waiting list for {} is:".format(groupExercise1.name))
if len(groupExercise1.waitlist) > 0:
    for member in groupExercise1.waitlist:
        print(member)
else:
    print("None\n")

# display the available slots for a group exercise class
print("Number of available slots for {} is: {}.".format(groupExercise1.name, groupExercise1.numberOfAvailableSlots()))
print("Number of available slots for {} is: {}.".format(groupExercise2.name, groupExercise2.numberOfAvailableSlots()))
print("\n")

# display the number of enrolled members of a group exercise class
print("Number of enrolled members of {} is: {}.".format(groupExercise1.name, groupExercise1.numberOfEnrolledMembers()))
print("Number of enrolled members of {} is: {}.".format(groupExercise2.name, groupExercise2.numberOfEnrolledMembers()))
print("\n")

# display the number of waitlist members of group exercise class
print("Number of wait list participants in {} is: {}.".format(groupExercise1.name, len(groupExercise1.waitlist)))
print("Number of wait list participants in {} is: {}.".format(groupExercise2.name, len(groupExercise1.waitlist)))
print("\n")

# display the number of attendees for a groupExercise class
print("Number of attendees for {} is: {}.".format(groupExercise1.name, len(groupExercise1.checkedInMemberList)))
print("Number of attendees for {} is: {}.".format(groupExercise2.name, len(groupExercise2.checkedInMemberList)))

# display the attendance percentage for groupExcercise1
print("\nAttendance percentage:")
print(f'{groupExercise1.name}: {groupExercise1.attendancePercentage():.2f}')
print(f'{groupExercise2.name}: {groupExercise2.attendancePercentage():.2f}')

# display the total payment collected for groupExercise1
print("\nTotal payment collected:")
print(f'{groupExercise1.name}: ${groupExercise1.totalPayment():.2f}')
print(f'{groupExercise2.name}: ${groupExercise2.totalPayment():.2f}')

# display the list of group exercise classes member1 is enrolled
print("\nGroup exercise classes member {} enrolled:".format(member1.name))
member1.displayBookedClass()

# display the list of classes a trainer is offering
print("\nTrainer {} offers the following classes:".format(trainer1.name))
trainer1.displayClass()













