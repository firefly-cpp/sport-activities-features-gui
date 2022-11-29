
from sport_activities_features_gui.models.User import User
import matplotlib.pyplot as plt
from sport_activities_features import TCXFile
from sport_activities_features.plot_data import PlotData
from sport_activities_features.interval_identification import (
    IntervalIdentificationByHeartRate,
    IntervalIdentificationByPower,
)
from sport_activities_features.hill_identification import HillIdentification

class Graphs:
    activity_list = []
    
    def __init__(self, data):
        self.activity_list = data
        
    # All biking distances ridden
    def allBikingDistanceRidden(self):
        gData = []
        for a in self.activity_list:
            if (a['activity_type'] == 'Biking'):
                gData.append(a['distance'])
        plt.plot(gData)
        plt.title('All biking distances ridden')
        plt.xlabel('Activity record')
        plt.ylabel('Distance')
        plt.show()
        print('Graph 1')



    # Sum of biking duration for competitor
    def sumOfBikingDurationForCompetitor(self):
        s1 = [x for x in User.data if x['activity_type'] == 'Biking' and x['competitor_id'] == '1']
        s2 = [x for x in User.data if x['activity_type'] == 'Biking' and x['competitor_id'] == '2']
        s3 = [x for x in User.data if x['activity_type'] == 'Biking' and x['competitor_id'] == '3']
        s4 = [x for x in User.data if x['activity_type'] == 'Biking' and x['competitor_id'] == '4']
        sum = []
        sum.append(self._sumProp(s1, 'duration'))
        sum.append(self._sumProp(s2, 'duration'))
        sum.append(self._sumProp(s3, 'duration'))
        sum.append(self._sumProp(s4, 'duration'))

        plt.subplot(131)
        plt.bar(['1','2','3','4'], sum)
        plt.title('Sum of biking duration for competitor')
        plt.xlabel('Competitor')
        plt.ylabel('Duration')
        plt.show()
        print('Graph 2')

    # altitude vs calories
    def altitudeVsCalories(self):
        calories = []
        altitude = []
        for a in self.activity_list:
            calories.append(a['calories'])
            altitude.append(a['altitude_avg'])
        plt.scatter(altitude, calories)
        plt.title('Altitude vs calories')
        plt.xlabel('Altitude')
        plt.ylabel('Calories')
        print('Graph 3')
        plt.show()

    # activity type vs calories
    def activityTypeVsCalories(self):
        caloriesBiking = []
        caloriesRunning = []
        caloriesOther = []
        for a in self.activity_list:
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
        print('Graph 4')
        plt.show()

    # Map with identified hills
    def mapWithIdentifiedHills():
        tcx_file = TCXFile()
        (
            activity_type,
            positions,
            altitudes,
            distances,
            total_distance,
            timestamps,
            heartrates,
            speeds
        ) = tcx_file.read_one_file('data/1/1.tcx').values()

        # detect hills in data
        Hill = HillIdentification(altitudes, 30)
        Hill.identify_hills()
        all_hills = Hill.return_hills()

        # draw detected hills
        Map = PlotData()
        print('Graph activites 1')
        Map.draw_hills_in_map(altitudes, distances, all_hills)

    # Map with identified intervals
    def mapWithIdentifiedIntervals():
        # Reading the TCX file
        tcx_file = TCXFile()
        (
            activity_type,
            positions,
            altitudes,
            distances,
            total_distance,
            timestamps,
            heartrates,
            speeds
        ) = tcx_file.read_one_file('data/1/1.tcx').values()

        # Identifying the intervals in the activity by power and drawing the map
        Intervals = IntervalIdentificationByPower(distances, timestamps, altitudes, 70)
        Intervals.identify_intervals()
        all_intervals = Intervals.return_intervals()
        Map = PlotData()
        print('Graph activites 2')
        Map.draw_intervals_in_map(timestamps, distances, all_intervals)

        # Identifying the intervals in the activity by heart rate and drawing the map
        Intervals = IntervalIdentificationByHeartRate(
            distances, timestamps, altitudes, heartrates
        )
        Intervals.identify_intervals()
        all_intervals = Intervals.return_intervals()
        Map = PlotData()
        Map.draw_intervals_in_map(timestamps, distances, all_intervals)
        
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
    
    def customGraph():
        print("not implemented")