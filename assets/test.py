import urllib2
data = eval(urllib2.urlopen("http://olympics.clearlytech.com/api/v1/medals").readline())
countryScores = []     

for line in data:      
  country = line['country_name']  
  gold = line['gold_count']
  silver = line['silver_count']   
  bronze = line['bronze_count']   
  code = ''
  country_key = country.lower()

  gold_weight = 5
  silver_weight = 3
  bronze_weight = 1


  score = gold*gold_weight+silver*silver_weight+bronze*bronze_weight
  countryScore = {'name':country,'score':score, 'code':code}
  countryScores.append(countryScore)

countryScores = sorted(countryScores, key=lambda x: -x['score'])

for i in range(len(countryScores)):
  countryScores[i]['rank']=i+1    

print countryScores
