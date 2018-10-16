import pandas as pd
import sys
sys.path.insert(0, '../..')
from .rundb import *
import pdb;
import datetime
conn, cur = init()
figures = pd.read_sql('select * from figures', con = engine)
bangmok = pd.read_sql('select * from bangmok', con = engine)

# 한자 동명이인들을 찾아서 합칠 사람들을 본다.
# duplicates = figures[figures['chnname'].duplicated(keep=False)].sort_values('chnname')

def delete_request(delete):
    # delete = ['first article']
    for d in delete:
        cur.execute("UPDATE figures SET deleted = %s WHERE manid = %s",(1,d))
        cur.execute("UPDATE figures SET deleted_time = %s where manid = %s", (datetime.datetime.now(), d))
        conn.commit()
        # cur.execute("SELECT * from figures WHERE manid = %s", (d,))
        # deleted_manid, deleted_manname = cur.fetchone()[0:2]
        # with open('deleted_man.txt','a') as f:
        #     f.write(str(deleted_manid)+'\t'+str(datetime.datetime.now())+'\t'+str(deleted_manname)+'\n')

        # print(deleted_manid, deleted_manname)
        # cur.execute("DELETE FROM blog_post where title = %s", (d,))
        # conn.commit()
def merge_request(merge):
    source = merge[0]
    target = merge[1:]
    for t in target:
        cur.execute("UPDATE figures set merged = %s WHERE manid = %s", (source, t))
        conn.commit()

def check_request(check):
    for c in check:
        cur.execute("UPDATE figures set checked = %s WHERE manid = %s", (1, c))
        conn.commit()