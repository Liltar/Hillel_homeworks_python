import csv
import argparse


def check_arguments(arguments):
    arg_dict = {'BRAND': arguments.brand, 'COLOR': arguments.color,
                'MAKE_YEAR': arguments.year, 'FUEL': arguments.fuel,
                'N_REG_NEW': arguments.reg_num}
    arg_dict = {key: value for key, value in arg_dict.items() if value is not None}
    if len(arg_dict) == 1:
        return arg_dict
    else:
        raise SystemExit('No optional arguments!')


def read_csv(file):
    with open('tz_opendata_z01012020_po01122020.csv', 'r', encoding='utf-8') as f:
        csv_file = csv.DictReader(f, delimiter=';')
        result = []
        for row in csv_file:
            if row['BRAND'] == args_dict['brand'] and \
                row['COLOR'] == args_dict['color'] and \
                    row['MAKE_YEAR'] == args_dict['year']:
                result.append(row)
    return write_in_csv(result)


def write_in_csv(result):
    file_name = '-'.join(args_dict.values()) + '.csv'
    with open(file_name, 'w', newline='') as cvsresult:
        headers = ['D_REG', 'BRAND', 'MODEL', 'MAKE_YEAR', 'COLOR',
                   'N_REG_NEW']
        csv_writer = csv.DictWriter(cvsresult, fieldnames=headers)
        csv_writer.writeheader()
        csv_writer.writerows(result)
        print(f'Writed to {file_name}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Transport Registry')
    parser.add_argument('o', help='Enter the file name in cvs format')
    parser.add_argument('--brand', help='Enter the brand')
    parser.add_argument('--color', help='Enter the color')
    parser.add_argument('--year', help='Enter the year make')
    parser.add_argument('--fuel', help='Enter the fuel type')
    parser.add_argument('--reg_num', help='Enter the licence plate')
    arguments = parser.parse_args()
    args_dict = check_arguments(arguments)
    read_csv(arguments.o)
