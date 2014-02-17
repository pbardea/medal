import cherrypy
import json
import os
import routes
import urllib2
from country_codes import country_codes

class Core:
  def scores(self):
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

    return json.dumps(countryScores)


  def index(self):
    raise cherrypy.HTTPRedirect('/assets/index.html')

  scores.exposed = True
  index.exposed = True
  

def setup_routes():
    d = cherrypy.dispatch.RoutesDispatcher()
    d.connect('main', '/', controller=Core(), action='index')
    return d

def start():
    # conf = {
    #     '/': {
    #         'request.dispatch': setup_routes(),
    #         'tools.staticdir.on': True,
    #         'tools.staticdir.root':  os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + '/assets',
    #         'tools.staticdir.debug': True,
    #         'tools.staticdir.dir': 'assets'}}#cherrypy.config.get('static.dir.dir')}}
    conf = {
        '/assets':{
        'tools.staticdir.on': True,
        'tools.staticdir.dir': os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets')
        }}


    app = cherrypy.tree.mount(Core(), '/', config=conf)
    #cherrypy.quickstart(app)
    cherrypy.engine.start()


if __name__ == '__main__':
  start()
