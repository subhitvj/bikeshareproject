import pandas as pd
import datetime
import calendar


def locate_city():
    """Question the user for a city name."""

    city = input('\nHello! Lets\'s go and explore US Bikeshare data!\n'
                 'Would you like to check data for Chicago, New York or Washington?\n')

    if city =='Chicago':
        return'chicago.csv'
    elif city =='New York':
        return'new_york_city.csv'
    elif city =='Washington':
        return'washington.csv'
    else:
        print("\nI am sorry, Kindly enter correct name Let's try again.")
        return locate_city()


def locate_period():
    """Question the user for a time period"""

    time_period = input('\nHow you like to filter the data! by month, day or not at all?'
                        'Type "none" for no time filter.\n')

    if time_period =='month':
        return['month', locate_month()]
    elif time_period =='day':
        return['day',locate_day()]
    elif time_period =='none':
        return['none','no filter']
    else:
        print('\nI am Sorry, Kindly enter from given value. Lets try again.')
        return locate_period()


def locate_month():
    """Asks the user for a month and returns it"""

    month = input('\nEnter month from range. January, February, March, April, May, or June\n')

    if month == 'January':
        return '01'
    elif month == 'February':
        return '02'
    elif month == 'March':
        return '03'
    elif month == 'April':
        return '04'
    elif month == 'May':
        return '05'
    elif month == 'June':
        return '06'
    else:
        print('\nI am Sorry, Kindly enter correct month from given range'
              'Let\'s try again.')
        return locate_month()


def locate_day():
    """ Get user input of asking day name"""

    day_of_week = input('\nEnter any day of the week\n').title()

    if day_of_week == 'Monday':
        return 0
    elif day_of_week == 'Tuesday':
        return 1
    elif day_of_week == 'Wednesday':
        return 2
    elif day_of_week == 'Thursday':
        return 3
    elif day_of_week == 'Friday':
        return 4
    elif day_of_week == 'Saturday':
        return 5
    elif day_of_week == 'Sunday':
        return 6
    else:
        print('\nI am Sorry, kindly enter correct week name\n')
        return locate_day()


def most_popular_month(df):
    """gives you the data of popular month """

    monthly_trips = df.groupby("Month")['Start Time'].count()
    return "Most Popular Month:" + calendar.month_name[int(monthly_trips.sort_values(ascending=False).index[0])]


def most_popular_day(df):
    """gives you the data of most popular day"""

    daily_trips = df.groupby('Day of Week')['Start Time'].count()
    return "Most Popular day:" + calendar.day_name[int(daily_trips.sort_values(ascending=False).index[0])]


def most_popular_hour(df):
    """gives data of most popular hour"""

    hourly_trips = df.groupby('Hour of Day')['Start Time'].count()
    most_pop_hour = hourly_trips.sort_values(ascending=False).index[0]
    d = datetime.datetime.strptime(most_pop_hour, "%H")
    return "Most popular hour of the day: " + d.strftime("%I %p")


def most_trip_duration(df):
    """"gives data of trip durations"""

    total_trip_duration = df['Trip Duration'].sum()
    avg_trip_duration = df['Trip Duration'].mean()
    m, s = divmod(total_trip_duration, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    y, d = divmod(d, 365)
    total_trip_duration = "\ntrip duration: %d years %02d days %02d hrs %02d min %02d sec" % (y, d, h, m, s)
    m, s = divmod(avg_trip_duration, 60)
    h, m = divmod(m, 60)
    avg_trip_duration = "trip duration: %d hrs %02d min %02d sec" % (h, m, s)
    return [total_trip_duration, avg_trip_duration]


def very_popular_stations(df):
    """"gives data of popular station"""

    start_station_counts = df.groupby('Start Station')['Start Station'].count()
    end_station_counts = df.groupby('End Station')['End Station'].count()
    sorted_start_stations = start_station_counts.sort_values(ascending=False)
    sorted_end_stations = end_station_counts.sort_values(ascending=False)
    total_trips = df['Start Station'].count()
    most_popular_start_station = "\n popular start station: " + sorted_start_stations.index[0] + " (" + str(sorted_start_stations[0]) + " trips, " + '{0:.2f}%'.format(((sorted_start_stations[0]/total_trips) * 100)) + " of trips)"
    most_popular_end_station = " popular end station: " + sorted_end_stations.index[0] + " (" + str(sorted_end_stations[0]) + " trips, " + '{0:.2f}%'.format(((sorted_end_stations[0]/total_trips) * 100)) + " of trips)"
    return [most_popular_start_station, most_popular_end_station]


def very_popular_trip(df):
    """"gives data of popular trip"""

    trip_counts = df.groupby(['Start Station', 'End Station'])['Start Time'].count()
    sorted_trip_stations = trip_counts.sort_values(ascending=False)
    total_trips = df['Start Station'].count()
    return "popular trip: " + "\n  Start station: " + str(sorted_trip_stations.index[0][0]) + "\n  End station: " + str(sorted_trip_stations.index[0][1]) + "\n  (" + str(sorted_trip_stations[0]) +  " trips, " + '{0:.2f}%'.format(((sorted_trip_stations[0]/total_trips) * 100)) + " of trips)"


def end_users(df):

    user_type_counts = df.groupby('User Type')['User Type'].count()
    return user_type_counts


def human_gender(df):

    gender_counts = df.groupby('Gender')['Gender'].count()
    return gender_counts


def born_years(df):

    earliest_birth_year = "Earliest birth year: " + str(int(df['Birth Year'].min()))
    most_recent_birth_year = "Most recent birth year: " + str(int(df['Birth Year'].max()))
    birth_year_counts = df.groupby('Birth Year')['Birth Year'].count()
    sorted_birth_years = birth_year_counts.sort_values(ascending=False)
    total_trips = df['Birth Year'].count()
    most_common_birth_year = "Most common birth year: " + str(int(sorted_birth_years.index[0])) + " (" + str(sorted_birth_years.iloc[0]) + " trips, " + '{0:.2f}%'.format(((sorted_birth_years.iloc[0]/total_trips) * 100)) + " of trips)"
    return [earliest_birth_year, most_recent_birth_year, most_common_birth_year]


def display_output_data(df, current_line):

    present = input('\nWant to view more trip data?'
                    ' Type \'yes\' or \'no\'.\n')
    display = present.lower()
    if present == 'yes' or present == 'y':
        print(df.iloc[current_line:current_line+5])
        current_line += 5
        return display_output_data(df, current_line)
    if present == 'no' or present == 'n':
        return
    else:
        print("\nI'm sorry, kindly enter valid option. Let's try again.")
        return display_output_data(df, current_line)


def stats():
    """Filter by city (Chicago, New York, Washington)"""

    city = locate_city()
    city_df = pd.read_csv(city)

    def get_day_of_the_week(str_date):

        date_obj = datetime.date(int(str_date[0:4]), int(str_date[5:7]), int(str_date[8:10]))
        return date_obj.weekday()
    city_df['Day of Week'] = city_df['Start Time'].apply(get_day_of_the_week)
    city_df['Month'] = city_df['Start Time'].str[5:7]
    city_df['Hour of Day'] = city_df['Start Time'].str[11:13]
    time_period = locate_period()
    filter_period = time_period[0]
    filter_period_value = time_period[1]
    filter_period_label = 'No filter'

    if filter_period == 'none':
        filtered_df = city_df
    elif filter_period == 'month':
        filtered_df = city_df.loc[city_df['Month'] == filter_period_value]
        filter_period_label = calendar.month_name[int(filter_period_value)]
    elif filter_period == 'day':
        filtered_df = city_df.loc[city_df['Day of Week'] == filter_period_value]
        filter_period_label = calendar.day_name[int(filter_period_value)]

    print('\n')
    print(city[:-4].upper().replace("_", " ") + ' -- ' + filter_period_label.upper())
    print('----------------------------------------------')
    print('Total trips: ' + "{:,}".format(filtered_df['Start Time'].count()))

    if filter_period == 'none' or filter_period == 'day':
        print(most_popular_month(filtered_df))

    if filter_period == 'none' or filter_period == 'month':
        print(most_popular_day(filtered_df))

    print(most_popular_hour(filtered_df))
    trip_duration_stats = most_trip_duration(filtered_df)
    print(trip_duration_stats[0])
    print(trip_duration_stats[1])
    most_popular_stations = very_popular_stations(filtered_df)
    print(most_popular_stations[0])
    print(most_popular_stations[1])
    print(very_popular_trip(filtered_df))
    print('')
    print(end_users(filtered_df))

    if city == 'chicago.csv' or city == 'new_york_city.csv':

        print('')
        print(human_gender(filtered_df))
        birth_years_data = born_years(filtered_df)
        print('')
        print(birth_years_data[0])
        print(birth_years_data[1])
        print(birth_years_data[2])

    display_output_data(filtered_df, 0)

    # Reboot?
    def reboot_verify():

        reboot = input('\nWant to reboot? Type \'yes\' or \'no\'. (fyi: no will end the program.)\n')
        if reboot.lower() == 'yes' or reboot.lower() == 'y':
            stats()
        elif reboot.lower() == 'no' or reboot.lower() == 'n':
            return
        else:
            print("\nLet's try again from start.")
            return reboot_verify()

    reboot_verify()


if __name__ == "__main__":
    stats()

