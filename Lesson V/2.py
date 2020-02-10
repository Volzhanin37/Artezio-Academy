class Student(object):

    def __init__(self, name, conf=None):
        if conf is None:
            conf = {
                'exam_max': 30,  # кол. баллов, доступное за сдачу экзамена
                'lab_max': 7,  # кол. баллов, за выполнение 1 практич. работы
                'k': 0.61,  # доля баллов для получения сертификата
                'lab_num': 10  # кол. практических работ в курсе
            }
        self.name = name
        self.conf = conf
        self.lab_points = [0] * conf['lab_num']

    def make_lab(self, m, n=None):
        if 0 <= m <= self.conf['lab_max']:  # не учитываем сбои в системе
            if (n is not None) and 1 <= n <= self.conf['lab_num']:
                # номер указан, не учитываем дополнительные задачи
                self.lab_points[n - 1] = m
            elif n is None:  # обработка вызова без номера задачи
                for i in range(self.conf['lab_num']):
                    if self.lab_points[i] == 0:
                        self.lab_points[i] = m
                        break
        return self

    def make_exam(self, m):
        if 0 <= m <= self.conf['exam_max']:  # не учитываем сбои в системе
            self.exam_points = m
        return self

    def is_certified(self):
        self.all_points = sum(self.lab_points) + self.exam_points
        self.is_enough = self.all_points >= self.conf['k'] * (
                         self.conf['lab_num'] * self.conf['lab_max'] +
                         self.conf['exam_max'])
        return self.all_points, self.is_enough


# Ivan = Student('Ivan')
# Ivan.make_lab(5, 1)
# Ivan.make_lab(10, 1)
# Ivan.make_lab(5, 11)
# Ivan.make_lab(7)
# Ivan.make_lab(7, 9)
# Ivan.make_exam(30)
# Ivan.make_exam(50)
# print(Ivan.lab_points)
# print(Ivan.is_certified())
