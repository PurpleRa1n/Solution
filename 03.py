# 1
lst = ['Email:', 'SSN:', 'Address:', 'Home Phone:', 'Mobile Phone: ', 'DOB:',
       'Date of Surgery:', 'Date of Service:', 'Facility of Service:',
       'Clinic Number:', 'Employer:', 'Work Phone: ', 'Fax: ', 'Type:', 'IPA:',
       'Health Plan:', 'ID #:', 'Claims Address:', 'Group #:',
       'Claim # / PO #:', 'Phone:', 'Fax:', 'Contact', 'Adjuster Email',
       'Util Review Phone', 'Util Review Fax', 'Doctor:', 'NPI #: ',
       'Date of Injury: ', 'Body Parts:', 'Body Part Side:', 'Gender:',
       'Diagnosis:', 'Diagnosis 2:', 'Procedure:']
print(lst[0], lst[-1])

# 2
lst = ['Email:', 'SSN:', 'Address:', 'Home Phone:', 'Mobile Phone: ', 'DOB:',
       'Date of Surgery:', 'Date of Service:', 'Facility of Service:',
       'Clinic Number:', 'Employer:', 'Work Phone: ', 'Fax: ', 'Type:', 'IPA:',
       'Health Plan:', 'ID #:', 'Claims Address:', 'Group #:',
       'Claim # / PO #:', 'Phone:', 'Fax:', 'Contact', 'Adjuster Email',
       'Util Review Phone', 'Util Review Fax', 'Doctor:', 'NPI #: ',
       'Date of Injury: ', 'Body Parts:', 'Body Part Side:', 'Gender:',
       'Diagnosis:', 'Diagnosis 2:', 'Procedure:']
print(lst[-2])

# 3
value = input()
first = value
second = value * 2
third = value * 3
fourth = value * 4
print(first + second - third * fourth)

# 4
import calendar

month = int(input())
year = int(input())
print(calendar.month(year, month))

# 5
import datetime

date_format = '%Y_%m_%d'
from_date = datetime.datetime.strptime(input(), date_format)
to_date = datetime.datetime.strptime(input(), date_format)
date_series = [from_date + datetime.timedelta(days=day_num) for day_num in
               range((to_date - from_date).days)]
result = sum(1 for day in date_series if day.weekday() < 5)

# 6
value = int(input())
prunt(value ** .5)

# 7
import operator

lst = [int(x) for x in input().split(', ')]
counter = {num: lst.count(num) for num in lst}
print(max(counter.items(), key=operator.itemgetter(1))[0])

# 8
lst = [25, 6, 72, 4]
res = ''
for i in lst:
    res = res + str(i)
print(res)

# 9
lst = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953,
    345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
    687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831,
    445, 742, 717, 958, 743, 527]
idx = lst.index(237)
print(sum(num for num in lst[idx:] if num % 2 == 0))


# 10
def is_sublist(lst_1, lst_2):
    def all_in(list_1, list_2):
        for elem in list_1:
            if elem in list_2:
                yield elem
    return all(item_1 == item_2 for item_1, item_2 in
               zip(all_in(lst_1, lst_2), all_in(lst_2, lst_1)))
