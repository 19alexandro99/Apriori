import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
import time

ordered = 'Confidence'


def program(set_path, support_threshold, confidence_threshold):
    f = open(set_path, 'r')
    transacts = []
    lines = f.readlines()
    for line in lines:
        transacts.append(line.split())

    rule = apriori(transactions = transacts, min_support = support_threshold, min_confidence=confidence_threshold)

    output = list(rule) # returns a non-tabular output
    return output


def inspect(output):
    Rules = []
    confidence = []
    for result in output:
        data = result[2]
        for sample in data:
            if sample[0] and sample[1]:
                rule = "{" + ", ".join((sorted(list(sample[0])))) + "} -> {" + ", ".join((sorted(list(sample[1])))) + "}"
                Rules.append(rule)
                confidence.append(sample[2])
    return list(zip(Rules, confidence)), len(Rules)


def order_by(rule, data):
    if rule == "Confidence":
        print(data.sort_values(by="Confidence", ascending=False))
    elif rule == "Rule":
        print(data.sort_values(by="Rule"))


time_retail = []

start_time = time.time()
retail_70 = program('retail.txt', 0.01, 0.7)
time_retail.append(time.time() - start_time)


start_time = time.time()
retail_75 = program('retail.txt', 0.01, 0.75)
time_retail.append(time.time() - start_time)


start_time = time.time()
retail_80 = program('retail.txt', 0.01, 0.8)
time_retail.append(time.time() - start_time)


start_time = time.time()
retail_85 = program('retail.txt', 0.01, 0.85)
time_retail.append(time.time() - start_time)


start_time = time.time()
retail_90 = program('retail.txt', 0.01, 0.9)
time_retail.append(time.time() - start_time)


start_time = time.time()
retail_95 = program('retail.txt', 0.01, 0.95)
time_retail.append(time.time() - start_time)


time_accidents = []

start_time = time.time()
accidents_70 = program('accidents.txt', 0.8, 0.7)
time_accidents.append(time.time() - start_time)


start_time = time.time()
accidents_75 = program('accidents.txt', 0.8, 0.75)
time_accidents.append(time.time() - start_time)


start_time = time.time()
accidents_80 = program('accidents.txt', 0.8, 0.8)
time_accidents.append(time.time() - start_time)


start_time = time.time()
accidents_85 = program('accidents.txt', 0.8, 0.85)
time_accidents.append(time.time() - start_time)


start_time = time.time()
accidents_90 = program('accidents.txt', 0.8, 0.9)
time_accidents.append(time.time() - start_time)


start_time = time.time()
accidents_95 = program('accidents.txt', 0.8, 0.95)
time_accidents.append(time.time() - start_time)


retail_len = []
print("retail, min support = 0.01, min confidence = 0.7")
data, count = inspect(retail_70)
retail_len.append(count)
order_by(ordered, pd.DataFrame(data, columns = ['Rule', 'Confidence']))

print("retail, min support = 0.01, min confidence = 0.75")
data, count = inspect(retail_75)
retail_len.append(count)
order_by(ordered, pd.DataFrame(data, columns = ['Rule', 'Confidence']))

print("retail, min support = 0.01, min confidence = 0.8")
data, count = inspect(retail_80)
retail_len.append(count)
order_by(ordered, pd.DataFrame(data, columns = ['Rule', 'Confidence']))

print("retail, min support = 0.01, min confidence = 0.85")
data, count = inspect(retail_85)
retail_len.append(count)
order_by(ordered, pd.DataFrame(data, columns = ['Rule', 'Confidence']))

print("retail, min support = 0.01, min confidence = 0.9")
data, count = inspect(retail_90)
retail_len.append(count)
order_by(ordered, pd.DataFrame(data, columns = ['Rule', 'Confidence']))

print("retail, min support = 0.01, min confidence = 0.95")
data, count =inspect(retail_95)
retail_len.append(count)
order_by(ordered, pd.DataFrame(data, columns = ['Rule', 'Confidence']))

accidents_len = []
print("accidents, min support = 0.8, min confidence = 0.7")
data, count = inspect(accidents_70)
accidents_len.append(count)
order_by(ordered, pd.DataFrame(data, columns = ['Rule', 'Confidence']))

print("accidents, min support = 0.8, min confidence = 0.75")
data, count = inspect(accidents_75)
accidents_len.append(count)
order_by(ordered, pd.DataFrame(data, columns = ['Rule', 'Confidence']))

print("accidents, min support = 0.8, min confidence = 0.8")
data, count = inspect(accidents_80)
accidents_len.append(count)
order_by(ordered, pd.DataFrame(data, columns = ['Rule', 'Confidence']))

print("accidents, min support = 0.8, min confidence = 0.85")
data, count = inspect(accidents_85)
accidents_len.append(count)
order_by(ordered, pd.DataFrame(data, columns = ['Rule', 'Confidence']))

print("accidents, min support = 0.8, min confidence = 0.9")
data, count = inspect(accidents_90)
accidents_len.append(count)
order_by(ordered, pd.DataFrame(data, columns = ['Rule', 'Confidence']))

print("accidents, min support = 0.8, min confidence = 0.95")
data, count = inspect(accidents_95)
accidents_len.append(count)
order_by(ordered, pd.DataFrame(data, columns = ['Rule', 'Confidence']))


fig, ax = plt.subplots()
ax.bar(["70%", "75%", "80%", "85%", "90%", "95%"], time_retail)
ax.set_facecolor('seashell')
fig.set_facecolor('floralwhite')
fig.set_figwidth(12)
fig.set_figheight(6)

plt.show()

fig, ax = plt.subplots()
ax.bar(["70%", "75%", "80%", "85%", "90%", "95%"], time_accidents)
ax.set_facecolor('seashell')
fig.set_facecolor('floralwhite')
fig.set_figwidth(12)
fig.set_figheight(6)

plt.show()

fig, ax = plt.subplots()
ax.bar(["70%", "75%", "80%", "85%", "90%", "95%"], retail_len)
ax.set_facecolor('seashell')
fig.set_facecolor('floralwhite')
fig.set_figwidth(12)
fig.set_figheight(6)

plt.show()

fig, ax = plt.subplots()
ax.bar(["70%", "75%", "80%", "85%", "90%", "95%"], accidents_len)
ax.set_facecolor('seashell')
fig.set_facecolor('floralwhite')
fig.set_figwidth(12)
fig.set_figheight(6)

plt.show()

print("end")
