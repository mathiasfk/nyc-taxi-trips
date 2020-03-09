import json
import csv
from pathlib import Path
import mysql.connector as mariadb
import urllib.request

def main():
    connection = mariadb.connect(user='root', password='',  allow_local_infile=True)
    cursor = connection.cursor()
    connection.autocommit = True

    # Baixa o dataset
    download_file('https://s3.amazonaws.com/data-sprints-eng-test/data-payment_lookup-csv.csv','datasets/data-payment_lookup-csv.csv')
    download_file('https://s3.amazonaws.com/data-sprints-eng-test/data-vendor_lookup-csv.csv','datasets/data-vendor_lookup-csv.csv')
    download_file('https://s3.amazonaws.com/data-sprints-eng-test/data-sample_data-nyctaxi-trips-2009-json_corrigido.json','datasets/data-sample_data-nyctaxi-trips-2009-json_corrigido.json')
    download_file('https://s3.amazonaws.com/data-sprints-eng-test/data-sample_data-nyctaxi-trips-2010-json_corrigido.json','datasets/data-sample_data-nyctaxi-trips-2010-json_corrigido.json')
    download_file('https://s3.amazonaws.com/data-sprints-eng-test/data-sample_data-nyctaxi-trips-2011-json_corrigido.json','datasets/data-sample_data-nyctaxi-trips-2011-json_corrigido.json')
    download_file('https://s3.amazonaws.com/data-sprints-eng-test/data-sample_data-nyctaxi-trips-2012-json_corrigido.json','datasets/data-sample_data-nyctaxi-trips-2012-json_corrigido.json')

    # Cria o banco e tabelas
    execute_sql_file(cursor, absolute_path('sql/structures.sql'))

    # Converte os arquivos para facilitar a inserção no MySQL
    json_to_csv(cursor, absolute_path('datasets/data-sample_data-nyctaxi-trips-2009-json_corrigido.json'), absolute_path('datasets/trips_2009.csv'))
    json_to_csv(cursor, absolute_path('datasets/data-sample_data-nyctaxi-trips-2010-json_corrigido.json'), absolute_path('datasets/trips_2010.csv'))
    json_to_csv(cursor, absolute_path('datasets/data-sample_data-nyctaxi-trips-2011-json_corrigido.json'), absolute_path('datasets/trips_2011.csv'))
    json_to_csv(cursor, absolute_path('datasets/data-sample_data-nyctaxi-trips-2012-json_corrigido.json'), absolute_path('datasets/trips_2012.csv'))

    # Carrega os dados no banco
    load_csv(cursor, absolute_path('datasets/trips_2009.csv'), 'trips')
    load_csv(cursor, absolute_path('datasets/trips_2010.csv'), 'trips')
    load_csv(cursor, absolute_path('datasets/trips_2011.csv'), 'trips')
    load_csv(cursor, absolute_path('datasets/trips_2012.csv'), 'trips')

    # Carrega as tabelas auxiliares
    load_csv(cursor, absolute_path('datasets/data-payment_lookup-csv.csv'), 'payment_lookup', line_terminator='\r\n', ignore_lines=2)
    load_csv(cursor, absolute_path('datasets/data-vendor_lookup-csv.csv'), 'vendor_lookup', enclosed_by='"', ignore_lines=1)

    cursor.close()
    connection.close()


def execute_sql_file(cursor, path):
    print('Executing ',path,'...')
    with open(path) as f:
        commands = f.read().split(';')

    for command in commands:
        cursor.execute(command)

def load_csv(cursor, path_csv, table, enclosed_by=False,line_terminator=False, ignore_lines=False):

    enclosed_by = (' enclosed by \'' + enclosed_by + '\'') if enclosed_by else ''
    line_terminator = ('lines terminated by \'' + line_terminator + '\'') if line_terminator else ''
    ignore_lines = ('ignore ' + str(ignore_lines) + ' lines') if ignore_lines else ''

    load_data = """
    load data local infile '%s'
    into table nyctaxi.%s 
    fields terminated by ',' %s
    %s %s
    """
    print(load_data % (path_csv, table, enclosed_by, line_terminator, ignore_lines))
    cursor.execute(load_data % (path_csv, table, enclosed_by, line_terminator, ignore_lines))

def json_to_csv(cursor, path_json, path_csv):
    print('Converting ' + path_json + '...')
    with open(path_csv, 'w') as csv_file:
        writer = csv.writer(csv_file) #  quotechar='"',quoting=csv.QUOTE_ALL

        with open(path_json) as json_file:
            for line in json_file:
                json_obj = json.loads(line)
                writer.writerow(list(json_obj.values()))

def download_file(url, path):
    print('Downloading ' + url + '...')
    urllib.request.urlretrieve(url, path)

def absolute_path(relative_path):
    return str(Path(relative_path).absolute())

if __name__ == "__main__":
    main()

