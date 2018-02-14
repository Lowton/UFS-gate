import config, sqlite
import random

print(random.randrange(251))

randomranks = [1,2,3,4,5,6,7,8,10,12,16,22,33,47,74,124,183,
               259,457,798,1080,3905]
rankid = 0

while sum((int(randomranks[i]) for i in range(0, int(len(randomranks))))) >= 1:
	randomlimit = sum((int(randomranks[i]) for i in range(0, int(len(randomranks)))))

	if randomlimit == 1:
		value = 1
	elif randomlimit > 1:
		value = random.randrange(1,randomlimit)

	print(randomlimit, value)
		
	curranks=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	for i in range(int(len(randomranks))):
		curranks[i] = sum(int(randomranks[i]) for i in range(0, i+1))
		#print(i, randomranks[i],curranks[i])
	print(curranks)
	print(randomranks)
	if value <= curranks[0]:
		print(rankid,'=',value, '(1)')
		sqlite.__addRank(rankid, '1')
		rankid += 1
		randomranks[0] -= 1
	elif curranks[0] < value <= curranks[1]:
		print(rankid,'=',value, '(2)')
		sqlite.__addRank(rankid, '2')
		rankid += 1
		randomranks[1] -= 1
	elif curranks[1] < value <= curranks[2]:
		print(rankid,'=',value, '(3)')
		sqlite.__addRank(rankid, '3')
		rankid += 1
		randomranks[2] -= 1
	elif curranks[2] < value <= curranks[3]:
		print(rankid,'=',value, '(4)')
		sqlite.__addRank(rankid, '4')
		rankid += 1
		randomranks[3] -= 1
	elif curranks[3] < value <= curranks[4]:
		print(rankid,'=',value, '(5)')
		sqlite.__addRank(rankid, '5')
		rankid += 1
		randomranks[4] -= 1
	elif curranks[4] < value <= curranks[5]:
		print(rankid,'=',value, '(6)')
		sqlite.__addRank(rankid, '6')
		rankid += 1
		randomranks[5] -= 1
	elif curranks[5] < value <= curranks[6]:
		print(rankid,'=',value, '(7)')
		sqlite.__addRank(rankid, '7')
		rankid += 1
		randomranks[6] -= 1
	elif curranks[6] < value <= curranks[7]:
		print(rankid,'=',value, '(8)')
		sqlite.__addRank(rankid, '8')
		rankid += 1
		randomranks[7] -= 1
	elif curranks[7] < value <= curranks[8]:
		print(rankid,'=',value, '(9)')
		sqlite.__addRank(rankid, '9')
		rankid += 1
		randomranks[8] -= 1
	elif curranks[8] < value <= curranks[9]:
		print(rankid,'=',value, '(10)')
		sqlite.__addRank(rankid, '10')
		rankid += 1
		randomranks[9] -= 1
	elif curranks[9] < value <= curranks[10]:
		print(rankid,'=',value, '(11)')
		sqlite.__addRank(rankid, '11')
		rankid += 1
		randomranks[10] -= 1
	elif curranks[10] < value <= curranks[11]:
		print(rankid,'=',value, '(12)')
		sqlite.__addRank(rankid, '12')
		rankid += 1
		randomranks[11] -= 1
	elif curranks[11] < value <= curranks[12]:
		print(rankid,'=',value, '(13)')
		sqlite.__addRank(rankid, '13')
		rankid += 1
		randomranks[12] -= 1
	elif curranks[12] < value <= curranks[13]:
		print(rankid,'=',value, '(14)')
		sqlite.__addRank(rankid, '14')
		rankid += 1
		randomranks[13] -= 1
	elif curranks[13] < value <= curranks[14]:
		print(rankid,'=',value, '(15)')
		sqlite.__addRank(rankid, '15')
		rankid += 1
		randomranks[14] -= 1
	elif curranks[14] < value <= curranks[15]:
		print(rankid,'=',value, '(16)')
		sqlite.__addRank(rankid, '16')
		rankid += 1
		randomranks[15] -= 1
	elif curranks[15] < value <= curranks[16]:
		print(rankid,'=',value, '(17)')
		sqlite.__addRank(rankid, '17')
		rankid += 1
		randomranks[16] -= 1
	elif curranks[16] < value <= curranks[17]:
		print(rankid,'=',value, '(18)')
		sqlite.__addRank(rankid, '18')
		rankid += 1
		randomranks[17] -= 1
	elif curranks[17] < value <= curranks[18]:
		print(rankid,'=',value, '(19)')
		sqlite.__addRank(rankid, '19')
		rankid += 1
		randomranks[18] -= 1
	elif curranks[18] < value <= curranks[19]:
		print(rankid,'=',value, '(20)')
		sqlite.__addRank(rankid, '20')
		rankid += 1
		randomranks[19] -= 1	
	elif curranks[19] < value <= curranks[20]:
		print(rankid,'=',value, '(21)')
		sqlite.__addRank(rankid, '21')
		rankid += 1
		randomranks[20] -= 1
	elif curranks[20] < value <= curranks[21]:
		print(rankid,'=',value, '(22)')
		sqlite.__addRank(rankid, '22')
		rankid += 1
		randomranks[21] -= 1
	else: print(rankid,'=',value, 'Error')

print(randomranks)
