import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    
    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city= input("Would you like to see data for chicago,new york or washington?  ").lower()
        
        if city =='chicago' or city =='new york city' or city == 'washington':
            break
            
        else:
            print('please enter a valid city')
            continue
                
    while True:
        month= input("which month do you want to filter by january, february, march, april, may or june or all to apply no month filter?").lower()
       
        months = ['all','january', 'february', 'march', 'april', 'may', 'june']
        
        if month in months:
            break
        else:
            print('please enter a valid month')
            continue
            
    while True:
        
        day= input("which day do you want to filter by? saturday, sunday, monday, tuesday, wednesday, thursday or friday or all to apply no day filter?   ").lower()
        days = ['all','saturday','sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        
        if day in days:
            break
        else:
            print('please enter a valid day')
            continue
 
    print('-'*40)
    return city, month,day


def load_data(city, month,day):
   
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
   
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month= df['month'].mode()[0]
    print('most common month:', popular_month)


    # TO DO: display the most common day of week
    
    popular_month= df['day_of_week'].mode()[0]
    print('most common day:', popular_month)
    
   
    df['hour'] = df['Start Time'].dt.hour
    
    popular_hour= df['hour'].mode()[0]
        
    print('most common hour:', popular_hour)
    


    # TO DO: display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    popular_station= df['Start Station'].mode()[0]
    print('most common station: ', popular_station)


    # TO DO: display most commonly used end station
    
    popular_Endstation= df['End Station'].mode()[0]
    print('most common end station:  ',   popular_Endstation)
    
    frequent_combination= (df['Start Station'] +' '+ 'and' + ' ' + df['End Station']).mode()[0]
    print('mmost frequent combination of start station and end station:  ',  frequent_combination )
    
    


    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_travel_time = df['Trip Duration'].sum()
    
    print('total travel time: ',total_travel_time)


    # TO DO: display mean travel time
    
    mean_travel_time = df['Trip Duration'].mean()
    
    print('average travel time: ',mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_types = df.groupby(['User Type'])['User Type'].count()

    print('counts of user types',user_types)


    # TO DO: Display counts of gender
    
    if 'Gender' in df:
        
        gender = df.groupby(['Gender'])['Gender'].count()
        print('counts of Gender',gender)



    # TO DO: Display earliest, most recent, and most common year of birth
    
    if 'Birth Year' in df:
        print('earliest, most recent, and most common year of birth',(df['Birth Year'].min(),df['Birth Year'].max(),df['Birth Year'].mode()[0]))
        
        


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    end_loc = 5
    while (True):
        if view_data == 'no':
            break
        elif view_data == 'yes':
            print(df.iloc[start_loc:end_loc])
            start_loc += 5
            end_loc += 5
            view_data = input('\nWould you like to view another 5 rows of individual trip data? Enter yes or no\n').lower()
            continue
            
        else:
            print("enter a valid answer")
            break 



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
