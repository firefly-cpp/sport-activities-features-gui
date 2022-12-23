import matplotlib.pyplot as plt
from sport_activities_features import TCXFile
from sport_activities_features.plot_data import PlotData
from sport_activities_features.interval_identification import (
    IntervalIdentificationByHeartRate,
    IntervalIdentificationByPower,
)
from sport_activities_features.hill_identification import HillIdentification
import pandas as pd
class Graphs:
    activity_list = []
    
    def __init__(self, data):
        self.activity_list = data
        
    def allBikingDistanceRidden(self):
        dict = self.activity_list.to_dict('records')
        gData = []
        for a in dict:
            if (a['activity_type'] == 'Biking'):
                gData.append(a['distance'])
        plt.plot(gData)
        plt.title('All biking distances ridden')
        plt.xlabel('Activity record')
        plt.ylabel('Distance')
        plt.show()

    def sumOfBikingDurationForCompetitor(self):
        # sum = []
        # for act in self.activity_list.to_dict('records'):
        #     s1 = [x for x in User.data if x['activity_type'] == 'Biking' and x['competitor_id'] == '1']
        #     sum.append(self._sumProp(s1, 'duration'))

        # plt.subplot(131)
        # plt.bar(['1','2','3','4'], sum)
        # plt.title('Sum of biking duration for competitor')
        # plt.xlabel('Competitor')
        # plt.ylabel('Duration')
        # plt.show()
        print('Not implemented')
        
    def altitudeVsCalories(self):
        calories = []
        altitude = []
        for a in self.activity_list.to_dict('records'):
            calories.append(a['calories'])
            altitude.append(a['altitude_avg'])
        plt.scatter(altitude, calories)
        plt.title('Altitude vs calories')
        plt.xlabel('Altitude')
        plt.ylabel('Calories')
        plt.show()

    def activityTypeVsCalories(self):
        caloriesBiking = []
        caloriesRunning = []
        caloriesOther = []
        for a in self.activity_list.to_dict('records'):
            if a['activity_type'] == 'Biking' :
                caloriesBiking.append(a['calories'])
            if a['activity_type'] == 'Running' :
                caloriesRunning.append(a['calories'])
            if a['activity_type'] == 'Other' :
                caloriesOther.append(a['calories'])

        sum = []
        sum.append(self._sum(caloriesBiking))
        sum.append(self._sum(caloriesRunning))
        sum.append(self._sum(caloriesOther))
        plt.subplot(131)
        plt.bar(['Biking','Running','Other'], sum)
        plt.title('Activity type vs calories')
        plt.ylabel('Calories')
        plt.show()

    def mapWithIdentifiedHills(self):
        # TODO - enable to choose for which file
        print('Not fully implemented')
        el = self.activity_list.to_dict('records')[10]
        # detect hills in data
        Hill = HillIdentification(el.altitudes, 30)
        Hill.identify_hills()
        all_hills = Hill.return_hills()

        # draw detected hills
        Map = PlotData()
        Map.draw_hills_in_map(el.altitudes, el.distances, all_hills)

    def mapWithIdentifiedIntervals(self):
        # TODO - enable to choose for which file
        print('Not fully implemented')
        el = self.activity_list.to_dict('records')[10]

        # Identifying the intervals in the activity by power and drawing the map
        Intervals = IntervalIdentificationByPower(el.distances, el.timestamps, el.altitudes, 70)
        Intervals.identify_intervals()
        all_intervals = Intervals.return_intervals()
        Map = PlotData()
        Map.draw_intervals_in_map(el.timestamps, el.distances, all_intervals)

        # Identifying the intervals in the activity by heart rate and drawing the map
        Intervals = IntervalIdentificationByHeartRate(
            el.distances, el.timestamps, el.altitudes, el.heartrates
        )
        Intervals.identify_intervals()
        all_intervals = Intervals.return_intervals()
        Map = PlotData()
        Map.draw_intervals_in_map(el.timestamps, el.distances, all_intervals)
        
    def _sum(arr):
        sum = 0
        for i in arr:
            sum = sum + i
        return(sum)
    
    def _sumProp(array, property):
        sum = 0
        for i in array:
            if i[property] is not None:
                sum = sum + i[property]
        return(sum)
    
    def customGraph(self):
        print("Not implemented")