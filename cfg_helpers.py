from datetime import date, timedelta



def get_all_mondays(year, month):
    '''
    Inputs
    
    Outputs
    '''
    d = date(year, month, 1)                    
    d += timedelta(days = 7 - d.weekday())  
    while d.month == month:
        yield d
        d += timedelta(days = 7)

def 
