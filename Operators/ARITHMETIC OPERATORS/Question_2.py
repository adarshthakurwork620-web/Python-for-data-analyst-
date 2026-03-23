'''Take principal, rate, time and calculate simple interest.'''

principal= float(input("principal:"))
rate= float(input("Rate:"))/100
time= int(input("Time in second:"))

SI=principal*rate*time
print("simple interest =",SI)