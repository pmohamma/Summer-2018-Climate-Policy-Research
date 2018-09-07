import json
import collections
from collections import OrderedDict

class Law(object):
    pid = ""
    city = ""
    state = ""
    implementingSectorName = ""
    date = ""
    typeName = ""
    policyName = ""
    url = ""
    category = ""

    # The class "constructor" - It's actually an initializer 
    def __init__(self, pid, city, state, implementingSectorName, date, typeName, policyName, url, category):
        self.pid = pid
        self.city = city
        self.state = state
        self.implementingSectorName = implementingSectorName
        self.date = date
        self.typeName = typeName
        self.policyName = policyName
        self.url = url
        self.category = category

def make_law(pid, city, state, implementingSectorName, date, typeName, policyName, url, category):
    law = Law(pid, city, state, implementingSectorName, date, typeName, policyName, url, category)
    return law

cities_list = []
code_list = []
id_list = []
law_list = []
type_list = []
programId2 = ["programId", "city", "state", "implementingSectorName", "tempCity"] 

def ogDumpclean(obj):
    if type(obj) == dict:
        for k, v in obj.items():
            if hasattr(v, '__iter__'):
                print (k.encode("utf-8"))
                ogDumpclean(v)
            else:
            	print (('%s : %s' % (k, v)).encode("utf-8"))
    elif type(obj) == list:
        for v in obj:
            if hasattr(v, '__iter__'):
                ogDumpclean(v)
            else:
                print (v.encode("utf-8"))
    else:
        print (obj.encode("utf-8"))


def dumpcleaner(obj):
	if type(obj) == dict:
		mainObj = obj.get("data")
		for objs in mainObj:
			programId = str(objs.get("ProgramId"))
			code_list.append(programId)
			state = str(objs.get("State"))
			implementingSectorName = str(objs.get("ImplementingSectorName"))
			cityName = ""
			cities = objs.get("Cities")
			contacts = objs.get("Contacts")
			if cities:
				cityName = str(cities[0].get("name"))
			elif contacts:
				counter = 0
				while ((len(contacts) > counter) & ((cityName.strip() == "") | (cityName == "None Specified"))):
					contact = contacts[counter].get("contact")
					city = contact.get("city")
					stateObject = contact.get("stateObject")
					stateName = stateObject.get("name")
					if ((state == str(stateName)) & ((cityName.strip() == "") | (cityName == "None Specified"))):
						if str(city) == "None":
							cityName = "None Specified"
						else:
							cityName = str(city)
					else:
						cityName = "None Specified"
					counter += 1
			else:
				cityName = "None Specified"
			if cityName.strip() == "":
				cityName = "None Specified"
			category = objs.get("CategoryName")
			date = objs.get("StartDate")
			if ((date == "") | (str(date) == "None")):
				date = objs.get("enactedDate")
			if ((date == "") | (str(date) == "None")):
				date = objs.get("enactedDateDisplay")
			if ((date == "") | (str(date) == "None")):
				date = str(objs.get("enactedText"))
			if ((date == "") | (str(date) == "None")):
				date = str(objs.get("LastUpdate"))
			if str(date) == "None":
				date = "None given"
			typeName = str(objs.get("TypeName")).encode("utf-8")
			policyName = str(objs.get("Name")).encode("utf-8")
			if not typeName in type_list:
				if implementingSectorName == "Utility":
					type_list.append(typeName)
			url = str(objs.get("WebsiteUrl"))
			if url.strip() == "":
				url = "None"
			if cityName != "None Specified":
				cities_list.append(cityName)
			law_list.append(make_law(programId, cityName, state, implementingSectorName, 
				date, typeName, policyName, url, category))

with open('data_DSIRE.json') as f:
    data = json.load(f)

dumpcleaner(data)
#law_list.append(make_law(code_list[-1], programId[1], programId[2]))
#print("number of cities" + str(len(cities_list)))
print("number of codes" + str(len(code_list)))
print("programCode = " + code_list[-1])
f = open("parsed_DSIRE_data2.txt", "w+")
for x in law_list:
	f.write(x.category + "\n")
#	f.write(str(x.policyName)[2:-1] + "\n")
#	print(x.pid + "      " + x.city + "      " + x.state + "      " + x.implementingSectorName+ 
#		"       " + x.date + "       " + str(x.typeName)[2:-1] + "      " + str(x.policyName)[2:-1]) 
print(len(type_list))
print(len(law_list))

f.close()