#-*- coding: utf-8 -*-

'''
Created on 04.12.2010

@author: Dmitry
'''

import json
import kindergarden.gardens.models as models

kgs = open('d:/totalcmd/kindergarden/src/kindergarden/gardens/kindergardens.json')
gardens = json.load(kgs)
for g in gardens:
    print g['name'], g['address'], g['ll'][0], g['ll'][1], g['tel']
    kg = models.Kindergarden(name=g['name'],
                        lng=g['ll'][0],
                        lat=g['ll'][1],
                        address=g['address'],
                        telephone=g['tel'],
                        rst_description='Нет описания')
    kg.save()