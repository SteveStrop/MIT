import datetime


class Person:
    def __init__(self, name):
        """ create a person called name"""
        self.name = name
        self.birthday = None
        self.last_name = name.split()[-1]

    def get_last_name(self):
        """ return self's last name"""
        return self.last_name

    def __str__(self):
        """return self's name"""
        return self.name

    def set_Birthday(self, month, day, year):
        """set self's birthday to birth date"""
        self.birthday = datetime.date(year, month, day)

    def get_age(self):
        """ return self's current age"""
        if self.birthday is None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):  # implements sort method
        """ return True if self's name appears first in alphabet"""
        if self.last_name == other.last_name:
            return self.name < other.name
        return self.last_name < other.last_name


class MITPerson(Person):
    id_num = 0

    def __init__(self, name):
        Person.__init__(self, name)
        self.iD_num = MITPerson.id_num
        MITPerson.id_num += 1

    def get_iD_str(self):
        """ return string representation of id number"""
        return str(self.iD_num).zfill(3)

    def get_iD_num(self):
        """ return integer representation of id number"""
        return self.iD_num

    def __lt__(self, other):
        return self.iD_num < other.iD_num

    def speak(self, utterance):
        return f"{self.get_last_name()} says {utterance}"


m3 = MITPerson('Mark Zukerberg')
Person.set_Birthday(m3, 5, 14, 84)
m2 = MITPerson('Drew Houston')
Person.set_Birthday(m2, 3, 4, 83)
m1 = MITPerson('Bill Gates')
Person.set_Birthday(m1, 10, 28, 55)
person_list = [m1, m2, m3]

print(*person_list, sep='\n')
person_list.sort()
print(*person_list, sep='\n')
