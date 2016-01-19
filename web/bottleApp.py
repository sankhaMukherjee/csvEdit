'''
    This function provides a convinient method of creating a 
    bottle application and sending it to the main application. 
    This way we shall be able to segrigate the web framework 
    and the datawrangling operations and dramatically improve
    maintainability ...
'''
import bottle

'''
    This is the main app. It is just better to import 
    this app and then build all of the other layers
    around this, rather than creating a new app at the 
    main level. This way, we will be able to delegate 
    some routine tasks to this file and create the 
    specific routing calls in the main program ...
'''
app = bottle.Bottle()

@app.route('/')
def root():
    return 'This is the root application'

@bottle.error(404)
def error404():
    return 'Sorry this page cant be found ...'

# Static Routes
# http://stackoverflow.com/questions/10486224/bottle-static-files
@app.get('/<filename:re:.*\.js>')
def javascripts(filename):
    return bottle.static_file(filename, root='web/static/js')

@app.get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return bottle.static_file(filename, root='web/static/css')

@app.get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return bottle.static_file(filename, root='web/static/img')

@app.get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return bottle.static_file(filename, root='web/static/fonts')


