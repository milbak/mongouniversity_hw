#!/usr/bin/env python

import pymongo

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.school
col = db.students

docs = db.students.find({}, {"scores": 1})

for d in docs:
    hw = [s for s in d['scores'] if s['type'] == 'homework']
    scores = sorted(hw, key=lambda k: k['score'])[1:]
    for s in d['scores']:
        if s['type'] != 'homework':
            scores.append(s)

    db.students.update_one({"_id": d["_id"]}, {"$set": {"scores": scores}})


