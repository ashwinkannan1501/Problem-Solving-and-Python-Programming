# Tower of Hanoi

total_disks = int(input("Enter the total number of disks : "))
source_tower =[]
auxilliary_tower = []
destination_tower = []
for disk in range(1, total_disks + 1):
    source_tower.append(disk)
print(f"Source Tower : {source_tower}")
print(f"Auxillary Tower : {auxilliary_tower}")
print(f"Destination Tower : {destination_tower}")

for disk in source_tower:
    auxilliary_tower.append(disk)
else :
    source_tower.clear()

for disk in auxilliary_tower:
    destination_tower.append(disk)
else : 
    auxilliary_tower.clear()

print(f"Source Tower : {source_tower}")
print(f"Auxillary Tower : {auxilliary_tower}")
print(f"Destination Tower : {destination_tower}")

