m-load
############

Python script to load air a json file with quality measures to a PostgreSQL database.


Quickstart
==========

m-load is available on PyPI and can be installed with `pip <https://pip.pypa.io>`_.

.. code-block:: console

    $ pip install -e measure-load

After installing two scrpits are available in the command line: 

> m-load: Load measure file.

> r-views: Create the SQL questions as views in the database 


.. code-block:: console

   $ m-load --file-json URL_FILE_JSON -u <POSTGRES_USER> -a <POSTGRES_PASSWORD> -s <SERVER_HOST> 
 -p 5432 -d <DATABASE> -n <TABLENAME>

Running with default file location:

$ m-load --file-json https://data.cdc.gov/api/views/cjae-szjv/rows.json -u <POSTGRES_USER> -a <POSTGRES_PASSWORD> -s <SERVER_HOST> 
 -p 5432 -d <DATABASE> -n <TABLENAME>

* use the default TABLENAME air_quality_measures to test properly the sql_script.

Check SQL views 
 
   $ r-views --file-script-sql PATH_CREATE_VIEWS -u <POSTGRES_USER> -a <POSTGRES_PASSWORD> -s <SERVER_HOST> 
 -p 5432 -d <DATABASE>


The sql script file is available sql_script/create_views_measures.sql in the same repo.
 

Further improvements:

- Expose view results using a REST _API


