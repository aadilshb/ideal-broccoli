def can_traverse(gas, cost, start):
    n = len(gas)
    remaining = 0
    i = start
    started = False
    while i != start or not started:
        started = True
        remaining += gas[i] - cost[i]
        if remaining < 0:
            return False
        i = (i+1)%n
    return True
def gas_station1(gas, cost):
    for i in range(len(gas)):
        if can_traverse(gas, cost, i):
            return i
    return -1
def gas_station2(gas, cost):
    remaining = 0
    prev_remaining = 0
    candidate = 0
    for i in range(len(gas)):
        remaining += gas[i] - cost[i]
        if remaining < 0:
            candidate = i+1
            prev_remaining += remaining
            remaining = 0
    if candidate == len(gas) or remaining+prev_remaining < 0:
        return -1
    else:
        return candidate
    
gas=[1,5,3,3,5,3,1,3,4,5]
cost=[5,2,2,8,2,4,2,5,1,2]
print(gas_station1(gas,cost))
print(gas_station2(gas,cost))
