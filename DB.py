class sq():
    def conn(self):
        import sqlite3
        con = sqlite3.connect('mydb.db')
        print('connected to mydb')
        return con;
    def create_table(self):
        con=self.conn()
        c=con.cursor()
        sql = "create table Tag (name varchar(30) not null primary key,Tasks int not null);"
        try:
            c.execute(sql)
            con.commit()
            print('Table created')
        except Exception as e:
            print(e,'in create table')
        con.close()
    def show(self):
        con = self.conn()
        c = con.cursor()
        sql = "select * from Tag"
        try:
            c.execute(sql)
            var = c.fetchall()
            print('show')
        except Exception as e:
            print(e,'in show')
            var=e
        con.close()
        return var
    def add(self,name,task):
        con = self.conn()
        c = con.cursor()
        sql="insert into Tag values('{}','{}')".format(name,int(task))
        try:
            c.execute(sql)
            con.commit()
            print('added')
        except Exception as e:
            print(e)
            con.close()
            return e
        con.close()

    def get(self):
        import numpy.random as rd
        from numpy import floor
        al=self.show()
        id=int(floor(rd.rand() * len(al)))
        try:
            print('Get ',al[id])
            return al[id]
        except :return []
    def Update(self,name,task):
        con = self.conn()
        c = con.cursor()
        sql="UPDATE Tag SET Tasks={} where name='{}' and Tasks > 0".format(task,name)
        try:
            c.execute(sql)
            con.commit()
            print('updeted')
        except Exception as e:
            print(e,'in update')
        con.close()
    def Del(self,name):
        con = self.conn()
        c = con.cursor()
        sql = "DELETE from Tag where name='{}'".format(name)
        try:
            c.execute(sql)
            con.commit()
            print('Deleted')
        except Exception as e:
            print(e,'in delete')

