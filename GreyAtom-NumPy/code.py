# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data = np.genfromtxt(path, delimiter = ",", skip_header = 1)
census = np.concatenate((data, new_record), axis = 0)
print(census)


# --------------
#Code starts here
age = census[:,0]
print(age)
max_age = np.max(age)
min_age = np.min(age)
age_mean = age.mean()
print(round(age_mean, 2))
age_std = np.std(age)
print(round(age_std, 2))



# --------------
#Code starts here

race_0 = census[census[:,2] == 0]
race_1 = census[census[:,2] == 1]
race_2 = census[census[:,2] == 2]
race_3 = census[census[:,2] == 3]
race_4 = census[census[:,2] == 4]

#Store Length
len_0 = len(race_0)
print(len_0)
len_1 = len(race_1)
print(len_1)
len_2 = len(race_2)
print(len_2)
len_3 = len(race_3)
print(len_3)
len_4 = len(race_4)
print(len_4)


#Find min race
minority_race = 3
print(minority_race)



# --------------
#Code starts here
senior_citizens = census[census[:,0] > 60]

working_hours_sum = np.sum(senior_citizens[:,6])
print(working_hours_sum)

senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)

avg_working_hours = working_hours_sum / senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high_edu_cond = census[:,1] > 10
low_edu_cond = census[:,1] <= 10

high = census[high_edu_cond]
low =  census[low_edu_cond]

avg_pay_high = np.mean(high[:,7])
print(avg_pay_high)

avg_pay_low = np.mean(low[:,7])
print(avg_pay_low)


