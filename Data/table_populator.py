import random
import numpy as np
from numpy.random import SeedSequence
from configparser import ConfigParser
import psycopg2

# Function copied from
# gist.github.com/ZacharyMcGuire/d81aa85409594a007fdf80e9fa9b329e

def config(filename='database.ini', section = 'postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db_config = {}

    if section in parser:
        for key in parser[section]:
            db_config[key] = parser[section][key]

    return db_config

def connect_to_database():
    db_config = config()
    return psycopg2.connect(
        dbname = db_config['dbname'],
        user = db_config['user'],
        host = db_config['host'],
        password = db_config['password'],
        port = db_config['port']
    )

def get_cursor(conn):
    return conn.cursor()

def execute_sql(cursor, sql):
    cursor.execute(sql)

PORTFOLIO_FILE = 'portfolio.csv'

PORTFOLIO_TABLE_NAME = 'Stock_Investments'

PORTFOLIO_TUPLE_VARIANT_SUBSTRING = ''

PORTFOLIO_VARIANCE_VARIANT_SUBSTRING = 'Volatility'
PORTFOLIO_LAMBDA_VARIANT_SUBSTRING = 'Volatility_Lambda'

PORTFOLIO_TUPLE_VARIATION_SUBSTRINGS = ['100', '95', '90', '85', '80', '75', '70', 
                              '65', '60', '55', '50', '45', '40', '35',
                              '30', '25', '20', '15', '10', '5']

PORTFOLIO_TUPLE_VARIATIONS = [100, 95, 90, 85, 80, 75, 70, 
                              65, 60, 55, 50, 45, 40, 35,
                              30, 25, 20, 15, 10, 5]

portfolio_attributes = [
    'id',
    'ticker',
    'sell_after',
    'price',
    'volatility',
    'volatility_coeff',
    'drift'
]

portfolio_index = {
    'ticker' : 0,
    'price' : 1,
    'volatility' : 2,
    'drift' : 3
}

INIT_SEED = SeedSequence(2342123)
rng = np.random.default_rng(INIT_SEED)

def create_portfolio_tuple_variant_datasets(
        interval, interval_string, cursor
):
    table_name = PORTFOLIO_TABLE_NAME + '_' + interval_string
    is_first_line = True
    row_number = 0
    for line in open(PORTFOLIO_FILE, 'r').readlines():
        if is_first_line:
            is_first_line = False
        else:
            values = line.split(',')
            sell_after = 0
            while sell_after < 730:
                sell_after += interval
                tuple = dict()
                for attribute in portfolio_attributes:
                    if attribute == 'id':
                        tuple[attribute] = str(row_number)
                        row_number += 1
                    if attribute in portfolio_index:
                        if attribute == 'ticker':
                            tuple[attribute] = "'" + \
                                str(values[portfolio_index[attribute]])\
                                + "'"
                        else:
                            tuple[attribute] = str(values[
                                portfolio_index[attribute]])
                    if attribute == 'sell_after':
                        tuple[attribute] = str(sell_after)
                    if attribute == 'volatility_coeff':
                        tuple[attribute] = str(1)
                values_string = ''
                for attribute in tuple:
                    if len(values_string) > 0:
                        values_string += ', '
                    values_string += tuple[attribute]
                sql_command = "INSERT INTO " + table_name + " VALUES (" + \
                values_string + ");"
                execute_sql(cursor, sql_command)
    print('Populated', table_name)

def create_portfolio_volatility_variant_datasets(
        volatility_coeff, volatility_coeff_string, cursor
):
    table_name = PORTFOLIO_TABLE_NAME + '_' + PORTFOLIO_VARIANCE_VARIANT_SUBSTRING \
        + '_' + volatility_coeff_string
    is_first_line = True
    row_number = 0
    interval = 90
    for line in open(PORTFOLIO_FILE, 'r').readlines():
        if is_first_line:
            is_first_line = False
        else:
            values = line.split(',')
            sell_after = 0
            while sell_after < 730:
                sell_after += interval
                tuple = dict()
                for attribute in portfolio_attributes:
                    if attribute == 'id':
                        tuple[attribute] = str(row_number)
                        row_number += 1
                    if attribute in portfolio_index:
                        if attribute == 'ticker':
                            tuple[attribute] = "'" + \
                                str(values[portfolio_index[attribute]])\
                                + "'"
                        else:
                            tuple[attribute] = str(values[
                                portfolio_index[attribute]])
                    if attribute == 'sell_after':
                        tuple[attribute] = str(sell_after)
                    if attribute == 'volatility_coeff':
                        tuple[attribute] = str(volatility_coeff)
                values_string = ''
                for attribute in tuple:
                    if len(values_string) > 0:
                        values_string += ', '
                    values_string += tuple[attribute]
                sql_command = "INSERT INTO " + table_name + " VALUES (" + \
                values_string + ");"
                execute_sql(cursor, sql_command)
    print('Populated', table_name)

def create_portfolio_volatility_coeff_variant_datasets(
        volatility_coeff, volatility_coeff_string, cursor
):
    table_name = PORTFOLIO_TABLE_NAME + '_' + PORTFOLIO_LAMBDA_VARIANT_SUBSTRING \
        + '_' + volatility_coeff_string
    volatility_coeffs = rng.exponential(scale = (1/volatility_coeff),
                                              size = 3457*730*2)
    is_first_line = True
    row_number = 0
    interval = 0.5
    for line in open(PORTFOLIO_FILE, 'r').readlines():
        if is_first_line:
            is_first_line = False
        else:
            values = line.split(',')
            sell_after = 0
            while sell_after < 730:
                sell_after += interval
                tuple = dict()
                for attribute in portfolio_attributes:
                    if attribute == 'id':
                        tuple[attribute] = str(row_number)
                    if attribute in portfolio_index:
                        if attribute == 'ticker':
                            tuple[attribute] = "'" + \
                                str(values[portfolio_index[attribute]])\
                                + "'"
                        else:
                            tuple[attribute] = str(values[
                                portfolio_index[attribute]])
                    if attribute == 'sell_after':
                        tuple[attribute] = str(sell_after)
                    if attribute == 'volatility_coeff':
                        tuple[attribute] = str(volatility_coeffs[row_number])
                values_string = ''
                for attribute in tuple:
                    if len(values_string) > 0:
                        values_string += ', '
                    values_string += tuple[attribute]
                row_number += 1
                sql_command = "INSERT INTO " + table_name + " VALUES (" + \
                values_string + ");"
                execute_sql(cursor, sql_command)
    print('Populated', table_name)



conn = connect_to_database()
cursor = get_cursor(conn)

for _ in range(len(PORTFOLIO_TUPLE_VARIATIONS)):
    create_portfolio_tuple_variant_datasets(
        PORTFOLIO_TUPLE_VARIATIONS[_],
        PORTFOLIO_TUPLE_VARIATION_SUBSTRINGS[_],
        cursor
    )

print('Populated portfolio relations with different number of tuples')



conn.commit()
cursor.close()
conn.close()
