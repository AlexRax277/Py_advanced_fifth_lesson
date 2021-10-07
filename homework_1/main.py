import time
from hashlib import md5


def decorator_foo(path_to_log_file):
    def decorator_logger(old_foo):
        def new_foo(argument):
            data = {'time_call_foo': time.ctime(), 'result': old_foo(argument), 'foo_name': old_foo.__name__,
                    'foo_argument': argument}
            with open(path_to_log_file, 'a', encoding='utf-8') as f:
                for key, val in data.items():
                    f.write(f'{key}: {val}\n')
            return data
        return new_foo
    return decorator_logger


@decorator_foo('log.json')
def my_gen(file):
    with open(file, 'r', encoding='utf-8') as f:
        read_line = f.readlines()
        number_str = 0
    while number_str < len(read_line):
        data = md5(read_line[number_str].encode())
        hash_1 = data.hexdigest()
        print(f'Хэш строки № {number_str} = {hash_1}')
        yield number_str
        number_str += 1
    return None


if __name__ == '__main__':
    for string in my_gen('result.json'):
        print(my_gen('result.json'))















