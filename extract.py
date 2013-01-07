# -*- encoding: utf8 -*-

import gardens.models as models
import gardens.forms as forms
import json

def export(request):
    d = json.load(open("test.js"), encoding="utf8")
    for elem in d["features"]:
        phone = "-"
        try:
            phone = elem["properties"]["CompanyMetaData"]["Phones"][0]["formatted"]
        except KeyError as e:
            pass
        kg = models.Kindergarden(name=elem["properties"]["name"],
                                lng=elem["geometry"]["coordinates"][0],
                                lat=elem["geometry"]["coordinates"][1],
                                address=elem["properties"]["description"],
                                telephone=phone,
                                rst_description='Нет описания')
        kg.save()
   

