#!/usr/bin/env python

import pymongo
import bottle


def remove_lowest():

    connection = pymongo.MongoClient("mongodb://localhost")
    db = connection.students
    col = db.grades
    sids = col.distinct('student_id')

    for s in sids:
        docs = col.find({'student_id': s, 'type':'homework'})\
            .sort([('student_id', pymongo.ASCENDING),
                   ('score', pymongo.ASCENDING)])\
            .limit(1)
        for d in docs:
            col.remove(d)

remove_lowest()
