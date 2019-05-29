import pandas as pd

def output_reader(outputFilename):
    '''
    Process output from `tap-b` and returns resulting DataFrame and total system travel time TSTT
    '''
    df = pd.read_csv("tap-b/full_log.txt", sep=' ', index_col=0, skiprows=2, header=None, names=[
        'ID',
        'OD',
        'flow',
        'cost',
        'der'
    ])
    return df, df['cost'].sum()
