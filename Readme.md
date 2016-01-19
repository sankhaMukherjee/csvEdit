# csvEdit: Web-based configuration utility in Python 

## What is it?

This is a tiny Python module that can be used for keeping track of data and configuration files, which were perviously kept in Excel or .csv files using the bottle web framework. Just convert your Excel files to .csv files and use this utility to provide for a clear web interface that will allow you to keep track of these files. 

### Main Features

1. Simple to set up. Just copy whatever .csv files you have to the designated folder, edit the dictionaty within `main.py` to include all the files you want to save, and you are up-and-running. 
2. The current version creates a `localhost` server. It should not be too much of an effort to provide an IP adress so anyone can access the service.

### Dependencies

 - [Python](https://www.python.org)
 - [Pandas](https://github.com/pydata/pandas) (Python panel document manipulation)
 - [Bottle](http://bottlepy.org/docs/dev/index.html#) (Python Web Framework)
 - [jQuery](https://jquery.com) (Javascripting made easy)
 - [sort](http://tablesorter.com/docs/) (Javascript utility for easily sorting items within an HTML table)
 - [Multifilter](http://www.jqueryscript.net/table/jQuery-Plugin-To-Filter-Html-Table-with-Multiple-Criteria-multifilter.html) (Javascript utility for easily filtering items within an HTML table)

## License

BSD

## Documentation

Download this folder into a directory of your chocie, open a terminal, change to the folder and type 

```bash
$ python main.py
```

You should see the following WSGI session start ...

```bash
Bottle v0.13-dev server starting up (using WSGIRefServer())...
Listening on http://localhost:8080/
Hit Ctrl-C to quit.

```

Now open your favourite browser and load the following location `http://localhost:8080/config` 

You should be able to see the following HTML message

```html
Please select the page you want to see ...

The following are links to the values that you may wish to view/configure.

test
```

Note that a `test.csv` file has been added in the `config\data` folder. All configuration files can be placed in this folder, or any other folder of choice. These new files must be added in the new program in the dictionary in the file `main.py`

Currently, it only contains the single entry:

```python
    configFiles = {
        'test'  : 'config/data/test.csv',
    }
```

This dictionary needs to be edited to include other files to edit ...
