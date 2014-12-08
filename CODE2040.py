"""---------Dayanna Espinoza---------"""

import urllib2, json

###################---------REGISTRATION--------####################
url = "http://challenge.code2040.org/api/register"
post_data = {"email": "espinoza@mit.edu", "github": "https://github.com/DayannaEspinoza/despinoza"}
my_token = {'token': 'eG9y74sjrL'}

def post(url, post_data):
    request = urllib2.Request(url)
    request.add_header('Content-Type', 'application/json')
    data = json.dumps(post_data)
    response = urllib2.urlopen(request, data).readline()
    return json.loads(response)["result"]

#print post(url, post_data)


##################----------STAGE 1-----------######################

url = "http://challenge.code2040.org/api/getstring"
#print post(url, my_token)
#string = tuCJt

 
def Reverse_string(string):
    
    """
    ### one way to do it ###
    reversed_string = [] #initializing a new list 
    string_list = list(string) #converts the string in a list 

    while len(string_list)>0:
        reversed_string.append(string_list[-1])
        string_list.pop(-1)
        
    return ''.join(reversed_string)"""

    #straight forward way:  
    return string[::-1]


reversed_string = Reverse_string("tuCJt")
url ="http://challenge.code2040.org/api/validatestring"
post_data = {'token': 'eG9y74sjrL', 'string' : reversed_string}
#print post(url, post_data)

 
    
##################----------STAGE 2-----------######################

url = "http://challenge.code2040.org/api/haystack"
#print post(url, my_token)


Dict = {u'haystack': [u'6qZty', u'Nq3X1', u'7wVwA', u'2cerV', u'c5ZID',
               u'lFsr7', u'gEL8S', u'40L6m', u'6pFkU',
               u'Qk1Vt', u'WYNyO', u'f3TRg', u'hUvUt',
               u'1JBqL', u'0FD93', u'sgIv2', u'rV8Qn', 
               u'Ym33K', u't2eSa', u'Hfbmr'], u'needle': u'6qZty'}

def Finding_needle(dictionary):
    needle = dictionary[unicode('needle')]
    haystack = dictionary[unicode('haystack')]
    for i in range(len(haystack)):
        if haystack[i] == needle:
            return i

get_index = Finding_needle(Dict)
     
url ="http://challenge.code2040.org/api/validateneedle"
post_data = {'token': 'eG9y74sjrL', "needle":get_index}
        
#print post(url, post_data)      


##################----------STAGE 3-----------######################

url = "http://challenge.code2040.org/api/prefix"
#print  post(url, my_token)

Dict2 = {u'array': [u'271Tcs7f', u'271gJiW2', u'271uV1Ln',
                    u'271ZyLfO', u'430UvE7v', u'271a10pv'],
         u'prefix': u'430'}

def different_prefix (dictionary):
    new_array = []
    prefix = dictionary[unicode('prefix')]
    
    for word in dictionary[unicode('array')]:
        if not (word.startswith(prefix)):
            #string.startwith(prefix)checks if a words starts with prefix
            new_array.append(word)
    return new_array

url = "http://challenge.code2040.org/api/validateprefix"
post_data = {'token': 'eG9y74sjrL', 'array': different_prefix(Dict2)}
#print post(url, post_data)


##################----------STAGE 4-----------######################

url = "http://challenge.code2040.org/api/time"
#print post(url, my_token)

Dict3 = {u'datestamp': u'1985-01-05T07:26:00.000Z', u'interval': 261158675}

import dateutil.parser
from datetime import *

def new_date(dictionary):
    old_date = dateutil.parser.parse(dictionary[unicode('datestamp')])
    #converts the string into a date object

    delta = timedelta(seconds= dictionary[unicode('interval')])
    #converts interval number into a date object

    new_date = old_date + delta
    #new_date.isoformat() converts the date object into a string
    return new_date.isoformat()

new_datestamp = new_date(Dict3)

url = "http://challenge.code2040.org/api/validatetime"
post_data = {"token":'eG9y74sjrL', "datestamp": new_datestamp}
#print post(url, post_data)


#url = "http://challenge.code2040.org/api/status"
#print post(url, my_token)

    
    

