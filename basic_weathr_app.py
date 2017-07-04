import json
import urllib2

zipcode = raw_input("Enter Zip Code: ")
url = 'http://samples.openweathermap.org/data/2.5/weather?appid=b1b15e88fa797225412429c1c50c122a1&zip='+ zipcode +',us'

json_obj = urllib2.urlopen(url)
data = json.load(json_obj)


temp_k = float(data['main']['temp'])
temp_f = (temp_k - 273) *1.8 + 32
print "Current Temp: "+str(temp_f)+" degrees"
