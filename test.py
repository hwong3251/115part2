import requests, time, datetime
from numpy import percentile

def sort_date(v):
    return v['BreachDate']


def get_breachsites_data(url):
    response = requests.get(url)
    # Get the response data as a python object.  Verify that it's a dictionary.
    site_data = response.json()
    new_arr = site_data
    new_arr.sort(key=sort_date)
    return new_arr


def get_reverse_breachsites_data(url):
    response = requests.get(url)
    # Get the response data as a python object.  Verify that it's a dictionary.
    site_data = response.json()
    new_reverse_arr = site_data
    new_reverse_arr.sort(key=sort_date, reverse=True)
    return new_reverse_arr


def get_map_data(url):
    data_arr = get_breachsites_data(url)
    new_time_sort = {}
    for i in data_arr:
        timeutc = i['BreachDate']
        pwn = i['PwnCount']
        timeutcnew = time.mktime(datetime.datetime.strptime(timeutc, "%Y-%m-%d").timetuple())
        # print(time.mktime(datetime.datetime.strptime(timeutc, "%Y-%m-%d").timetuple()))
        new_time_sort.update({str(int(timeutcnew)): pwn})
    return new_time_sort


def ten_recent_breach_site(str):
    arr = get_reverse_breachsites_data(str)
    site_name = []
    site_breach_date = []
    site_description = []
    site_pwncount = []
    for i in range(0, 10):
        site_name.append(arr[i]["Name"])
        site_breach_date.append(arr[i]["BreachDate"])
        site_description.append(arr[i]["Description"])
        site_pwncount.append(arr[i]["PwnCount"])
    return {"pwncount": site_pwncount, "site_name": site_name, "site_description": site_description, "site_breach_date": site_breach_date}

x = []
for i in get_map_data("https://haveibeenpwned.com/api/v2/breaches").values():
    x.append(i)
quartiles = percentile(x, [25,50, 75])
print('Q1: %.3f' % quartiles[0])
print('Median: %.3f' % quartiles[1])
print('Q3: %.3f' % quartiles[2])
