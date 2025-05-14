def time(str):
    time_parts = str.split(':')
    hou = int(time_parts[0])
    mminu = int(time_parts[1])
    return hou * 60 + mminu
def custom_sort(trains, N):
    for i in range(N - 1):
        for j in range(N - i - 1):
            if (trains[j][0] > trains[j + 1][0]):
                trains[j], trains[j + 1] = trains[j + 1], trains[j]
            elif (trains[j][0] == trains[j + 1][0] and trains[j][1] < trains[j + 1][1]):
                trains[j], trains[j + 1] = trains[j + 1], trains[j]
            elif (trains[j][0] == trains[j + 1][0] and trains[j][1] == trains[j + 1][1] and trains[j][2] > trains[j + 1][2]):
                trains[j], trains[j + 1] = trains[j + 1], trains[j]
N = int(input().strip())
trains = []
for index in range(N):
    line = input().strip()
    
    parts = line.split(" at ")
    name = parts[0].split(" will departure for ")[0]
    dep = parts[1]

    trains.append((name, time(dep), index, line))
custom_sort(trains, N)
for i in trains:
    print(i[3])

