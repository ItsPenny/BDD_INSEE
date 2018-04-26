def liste_regions():
	# Try to connect to an existing database
	print('Trying to connect to the database')
	try:
		conn = psycopg2.connect(host='dbserver', dbname='bpinaud', user = 'kdorne')
		print('Connected to the database')
		cur = conn.cursor()
		command = 'select nom from REGIONS'
		try:
		# Query the database and obtain data as Python objects
			cur.execute(command)
			rows = cur.fetchall()
			regions = []
			for reg in rows:
				region.append(reg[0])
			# Close communication with the database
			cur.close()
			conn.close()
			return regions
		except Exception as e :
			return "error when running command: " + command + " : " + str(e)
	except Exception as e :
		return "Cannot connect to database: " + str(e)

def display_dpt(region):
	# Try to connect to an existing database
	print('Trying to connect to the database')
	try:
		conn = psycopg2.connect(host='dbserver', dbname='bpinaud', user = 'kdorne')
		print('Connected to the database')
		cur = conn.cursor()
		command = 'select NUM from REGIONS where NOM=region'
		command2 = 'select NOm from DEPARTEMENTS where REGION=command asc'
		try:
		# Query the database and obtain data as Python objects
			cur.execute(command2)
			rows = cur.fetchall()
			dpt = []
			for reg in rows:
				dpt.append(reg[0])
			# Close communication with the database
			cur.close()
			conn.close()
			return dpt
		except Exception as e :
			return "error when running command: " + command + " : " + str(e)
	except Exception as e :
		return "Cannot connect to database: " + str(e)



@app.route('/dept_region', method = ['¨POST'])
def selected_region():
	temp_reg = request.form['Région']
	dpt_list = display_dpt(temp_reg)
	print(dpt_list)
	return render_template("dept_region.html", dept = dpt_list)
