import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn_extra.cluster import KMedoids
import random
import copy


def load_data(path):
    f = open(path, 'r')
    transacts = []
    lines = f.readlines()
    for line in lines:
        transacts.append(line.split(','))
    return transacts


def algoritm_kmeans(clusters, data):
    model = KMeans(n_clusters=clusters)
    model.fit(data)
    return model.inertia_, model.labels_


def algoritm_kmedoids(clusters, data):
    model = KMedoids(n_clusters=clusters)
    model.fit(data)
    return model.inertia_, model.labels_


def generate_noise(data, noise):
    new_data = copy.deepcopy(data)
    to_change = int(len(data) * noise)
    if to_change > 0:
        indexes = [i for i in range(0, len(new_data)-1)]
        ix_to_change = random.sample(indexes, to_change)
        for i in range(len(ix_to_change)):
            l = new_data[ix_to_change[i]]
            for j in range(len(l)):
                sign = random.randint(0,1)
                if sign == 0:
                    l[j] = l[j] - random.uniform(0.1, 50.0)
                else:
                    l[j] = l[j] + random.uniform(0.1, 50.0)
            new_data[ix_to_change[i]] = l
    return new_data


def output_results(data, set_name, method_name):
    labels_list = []
    sse_list = []
    for i in range(3, 10):
        if method_name == "kmeans":
            sse, labels = algoritm_kmeans(i, data)
        else:
            sse, labels = algoritm_kmedoids(i, data)
        sse_list.append(sse)
        labels_list.append(labels)
        print(set_name,", ", method_name,", ", i, " clusters")
        print("Координаты точек:", data, "\n", "Назначенные кластера:", labels, "\n",
              "Значение ошибки кластеризации", sse)
    if set_name == "iris":
        sepal_length = []
        sepal_width = []
        for item in data:
            sepal_length.append(item[0])
            sepal_width.append(item[1])
        for label in labels_list:
            plt.xlabel("sepal length (cm)")
            plt.ylabel("sepal width (cm)")
            plt.scatter(sepal_length, sepal_width, c=label)
            plt.show()
    else:
        age = []
        income = []
        yearsemployed = []
        for item in data:
            age.append(item[0])
            income.append(item[3])
            yearsemployed.append(item[2])
        for label in labels_list:
            ax = plt.axes(projection="3d")
            plt.xlabel("income")
            plt.ylabel("age")
            ax.scatter(income, age, yearsemployed, c=label)
            plt.show()

    plt.xlabel("Number of clusters")
    plt.ylabel("SSE")
    plt.plot([3, 4, 5, 6, 7, 8, 9], sse_list)
    plt.show()


customers_data = load_data("customers.csv")
customers_labels = customers_data[0]
customers_data.pop(0)
data1 = []

for item in customers_data:
    data1.append([float(item[2]), float(item[3]), float(item[4]), float(item[5]),float(item[6]),float(item[7]),float(item[9])])

iris_data = load_data("iris.data")
iris_data.pop()
target = []
data2 = []
for item in iris_data:
    target.append(item[4])
    data2.append([float(item[0]),float(item[1]), float(item[2]), float(item[3])])


output_results(data2, "iris", "kmeans")
output_results(data2, "iris", "kmedoids")
output_results(data1, "customers", "kmeans")
output_results(data1, "customers", "kmedoids")

noise_data2_1 = generate_noise(data2, 0.01)
noise_data2_3 = generate_noise(data2, 0.03)
noise_data2_5 = generate_noise(data2, 0.05)
noise_data2_10 = generate_noise(data2, 0.1)

noise_data1_1 = generate_noise(data1, 0.01)
noise_data1_3 = generate_noise(data1, 0.03)
noise_data1_5 = generate_noise(data1, 0.05)
noise_data1_10 = generate_noise(data1, 0.1)

output_results(noise_data2_1, "iris", "kmeans")
output_results(noise_data2_1, "iris", "kmedoids")
output_results(noise_data1_1, "customers", "kmeans")
output_results(noise_data1_1, "customers", "kmedoids")

output_results(noise_data2_3, "iris", "kmeans")
output_results(noise_data2_3, "iris", "kmedoids")
output_results(noise_data1_3, "customers", "kmeans")
output_results(noise_data1_3, "customers", "kmedoids")

output_results(noise_data2_5, "iris", "kmeans")
output_results(noise_data2_5, "iris", "kmedoids")
output_results(noise_data1_5, "customers", "kmeans")
output_results(noise_data1_5, "customers", "kmedoids")

output_results(noise_data2_10, "iris", "kmeans")
output_results(noise_data2_10, "iris", "kmedoids")
output_results(noise_data1_10, "customers", "kmeans")
output_results(noise_data1_10, "customers", "kmedoids")