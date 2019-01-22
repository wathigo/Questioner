class Tables():
    """ Class to create tables """
    def table_queries(self):
        """ Create user registration table"""
        users = """CREATE TABLE IF NOT EXISTS user_table
        (
        userid SERIAL PRIMARY KEY NOT NULL,
        isadmin boolean DEFAULT False,
        firstname char(50) NOT NULL,
        lastname char varying(50) NOT NULL,
        othername char varying(50) NULL,
        username char(30) NOT NULL,
        phonenumber char varying(30) NULL,
        registeredon timestamp,
        email char varying(50) NOT NULL,
        password char varying(30) NOT NULL
        )"""

        """ Create meetup record creation table"""
        meetups = """CREATE TABLE IF NOT EXISTS meetups
        (
        meetupid SERIAL PRIMARY KEY NOT NULL,
        title char varying(30) NOT NULL,
        description char varying(100) NOT NULL,
        location char varying(30) NOT NULL,
        happeningon char(30) NOT NULL,
        createdon timestamp
        )"""

        """ Create question record creation table"""
        question = """CREATE TABLE IF NOT EXISTS question
        (
        questionid SERIAL PRIMARY KEY NOT NULL,
        title char varying(30) NOT NULL,
        question char varying(80) NOT NULL,
        votes integer NULL,
        userid integer NULL,
        meetupid integer NOT NULL,
        askedon timestamp,
        FOREIGN KEY (userid) REFERENCES user_table(userid),
        FOREIGN KEY (meetupid) REFERENCES meetups(meetupid)
        );"""

        """ Create reserve record creation table"""
        reserve = """CREATE TABLE IF NOT EXISTS reserve
        (
        id SERIAL NOT NULL,
        response char(20) NOT NULL,
        meetupid integer NOT NULL,
        reservedon timestamp,
        PRIMARY KEY (meetupid)
        )"""
        self.query = [users, meetups, question, reserve]
        return self.query


    def drop_table_query(self):
        """Resource for teardown when am testing"""
        drop_users = """DROP TABLE IF EXISTS users"""
        drop_meetups = """DROP TABLE IF EXISTS meetups CASCADE"""
        drop_question = """DROP TABLE IF EXISTS question CASCADE"""
        drop_reserve = """DROP TABLE IF EXISTS reserve CASCADE"""
        self.query = [drop_users, drop_meetups, drop_question, drop_reserve]
        return self.query
