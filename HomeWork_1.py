import datetime


class Logger

    def __init__(self, log_path, encoding='utf-8')
        self.log_file = open(log_path, 'a', encoding=encoding)

    def __enter__(self)
        self.start_time = datetime.datetime.utcnow()
        return self

    def write_log(self, action)
        self.log_file.write(f'{datetime.datetime.utcnow()} {action}n')

    def __exit__(self, exc_type, exc_val, exc_tb)
        if exc_type is not None
            self.write_log(f'error {exc_val}')
            self.write_log('end')
        end_time = datetime.datetime.utcnow() - self.start_time
        self.log_file.write(f'Время, потраченное на выполнение кода {end_time}n')
        self.log_file.close()


cook_book = [
    ['салат',
     [
         ['картофель', 100, 'гр.'],
         ['морковь', 50, 'гр.'],
         ['огурцы', 50, 'гр.'],
         ['горошек', 30, 'гр.'],
         ['майонез', 70, 'мл.'],
     ]
     ],
    ['пицца',
     [
         ['сыр', 50, 'гр.'],
         ['томаты', 50, 'гр.'],
         ['тесто', 100, 'гр.'],
         ['бекон', 30, 'гр.'],
         ['колбаса', 30, 'гр.'],
         ['грибы', 20, 'гр.'],
     ],
     ],
    ['фруктовый десерт',
     [
         ['хурма', 60, 'гр.'],
         ['киви', 60, 'гр.'],
         ['творог', 60, 'гр.'],
         ['сахар', 10, 'гр.'],
         ['мед', 50, 'мл.'],
     ]
     ]
]

person = 5


def cook_book_list()

    for cooking in cook_book
        print((cooking[0].capitalize()), '', end='')
        print()
        for eat in cooking[1]
            print(f'{eat[0]}, {eat[1]  person},{eat[2]}')


if __name__ == '__main__'
    with Logger('my.log') as log
        log.write_log('Начало рабты')
        cook_book_list()
        log.write_log('конец')



