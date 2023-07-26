import matplotlib.pyplot as plt
import math
import numpy as np

class Graphs:
    user = None

    def __init__(self, user):
        self.user = user

    def _sum(self, arr):
        sum = 0
        for i in arr:
            sum = sum + i
        return (sum)

    def _sumProp(self, array, property):
        sum = 0
        for i in array:
            if i[property] is not None:
                sum = sum + i[property]
        return (sum)

    def allBikingDistanceRidden(self):
        gData = []
        for a in self.user.data.to_dict('records'):
            if (a['activity_type'] == 'Biking'):
                gData.append(a['distance'])
        plt.plot(gData)
        plt.title('All biking distances ridden')
        plt.xlabel('Activity record')
        plt.ylabel('Distance')
        plt.show()

    def sumOfBikingDurationForCompetitor(self):
        sum = 0
        for act in filter(lambda x: x['activity_type'] == 'Biking', self.user.data.to_dict('records')):
            sum += act['duration'] if act['duration'] != None and math.isnan(act['duration']) == False else 0

        plt.subplot(131)
        plt.bar([self.user.username], sum)
        plt.title('Sum of biking duration for competitor')
        plt.xlabel('Competitor')
        plt.ylabel('Duration')
        plt.show()

    def altitudeVsCalories(self):
        calories = []
        altitude = []
        for a in self.user.data.to_dict('records'):
            calories.append(a['calories'])
            altitude.append(a['altitude_avg'])
        plt.scatter(altitude, calories)
        plt.title('Altitude vs calories')
        plt.xlabel('Altitude')
        plt.ylabel('Calories')
        plt.show()

    def caloriesByActivityType(self):

        activity_types=list(set(self.user.data["activity_type"]))
        caloriesDictionary = {}
        for activity in activity_types:
            caloriesDictionary[activity] = 0

        for record in self.user.data.to_dict('records'):
            caloriesDictionary[record['activity_type']] += record['calories']

        plt.subplot(131)
        plt.bar(caloriesDictionary.keys(), caloriesDictionary.values())
        plt.title('Calories by activity type')
        plt.ylabel('Calories')
        plt.show()

    def heartRateByActivities(self):
        activity_number = []
        hr_avg = []
        hr_max = []
        hr_min = []
        i = 0
        for a in self.user.data.to_dict('records'):
            activity_number.append(i)
            hr_avg.append(a['hr_avg'])
            hr_max.append(a['hr_max'])
            hr_min.append(a['hr_min'])
            i += 1

        width = 0.35
        x = np.arange(len(activity_number))
        fig, ax = plt.subplots()
        r1 = ax.bar(x - (width / 2 + 0.05), hr_avg, width, label='HR-avg')
        r2 = ax.bar(x, hr_max, width, label='HR-max')
        r3 = ax.bar(x + (width / 2 + 0.05), hr_min, width, label='HR-min')

        ax.set_ylabel('Heart rate')
        ax.set_title('Heart rates by activities')
        ax.set_xticks(activity_number, activity_number)
        ax.legend()

        ax.bar_label(r1, padding=3)
        ax.bar_label(r2, padding=3)
        ax.bar_label(r3, padding=3)

        fig.tight_layout()
        plt.show()

    def customGraph(self, xAttr, yAttr, plotType):
        match plotType:
            case "Bar":
                self.customBarPlot(yAttr)
            case "Scatter":
                self.customScatterPlot(xAttr, yAttr)
            case "Line":
                self.customLinePlot(yAttr)

    def customBarPlot(self, yAttr):
        activityNum = []
        y = []
        activities = self.user.data.to_dict('records')

        for act in activities:
            if (yAttr != ''):
                res = act[yAttr] if math.isnan(act[yAttr]) == False else 0
                y.append(res)

        i = 1
        for y1 in y:
            activityNum.append(i)
            i += 1
        plt.bar(activityNum, y)
        plt.ylabel(yAttr)
        plt.show()

    def customScatterPlot(self, xAttr, yAttr):
        x = []
        y = []
        if (xAttr != '' and yAttr != ''):
            activities = self.user.data.to_dict('records')

            for act in activities:
                if (xAttr != ''):
                    res = act[xAttr] if math.isnan(act[xAttr]) == False else 0
                    x.append(res)
            for act in activities:
                if (yAttr != ''):
                    res = act[yAttr] if math.isnan(act[yAttr]) == False else 0
                    y.append(res)

            plt.scatter(x, y)
            plt.title(xAttr + ' vs ' + yAttr)
            plt.xlabel(xAttr)
            plt.ylabel(yAttr)
            plt.show()

    def customLinePlot(self, yAttr):
        y = []
        activities = self.user.data.to_dict('records')

        for act in activities:
            if (yAttr != ''):
                res = act[yAttr] if math.isnan(act[yAttr]) is False else 0
                y.append(res)

        plt.plot(y, linestyle='dotted')
        plt.show()