from recommendation_data1 import 
from math import sqrt

def simScore(p1,p2):
	both = {}		
	for item in data[p1]:
		if item in data[p2]:
			both[item] = 1
		if len(both) == 0:
			return 0
		sum_ecli = []	

		for item in data[p1]:
			if item in data[p2]:
				sum_ecli.append(pow(data[p1][item] - data[p2][item],2))
		sum_ecli = sum(sum_ecli)

		return 1/(1+sqrt(sum_ecli))



def perCorrelation(p1,p2):
	both_rated = {}
	for item in data[p1]:
		if item in data[p2]:
			both_rated[item] = 1

	numOFrating = len(both_rated)		
	
	
	if numOFrating == 0:
		return 0

	p1prefSum = sum([data[p1][item] for item in both_rated])
	p2prefSum = sum([data[p2][item] for item in both_rated])

	
	p1_squareprefSum = sum([pow(data[p1][item],2) for item in both_rated])
	p2_squareprefSum = sum([pow(data[p2][item],2) for item in both_rated])

	
	prosumboth = sum([data[p1][item] * data[p2][item] for item in both_rated])

	
	n = prosumboth - (p1prefSum*p2prefSum/numOFrating)
	d = sqrt((p1_squareprefSum - pow(p1prefSum,2)/numOFrating) * (p2_squareprefSum -pow(p2prefSum,2)/numOFrating))
	if d == 0:
		return 0
	else:
		r = n/d
		return r 

def user_reommendations(person):

	
	totals = {}
	simSums = {}
	rankings_list =[]
	for other in data:
		
		if other == person:
			continue
		sim = perCorrelation(person,other)
		
		if sim <=0: 
			continue
		for item in data[other]:

			
			if item not in data[person] or data[person][item] == 0:

			
				totals.setdefault(item,0)
				totals[item] += data[other][item]* sim
				
				simSums.setdefault(item,0)
				simSums[item]+= sim

		
	rankings = [(total/simSums[item],item) for item,total in totals.items()]
	rankings.sort()
	rankings.reverse()
	
	rmlist = [(rmitem,score) for score,rmitem in rankings if score==5]
	return rmlist
		


if __name__ == '__main__':
	pno=raw_input('enter person number')
	pno=int(pno)
	print user_reommendations(pno)
	
