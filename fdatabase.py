import jwt
import re

class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getMenu(self):
        sql = """SELECT * FROM mainmenu"""
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except Exception as err:
            print(f"Error read db {err}")
        return []

    def add_user(self, username, password, permissions):
        try:
            add_user_comand = """INSERT INTRO users VALUES(NULL, ?, ?, ?)"""
            self.__cur.executescript(add_user_comand, (username, password, permissions))
            self.__db.commit()
            self.__db.close()
        except Exception as err:
            print(f"Error added user {err}")

    def get_user(self, name):
        try:
            get_user_comand = """SELECT usernsme FROM users WHERE usename = name"""
            self.__cur.executescript(get_user_comand)
            self.__db.close()
        except Exception as err:
            print(f"Error added user {err}")


class Users:
    def __init__(self, db, name, password, read=True, write=False, added=False):
        self.fdb = FDataBase(db)
        self.username = name
        self.psw = password if self.check_psw(password) else None
        self.permissions ={"read": read,
                          "write": write,
                          "added": added}
    @staticmethod
    def check_psw(psw: str) -> bool:
        return True
        # pattern_password = re.compile(r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{8,}$')
        # return boll(pattern_password.match(psw))

    def add_user_to_db(self):
        en_pwd = jwt.encode(self.psw, "&sD9*$3$%^&(jjkl,mKLJd", algorithm="HS256")
        perm = self.permision_to_int(self.permissions.values())
        self.fdb.add_user(self.username, en_pwd, perm)

    @staticmethod
    def permision_to_int(permissions: tuple) -> int:
        """transform permissions to bin after to int"""
        return int("".join(str(x) for x in permissions), 2)
