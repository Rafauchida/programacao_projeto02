import mysql.connector as mysql
from datetime import datetime

db = mysql.connect(
    host = "localhost",
    user = "root",
    password = "rouben10",
    database = "cassino"
)

mycursor = db.cursor()


class database:
    def insert(name, points):
        try:
            mycursor.execute("create table IF NOT EXISTS leaderboards(id int not null auto_increment primary key, time date not null, name char(30) default 'None', points int);")
            db.commit()
        finally:
            mycursor.execute("insert into leaderboards(id, time, name, points) values(default, %s, %s, %s);", (datetime.now().isoformat(timespec="hours"), name, points))
            db.commit()



    def ranking():
        mycursor.execute("select name from leaderboards order by points desc;")
        names = mycursor.fetchall()
        mycursor.execute("select points from leaderboards order by points desc;")
        points = mycursor.fetchall()
        players = []
        for c in range(len(names)):
            data = names[c][0], points[c][0]
            players.append(data)
        return players