#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import psycopg2
from sqlalchemy import create_engine

import requests


#url_json = "https://data.cdc.gov/api/views/cjae-szjv/rows.json"

def get_column_names(cols):
    colums_name = []
   
    for index in range(len(cols)):
        colums_name += [cols[index]['fieldName']]
    return colums_name


def load_json_2_dataframe(url_json):
    '''Load CSV file in a pandas Dataframe'''
    resp_json = requests.get(url_json).json()
    cols = get_column_names(resp_json['meta']['view']['columns'])
    df = pd.DataFrame(resp_json['data'], columns=cols)
    return df


def convert_str2float(df,column):
    df[column] = df[column].astype('float')
    return df


def convert_str2int32(df,column):
    df[column] = df[column].astype('int32')
    return df


def trans_columns(df):
    convert_str2int32(df, 'measureid')
    convert_str2int32(df, 'statefips')
    convert_str2int32(df, 'countyfips')
    convert_str2int32(df, 'reportyear')
    convert_str2float(df, 'value')
    return df   


def save_to_db(df, engine, table_name):
    try:
        df.to_sql('measures_air_quality', con=engine, if_exists='replace')
    except psycopg2.Error as e:
        print('Unable to connect!')
        print(e.pgerror)
        print(e.diag.message_detail)
        sys.exit(1)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--file-measures",
                        help="JSON file with air quality measures")
    parser.add_argument("-u", "--db-user",
                        default="postgres",
                        help="DB user")
    parser.add_argument("-a", "--db-password",
                        default="postgres",
                        help="DB password")
    parser.add_argument("-s", "--db-host",
                        default="localhost",
                        help="Host")
    parser.add_argument("-p", "--db-port",
                        default="5432",
                        help="Connexion port")
    parser.add_argument("-d", "--db-name",
                        default="Tests",
                        help="DB name")
    parser.add_argument("-n", "--table-name",
                        default="product",
                        help="Table name")                                                                                                                                                                 
    args = parser.parse_args()

    db_url = f'postgresql://{args.db_user}:{args.db_password}@{args.db_host}:{args.db_port}/{args.db_name}'
    engine = create_engine(db_url, echo=False)

    data = load_json_2_dataframe(args.file_measures)

    trans_columns(data)

    save_to_db(data, engine, args.table_name)      
    print("Measures imported sucessfull!")


if __name__ == '__main__':
    main()