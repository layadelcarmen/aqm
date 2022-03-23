#!/usr/bin/env python
# coding: utf-8

import psycopg2


def executeScriptsFromFile(filename, cursor):
    '''Execute SQL create views'''
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()

    sqlCommands = sqlFile.split(';')

    for command in sqlCommands:
        try:
            print(command)
            cursor.execute(command)
        except psycopg2.Error as e:
            print("Command skipped: ", e.pgerror)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file-script-sql",
                    help="File with SQL comands ; separated")
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
    args = parser.parse_args()

    conn = psycopg2.connect(
    database=args.db_name, user=args.db_user, password=args.db_password, host=args.db_host, port=int(args.db_port)
    )
    conn.autocommit = True
    cursor_c = conn.cursor()

    executeScriptsFromFile(args.file_script_sql, cursor_c)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()