class Complex(object):

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return (Complex(format(self.re + other.re, '.2f'),
                        format(self.im + other.im, '.2f')))

    def __sub__(self, other):
        return (Complex(format(self.re - other.re, '.2f'),
                        format(self.im - other.im, '.2f')))

    def __mul__(self, other):
        return (Complex(format(self.re * other.re - self.im * other.im, '.2f'),
                format(self.re * other.im + self.im * other.re, '.2f')))

    def __truediv__(self, other):
        return (Complex(format((self.re * other.re + self.im * other.im) /
                               (other.re ** 2 + other.im ** 2), '.2f'),
                        format((self.im * other.re - self.re * other.im) /
                               (other.re ** 2 + other.im ** 2), '.2f')))

    def __abs__(self):
        return (Complex(format((self.re ** 2 +
                self.im ** 2) ** (1 / 2), '.2f'), '0.00'))

    def alg(self):  # возвращает запись комплексного числа в алгебраич. форме
        return (self.re + '+' + self.im + 'j' if float(self.im) >= 0
                else self.re + self.im + 'j')


def complex_number_operations(a, b):
    return ((a + b).alg(),
            (a + b).alg(),
            (a * b).alg(),
            (a / b).alg(),
            abs(a).alg(),
            abs(b).alg())


a = Complex(*list(map(float, input().split())))
b = Complex(*list(map(float, input().split())))

for i in complex_number_operations(a, b):
    print(i, end='\n')
