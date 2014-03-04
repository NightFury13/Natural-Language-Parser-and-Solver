import nltk	
import sys

# function to add the contents of file, after proper parsing, to the given dictionary
def add_to_dict(dictionary, fname):
	f = open(fname, 'r')
	for line in f:
		temp = line[:-1]
		temp = temp.split(',')
		a = temp[0]
		b = temp[1:]
		if a not in dictionary:
			dictionary[a] = b

def addteam_to_dict(dictionary, fname):
	f = open(fname, 'r')
	for line in f:
		temp = line[:-1]
		temp = temp.split('\t')
		a = temp[0]
		b = temp[1:]
		if a not in dictionary:
			dictionary[a] = b

def add_to_list(arr, fname):
	f = open(fname, 'r')
	c = []
	for line in f:
		b = []
		temp = line[:-1]
		temp = temp.split(',')
		for i in temp:
			b.append(i)
		c.append(b)
	arr.append(c)

# Returns list of teams the mom belongs to.
def parse_for_momTeam(mom):
	toreturn = []

	for i in mom:
		temp = mom[i]
		toreturn.append(temp[0])
	return toreturn

# Returns list of winning teams.
def parse_for_wonby(wonby):
	toreturn = []

	for i in wonby:
		toreturn.append(i)
	return toreturn

def parse_for_duck(bat, team):
	toreturn = []
	
	for i in bat:
		if i in team:
			if bat[i][1] == "0":
				toreturn.append(i)
	return toreturn
		
def parse_for50(bat):
	toreturn = []
	
	for i in bat:
		if bat[i] and int(bat[i][1]) > 50:
			toreturn.append(i)
	return toreturn

def parse_forWicket(bowl):
	toreturn = []

	for i in bowl:
		if bowl[i] and int(bowl[i][3]) == 0:
			toreturn.append(i)
	return toreturn

def parse_forSR(bat):
	toreturn = []

	for i in bat:
		if bat[i] and float(bat[i][6]) > 200.0:
			toreturn.append(i)
	return toreturn

def parse_for64(bat):
	toreturn = []

	for i in bat:
		if bat[i] and int(bat[i][4]) < int(bat[i][5]):
			toreturn.append(i)
	return toreturn

def parse_for7ov(bowl):
	toreturn = []

	for i in bowl:
		if bowl[i] and float(bowl[i][0]) > 7:
			toreturn.append(i)
	return toreturn

def parse_for0w(bowl):
	toreturn = []

	for i in bowl:
		if bowl[i] and int(bowl[i][3]) == 0:
			toreturn.append(i)
	return toreturn

def parse_for8ec(bowl):
	toreturn = []

	for i in bowl:
		if bowl[i] and float(bowl[i][4]) > 8:
			toreturn.append(i)
	return toreturn

def parse_for100(bat):
	toreturn= []

	for i in bat:
		if bat[i] and int(bat[i][1]) > 100:
			toreturn.append(i)
	return toreturn

def parse_forTeam(team):
	toreturn = []

	for i in team:
		toreturn.append(i)
	return toreturn

def parse_forLR(bowl, nzplayer, inplayer):
	toreturn = []

	l_wic = r_wic = 0

	for i in bowl:
		if i in nzplayer:
			if nzplayer[i][6][0] == "L":
				l_wic += int(bowl[i][3])
			elif nzplayer[i][6][0] == "R":
				r_wic += int(bowl[i][3])
		elif i in inplayer:
			if inplayer[i][6][0] == "L":
				l_wic += int(bowl[i][3])
			elif inplayer[i][6][0] == "R":
				r_wic += int(bowl[i][3])
	
	if r_wic > l_wic:
		toreturn.append("yes")
	return toreturn

def parse_forAge26(team):
	toreturn = []

	for i in team:
		if int(team[i][2][0]+team[i][2][1]) < 26:
			toreturn.append(i)
	return toreturn

def parse_for250(bat1, bat2, bat3, bat4, bat5):
	toreturn = []

	c = [bat1, bat2, bat3, bat4, bat5]

	runs = {}
	for i in c:
		if i:
			for j in i:
				runs[j] = 0
	for i in c:
		if i:
			for j in i:
				runs[j] += int(i[j][1])

	for i in runs:
		if runs[i] > 250:
			toreturn.append(i)
	return toreturn

def parse_forNoDuck(bat1, bat2, bat3, bat4, bat5):
	toreturn = []

	c = [bat1, bat2, bat3, bat4, bat5]
	
	flag = {}
	for i in c:
		if i:
			for j in i:
				flag[j] = 0

	for i in c:
		if i:
			for j in i:
				if int(i[j][1]) == 0:
					flag[j] = 1
	
	for i in flag:
		if flag[i] == 0:
			toreturn.append(i)
	return toreturn

def parse_forPlay(bat, bowl):
	toreturn = []

	temp = {}
	count = 0
	for i in bat:
		if i not in temp:
			temp[count] = i
			count += 1
	for i in bowl:
		if i not in temp:
			temp[count] = i
			count += 1
	for i in temp:
		toreturn.append(temp[i])
	return toreturn

def solve_forWide(bowl1, bowl2, bowl3, bowl4, bowl5):

	c = [bowl1, bowl2, bowl3, bowl4, bowl5]

	is_wide = jad_wide = 0
	ish = 'I Sharma'
	jad = 'RA Jadeja'
	for i in c:
		if i:
			if ish in i:
				if len(i[ish]) == 6:
					is_wide += int(i[ish][5][0])
			if jad in i:
				if len(i[jad]) == 6:
					jad_wide += int(i[jad][5][0])
	
	if is_wide > jad_wide:
		return True
	else:
		return False

def solve_forCatch(bat1, bat2, bat3, bat4, bat5):

	c = [bat1, bat2, bat3, bat4, bat5]

	sou_cat = ryd_cat = 0
	sou = 'Southee'
	ryd = 'Ryder'

	for i in c:
		if i:
			for j in i:
				temp = i[j][0]
				temp = temp.split(' ')
				if sou == temp[1]:
					sou_cat += 1
				elif ryd == temp[1]:
					ryd_cat += 1

	if sou_cat > ryd_cat:
		return True
	else:
		return False

def solve_forMan(mom1, mom2, mom3, mom4, mom5):

	c = [mom1, mom2, mom3, mom4, mom5]

	temp = {}
	for i in c:
		if i:
			for j in i:
				if j in temp:
					return True
				else:
					temp[j] = i[j]
	return False

def solve_forBetBowl(bo11,bo12,bo21,bo22,bo31,bo32,bo41,bo42,bo51,bo52):

	c1 = [bo11,bo21,bo31,bo41,bo51]
	c2 = [bo12,bo22,bo32,bo42,bo52]
	
	jad = 'RA Jadeja'
	in1 = in2 = 0

	for i in c1:
		if i:
			if jad in i:
				in1 += ((int(i[jad][1])*100)+(int(i[jad][2])*-1)+(int(i[jad][3])*10))/int(i[jad][0])

	for i in c2:
		if i:
			if jad in i:
				in2 += ((int(i[jad][1])*100)+(int(i[jad][2])*-1)+(int(i[jad][3])*10))/int(i[jad][0])
	if in1 > in2:
		return True
	else:
		return False

def parse_forHardHit(bat1, bat2, bat3, bat4, bat5, pl):

	c = [bat1, bat2, bat3, bat4, bat5]

	sr = 0
	count = 0
	for i in c:
		if i:
			if pl in i:
				sr += float(i[pl][6])
				count += 1
	sr = sr/count
	return sr

def parse_forGoodBowl(c, pl):

	p = 0

	for i in c:
		if i:
			if pl in i:
				p += ((int(i[pl][1])*100)+(int(i[pl][2])*-1)+(int(i[pl][3])*10))/int(i[pl][0])

	return pl

def parse_forBetBat(bat11,bat12,bat21,bat22,bat31,bat32,bat41,bat42,bat51,bat52, order):

	val = 0
	count = 0
	c = [bat11[0],bat12[0],bat21[0],bat22[0],bat31[0],bat32[0],bat41[0],bat42[0],bat51[0],bat52[0]]
	for j in c:
		for i in order:
			if j[i]:
				val += (float(j[i][2])+float(j[i][7]))
				count += 1
	val = val/count
	return val

def solve_forSame(c):

#c = [m1,m2,m3,m4,m5]
#m1 = [win1, t1]

	for i in c:
		if i:
			for x in i[0]:
				for y in i[1]:
					if x!=y:
						return False
	return True

# the function to make the model and answer the query, given the properly formatted strings
def make_model_and_answer(v, query, dt):
	val = nltk.parse_valuation(v)
	dom = val.domain

	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])
	print "The answer for the query is : ",
	print m.evaluate(query, g)

# query generator for q1.
def generate_and_solve_query1(mom, wonby):
	
	#for query1 (mom by winning team)
	c1 = parse_for_momTeam(mom)
	c2 = parse_for_wonby(wonby)

	#print c1
	#print c2

	#Now constructing strings which are needed to create the model:

	#first creating mapping from playername to variable: we create a temporary dictionary
	# For example,
	# MS Dhoni => r1
	# SK Raina => r2

	name_to_var = {}
	count = 0
	for i in c1:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	name_to_var['Tie'] = 'r' + str(count)

	# Now for creating a Model, we need to write down a string which shows mapping from predicates to varible names
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'

	temp_strin2 = 'momTeam => {'
	fl = 0
	for i in c1:
		temp_strin2 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'


	temp_strin3 = 'wonby => {'
	fl = 0
	for i in c2:
		temp_strin3 += name_to_var[i] + ','
		fl = 1
	if fl == 1:
		temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'


	v = temp_strin1 + temp_strin2 + temp_strin3
	#print v

	# now forming the query
	query = 'all x. (momTeam(x) & wonby(x))'

	make_model_and_answer(v, query, name_to_var)

def generate_and_solve_query2(win1, win2, win3, win4, win5, bat1, bat2, bat3, bat4, bat5, inplayer, nzplayer):
	
	npl = []
	for i in nzplayer:
		npl.append(i)
	ipl = []
	for i in inplayer:
		ipl.append(i)

	p1 = p2 = p3 = p4 = p5 = []

	w1 = parse_for_wonby(win1)
	b1 = []
	if w1[0] == 'India':
		b1 = parse_for_duck(bat1,nzplayer)
		p1 = npl		
	elif w1[0] == 'New Zealand':
		b1 = parse_for_duck(bat1,inplayer)
		p1 = ipl

	w2 = parse_for_wonby(win2)
	b2 = []
	if w2[0] == 'India':
		b2 = parse_for_duck(bat2,nzplayer)
		p2 = npl
	elif w2[0] == 'New Zealand':
		b2 = parse_for_duck(bat2,inplayer)
		p2 = ipl

	w3 = parse_for_wonby(win3)
	b3 = []
	if w3[0] == 'India':
		b3 = parse_for_duck(bat3,nzplayer)
		p3 = npl
	elif w3[0] == 'New Zealand':
		b3 = parse_for_duck(bat3,inplayer)
		p3 = ipl
	
	w4 = parse_for_wonby(win4)
	b4 = []
	if w4[0] == 'India':
		b4 = parse_for_duck(bat4,nzplayer)
		p4 = npl
	elif w4[0] == 'New Zealand':
		b4 = parse_for_duck(bat4,inplayer)
		p4 = ipl
	
	w5 = parse_for_wonby(win5)
	b5 = []
	if w5[0] == 'India':
		b5 = parse_for_duck(bat5,nzplayer)
		p5 = npl
	elif w5[0] == 'New Zealand':
		b5 = parse_for_duck(bat5,inplayer)
		p5 = ipl
	
	c=[b1, b2, b3, b4, b5]

	name_to_var = {}
	count = 0
	for i in c:
		if i and i[0] not in name_to_var:
			name_to_var[i[0]] = 'r' + str(count)
			count += 1
	
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'

	temp_strin2 = ''
	temp_strin3 = ''
	temp_strin4 = ''
	temp_strin5 = ''
	temp_strin6 = ''
	if b1:		
		temp_strin2 = 'duckLose1 => {'+name_to_var[b1[0]]+'} \n'
	else:
		temp_strin2 = 'duckLose1 => {}\n'
	if b2:		
		temp_strin3 = 'duckLose2 => {'+name_to_var[b2[0]]+'} \n'
	else:
		temp_strin3 = 'duckLose2 => {}\n'
	if b3:		
		temp_strin4 = 'duckLose3 => {'+name_to_var[b3[0]]+'} \n'
	else:
		temp_strin4 = 'duckLose3 => {}\n'
	if b4:		
		temp_strin5 = 'duckLose4 => {'+name_to_var[b4[0]]+'} \n'
	else:
		temp_strin5 = 'duckLose4 => {}\n'
	if b5:		
		temp_strin6 = 'duckLose5 => {'+name_to_var[b5[0]]+'} \n'
	else:
		temp_strin6 = 'duckLose5 => {}\n'

	
	temp_strin7 = 'pl1 => {'
	fl = 0 
	for i in p1:
		if i in name_to_var:
			temp_strin7 += name_to_var[i] + ','
			fl = 1
	if fl == 1:
		temp_strin7 = temp_strin7[:-1]
	temp_strin7 += '} \n'

	temp_strin8 = 'pl2 => {'
	fl = 0
	for i in p2:
		if i in name_to_var:
			temp_strin8 += name_to_var[i] + ','
			fl =1
	if fl == 1:
		temp_strin8 = temp_strin8[:-1]
	temp_strin8 += '} \n'

	temp_strin9 = 'pl3 => {'
	fl = 0
	for i in p3:
		if i in name_to_var:
			temp_strin9 += name_to_var[i] + ','
			fl = 1
	if fl == 1:
		temp_strin9 = temp_strin9[:-1]
	temp_strin9 += '} \n'

	temp_strin10 = 'pl4 => {'
	fl = 0 
	for i in p4:
		if i in name_to_var:
			temp_strin10 += name_to_var[i] + ','
			fl = 1
	if fl == 1:
		temp_strin10 = temp_strin10[:-1]
	temp_strin10 += '} \n'

	temp_strin11 = 'pl5 => {'
	fl = 0
	for i in p5:
		if i in name_to_var:
			temp_strin11 += name_to_var[i] + ','
			fl = 1
	if fl == 1:
		temp_strin11 = temp_strin11[:-1]
	temp_strin11 += '} \n'

	v = temp_strin1 + temp_strin2 + temp_strin3 + temp_strin4 + temp_strin5 + temp_strin6 + temp_strin7 + temp_strin8 + temp_strin9 + temp_strin10+ temp_strin11
	#print v
	
#	v = "match1 => m1\nabc => {}\n"
#	query = '(exists x. abc(x))'

	# now forming the query
	query = '(exists x.(duckLose1(x)&pl1(x))) & (exists a.(duckLose2(a)&pl2(a))) & (exists b.(duckLose3(b)&pl3(b))) & (exists c.(duckLose4(c)&pl4(c))) & (exists d.(duckLose5(d)&pl5(d)))'

	make_model_and_answer(v, query, name_to_var)

def generate_and_solve_query3(bat1, bat2, bat3, bat4, bat5):

	a1 = parse_forSR(bat1)
	a2 = parse_forSR(bat2)
	a3 = parse_forSR(bat3)
	a4 = parse_forSR(bat4)
	a5 = parse_forSR(bat5)
	
	b1 = parse_for64(bat1)
	b2 = parse_for64(bat2)
	b3 = parse_for64(bat3)
	b4 = parse_for64(bat4)
	b5 = parse_for64(bat5)

	c1 = [a1, a2, a3, a4, a5, b1, b2, b3, b4, b5]
	
	name_to_var = {}
	count = 0
	for i in c1:
		if i:
			for j in i:
				if j not in name_to_var:
					name_to_var[j] = 'r' + str(count)
					count += 1
	
	temp_strin0 = ''
	for i in name_to_var:
		temp_strin0 += i + ' => ' + name_to_var[i] + '\n'

	temp_strin1 = 'sr1 => {'
	fl = 0
	for i in a1:
		temp_strin1 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin1 = temp_strin1[:-1]  #removing the extra "," character
	temp_strin1 += '} \n'

	temp_strin2 = 'sr2 => {'
	fl = 0 
	for i in a2:
		temp_strin2 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'

	temp_strin3 = 'sr3 => {'
	fl = 0
	for i in a3:
		temp_strin3 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin3 = temp_strin3[:-1]  #removing the extra "," character
	temp_strin3 += '} \n'

	temp_strin4 = 'sr4 => {'
	fl = 0
	for i in a4:
		temp_strin4 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin4 = temp_strin4[:-1]  #removing the extra "," character
	temp_strin4 += '} \n'

	temp_strin5 = 'sr5 => {'
	fl = 0
	for i in a5:
		temp_strin5 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin5 = temp_strin5[:-1]  #removing the extra "," character
	temp_strin5 += '} \n'

	temp_strin6 = '64_1 => {'
	fl = 0 
	for i in b1:
		temp_strin6 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin6 = temp_strin6[:-1]  #removing the extra "," character
	temp_strin6 += '} \n'

	temp_strin7 = '64_2 => {'
	fl = 0
	for i in b2:
		temp_strin7 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin7 = temp_strin7[:-1]  #removing the extra "," character
	temp_strin7 += '} \n'

	temp_strin8 = '64_3 => {'
	fl = 0
	for i in b3:
		temp_strin8 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin8 = temp_strin8[:-1]  #removing the extra "," character
	temp_strin8 += '} \n'

	temp_strin9 = '64_4 => {'
	fl = 0
	for i in b4:
		temp_strin9 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin9 = temp_strin9[:-1]  #removing the extra "," character
	temp_strin9 += '} \n'

	temp_strin10 = '64_5 => {'
	fl = 0
	for i in b5:
		temp_strin10 += name_to_var[i] +  ','
		fl = 1
	if fl==1:
		temp_strin10 = temp_strin10[:-1]  #removing the extra "," character
	temp_strin10 += '} \n'

	v = temp_strin0 + temp_strin1 + temp_strin2 + temp_strin3 + temp_strin4 + temp_strin5 + temp_strin6 + temp_strin7 + temp_strin8 + temp_strin9 + temp_strin10

	query = '(all a.(sr1(a)&64_1(a))) &(all b.(sr2(b)&64_2(b))) &(all c.(sr3(c)&64_3(c))) &(all d.(sr4(d)&64_4(d))) &(all e.(sr5(e)&64_5(e)))'

	make_model_and_answer(v, query, name_to_var)

def generate_and_solve_query4(win1, win2, win3, win4, win5, bat1, bat2, bat3, bat4, bat5, nzplayer, inplayer):

	c = [win1, win2, win3, win4, win5]
	b = [bat1, bat2, bat3, bat4, bat5]

	ans = [0,0,0,0,0]

	count = 0
	for i in c:
		for j in i:
			if j=='New Zealand':
				for k in b[count]:
					if k in nzplayer:
						if int(b[count][k][4]) > 0 and float(b[count][k][6]) < 100.0:
							ans[count] = 1
			elif j=='India':
				for k in b[count]:
					if k in inplayer:
						if int(b[count][k][4]) > 0 and float(b[count][k][6]) < 100.0:
							ans[count] = 1
	fl = 0
	for i in ans:
		if i == 0:
			print "False"
			fl = 1
			break
	if fl == 0:
		print "True"

def generate_and_solve_query5(bat1, bat2, bat3, bat4, bat5, bowl1, bowl2, bowl3, bowl4, bowl5):

	m1 = parse_for50(bat1)
	m2 = parse_for50(bat2)
	m3 = parse_for50(bat3)
	m4 = parse_for50(bat4)
	m5 = parse_for50(bat5)
	
	n1 = parse_forWicket(bowl1)
	n2 = parse_forWicket(bowl2)
	n3 = parse_forWicket(bowl3)
	n4 = parse_forWicket(bowl4)
	n5 = parse_forWicket(bowl5)

	c1 = [m1, m2, m3, m4, m5, n1, n2, n3, n4 ,n5]

	name_to_var = {}
	count = 0
	for i in c1:
		if i:
			for j in i:
				if j not in name_to_var:
					name_to_var[j] = 'r' + str(count)
					count += 1
	
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'

	temp_strin2 = 'bat50_1 => {'
	fl = 0
	for i in m1:
		temp_strin2 += name_to_var[i] +  ','
		fl = 1
	if fl==1:
		temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	
	temp_strin3 = 'bat50_2 => {'
	fl = 0
	for i in m2:
		temp_strin3 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin3 = temp_strin3[:-1]  #removing the extra "," character
	temp_strin3 += '} \n'
	
	temp_strin4 = 'bat50_3 => {'
	fl = 0
	for i in m3:
		temp_strin4 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin4 = temp_strin4[:-1]  #removing the extra "," character
	temp_strin4 += '} \n'
	
	temp_strin5 = 'bat50_4 => {'
	fl = 0
	for i in m4:
		temp_strin5 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin5 = temp_strin5[:-1]  #removing the extra "," character
	temp_strin5 += '} \n'
	
	temp_strin6 = 'bat50_5 => {'
	fl = 0
	for i in m5:
		temp_strin6 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin6 = temp_strin6[:-1]  #removing the extra "," character
	temp_strin6 += '} \n'
	
	temp_strin21 = 'bowl1_1 => {'
	fl = 0
	for i in n1:
		temp_strin21 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin21 = temp_strin21[:-1]  #removing the extra "," character
	temp_strin21 += '} \n'
	
	temp_strin31 = 'bowl1_2 => {'
	fl = 0
	for i in n2:
		temp_strin31 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin31 = temp_strin31[:-1]  #removing the extra "," character
	temp_strin31 += '} \n'
	
	temp_strin41 = 'bowl1_3 => {'
	fl = 0
	for i in n3:
		temp_strin41 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin41 = temp_strin41[:-1]  #removing the extra "," character
	temp_strin41 += '} \n'
	
	temp_strin51 = 'bowl1_4 => {'
	fl = 0
	for i in n4:
		temp_strin51 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin51 = temp_strin51[:-1]  #removing the extra "," character
	temp_strin51 += '} \n'
	
	temp_strin61 = 'bowl1_5 => {'
	fl = 0
	for i in n5:
		temp_strin61 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin61 = temp_strin61[:-1]  #removing the extra "," character
	temp_strin61 += '} \n'
	
	v = temp_strin1 + temp_strin2 + temp_strin3 + temp_strin4 + temp_strin5 + temp_strin6 + temp_strin21 + temp_strin31 + temp_strin41 + temp_strin51 + temp_strin61

	query = "exists x. (bat50_1(x) & bowl1_1(x)) | (bat50_2(x) & bowl1_2(x)) | (bat50_3(x) & bowl1_3(x)) | (bat50_4(x) & bowl1_4(x)) | (bat50_5(x) & bowl1_5(x))"

	make_model_and_answer(v, query, name_to_var)

def generate_and_solve_query6(b11, b12, b21, b22, b31, b32, b41, b42, b51, b52):
	
	m11 = parse_for7ov(b11)
	m12 = parse_for7ov(b12)
	m21 = parse_for7ov(b21)
	m22 = parse_for7ov(b22)
	m31 = parse_for7ov(b31)
	m32 = parse_for7ov(b32)
	m41 = parse_for7ov(b41)
	m42 = parse_for7ov(b42)
	m51 = parse_for7ov(b51)
	m52 = parse_for7ov(b52)

	n11 = parse_for0w(b11)
	n12 = parse_for0w(b12)
	n21 = parse_for0w(b21)
	n22 = parse_for0w(b22)
	n31 = parse_for0w(b31)
	n32 = parse_for0w(b32)
	n41 = parse_for0w(b41)
	n42 = parse_for0w(b42)
	n51 = parse_for0w(b51)
	n52 = parse_for0w(b52)

	c1 = [m11,m12,m21,m22,m31,m32,m41,m42,m51,m52,n11,n12,n21,n22,n31,n32,n41,n42,n51,n52]

	name_to_var = {}
	count = 0
	for i in c1:
		if i:
			for j in i:
				if j not in name_to_var:
					name_to_var[j] = 'r' + str(count)
					count += 1
	
	temp_strin0 = ''
	for i in name_to_var:
		temp_strin0 += i + ' => ' + name_to_var[i] + '\n'

	temp_strin11 = 'm11_7 => {'
	fl = 0
	for i in m11:
		temp_strin11 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin11 = temp_strin11[:-1]  #removing the extra "," character
	temp_strin11 += '} \n'

	temp_strin12 = 'm12_7 => {'
	fl = 0
	for i in m12:
		temp_strin12 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin12 = temp_strin12[:-1]  #removing the extra "," character
	temp_strin12 += '} \n'

	temp_strin21 = 'm21_7 => {'
	fl = 0
	for i in m21:
		temp_strin21 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin21 = temp_strin21[:-1]  #removing the extra "," character
	temp_strin21 += '} \n'

	temp_strin22 = 'm22_7 => {'
	fl = 0
	for i in m22:
		temp_strin22 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin22 = temp_strin22[:-1]  #removing the extra "," character
	temp_strin22 += '} \n'

	temp_strin31 = 'm31_7 => {'
	fl = 0
	for i in m31:
		temp_strin31 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin31 = temp_strin31[:-1]  #removing the extra "," character
	temp_strin31 += '} \n'

	temp_strin32 = 'm32_7 => {'
	fl = 0
	for i in m32:
		temp_strin32 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin32 = temp_strin32[:-1]  #removing the extra "," character
	temp_strin32 += '} \n'

	temp_strin41 = 'm41_7 => {'
	fl = 0
	for i in m41:
		temp_strin41 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin41 = temp_strin41[:-1]  #removing the extra "," character
	temp_strin41 += '} \n'

	temp_strin42 = 'm42_7 => {'
	fl = 0
	for i in m42:
		temp_strin42 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin42 = temp_strin42[:-1]  #removing the extra "," character
	temp_strin42 += '} \n'

	temp_strin51 = 'm51_7 => {'
	fl = 0
	for i in m51:
		temp_strin51 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin51 = temp_strin51[:-1]  #removing the extra "," character
	temp_strin51 += '} \n'

	temp_strin52 = 'm52_7 => {'
	fl = 0
	for i in m52:
		temp_strin52 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin52 = temp_strin52[:-1]  #removing the extra "," character
	temp_strin52 += '} \n'

	temp_strin101 = 'n11_0 => {'
	fl = 0
	for i in n11:
		temp_strin101 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin101 = temp_strin101[:-1]  #removing the extra "," character
	temp_strin101 += '} \n'

	temp_strin102 = 'n12_0 => {'
	fl = 0
	for i in n12:
		temp_strin102 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin102 = temp_strin102[:-1]  #removing the extra "," character
	temp_strin102 += '} \n'

	temp_strin201 = 'n21_0 => {'
	fl = 0
	for i in n21:
		temp_strin201 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin201 = temp_strin201[:-1]  #removing the extra "," character
	temp_strin201 += '} \n'

	temp_strin202 = 'n22_0 => {'
	fl = 0
	for i in n22:
		temp_strin202 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin202 = temp_strin202[:-1]  #removing the extra "," character
	temp_strin202 += '} \n'

	temp_strin301 = 'n31_0 => {'
	fl = 0
	for i in n31:
		temp_strin301 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin301 = temp_strin301[:-1]  #removing the extra "," character
	temp_strin301 += '} \n'

	temp_strin302 = 'n32_0 => {'
	fl = 0
	for i in n32:
		temp_strin302 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin302 = temp_strin302[:-1]  #removing the extra "," character
	temp_strin302 += '} \n'

	temp_strin401 = 'n41_0 => {'
	fl = 0
	for i in n41:
		temp_strin401 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin401 = temp_strin401[:-1]  #removing the extra "," character
	temp_strin401 += '} \n'

	temp_strin402 = 'n42_0 => {'
	fl = 0
	for i in n42:
		temp_strin402 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin402 = temp_strin402[:-1]  #removing the extra "," character
	temp_strin402 += '} \n'

	temp_strin501 = 'n51_0 => {'
	fl = 0
	for i in n51:
		temp_strin501 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin501 = temp_strin501[:-1]  #removing the extra "," character
	temp_strin501 += '} \n'

	temp_strin502 = 'n52_0 => {'
	fl = 0
	for i in n52:
		temp_strin502 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin502 = temp_strin502[:-1]  #removing the extra "," character
	temp_strin502 += '} \n'

	v = temp_strin0+temp_strin11+temp_strin12+temp_strin21+temp_strin22+temp_strin31+temp_strin32+temp_strin41+temp_strin42+temp_strin51+temp_strin52+temp_strin101+temp_strin102+temp_strin201+temp_strin202+temp_strin301+temp_strin302+temp_strin401+temp_strin402+temp_strin501+temp_strin502

	query = '((exists x11.(m11_7(x11)&n11_0(x11)))&(exists x12.(m12_7(x12)&n12_0(x12)))&(exists x21.(m21_7(x21)&n21_0(x21)))&(exists x22.(m22_7(x22)&n22_0(x22)))&(exists x31.(m31_7(x31)&n31_0(x31)))&(exists x32.(m32_7(x32)&n32_0(x32)))&(exists x41.(m41_7(x41)&n41_0(x41)))&(exists x42.(m42_7(x42)&n42_0(x42)))&(exists x51.(m51_7(x51)&n51_0(x51)))&(exists x52.(m52_7(x52)&n52_0(x52))))'

	make_model_and_answer(v, query, name_to_var)

def generate_and_solve_query7(bowl1, bowl2, bowl3, bowl4, bowl5):
	
	n1 = parse_for0w(bowl1)
	n2 = parse_for0w(bowl2)
	n3 = parse_for0w(bowl3)
	n4 = parse_for0w(bowl4)
	n5 = parse_for0w(bowl5)

	m1 = parse_for8ec(bowl1)
	m2 = parse_for8ec(bowl2)
	m3 = parse_for8ec(bowl3)
	m4 = parse_for8ec(bowl4)
	m5 = parse_for8ec(bowl5)
	
	c1 = [n1,n2,n3,n4,n5,m1,m2,m3,m4,m5]

	name_to_var = {}
	count = 0
	for i in c1:
		if i:
			for j in i:
				if j not in name_to_var:
					name_to_var[j] = 'r' + str(count)
					count += 1
	
	temp_strin0 = ''
	for i in name_to_var:
		temp_strin0 += i + ' => ' + name_to_var[i] + '\n'

	temp_strin1 = '0w_1 => { '
	fl = 0
	for i in n1:
		temp_strin1 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin1 = temp_strin1[:-1]  #removing the extra "," character
	temp_strin1 += '} \n'

	temp_strin2 = '0w_2 => {'
	fl = 0
	for i in n2:
		temp_strin2 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'

	temp_strin3 = '0w_3 => {'
	fl = 0
	for i in n3:
		temp_strin3 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin3 = temp_strin3[:-1]  #removing the extra "," character
	temp_strin3 += '} \n'

	temp_strin4 = '0w_4 => {'
	fl = 0
	for i in n4:
		temp_strin4 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin4 = temp_strin4[:-1]  #removing the extra "," character
	temp_strin4 += '} \n'

	temp_strin5 = '0w_5 => {'
	fl = 0
	for i in n5:
		temp_strin5 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin5 = temp_strin5[:-1]  #removing the extra "," character
	temp_strin5 += '} \n'

	temp_strin6 = '8ec_1 => {'
	fl = 0
	for i in m1:
		temp_strin6 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin6 = temp_strin6[:-1]  #removing the extra "," character
	temp_strin6 += '} \n'

	temp_strin7 = '8ec_2 => {'
	fl = 0
	for i in m2:
		temp_strin7 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin7 = temp_strin7[:-1]  #removing the extra "," character
	temp_strin7 += '} \n'

	temp_strin8 = '8ec_3 => {'
	fl = 0
	for i in m3:
		temp_strin8 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin8 = temp_strin8[:-1]  #removing the extra "," character
	temp_strin8 += '} \n'

	temp_strin9 = '8ec_4 => {'
	fl = 0
	for i in m4:
		temp_strin9 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin9 = temp_strin9[:-1]  #removing the extra "," character
	temp_strin9 += '} \n'

	temp_strin10 = '8ec_5 => {'
	fl = 0
	for i in m5:
		temp_strin10 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin10 = temp_strin10[:-1]  #removing the extra "," character
	temp_strin10 += '} \n'

	v = temp_strin0+temp_strin1+temp_strin2+temp_strin3+temp_strin4+temp_strin5+temp_strin6+temp_strin7+temp_strin8+temp_strin9+temp_strin10

	query = '((exists x1.(0w_3(x1)&8ec_3(x1)))|(exists x2.(0w_2(x2)&8ec_2(x2)))|(exists x3.(0w_3(x3)&8ec_3(x3)))|(exists x4.(0w_4(x4)&8ec_4(x4)))|(exists x5.(0w_5(x5)&8ec_5(x5))))'

	make_model_and_answer(v, query, name_to_var)

def generate_and_solve_query8(bat1, bat2, bat3, bat4, bat5, win1, win2, win3, win4, win5, nzplayer, inplayer):

	m1 = parse_for100(bat1)
	m2 = parse_for100(bat2)
	m3 = parse_for100(bat3)
	m4 = parse_for100(bat4)
	m5 = parse_for100(bat5)

	p1 = parse_forTeam(nzplayer)
	p2 = parse_forTeam(inplayer)

	c1 = [m1,m2,m3,m4,m5,p1,p2]
	
	name_to_var = {}
	count = 0
	for i in c1:
		if i:
			for j in i:
				if j not in name_to_var:
					name_to_var[j] = 'r' + str(count)
					count += 1
	
	temp_strin0 = ''
	for i in name_to_var:
		temp_strin0 += i + ' => ' + name_to_var[i] + '\n'
	
	temp_strin1=''
	for i in win1:
		if i == 'New Zealand':
			temp_strin1 = '100_1 => { '
			fl = 0
			for i in m1 :
				if i in inplayer:
					temp_strin1 += name_to_var[i] +  ','
					fl = 1
			if fl == 1:
				temp_strin1 = temp_strin1[:-1]  #removing the extra "," character
			temp_strin1 += '} \n'
		else:
			temp_strin1 = '100_1 => { '
			fl = 0
			for i in m1 :
				if i in nzplayer:
					temp_strin1 += name_to_var[i] +  ','
					fl = 1
			if fl == 1:
				temp_strin1 = temp_strin1[:-1]  #removing the extra "," character
			temp_strin1 += '} \n'

	temp_strin2=''
	for i in win2:
		if i == 'New Zealand':
			temp_strin2 = '100_2 => { '
			fl = 0
			for i in m2 :
				if i in inplayer:
					temp_strin2 += name_to_var[i] +  ','
					fl = 1
			if fl == 1:
				temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
			temp_strin2 += '} \n'
		else:
			temp_strin2 = '100_2 => { '
			fl = 0
			for i in m2 :
				if i in nzplayer:
					temp_strin2 += name_to_var[i] +  ','
					fl = 1
			if fl == 1:
				temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
			temp_strin2 += '} \n'

	temp_strin3=''
	for i in win3:
		if i == 'New Zealand':
			temp_strin3 = '100_3 => { '
			fl = 0
			for i in m3 :
				if i in inplayer:
					temp_strin3 += name_to_var[i] +  ','
					fl = 1
			if fl == 1:
				temp_strin3 = temp_strin3[:-1]  #removing the extra "," character
			temp_strin3 += '} \n'
		else:
			temp_strin3 = '100_3 => { '
			fl = 0
			for i in m3 :
				if i in nzplayer:
					temp_strin3 += name_to_var[i] +  ','
					fl = 1
			if fl == 1:
				temp_strin3 = temp_strin3[:-1]  #removing the extra "," character
			temp_strin3 += '} \n'

	temp_strin4=''
	for i in win4:
		if i == 'New Zealand':
			temp_strin4 = '100_4 => { '
			fl = 0
			for i in m4 :
				if i in inplayer:
					temp_strin4 += name_to_var[i] +  ','
					fl = 1
			if fl == 1:
				temp_strin4 = temp_strin4[:-1]  #removing the extra "," character
			temp_strin4 += '} \n'
		else:
			temp_strin4 = '100_4 => { '
			fl = 0
			for i in m4:
				if i in nzplayer:
					temp_strin4 += name_to_var[i] +  ','
					fl = 1
			if fl == 1:
				temp_strin4 = temp_strin4[:-1]  #removing the extra "," character
			temp_strin4 += '} \n'

	temp_strin5=''
	for i in win5:
		if i == 'New Zealand':
			temp_strin5 = '100_5 => { '
			fl = 0
			for i in m5:
				if i in inplayer:
					temp_strin5 += name_to_var[i] +  ','
					fl = 1
			if fl == 1:
				temp_strin5 = temp_strin5[:-1]  #removing the extra "," character
			temp_strin5 += '} \n'
		else:
			temp_strin5 = '100_5 => { '
			fl = 0
			for i in m5:
				if i in nzplayer:
					temp_strin5 += name_to_var[i] +  ','
					fl = 1
			if fl == 1:
				temp_strin5 = temp_strin5[:-1]  #removing the extra "," character
			temp_strin5 += '} \n'

	v = temp_strin0+temp_strin1+temp_strin2+temp_strin3+temp_strin4+temp_strin5

	query = '((exists x1.100_1(x1))|(exists x2.100_2(x2))|(exists x3.100_3(x3))|(exists x4.100_4(x4))|(exists x5.100_5(x5)))'

	make_model_and_answer(v, query, name_to_var)

def generate_and_solve_query9(bowl1, bowl2, bowl3, bowl4, bowl5, nzplayer, inplayer):

	m1 = parse_forLR(bowl1, nzplayer, inplayer)
	m2 = parse_forLR(bowl2, nzplayer, inplayer)
	m3 = parse_forLR(bowl3, nzplayer, inplayer)
	m4 = parse_forLR(bowl4, nzplayer, inplayer)
	m5 = parse_forLR(bowl5, nzplayer, inplayer)

	c1 = [m1, m2, m3, m4, m5]
	
	name_to_var = {}
	count = 0
	for i in c1:
		if i:
			for j in i:
				if j not in name_to_var:
					name_to_var[j] = 'r' + str(count)
					count += 1
	
	temp_strin0 = ''
	for i in name_to_var:
		temp_strin0 += i + ' => ' + name_to_var[i] + '\n'
	
	temp_strin1 = 'm_1 => {'
	fl = 0
	for i in m1:
		temp_strin1 += name_to_var[i] +  ','
		fl = 1
	if fl==1:
		temp_strin1 = temp_strin1[:-1]  #removing the extra "," character
	temp_strin1 += '} \n'
	
	temp_strin2 = 'm_2 => {'
	fl = 0
	for i in m2:
		temp_strin2 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	
	temp_strin3 = 'm_3 => {'
	fl = 0
	for i in m3:
		temp_strin3 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin3 = temp_strin3[:-1]  #removing the extra "," character
	temp_strin3 += '} \n'
	
	temp_strin4 = 'm_4 => {'
	fl = 0
	for i in m4:
		temp_strin4 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin4 = temp_strin4[:-1]  #removing the extra "," character
	temp_strin4 += '} \n'
	
	temp_strin5 = 'm_5 => {'
	fl = 0
	for i in m5:
		temp_strin5 += name_to_var[i] +  ','
		fl = 1
	if fl == 1:
		temp_strin5 = temp_strin5[:-1]  #removing the extra "," character
	temp_strin5 += '} \n'
	
	v = temp_strin0+temp_strin1+temp_strin2+temp_strin3+temp_strin4+temp_strin5

	query = '(exists x1.m_1(x1)) & (exists x2.m_2(x2)) & (exists x3.m_3(x3)) & (exists x4.m_4(x4)) & (exists x5.m_5(x5))'

	make_model_and_answer(v, query, name_to_var)

def generate_and_solve_query10(bat1, bat2, bat3, bat4, bat5, nzplayer, inplayer):

	p1 = parse_forAge26(nzplayer)
	p2 = parse_forAge26(inplayer)

	m1 = parse_forNoDuck(bat1, bat2, bat3, bat4, bat5)

	n1 = parse_for250(bat1, bat2, bat3, bat4, bat5)

	c1 = [p1, p2, m1, n1]
	
	name_to_var = {}
	count = 0
	for i in c1:
		if i:
			for j in i:
				if j not in name_to_var:
					name_to_var[j] = 'r' + str(count)
					count += 1
	
	temp_strin0 = ''
	for i in name_to_var:
		temp_strin0 += i + ' => ' + name_to_var[i] + '\n'
	
	temp_strin1 = 'NoDuck => {'
	fl = 0
	for i in m1:
		temp_strin1 += name_to_var[i] +  ','
		fl = 1
	if fl==1:
		temp_strin1 = temp_strin1[:-1]  #removing the extra "," character
	temp_strin1 += '} \n'
	
	temp_strin2 = '250 => {'
	fl = 0
	for i in n1:
		temp_strin2 += name_to_var[i] +  ','
		fl = 1
	if fl==1:
		temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	
	temp_strin3 = 'age26 => {'
	fl = 0
	for i in p1:
		temp_strin3 += name_to_var[i] +  ','
		fl = 1
	for i in p2:
		temp_strin3 += name_to_var[i] + ','
		fl = 1
	if fl==1:
		temp_strin3 = temp_strin3[:-1]  #removing the extra "," character
	temp_strin3 += '} \n'
	
	v = temp_strin0 + temp_strin1 + temp_strin2 + temp_strin3

	query = 'exists x.(NoDuck(x) & 250(x) & age26(x))'

	make_model_and_answer(v, query, name_to_var)

def generate_and_solve_query11(bat1, bat2, bat3, bat4, bat5, bowl1, bowl2, bowl3, bowl4, bowl5):

	m1 = parse_forPlay(bat1, bowl1)
	m2 = parse_forPlay(bat2, bowl2)
	m3 = parse_forPlay(bat3, bowl3)
	m4 = parse_forPlay(bat4, bowl4)
	m5 = parse_forPlay(bat5, bowl5)

	c = [m1, m2, m3, m4, m5]

	name_to_var = {}
	count = 0
	for i in c:
		if i:
			for j in i:
				if j not in name_to_var:
					name_to_var[j] = 'r' + str(count)
					count += 1

	toprint = []
	for i in name_to_var:
		if i in m1 and i in m2 and i in m3 and i in m4 and i in m5:
			print i,
	print ''

def generate_and_solve_query12(bowl1, bowl2, bowl3, bowl4, bowl5):

	p1 = solve_forWide(bowl1, bowl2, bowl3, bowl4, bowl5)
	print p1

def generate_and_solve_query13(bat1, bat2, bat3, bat4, bat5):

	p1 = solve_forCatch(bat1, bat2, bat3, bat4, bat5)
	print p1

def generate_and_solve_query14(mom1, mom2, mom3, mom4, mom5):

	p1 = solve_forMan(mom1, mom2, mom3, mom4, mom5)
	print p1

def generate_and_solve_query15(bo11,bo12,bo21,bo22,bo31,bo32,bo41,bo42,bo51,bo52):

	p1 = solve_forBetBowl(bo11,bo12,bo21,bo22,bo31,bo32,bo41,bo42,bo51,bo52)
	print p1

def generate_and_solve_query16(bat1, bat2, bat3, bat4, bat5):

	dh = 'MS Dhoni'
	p1 = parse_forHardHit(bat1, bat2, bat3, bat4, bat5, dh)
	
	thresh = 80.0
		
	if p1 > thresh:
		print "True, St-Rate : "+str(p1)
	else:
		print "False, St-Rate : "+str(p1)

def generate_and_solve_query17(bowl1, bowl2, bowl3, bowl4, bowl5):

	c = [bowl1, bowl2, bowl3, bowl4, bowl5]
	
	pl1 = 'I Sharma'
	p1 = parse_forGoodBowl(c, pl1)

	pl2 = 'RA Jadeja'
	p2 = parse_forGoodBowl(c, pl2)

	if p1 > p2:
		print "True"
	else:
		print "False"

def generate_and_solve_query18(bat11, bat12, bat21, bat22, bat31, bat32, bat41, bat42, bat51, bat52):
	
	op = [0,1]
	mid = [3,4]

	p1 = parse_forBetBat(bat11, bat12, bat21, bat22, bat31, bat32, bat41, bat42, bat51, bat52, op)
	p2 = parse_forBetBat(bat11, bat12, bat21, bat22, bat31, bat32, bat41, bat42, bat51, bat52, mid)

	if p2 > p1:
		print "True"
	else:
		print "False"

def generate_and_solve_query19(win1,win2,win3,win4,win5,t1,t2,t3,t4,t5):

	m1 = [win1,t1]
	m2 = [win2,t2]
	m3 = [win3,t3]
	m4 = [win4,t4]
	m5 = [win5,t5]

	c = [m1,m2,m3,m4,m5]

	q = solve_forSame(c)
	print q

def generate_and_solve_query20(win1, win2, win3, win4, win5):

	m = n = 0
	c = [win1, win2, win3, win4, win5]
	for i in c:
		for j in i:
			if j=='New Zealand':
				n += 1
			else:
				m += 1
	if m > n:
		print "India"
	else:
		print "New Zealand"

def main():

	mom = {}
	mom1 = {}
	mom2 = {}
	mom3 = {}
	mom4 = {}
	mom5 = {}
	wonby = {}
	bat1 = {}
	bat2 = {}
	bat3 = {}
	bat4 = {}
	bat5 = {}
	bat11 = []
	bat12 = []
	bat21 = []
	bat22 = []
	bat31 = []
	bat32 = []
	bat41 = []
	bat42 = []
	bat51 = []
	bat52 = []
	bowl1 = {}
	bowl2 = {}
	bowl3 = {}
	bowl4 = {}
	bowl5 = {}
	bo11 = {}
	bo12 = {}
	bo21 = {}
	bo22 = {}
	bo31 = {}
	bo32 = {}
	bo41 = {}
	bo42 = {}
	bo51 = {}
	bo52 = {}
	win1 = {}
	win2 = {}
	win3 = {}
	win4 = {}
	win5 = {}
	t1 = {}
	t2 = {}
	t3 = {}
	t4 = {}
	t5 = {}
	inplayer = {}
	nzplayer = {}

	f1 = './dataset/match1/mom'
	f2 = './dataset/match2/mom'
	f3 = './dataset/match3/mom'
	f4 = './dataset/match4/mom'
	f5 = './dataset/match5/mom'
	
	f6 = './dataset/match1/wonby'
	f7 = './dataset/match2/wonby'
	f8 = './dataset/match3/wonby'
	f9 = './dataset/match4/wonby'
	f0 = './dataset/match5/wonby'

	b11 = './dataset/match1/odi1_inn1_bat.txt'
	b12 = './dataset/match1/odi1_inn2_bat.txt'
	b21 = './dataset/match2/odi2_inn1_bat.txt'
	b22 = './dataset/match2/odi2_inn2_bat.txt'
	b31 = './dataset/match3/odi3_inn1_bat.txt'
	b32 = './dataset/match3/odi3_inn2_bat.txt'
	b41 = './dataset/match4/odi4_inn1_bat.txt'
	b42 = './dataset/match4/odi4_inn2_bat.txt'
	b51 = './dataset/match5/odi5_inn1_bat.txt'
	b52 = './dataset/match5/odi5_inn2_bat.txt'

	c11 = './dataset/match1/odi1_inn1_bowl.txt'
	c12 = './dataset/match1/odi1_inn2_bowl.txt'
	c21 = './dataset/match2/odi2_inn1_bowl.txt'
	c22 = './dataset/match2/odi2_inn2_bowl.txt'
	c31 = './dataset/match3/odi3_inn1_bowl.txt'
	c32 = './dataset/match3/odi3_inn2_bowl.txt'
	c41 = './dataset/match4/odi4_inn1_bowl.txt'
	c42 = './dataset/match4/odi4_inn2_bowl.txt'
	c51 = './dataset/match5/odi5_inn1_bowl.txt'
	c52 = './dataset/match5/odi5_inn2_bowl.txt'

	w1 = './dataset/match1/wonby'
	w2 = './dataset/match2/wonby'
	w3 = './dataset/match3/wonby'
	w4 = './dataset/match4/wonby'
	w5 = './dataset/match5/wonby'
	
	to1 = './dataset/match1/toss'
	to2 = './dataset/match2/toss'
	to3 = './dataset/match3/toss'
	to4 = './dataset/match4/toss'
	to5 = './dataset/match5/toss'

	p1 = './dataset/player_profile/indian_players_profile.txt'
	p2 = './dataset/player_profile/nz_players_profile.txt'

	add_to_list(bat11,b11)
	add_to_list(bat12,b12)
	add_to_list(bat21,b21)
	add_to_list(bat22,b22)
	add_to_list(bat31,b31)
	add_to_list(bat32,b32)
	add_to_list(bat41,b41)
	add_to_list(bat42,b42)
	add_to_list(bat51,b51)
	add_to_list(bat52,b52)

	add_to_dict(t1, to1)
	add_to_dict(t2, to2)
	add_to_dict(t3, to3)
	add_to_dict(t4, to4)
	add_to_dict(t5, to5)

	add_to_dict(mom, f1)
	add_to_dict(mom, f2)
	add_to_dict(mom, f3)
	add_to_dict(mom, f4)
	add_to_dict(mom, f5)

	add_to_dict(mom1, f1)
	add_to_dict(mom2, f2)
	add_to_dict(mom3, f3)
	add_to_dict(mom4, f4)
	add_to_dict(mom5, f5)
	
	add_to_dict(wonby, f6)
	add_to_dict(wonby, f7)
	add_to_dict(wonby, f8)
	add_to_dict(wonby, f9)
	add_to_dict(wonby, f0)

	add_to_dict(bat1, b11)
	add_to_dict(bat1, b12)
	add_to_dict(bat2, b21)
	add_to_dict(bat2, b22)
	add_to_dict(bat3, b31)
	add_to_dict(bat3, b32)
	add_to_dict(bat4, b41)
	add_to_dict(bat4, b42)
	add_to_dict(bat5, b51)
	add_to_dict(bat5, b52)

	add_to_dict(bo11, c11)
	add_to_dict(bo12, c12)
	add_to_dict(bo21, c21)
	add_to_dict(bo22, c22)
	add_to_dict(bo31, c31)
	add_to_dict(bo32, c32)
	add_to_dict(bo41, c41)
	add_to_dict(bo42, c42)
	add_to_dict(bo51, c51)
	add_to_dict(bo52, c52)

	add_to_dict(bowl1, c11)
	add_to_dict(bowl1, c12)
	add_to_dict(bowl2, c21)
	add_to_dict(bowl2, c22)
	add_to_dict(bowl3, c31)
	add_to_dict(bowl3, c32)
	add_to_dict(bowl4, c41)
	add_to_dict(bowl4, c42)
	add_to_dict(bowl5, c51)
	add_to_dict(bowl5, c52)

	add_to_dict(win1, w1)
	add_to_dict(win2, w2)
	add_to_dict(win3, w3)
	add_to_dict(win4, w4)
	add_to_dict(win5, w5)

	addteam_to_dict(inplayer, p1)
	addteam_to_dict(nzplayer, p2)

	print "For all matches, 'Player of the Match' award is given to a player of the winning team."
	generate_and_solve_query1(mom, wonby)

	print "For all matches, Losing side contains atleast one ducks in the batting innings."
	generate_and_solve_query2(win1, win2, win3, win4, win5, bat1, bat2, bat3, bat4, bat5, inplayer, nzplayer)

	print "For all innings, if the strike rate of player is above 200.0 then he has hit more sixes than fours."
	generate_and_solve_query3(bat1, bat2, bat3, bat4, bat5)

	print "For every match, there exists a player on winning side who scored a 4 and had a st-rate less than 100.0"
	generate_and_solve_query4(win1, win2, win3, win4, win5, bat1, bat2, bat3, bat4, bat5, inplayer, nzplayer)

	print "There exist player(s) in the series, who have scored more than 50 runs in batting and claimed atleast 1 wicket in bowling, in the same match."
	generate_and_solve_query5(bat1, bat2, bat3, bat4, bat5, bowl1, bowl2, bowl3, bowl4, bowl5)

	print "For all matches, for any side, there exist at least 1 bowler who has bowled more than 7 overs and failed to get any wicket."
	generate_and_solve_query6(bo11, bo12, bo21, bo22, bo31, bo32, bo41, bo42, bo51, bo52)

	print "In any of the matches, there exists a bowler who did not claim any wicket and went for more than 8 runs per over."
	generate_and_solve_query7(bowl1, bowl2, bowl3, bowl4, bowl5)

	print "There exists a match, where a batsman scored hundred and despite that the team lost."
	generate_and_solve_query8(bat1, bat2, bat3, bat4, bat5, win1, win2, win3, win4, win5, nzplayer, inplayer)

	print "For all matches, right handed bowlers claim more wickets than left handed bowlers."
	generate_and_solve_query9(bowl1, bowl2, bowl3, bowl4, bowl5, nzplayer, inplayer)

	print "There exists a player, who is less than 26 years old and has scored more than 250 runs in the series without any ducks in any of the matches."
	generate_and_solve_query10(bat1, bat2, bat3, bat4, bat5, nzplayer, inplayer)

	print "Who are the players who played all matches in the series ?"
	generate_and_solve_query11(bat1, bat2, bat3, bat4, bat5, bowl1, bowl2, bowl3, bowl4, bowl5)

	print "Did Ishant sharma bowl more wides than Sir Jadeja?"
	generate_and_solve_query12(bowl1, bowl2, bowl3, bowl4, bowl5)

	print "Did Southee caught more than Ryder ?"
	generate_and_solve_query13(bat1, bat2, bat3, bat4, bat5)

	print "Is there a player who has been awarded player of the match twice ?"
	generate_and_solve_query14(mom1, mom2, mom3, mom4, mom5)

	print "Did Sir Jadeja bowl better in innings1 than innings2?"
	generate_and_solve_query15(bo11,bo12,bo21,bo22,bo31,bo32,bo41,bo42,bo51,bo52)

	print "Prove that Dhoni is a hard hitting batsmen."
	generate_and_solve_query16(bat1, bat2, bat3, bat4, bat5)

	print "Is  Ishant  sharma  a  better  bowler  than  Sir  Jadeja  ?"
	generate_and_solve_query17(bowl1, bowl2, bowl3, bowl4, bowl5)

	print "Do  the  middle  order  batsmen  perform  better  than  the  opening  batsmen  in  general  ?"
	generate_and_solve_query18(bat11, bat12, bat21, bat22, bat31, bat32, bat41, bat42, bat51, bat52)

	print "Do the teams that win matches win tosses too ?"
	generate_and_solve_query19(win1, win2, win3, win4, win5, t1, t2, t3, t4, t5)

	print "Based  on given matches, what do you predict  as the outcome of next match ?"
	generate_and_solve_query20(win1, win2, win3, win4, win5)

if __name__ == "__main__":
	main()
