import datetime

class s_class:
    def __init__(self, name, period,):
        self.name = name
        self.period = period

merge_periods = True
start_times = {
  1: datetime.time(8,45,0),
  2: datetime.time(9,30,0),
  3: datetime.time(10,30,0),
  4: datetime.time(11,15,0),
  5: datetime.time(13,0,0),
  6: datetime.time(13,45,0),
  7: datetime.time(14,45,0),
}
end_times = {
  1: datetime.time(9,30,0),
  2: datetime.time(10,15,0),
  3: datetime.time(11,15,0),
  4: datetime.time(12,0,0),
  5: datetime.time(13,45,0),
  6: datetime.time(14,30,0),
  7: datetime.time(15,45,0),
}
classes = [s_class("Gym",1), #1,
           s_class("Maths",1), #2
           s_class("English",1),#3
           s_class("ECR",1),#4
           s_class("French",1),#5
           s_class("Science",1),#6
           s_class("Spanish",1),#7
           s_class("History",1),#8
           s_class("Geography",1), #9
           s_class("Drama",1),#10
           s_class("Music",1)] #11
schedule_dict = {1:[5,5,7,1,2,8,3],
                2:[6,6,2,2,3,3,4],
                3:[9,9,2,2,6,6,5],
                4:[2,2,5,5,7,7,3],
                5:[5,5,1,1,10,10,6],
                6:[5,5,8,8,11,11,9]}
vacation_days = [[datetime.datetime(2020,9,7,0,0,0,0)],
                [datetime.datetime(2020,10,12,0,0,0,0)],
                [datetime.datetime(2020,11,2,0,0,0,0),
                 datetime.datetime(2020,11,6,0,0,0,0)],
                [datetime.datetime(2020,12,23,0,0,0,0),
                 datetime.datetime(2021,1,5,0,0,0,0)],
                [datetime.datetime(2021,3,1,0,0,0,0),
                 datetime.datetime(2021,3,5,0,0,0,0)],
                [datetime.datetime(2021,4,2,0,0,0,0),
                 datetime.datetime(2021,4,9,0,0,0,0)],
                [datetime.datetime(2021,5,24,0,0,0,0)],
                [datetime.datetime(2020,11,20,0,0,0,0)],
                [datetime.datetime(2020,11,27,0,0,0,0)]]
start_date = datetime.datetime(2020, 8, 28, 0, 0, 0, 0)
end_date = datetime.datetime(2021, 6, 22, 0, 0, 0, 0)
#in case you're too lazy to modify the start date or vacation days
offset = 0
