#!/usr/bin/python

import MySQLdb
from datetime import datetime, timedelta
import time,sys

def getIpTenantMatches(fileName):
	print "IP Tenant Matches List"
	# open file to write
	file = open(fileName, "w+")

	# Open database connection
	db = MySQLdb.connect("ip_address","elkusername","userpasswd","dbname" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	sql1 = "select a.tenant_id, b.ip_address from routers as a, ipallocations as b where a.gw_port_id=b.port_id;"
	sql2 = "select tenant_id, floating_ip_address from floatingips;"
        sql3 = "select ip_address from ipallocations WHERE NOT ip_address LIKE \"<floating_ip_network>\";"

	try:
	   cursor.execute(sql1)
	   results = cursor.fetchall()
	   for row in results:
	      # print ("\"%s\": \"%s\"" % (row[1], row[0]))
	      file.write ("\"%s\": \"%s\"\n" % (row[1], row[0]))
	
	   cursor.execute(sql2)
	   results = cursor.fetchall()
	   for row in results:
	      # print ("\"%s\": \"%s\"" % (row[1], row[0]))	
	      file.write ("\"%s\": \"%s\"\n" % (row[1], row[0]))


           cursor.execute(sql3)
           results = cursor.fetchall()
           for row in results:
              # print ("\"%s\": \"%s\"" % (row[1], row[0]))     
              file.write ("\"%s\": \"%s\"\n" % (row[0], "internal_traffic"))


	except:
	   print "Error: unable to fecth data"


	# disconnect from server
	db.close()
	file.close()

fName=sys.argv[1]
while 1:
    getIpTenantMatches(fName)

    dt = datetime.now() + timedelta(hours=1)
    #dt = datetime.now() + timedelta(minutes=1)
    dt = dt.replace(minute=10)
    #dt = dt.replace(second=10)

    while datetime.now() < dt:
        time.sleep(30):
