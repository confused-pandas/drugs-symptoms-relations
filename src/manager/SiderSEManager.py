import pymysql.cursors

connection = pymysql.connect(host='neptune.telecomnancy.univ-lorraine.fr',
                            user='gmd-read',
                            password='esial',
                            db='gmd',
                            cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        sql = "SELECT stitch_compound_id1, stitch_compound_id2, cui, meddra_concept_type, cui_of_meddra_term, side_effect_name FROM meddra_all_indications"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()