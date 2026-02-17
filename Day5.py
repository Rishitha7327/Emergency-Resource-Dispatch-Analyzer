n = int(input("Enter number of requests: "))

Requests = []

for i in range(n):
    value = int(input("Enter score:"))
    Requests.append(value)

low_demand = []
moderate_demand = []
high_demand = []
invalid_requests = []

Valid_count = 0
name  = input("Enter your Full-name: ")
L = len(name)

PLI = L % 3

for i in range(len(Requests)):
    demand = Requests[i]

    if demand < 0:
        print(f"Invalid request: {demand}")
        invalid_requests.append(demand)
    elif demand == 0:
        print(f"No demand: {demand}")
        Valid_count += 1
    elif 1 <= demand <= 20:
        print(f"Low demand: {demand}")
        low_demand.append(demand)
        Valid_count += 1
    elif 21 <= demand <= 50:
        print(f"Moderate demand: {demand}")
        moderate_demand.append(demand)
        Valid_count += 1
    elif demand == 50:
        print(f"High demand: {demand}")
        high_demand.append(demand)
        Valid_count += 1


Removed_count = 0

if PLI == 0:
    Removed_count = len(low_demand)
    low_demand = []
elif PLI == 1:
    Removed_count = len(moderate_demand)
    moderate_demand = []
else:
    Removed_count = len(low_demand) + len(high_demand)
    low_demand = []
    high_demand = []

print(f"Valid requests: {Valid_count}")
print(f"Removed requests: {Removed_count}")
print(f"Length of name: {L}")
print(f"PLI: {PLI}")

print("\nFinal Dispatch Report:")
print(f"Low Demand: {low_demand}")
print(f"Moderate Demand: {moderate_demand}")
print(f"High Demand: {high_demand}")
print(f"Invalid Requests: {invalid_requests}")



