
runners = ['daniel','pedro','juan','omar','luis']

print("Winners:")
for winner in runners[:3]:
     print(winner.title())

print("\nLosers:")
for losers in runners[3:]:
     print(losers.title())