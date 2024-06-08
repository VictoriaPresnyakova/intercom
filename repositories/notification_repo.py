from repositories.abc.notification_repo_abc import NotificationRepoABC
from repositories.db.common import insert_new_record, change_record_by_id, delete_record_by_id
from repositories.db.connect import connect
from contextlib import closing
from psycopg2.extras import NamedTupleCursor


class NotificationRepo(NotificationRepoABC):

    def get_all_notifications(self, limit, offset):
        try:
            res = []
            with closing(connect()) as conn:
                with conn.cursor(cursor_factory=NamedTupleCursor) as cursor:
                    cursor.execute('SELECT * FROM {} LIMIT %s offset %s'.format('notification'), (limit, offset))
                    for row in cursor:
                        res.append({x: getattr(row, x) for x in row._fields})
                    return res
        except Exception as e:
            return {}

    def create_notification(self, kwargs):
        return insert_new_record('notification', kwargs)

    def find_notification_by_id(self, id: int):
        try:
            with closing(connect()) as conn:
                with conn.cursor(cursor_factory=NamedTupleCursor) as cursor:
                    cursor.execute('SELECT * FROM {} where id = %s'.format('notification'), (id,))
                    res = cursor.fetchone()
                    return {x: getattr(res, x) for x in res._fields}
        except Exception as e:
            return {}
