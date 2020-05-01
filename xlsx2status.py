# Заполняем поле статуса в монго конвертируя его из Excel

import sys
from _datetime import datetime, timedelta, date
import time
import os
from mysql.connector import MySQLConnection, Error
from collections import OrderedDict
import openpyxl
from pymongo import MongoClient
import psycopg2
import argparse

from lib import read_config, s, l
from api_statuses import EVA_STATUS
from raif import raif
from keb import keb

# Обрабатываем только эти варианты
PRODUCTS = ['keb', 'raif']

def filter_x00(inp):
    inp = s(inp)
    inp = inp.replace('_x0020_',' ')
    inp = inp.replace('_X0020_',' ')
    while inp.upper().find('_X0') > -1:
        if inp.find('_x0') > -1:
            inp = inp.split('_x0')[0] + inp.split('_x0')[1].split('_')[1]
        else:
            inp = inp.split('_X0')[0] + inp.split('_X0')[1].split('_')[1]
    return inp

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Импорт статусов в Еву из .xlsx (Excel-2007) файлов', add_help=True)
    parser.add_argument('product', type=str, choices=PRODUCTS, help='продукт или продуктовая сеть')
    parser.add_argument('-d', '--dir', dest='dir', action='store', type=str, default='.',
                        help='путь к файлам со статусами')
    parser.add_argument('-f', '--file', dest='file', action='store', type=str, default=None,
                        help='обработать только этот файл')
    args = parser.parse_args()
    if args.file:
        if not str(args.file).endswith('.xlsx') and not os.path.exists(args.file):
            print(args.file, ' - файл отсутствует или не .xlsx '
                             'Укажите путь и имя существующего .xlsx (Excel-2007) файла')
            sys.exit()
    if args.dir != '.':
        if not os.path.exists(args.dir):
            print(args.dir, ' - директория отсутствует. Укажите путь к существующей директории')
            sys.exit()

    # Создаем директории загруженных файлов-логов для всех продуктов
    for product in PRODUCTS:
        if not os.path.exists('loaded' + product.upper() + '/'):
            os.mkdir('loaded' + product.upper() + '/')

    # подключаемся к серверу
    cfg = read_config(filename='status.ini', section='Mongo')
    conn = MongoClient('mongodb://' + cfg['user'] + ':' + cfg['password'] + '@' + cfg['ip'] + ':' + cfg['port'] + '/'
                       + cfg['db'])
    # выбираем базу данных
    db = conn.saturn_v
    # выбираем коллекцию документов db.Products

    # Вызываем функцию с именем модуля
    locals()[locals()['args'].product](args.product, db.Products, args.dir, file=args.file)


