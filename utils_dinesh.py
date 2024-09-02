''' Final Example

Module: Mahitha Analytics - Reusable Module for My Data Analytics Projects

'''

import statistics


has_international_clients: bool = True
years_in_operation: int = 10
average_client_satisfaction: float = 4.7 
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]
temperature_values: list = [40.8, 37.6, 44.9, 25.0, 44.7]

#####################################
# Calculate Basic Statistics using built in functions.

#####################################

# Calculate basic stats using built-in functions min(), max(), and statistics module functions mean() and stdev().
min_score:  float = min(client_satisfaction_scores)
max_score:  float = max(client_satisfaction_scores)
mean_score:  float = statistics.mean(client_satisfaction_scores)
stdev_score:  float = statistics.stdev(client_satisfaction_scores)
min_temp:  float = min(temperature_values)
max_temp:  float = max(temperature_values)
mean_temp:  float = statistics.mean(temperature_values)
stdev_temp:  float = statistics.stdev(temperature_values)

byline: str = f"""
-------------------------------------------------------------
Mahitha Analytics : Delivering Professional Insights
-------------------------------------------------------------
Has International Clients:  {has_international_clients}
Years in Operation:  {years_in_operation}
Skills Offered:  {skills_offered}
Client Satisfaction Scores:  {client_satisfaction_scores}
Minimum Client Satisfacton Score:  {min_score}
Maximum Client Satisfaction Score:  {max_score}
Average Client Satisfaction Score:  {mean_score}
Standard Deviation of Client Satisfaction Scores:  {stdev_score:.2f}
Minimum Temperature (F):  {min_temp}
Maximum Temperature (F):  {max_temp}
Mean Temperature (F):  {mean_temp}
Standard Deviation of Temperature (F):  {stdev_temp}

"""

#####################################
# Define the get_byline() function.
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline

#####################################
# Define a main() function for this module.
#####################################

# The main() function now calls the get_byline function to retrieve the byline.

def main() -> None:
    '''Print results of get_byline() when main() is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
