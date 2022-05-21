import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
import time

ordered = 'Set'


def program(set_path, support_threshold):
    f = open(set_path, 'r')
    transacts = []
    lines = f.readlines()
    for line in lines:
        transacts.append(line.split())

    rule = apriori(transactions = transacts, min_support = support_threshold)

    output = list(rule) # returns a non-tabular output
    return output


def inspect(output):
    Set = [list(result[0]) for result in output]
    Set = [sorted([eval(x) for x in result]) for result in Set]
    support = [result[1] for result in output]
    return list(zip(Set, support))


def order_by(rule, data):
    if rule == "Support":
        print(data.sort_values(by="Support", ascending=False))
    elif rule == "Set":
        print(data)


def counter(items):
    items_len = [0, 0, 0, 0, 0, 0, 0]
    for item in items:
        if len(item[0]) == 1:
            items_len[0] += 1
        elif len(item[0]) == 2:
            items_len[1] += 1
        elif len(item[0]) == 3:
            items_len[2] += 1
        elif len(item[0]) == 4:
            items_len[3] += 1
        elif len(item[0]) == 5:
            items_len[4] += 1
        elif len(item[0]) == 6:
            items_len[5] += 1
        elif len(item[0]) == 7:
            items_len[6] += 1
    return items_len


def add(x, y):
    return list(map(lambda a, b: a + b, x, y))

time_retail = []
retail_len = []
start_time = time.time()
retail_1 = program('retail.txt', 0.01)
time_retail.append(time.time() - start_time)
counts = counter(retail_1)
retail_len.append(counts)

start_time = time.time()
retail_3 = program('retail.txt', 0.03)
time_retail.append(time.time() - start_time)
counts = counter(retail_3)
retail_len.append(counts)

start_time = time.time()
retail_5 = program('retail.txt', 0.05)
time_retail.append(time.time() - start_time)
counts = counter(retail_5)
retail_len.append(counts)

start_time = time.time()
retail_10 = program('retail.txt', 0.1)
time_retail.append(time.time() - start_time)
counts = counter(retail_10)
retail_len.append(counts)

start_time = time.time()
retail_15 = program('retail.txt', 0.15)
time_retail.append(time.time() - start_time)
counts = counter(retail_15)
retail_len.append(counts)

time_accidents = []
accidents_len = []
start_time = time.time()
accidents_75 = program('accidents.txt', 0.75)
time_accidents.append(time.time() - start_time)
counts = counter(accidents_75)
accidents_len.append(counts)

start_time = time.time()
accidents_80 = program('accidents.txt', 0.8)
time_accidents.append(time.time() - start_time)
counts = counter(accidents_80)
accidents_len.append(counts)

start_time = time.time()
accidents_85 = program('accidents.txt', 0.85)
time_accidents.append(time.time() - start_time)
counts = counter(accidents_85)
accidents_len.append(counts)

start_time = time.time()
accidents_90 = program('accidents.txt', 0.9)
time_accidents.append(time.time() - start_time)
counts = counter(accidents_90)
accidents_len.append(counts)

start_time = time.time()
accidents_95 = program('accidents.txt', 0.95)
time_accidents.append(time.time() - start_time)
counts = counter(accidents_95)
accidents_len.append(counts)

print("retail, min support = 0.01")
order_by(ordered, pd.DataFrame(inspect(retail_1), columns = ['Set', 'Support']))

print("retail, min support = 0.03")
order_by(ordered, pd.DataFrame(inspect(retail_3), columns = ['Set', 'Support']))

print("retail, min support = 0.05")
order_by(ordered, pd.DataFrame(inspect(retail_5), columns = ['Set', 'Support']))

print("retail, min support = 0.1")
order_by(ordered, pd.DataFrame(inspect(retail_10), columns = ['Set', 'Support']))

print("retail, min support = 0.15")
order_by(ordered, pd.DataFrame(inspect(retail_15), columns = ['Set', 'Support']))

print("accidents, min support = 0.75")
order_by(ordered, pd.DataFrame(inspect(accidents_75), columns = ['Set', 'Support']))

print("accidents, min support = 0.8")
order_by(ordered, pd.DataFrame(inspect(accidents_80), columns = ['Set', 'Support']))

print("accidents, min support = 0.85")
order_by(ordered, pd.DataFrame(inspect(accidents_85), columns = ['Set', 'Support']))

print("accidents, min support = 0.9")
order_by(ordered, pd.DataFrame(inspect(accidents_90), columns = ['Set', 'Support']))

print("accidents, min support = 0.95")
order_by(ordered, pd.DataFrame(inspect(accidents_95), columns = ['Set', 'Support']))


fig, ax = plt.subplots()
ax.bar(["1%", "3%", "5%", "10%", "15%"], time_retail)
ax.set_facecolor('seashell')
fig.set_facecolor('floralwhite')
fig.set_figwidth(12)
fig.set_figheight(6)

plt.show()

fig, ax = plt.subplots()
ax.bar(["75%", "80%", "85%", "90%", "95%"], time_accidents)
ax.set_facecolor('seashell')
fig.set_facecolor('floralwhite')
fig.set_figwidth(12)
fig.set_figheight(6)

plt.show()


retail_len = list(map(list, zip(*retail_len)))
fig, ax = plt.subplots()
ax.bar(["1%", "3%", "5%", "10%", "15%"], retail_len[0])
ax.bar(["1%", "3%", "5%", "10%", "15%"], retail_len[1], bottom = retail_len[0])
ax.bar(["1%", "3%", "5%", "10%", "15%"], retail_len[2], bottom = add(retail_len[1], retail_len[0]))
ax.bar(["1%", "3%", "5%", "10%", "15%"], retail_len[3], bottom = add(retail_len[2],add(retail_len[1], retail_len[0])))
ax.set_facecolor('seashell')
fig.set_facecolor('floralwhite')
fig.set_figwidth(12)
fig.set_figheight(6)

plt.show()

accidents_len = list(map(list, zip(*accidents_len)))
fig, ax = plt.subplots()
ax.bar(["75%", "80%", "85%", "90%", "95%"], accidents_len[0])
ax.bar(["75%", "80%", "85%", "90%", "95%"], accidents_len[1], bottom = accidents_len[0])
ax.bar(["75%", "80%", "85%", "90%", "95%"], accidents_len[2], bottom = add(accidents_len[1],accidents_len[0]))
bottom = add(accidents_len[2],add(accidents_len[1],accidents_len[0]))
ax.bar(["75%", "80%", "85%", "90%", "95%"], accidents_len[3], bottom = bottom)
bottom = add(accidents_len[3],bottom)
ax.bar(["75%", "80%", "85%", "90%", "95%"], accidents_len[4], bottom = bottom)
bottom = add(accidents_len[4],bottom)
ax.bar(["75%", "80%", "85%", "90%", "95%"], accidents_len[5], bottom = bottom)
bottom = add(accidents_len[5],bottom)
ax.bar(["75%", "80%", "85%", "90%", "95%"], accidents_len[6], bottom = bottom)
ax.set_facecolor('seashell')
fig.set_facecolor('floralwhite')
fig.set_figwidth(12)
fig.set_figheight(6)

plt.show()

print("end")
