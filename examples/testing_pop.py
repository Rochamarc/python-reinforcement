clubs = [ f'Club {i}' for i in range(1,5) ]

confrontation = []

for club in clubs:
	confrontation.append( [ [club, away ] for away in clubs if club != away ])

calendar = {}

for i in range(6):
	calendar[f'week {i + 1}'] = []

for _ in range(16):
	
