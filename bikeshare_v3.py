import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'Chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'Washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello :) Let\'s explore some US bikeshare data!')
  

    city_is_select = True
    valid_city_list = ["0", "1", "2", "Chicago", "New York City", "Washington"]

    while(city_is_select):    
        isSelected="no"
        city = input("Which city do you want to select?  \n\n\n 0. Chicago\n 1. New York City\n 2. Washington\n\n").strip().lower()
    
        if(city in valid_city_list):
        
            if(city == "0"):
                city = "Chicago"
            elif(city == "1"):
                city = "New York City"
            elif(city == "2"):
                city = "Washington"

    # get user input for approval (selected City approve)
            isSelected = input("You have selected {}, write 'yes' to approve or write anything to start over.\n\n".format(city.title())).strip().lower()
            if(isSelected == "yes"):
                city_is_select = False

        else:
            print("\n Please Enter Number of City (0/1/2/3/4/5/6) !\n")


    # get user input for month (all, January, february, ... , june)

    month_is_select = True
    valid_month_list = ["0", "1", "2", "3", "4", "5", "6", "All", "January", "February", "March", "April", "May", "June"]

    while(month_is_select):    
        isSelected="no"
        month = input("Please select month: \n\n 0. All\n 1. January\n 2. February\n 3. March\n 4. April\n 5. May\n 6. June\n\n").strip().lower()
    
        if(month in valid_month_list):
        
            if(month == "0"):
                month = "all"
            elif(month == "1" ):
                month = "January"
            elif(month == "2"):
                month = "February"
            elif(month == "3" ):
                month = "March"
            elif(month == "4" ):
                month = "April"
            elif(month == "5" ):
                month = "May"
            elif(month == "6" ):
                month = "June"

    # get user input for approval
            isSelected = input("You have selected {}, type 'yes' to approve or type anything to start over.\n\n".format(month.title())).strip().lower()
            if(isSelected == "yes"):
                month_is_select = False

        else:
            print("\n!!! Please enter Number of Month (0/1/2/3/4/5/6)  !!!\n")

    # get user input for day of week (all, monday, tuesday, ... sunday)

    day_is_select = True
    valid_day_list = ["0", "1", "2", "3", "4", "5", "6", "7", "all","monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    while(day_is_select):    
        isSelected="no"
        day = input("Please select day: \n\n 0. All\n 1. Monday\n 2. Tuesday\n 3. Wednesday\n 4. Thursday\n 5. Friday\n 6. Saturday\n 7. Sunday\n\n").strip().lower()
    
        if(day in valid_day_list):
        
            if(day == "0"):
                day = "all"
            elif(day == "1" ):
                day = "monday"
            elif(day == "2" ):
                day = "tuesday"
            elif(day == "3" ):
                day = "wednesday"
            elif(day == "4" ):
                day = "thursday"
            elif(day == "5" ):
                day = "friday"
            elif(day == "6" ):
                day = "saturday"
            elif(day == "7" ):
                day = "sunday"

    # get user input for approval
            isSelected = input("You have selected {}, type 'yes' to approve or type anything to start over.\n\n".format(day.title())).strip().lower()
            if(isSelected == "yes"):
                day_is_select = False

        else:
            print("\n!!! Please enter 0/1/2/3/4/5/6/7  !!!\n")


    print('-'*80)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name()

# Convert month name to index.
    if(month != 'all'):
        months = ['all', 'January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month)
        df = df[df['Month'] == month]


    if(day != 'all'):
        df = df[df['Day of Week'] == day.title()]
    
    return df


def time_stats_func(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['all', 'January', 'February', 'March', 'April', 'May', 'June']
    print("The Most Common Month: {}".format(months[df['Month'].mode()[0]].title()))

    # display the most common day of week
    print("The Most Common Day Of Week: {}".format(df['Day of Week'].mode()[0]))

    # display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    print("The Most Common Hour Of Day: {}".format(df['Hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)

    df.drop('Month',axis=1,inplace=True)
    df.drop('Day of Week',axis=1,inplace=True)
    df.drop('Hour',axis=1,inplace=True)


def station_stats_func(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip.\n')
    start_time = time.time()

    # display most commonly used start station
    print("The Most Common Start Station  : {}".format(df['Start Station'].mode()[0]))


    # display most commonly used end station
    print("The Most Common End Station  :  {}".format(df['End Station'].mode()[0]))


    # display most frequent combination of start station and end station trip
    df['Comb Station'] = 'Start Station: ' + df['Start Station'] + '\n' + 31*' ' + 'End Station: ' + df['End Station']
    print("The Most Frequent Combination  : {}".format(df['Comb Station'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)

    df.drop('Comb Station',axis=1,inplace=True)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n *****   Calculating Trip Duration...  *****  \n')
    start_time = time.time()

    # display total travel time
    total_trip_duration = int(df['Trip Duration'].sum())
    trip_seconds = total_trip_duration % 60

    if(total_trip_duration > 86400):
       trip_days = total_trip_duration / 86400
       total_trip_duration = total_trip_duration % 86400
    else:
        trip_days = 0

    if(total_trip_duration > 3600):
       trip_hours = total_trip_duration / 3600
       total_trip_duration = total_trip_duration % 3600
    else:
        trip_hours = 0

    if(total_trip_duration > 60):
       trip_minutes = total_trip_duration / 60
    else:
        trip_minutes = 0

    print("Total trip duration: {} days {} hours {} minutes {} seconds.".format(int(trip_days), int(trip_hours), int(trip_minutes), int(trip_seconds)))




    # display mean travel time
    mean_trip_duration = int(df['Trip Duration'].mean())
#calculate secondss
    mean_seconds = mean_trip_duration % 60


#calculate days
    if(mean_trip_duration > 86400):
       mean_days = mean_trip_duration / 86400
       mean_trip_duration = mean_trip_duration % 86400
    else:
        mean_days = 0

#calculate hours
    if(mean_trip_duration > 3600):
       mean_hours = mean_trip_duration / 3600
       mean_trip_duration = mean_trip_duration % 3600
    else:
        mean_hours = 0

#calculate minutes
    if(mean_trip_duration > 60):
       mean_minutes = mean_trip_duration / 60
    else:
        mean_minutes = 0

    print("Mean trip duration: {} days {} hours {} minutes {} seconds.".format(int(mean_days), int(mean_hours), int(mean_minutes), int(mean_seconds)))




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def user_stats_func(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    total_user_type_count = 0
    user_type = df.groupby('User Type',as_index=False).count()
    for i in range(len(user_type)):
        print('{} count: {}'.format(user_type['User Type'][i], user_type['Trip Duration'][i]))
        total_user_type_count += user_type['Trip Duration'][i]
    print('Missing user type data count: {}'.format(len(df) - total_user_type_count))


    # Display counts of gender
    print("\n")
    """
    First of all we need to check whether Gender data present or not
    """

    if 'Gender' in df:
        total_gender_count = 0
        user_gender = df.groupby('Gender',as_index=False).count()
        for i in range(len(user_gender)):
            print('{} count: {}'.format(user_gender['Gender'][i], user_gender['Trip Duration'][i]))
            total_gender_count += user_gender['Trip Duration'][i]
        print('Missing gender data count: {}'.format(len(df) - total_gender_count))
    else:
        print('No gender data for this city')


    # Display earliest, most recent, and most common year of birth
    print("\n")
    """
    First of all we need to check whether Birth Year data present or not
    """

    if 'Birth Year' in df:
         print("The Most Earliest Birth Year: {}\nMost Recent Birth Year: {}\nMost Common Birth Year: {}".format(int(df['Birth Year'].min()), int(df['Birth Year'].max()), int(df['Birth Year'].mode()[0])))
    else:
        print('No birth year data for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)
    
def display_data(df,start_loc):
    """Display 5 line of sorted raw data each time."""
  
	
	view_data = input('\n Would you like to view 5 rows of individual trip data? Enter Yes or NO.\n')
	
	start_loc = 0
	
    # each loop displays 5 lines of raw data
    while True:
        for i in range(start_loc, len(df.index)):
            print("\n")
            print(df.iloc[start_loc:start_loc+5].to_string())
            print("\n")
            start_loc += 5

            if choice("Do you wish to continue?"
                      "\n\n[y]Yes\n[n]No\n\n>") == 'y':
                continue
            else:
                break
        break

    return start_loc


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats_func(df)
        station_stats_func(df)
        trip_duration_stats(df)
        user_stats_func(df)
        display_data(df,start_loc)
               

        restart = input('\n Do you want to restart? Enter Yes or NO.\n')
        if restart.lower() != 'Yes':
            break


if __name__ == "__main__":
	main()