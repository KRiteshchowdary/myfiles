a = float(input('what is your age in years '))
h = float(input('what is your height in inches '))
w = float(input('what is your weight in KG '))
c = float(input('what is your chest size in cm '))
if a > 18 and a < 25:
	r = 1
else:
	print('Disqualified due to age not in range.',a)
	r = 0
if h > 5.2 and  h < 5.6:
	s = 1
else:
	print('Disqualified due to height not in range.',h)
	s = 0
if w > 45 and w <60:
	t = 1
else:
	print('Disqualified due to weight not in range.',w)
	t = 0
if c > 45:
	u = 1
else:
	print('Disqaulified due to chest size not in range.',c)
	u = 0
if r == 1 and s == 1 and t == 1 and u == 1:
	print('Congrats you are SELECTED.')
else:
	print('Sorry YOU ARE NOT SELECTED.Try next time.')
