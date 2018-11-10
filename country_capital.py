cc = {"india" : "delhi","u.s.a" : "washington","nepal" : "katmandu","afganisthan" : "kabul","australia" : "canberra","canada":"ottawa"}
c = input('Country is ')
c1 = c.lower()
if c1 in cc:
	print("It's capital is ",cc[c1],".")
else:
	print("Country does not exist in database.")
