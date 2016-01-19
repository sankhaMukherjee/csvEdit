from web import bottleApp as app 

import web.bottle     as bottle
import config.config  as config

import os
import numpy as np

with app.app as report:

    configFiles = {
        'test'  : 'config/data/test.csv',
    }

    ######################################################################
    # All the configuration ideas go here ...
    ######################################################################
    @report.route('/config')
    @bottle.view('web/templates/configSummary')
    def configure():
        return dict(configFiles=configFiles)
    
    ######################################################################
    # All the Sepcific configurations go here ...
    ######################################################################
    @report.route('/config/<configKey>')
    @bottle.view('web/templates/configPage')
    def configure(configKey):
        configFileVals = config.configRead(configFiles[configKey])
        return dict(info=configFileVals.T, key=configKey)

    # Duplicate an item ...
    # --------------------------
    @report.route('/config/<configKey>/duplicate/<item>')
    def configure(configKey, item):
        
        fileName       = configFiles[configKey]
        configFileVals = config.configRead(fileName)
        item = int(item) + 1

        toInsert = configFileVals.ix[item, :]
        data = configFileVals.append( toInsert)

        config.configWrite(fileName, data, backup=True)
        bottle.redirect('/config/%s'%configKey)


    # Delete an item ...
    # -------------------------
    @report.route('/config/<configKey>/delete/<item>')
    def configure(configKey, item):
        
        fileName       = configFiles[configKey]
        configFileVals = config.configRead( fileName )
        item           = int(item) + 1
        data           = configFileVals.drop( item )

        config.configWrite(fileName, data, backup=True)
        bottle.redirect('/config/%s'%configKey)

    @report.route('/config/<configKey>/success')
    def redirectSuccess(configKey):
        return "Success... Return to <a href='http://localhost:8080/config/%s'>config</a> page"%configKey

    @report.route('/config/<configKey>/Update', method='POST')
    def configUpdate(configKey):

        fileName   = configFiles[configKey]

        postdata   = bottle.request.body.read()
        configVals = config.htmlToDf(postdata)
        config.configWrite(fileName, configVals, backup=True, headerPrint=True)
        bottle.redirect('/config/<configKey>/success')
    
        
    report.run(host = 'localhost', port=8080)
    

