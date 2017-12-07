# @2017, Juan E. Rolon
# https://github.com/juanerolon

#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.


import sqlite3
import os.path

class DBTaco:
    
    def __init__(self, name,path=None):
        """Initializes database (DB) object. Instantiates DB object by providing
        the name=file_name of the database file file_name.sqlite and optionally
        the file path variable path. The DB file is created if not already present 
        in the specified by path. 
        """
        
        
        if path != None:
            
            self.__db_path = path
            os.chdir(self.__db_path)
        else:
            self.__abspath = os.path.abspath(__file__)
            self.__db_path = os.path.dirname(self.__abspath)
            os.chdir(self.__db_path)
            
        
        self.__file_name = name + ".sqlite"
        
        if os.path.isfile(self.__file_name):
            print("Warning! Database {} already exists in the specified directory"\
                  .format(self.__file_name))
            self.__exists = True
        else:
            self.__exists = False
            self.__conn = sqlite3.connect(self.__file_name)           
            self.__conn.commit()
            self.__conn.close()
            
            
    def getWorkingDir(self):
        """
        Returns a string specifying the database working directory. By default
        the working directory contains the DB file and any other DB auxiliary files.
        """
        
        self.__working_dir = 'The working directory for database {dbname} is {dbpath}'.\
              format(dbname = self.__file_name, dbpath=self.__db_path)
              
        return self.__working_dir
    
    def setWorkingDir(self,path):
        """
        Manually sets the DB object working directory. By default
        the working directory contains the DB file and any other DB auxiliary files.
        """
        
        self.__db_path = path
        os.chdir(self.__db_path)
            
    def createTable(self,tname, cnames, ctypes):
        """Creates a table within the instantiated DB object. The table name is
        set as tname; the column (field) names are provided as the values of dictionary
        keys, i.e. cnmaes= {k1:col_name_1, k2:col_name_2, ..kn:col_name_n}. The data types
        (definitions) of columns are specified by a dictionary whose keys match those of 
        cnmaes, i.e. ctypes = {k1:col_type_1, k2:col_type_2, ...kn:col_type_n}
        """
        
        os.chdir(self.__db_path)
        
        self.__tname = tname
        self.__conn = sqlite3.connect(self.__file_name)
        self.__c = self.__conn.cursor()
        
        self.__col_names = cnames
        self.__col_types = ctypes
        
        self.__sorted_keys = list(self.__col_names.keys())
        self.__sorted_keys.sort()
        
        
        fieldtypes = ''
        
        for m in self.__sorted_keys:
            fieldtypes = fieldtypes + ' ' + self.__col_names[m]\
                             + ' ' + self.__col_types[m] + ','
                             
        fieldtypes = fieldtypes[1:-1]                                        
            
        
        self.__c.execute('CREATE TABLE {table_name} ({fntype})'\
                             .format(table_name=self.__tname, fntype=fieldtypes))


            
        self.__conn.commit()
        self.__conn.close()
        
    def insertRow(self, tname, cnames, data):
        """ Inserts a new row into a table with name = tname; the columns 
        to be updated are specified as the values of dictionary keys, i.e.
        cnames = {c1:col_name_1, c2:col_name_2,.. cm:col_name_m}; likewise, 
        the data entries are provided as the values of dictionary keys, i.e.
        entries = {e1:data_1, e2:data_2,... em:data_m}.
        """
        
        os.chdir(self.__db_path)
        
        self.__tname = tname
        self.__conn = sqlite3.connect(self.__file_name)
        self.__c = self.__conn.cursor()
        
        self.__col_names = cnames
        self.__col_values = data
        
        self.__sorted_keys = list(self.__col_names.keys())
        self.__sorted_keys.sort()
        
        strfields = ''
        strvalues = ''
        
        
        for m in self.__sorted_keys:
            strfields = strfields + ' ' + self.__col_names[m] + ','
            strvalues = strvalues + ' ' + self.__col_values[m] + ','
                                                       
        strfields = strfields[1:-1]  
        strvalues = strvalues[1:-1]
        
        print(self.__tname)
        print(strfields)
        print(strvalues)
            
        self.__c.execute('INSERT INTO {table_name} ({cols}) VALUES ({vals})'\
                         .format(table_name = self.__tname, cols=strfields\
                                 ,vals=strvalues))
        
        self.__conn.commit()
        self.__conn.close() 
        
    def updateCell(self, tname, colname, value, idcol, idval):
        """ Inserts or updates a table=tname with a value entered into particular cell specified
        by a given column name and row; the row is selected according to a restriction
        condition on a particular column (idcol) value (idval); i.e. update  column=colname
        with value=value for a row such that column =idcol has data entry=idval;
        """
        
        os.chdir(self.__db_path)
        
        self.__tname = tname
        self.__conn = sqlite3.connect(self.__file_name)
        self.__c = self.__conn.cursor()
        
        self.__colname = colname
        self.__value = value
        self.__idcol = idcol
        self.__idval = idval

        
        self.__c.execute('UPDATE {table_name} SET {col_name} = ({col_val}) WHERE {col_id} = ({id_val})'.\
                         format(table_name=self.__tname, col_name=self.__colname, col_val=str(self.__value),\
                                col_id=self.__idcol, id_val=str(self.__idval)))
        
        
        self.__conn.commit()
        self.__conn.close() 
        
        
    def insertColumn(self, tname, id_cname, id_type):
        """ Inserts a single new column into a database table with name = tname;
        the new column name is given by id_cname and its corresponding type (definition) is
        set by the paratmeter id_type;
        """
        os.chdir(self.__db_path)
        
        
        self.__tname = tname
        self.__conn = sqlite3.connect(self.__file_name)
        self.__c = self.__conn.cursor()
        
        self.__id_column_name = id_cname
        self.__id_column_type = id_type
        
        self.__c.execute('ALTER TABLE {table_name} ADD COLUMN {id_col_name} {id_col_type}'.\
                         format(table_name = self.__tname, id_col_name = self.__id_column_name,\
                                id_col_type = self.__id_column_type))
        
        
        self.__conn.commit()
        self.__conn.close() 
        
    def setAsIndex(self,tname,indexname,colnames):
        """ Description
        """
        self.__tname = tname
        self.__index_name = indexname
        self.__col_names = colnames
        
        self.__sorted_keys = list(self.__col_names.keys())
        self.__sorted_keys.sort()
        
          
        sfields = ''
       
        for m in self.__sorted_keys:
            sfields = sfields + ' ' + self.__col_names[m] + ','
                                                       
        sfields = sfields[1:-1]  
              
        self.__conn = sqlite3.connect(self.__file_name)
        self.__c = self.__conn.cursor()
        
        self.__c.execute('CREATE INDEX {iname} ON {table_name} ({columns})'.\
                         format(iname = self.__index_name, table_name=self.__tname,\
                                columns = sfields ))
        
        self.__conn.commit()
        self.__conn.close() 
        
        
if __name__ == "__main__":
    
    db = DBTaco("mongol")
    db2 = DBTaco("chukchi", "/Users/juanerolon/Dropbox/")
    
    nmd = {1:'col1', 2:'col2'}
    tpd = {1:'INTEGER', 2:'INTEGER'}
    valx = {1:3500, 2:7000}


    db.getWorkingDir()
    db2.getWorkingDir()
    
    #db2.createTable('Customers2', {1:'ID', 2:'Name'}, {1:'INTEGER PRIMARY KEY', 2:'TEXT'})
    
    #db2.insertColumn('Customers', 'PIDw', 'INTEGER')
    #db2.setAsIndex('Customers', 'Identity', {1:'PIDw'})
    db2.insertRow('Customers2', {1:'Name'}, {1:'"Frankie"'})
    
    
    
    #db.createTable('SOME_TABLE',nmd, tpd)
    
    #db.insertColumn('SOME_TABLE', 'franks', 'TEXT')
    
    #db.insertRow('SOME_TABLE', nmd,valx)
    #db.updateCell('SOME_TABLE', 'col1', 777,'col2',1000)
    
    
    






