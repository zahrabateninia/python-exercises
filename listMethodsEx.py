# This block of code changes the year on a list of dates (if the year is 2023 it will be changed to 2024)
# The "years" list is given with existing elements. 
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
updated_years = []
for year in years:
    if year.endswith('2023'):
        updated_year = year.replace('2023','2024')
        updated_years.append(updated_year)
    else:
        updated_years.append(year)
print(updated_years)
#refactering the code to a shorted and more efficient block of code:
def update_years(years):
    return [year.replace('2023','2024') if year.endswith('2023') else year for year in years] 
print(update_years(years))