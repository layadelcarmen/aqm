m-load
############

Python script to load air a json file with quality measures to a PostgreSQL database.


Quickstart
==========

m-load is available on PyPI and can be installed with `pip <https://pip.pypa.io>`_.

.. code-block:: console

    $ pip install -e m_load

After installing m-load you can use it like any other Python script.


To test the script use this example:

.. code-block:: console

   $ m-load --file-json URL_FILE_JSON -u <POSTGRES_USER> -a <POSTGRES_PASSWORD> -s <SERVER_HOST> 
 -p 5432 -d <DATABASE> -n <TABLENAME>

 

  -h, --help            show this help message and exit
  -t FILE_JSON, --file-json FILE_JSON
                        JSON file
  -u DB_USER, --db-user DB_USER
                        DB user
  -a DB_PASSWORD, --db-password DB_PASSWORD
                        DB password
  -s DB_HOST, --db-host DB_HOST
                        Host
  -p DB_PORT, --db-port DB_PORT
                        Connexion port
  -d DB_NAME, --db-name DB_NAME
                        DB name
  -n TABLE_NAME, --table-name TABLE_NAME
                        Table name


Further improvements:

This code solves the basic requiremets described for the Challenge in the easiest way. 
However some features could be added to improve the data quality and the process:

1) Analysis of the best matching data types in Postgres with the corresponding values in the dataframe.

2) For organizational/informational reasons would be desired the column discount after the related column old_price.
Transform function add_column_discount to use DAtaframe.insert instead, with the precalculated column discount as parameter.

3) A cleaning in some fields would be desired: Status contains some  points(.) at the end, colors are not normalized, etc.


