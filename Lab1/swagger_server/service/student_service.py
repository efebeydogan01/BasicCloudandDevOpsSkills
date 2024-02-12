import os
import tempfile
from functools import reduce
from pymongo import MongoClient

MONGO_URI = os.environ['MONGO_URI']
db = MongoClient(MONGO_URI)
database_name = db['tutorial1']
collection_name = database_name['student_db']

def add(student=None):
    res = collection_name.find_one({ 'first_name': student.first_name, 'last_name': student.last_name })
    if not res:
        return 'already exists', 409
    doc_id = collection_name.insert_one(student.to_dict())
    return student.student_id


def get_by_id(student_id=None, subject=None):
    student = collection_name.find_one({'student_id': student_id})
    if not student:
        return 'not found', 404
    return {
        'first_name': student['first_name'],
        'gradeRecords': student['grade_records'],
        'last_name': student['last_name'],
        'student_id': student['student_id']
    }


def delete(student_id=None):
    student = collection_name.find({'student_id': student_id})
    if not student:
        return 'not found', 404
    collection_name.delete_many({'student_id': student_id})
    return student_id
