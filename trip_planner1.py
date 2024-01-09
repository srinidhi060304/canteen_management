import sqlite3
import numpy as np
import pandas as pd

class TripPlanner:
    def __init__(self, destination, hotel):
        # Connect to the SQLite databases
        sightseeing_db = destination.lower() + '_sightseeing.db'
        self.dest = sqlite3.connect(sightseeing_db)
        self.sightseeing_data = pd.read_sql_query("SELECT * FROM sightseeing", self.dest)

        hotel_db = destination.lower() + '_' + hotel + 'star.db'
        self.hotels = sqlite3.connect(hotel_db)
        self.hotels_data = pd.read_sql_query("SELECT * FROM hotels", self.hotels)

    def generate_hotel(self, destination, people, days, budget):
        p = ""
        k = 0
        if people == "2" or people  == "1":
            k = 3
            p = "twopeople"
        elif people == "3":
            k = 2
            p = "threepeople"
        elif people == "4":
            k = 1
            p = "fourpeople"
        else:
            print("Invalid input")
        d = (int(budget) / int(days))

        # Example: Select hotels within budget for specified number of people
        selected_hotels = self.hotels_data[self.hotels_data[p] <= d]
        print(str(int(budget) / int(days)))

        itinerary = f"Your trip to {destination} with a budget of {budget} has been planned.\n"

        i = 1
        if not selected_hotels.empty:
            for index, hotel in selected_hotels.iterrows():
                itinerary += f"Hotel {i}: {hotel['hotel_name']} \nCost per night: {hotel[k]} \n" \
                              f"Cost for {days} days: {hotel[k] * int(days)}\n\n"
                i += 1

            # Remove selected hotels from the original DataFrame
            self.hotels_data = self.hotels_data[~self.hotels_data['hotel_name'].isin(selected_hotels['hotel_name'])]
        else:
            itinerary += "Stay at a comfortable place\n"
        return itinerary

    def generate_plan(self, people, child, budget, days, hotel):
        k = 0
        if people == "2" or people  == "1":
            k = 3
            p = "twopeople"
        elif people == "3":
            k = 2
            p = "threepeople"
        elif people == "4":
            k = 1
            p = "fourpeople"
        else:
            print("Invalid input")
        print("p=", p)

        b1 = int(self.hotels_data[self.hotels_data['hotel_name'] == hotel][p].values[0])
        rem = int(budget) - ((b1) * int(days))
        iter = f"Hotel name: {hotel}\nCost for {days} days: {b1 * int(days)}\nRemaining budget: {rem}\n\n"

        sightseeing_data = self.sightseeing_data[
            (self.sightseeing_data['adultentry'] <= rem) & (self.sightseeing_data['childentry'] <= rem)]

        for day in range(1, int(days) + 1):
            iter += f"Day {day}: "

            # Add logic to select sightseeing spot for the day
            t = 0
            if not sightseeing_data.empty:
                for index, spot in sightseeing_data.iterrows():
                    if t + spot['timerequired'] < 8:
                        iter += f"Visit {spot['name']}\nType {spot['tag']}\nOpen time - {spot['starttime']}" \
                                f"\nClose time - {spot['endtime']}\nTime taken to visit {spot['timerequired']} hrs\n" \
                                f"Cost for adults: {spot['adultentry']}  \nCost for children: {spot['childentry']} \n\n\n"
                        t += spot['timerequired']
                        sightseeing_data = sightseeing_data.drop(index)
                    else:
                        continue
            else:
                iter += "Relax and enjoy the surroundings\n"

        return iter
