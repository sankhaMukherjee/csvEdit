import os, time, csv
import pandas as pd 

def configFiles():
    files = [f for f in os.listdir('config/data') if f.endswith('.csv')]
    files = [os.path.join(os.path.abspath('.'), 'config', 'data', f) for f in files]
    return files

def configRead(fileName):
    '''
        This reads a condifuration file and returns the'
        values within it.
    '''
    
    with open(fileName) as f: 
        data = list(csv.reader(f))

    return pd.DataFrame(data)

def configWrite(fileName, data, backup=True, headerPrint=False):
    '''
        This function recreates a configuration file, given 
        a particular configuration information provided. It can 
        also automatically back up a particular configuration file 
    '''

    currTime = time.asctime().replace(':', '-')

    if os.path.exists(fileName) and backup:
        os.rename(fileName, fileName+'.backup.'+currTime)

    data.to_csv( fileName, index=False, header=headerPrint )
    
    return

def htmlToDf(data):
    '''
        The easiest way of dealing with csv files is to 
    '''
    data = '<table>' + data + '</table>'
    data = pd.read_html(data)
    data = data[0].ix[:, 2:]

    return data

if __name__ == '__main__':
    
    files = configFiles()
    print configRead(files[0])
    print configWrite(files[0], configRead(files[0]))