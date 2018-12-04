from collections import namedtuple

Module = namedtuple('Module', 'module title ects')

CA1_MODULES = {'CA103': Module('CA103', 'Computer Systems', 5),
               'CA106': Module('CA106', 'Web Design', 5),
               'CA115': Module('CA115', 'Digital Innovation', 5),
               'CA116': Module('CA116', 'Computer Programming I', 10),
               'CA117': Module('CA117', 'Computer Programming II', 10),
               'CA169': Module('CA169', 'Networks and Internet', 5),
               'CA170': Module('CA170', 'Operating Systems', 5),
               'CA172': Module('CA172', 'Problem Solving', 5),
               'MS121': Module('MS121', 'IT Mathematics', 10)}

class Student(object):

    def __init__(self, idnum, surname, firstname, mods=CA1_MODULES):
        self.__idnum = idnum
        self.__surname = surname
        self.__firstname = firstname
        self.__mods = mods
        self.__marks = {module: 0 for module in self.__mods.keys()}

    def __str__(self):
        name = '{} : {} {}'.format(self.__idnum,
                                   self.__firstname,
                                   self.__surname)
        uline = '-' * len(name)
        results =  '\n'.join([module + ' : ' + self.__mods[module].title +
                              ' : ' + str(self.__marks[module])
                              for module in sorted(self.__mods.keys())])
        precision_mark = 'Precision mark: {:.2f}'.format(self.precision_mark())
        if self.passed():
            outcome = 'Pass'
        elif self.passed_by_compensation():
            outcome = 'Pass by compensation'
        else:
            outcome = 'Fail'

        return '\n'.join([name, uline, results, precision_mark, outcome])

    def add_mark(self, module, mark):
        self.__marks[module] = int(mark)
        
    def precision_mark(self):
        precision_mark = 0
        total = 0
        for module in self.__marks:
            total += int(self.__mods[module][2])
            precision_mark += int(self.__mods[module][2]) * (self.__marks[module] / 100) 


        return (precision_mark / total) * 100

    def passed(self):
        self.__failed_mods = [module for module in self.__marks if int(self.__marks[module]) < 40]
        return len(self.__failed_mods) == 0

    def passed_by_compensation(self):
        if self.precision_mark() < 45:
            return False

        self.__failed_mods = [module for module in self.__marks if int(self.__marks[module]) < 40]
        credits_failed = 0
        total = 0
        for module in self.__mods:
          total += int(self.__mods[module][2])
          if module in self.__failed_mods:
            credits_failed += int(self.__mods[module][2])

        if (credits_failed * 6) > total:
          return False

        self.__failed = [module for module in self.__marks if int(self.__marks[module]) < 35]
        return not len(self.__failed)