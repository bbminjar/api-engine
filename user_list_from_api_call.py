#we are importing requests module to make RESTful HTTPS connection to the URL
#We importing the xml.etree.ElementTree as ET and xmltodict module to parse the xml format result
#we importing json module to get the results in json format

import requests
import xml.etree.ElementTree as ET
import xmltodict
import json

#Here we are providing the url to login to gain the access
login_url = 'https://twcdrive.cloud.twc.net/admin/api/login'

#Here we are providing the user credetials to login to the page
login_details = {'j_username': 'kartik', 'j_password': '*********'}

#We getting the login session JSONID from the above login
s = requests.session()
r = s.post(login_url, data=login_details)

#We are making the RESTful HTTPS API call to the webpage to get the users details
users_list_url = 'https://twcdrive.cloud.twc.net/admin/api/users'

#Bydefault the API call will provide the result in xml formate so we are convertion
#into json format
user_details_xml = s.get(users_list_url)

c=user_details_xml.text
root = ET.fromstring(c)

doc = xmltodict.parse(c)
json_obj = json.dumps(doc)
json_obj = json.loads(json_obj)
list_of_names = []

#Here we iterating only the name value(username) from the whole buch of json results
for attribute in json_obj["list"]["obj"]:
    for val in attribute['att']:
        if val['@id'] == 'name':
            list_of_names.append(val['val'])

#Finally we printing only the users list here.
print json.dumps(list_of_names)
