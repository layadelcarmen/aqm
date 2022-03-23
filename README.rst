measures-load

############

Python scripts to load air quality measure json file into a PostgreSQL database, 
and create some interesting views to inspect data.


Quickstart
==========

measures-load is available on PyPI and can be installed with `pip <https://pip.pypa.io>`_.

.. code-block:: console

    $ pip install -e measure-load

After installing, two scripts will be available in the command line: 

1.- m-load: Load measure file.

.. code-block:: console

   $ m-load --file-json URL_FILE_JSON -u <POSTGRES_USER> -a <POSTGRES_PASSWORD> -s <SERVER_HOST> 
 -p 5432 -d <DATABASE> -n <TABLENAME>

 Example to mload with default file location:

.. code-block:: console

$ m-load --file-json https://data.cdc.gov/api/views/cjae-szjv/rows.json -u <POSTGRES_USER> -a <POSTGRES_PASSWORD> -s <SERVER_HOST> 
 -p 5432 -d <DATABASE> 

* use the default TABLENAME air_quality_measures to test properly the sql_script.



2.- r-views: Create some SQL views in the database 

Check SQL views 
 
   $ r-views --file-script-sql PATH_CREATE_VIEWS -u <POSTGRES_USER> -a <POSTGRES_PASSWORD> -s <SERVER_HOST> 
 -p 5432 -d <DATABASE>


The sql script file is available sql_script/create_views_measures.sql in the same repo.
An aditional script to drop the views is also available.



Further improvements:

- Expose view's results using a REST_API

