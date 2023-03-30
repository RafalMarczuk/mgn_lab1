
import re

class EmailExtractor:
    def __init__(self, email):
        self.email = email

    def is_student(self) -> bool:
        result = re.match("(?P<name>^[^.]+)\.(?P<surname>[^@]+)\@(?P<domain>[^.]+)", self.email)
        if result:
            if result.group('domain') == 'student':
                return True
        return False

    def is_male(self) -> bool:
        result = re.match("(?P<name>^[^.]+)\.(?P<surname>[^@]+)\@(?P<domain>[^.]+)", self.email)
        if result:
            if result.group('name').endswith('a'):
                return False
            return True

    def get_name(self):
        result = re.match("(?P<name>^[^.]+)\.(?P<surname>[^@]+)\@(?P<domain>[^.]+)", self.email)
        if result:
           return result.group('name').capitalize()
        return 'Error'

    def get_surname(self):
        result = re.match("(?P<name>^[^.]+)\.(?P<surname>[^@]+)\@(?P<domain>[^.]+)", self.email)
        if result:
            surname_string = str(result.group('surname'))
            if surname_string[-1].isdigit():
                return surname_string.capitalize()[:-2]
            return surname_string.capitalize()
        return 'Error'

wiadomosc = EmailExtractor('andrzej.babacki@student.wat.edu.pl')
wiadomosc1 = EmailExtractor('joseph.abacki@wat.edu.pl')
wiadomosc2 = EmailExtractor('anna.kabacka01@wat.edu.pl')

# print(wiadomosc.get_name())
# print(wiadomosc.get_surname())
# print(wiadomosc.is_student())
# print(wiadomosc.is_male())
# print(wiadomosc1.get_name())
# print(wiadomosc1.get_surname())
# print(wiadomosc1.is_student())
# print(wiadomosc1.is_male())
# print(wiadomosc2.get_name())
# print(wiadomosc2.get_surname())
# print(wiadomosc2.is_student())
# print(wiadomosc2.is_male())