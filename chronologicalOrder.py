# The lists need to be combined with the years in chronological order.
def record_profit_years(recent_first, recent_last):
    recent_first.reverse()
    recent_last.extend(recent_first)
    
    

    return recent_last

recent_first = [2022, 2018, 2011, 2006]
recent_last = [1989, 1992, 1997, 2001]

print(record_profit_years(recent_first, recent_last))
# Should print [1989, 1992, 1997, 2001, 2006, 2011, 2018, 2022]