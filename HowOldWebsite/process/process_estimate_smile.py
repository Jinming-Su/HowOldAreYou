# -*- coding: UTF-8 -*-


from HowOldWebsite.estimators.estimator_smile import EstimatorSmile
from HowOldWebsite.models import RecordSmile

__author__ = 'Hao Yu'


def smile_estimate(database_face_array, feature_jar):
    success = False
    database_record = None

    try:
        n_faces = len(database_face_array)
        result_estimated = __do_estimate(feature_jar, n_faces)
        database_record = \
            __do_save_to_database(database_face_array, result_estimated)
        success = True
    except Exception as e:
        # print(e)
        pass

    return success, database_record


def __do_estimate(feature_jar, n_faces):
    feature = EstimatorSmile.feature_combine(feature_jar)
    feature = EstimatorSmile.feature_reduce(feature)
    result = EstimatorSmile.estimate(feature)
    return result


def __do_save_to_database(database_face, smile):
    database_record = []
    for ith in range(len(database_face)):
        record = RecordSmile(original_face=database_face[ith],
                             value_predict=smile[ith])
        database_record.append(record)
    return database_record
