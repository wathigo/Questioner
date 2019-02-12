""" Module to create all the tables"""

def table_queries():
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
    );"""

    """ Create meetup record creation table"""
    meetups = """CREATE TABLE IF NOT EXISTS meetups
    (
    meetupid SERIAL PRIMARY KEY NOT NULL,
    title char varying(30) NOT NULL,
    description char varying(100) NOT NULL,
    location char varying(30) NOT NULL,
    happeningon char(30) NOT NULL,
    userid int REFERENCES user_table(userid),
    createdon timestamp
    );"""

    """ Create question record creation table"""
    question = """CREATE TABLE IF NOT EXISTS question
    (
    questionid SERIAL PRIMARY KEY NOT NULL,
    title char varying(30) NOT NULL,
    question char varying(80) NOT NULL,
    votes integer NOT NULL DEFAULT 0,
    userid integer REFERENCES user_table(userid),
    meetupid integer REFERENCES meetups(meetupid) ON DELETE CASCADE,
    askedon timestamp
    );"""

    """ Create reserve record creation table"""
    reserve = """CREATE TABLE IF NOT EXISTS reserve
    (
    reserveid SERIAL PRIMARY KEY NOT NULL,
    response char(20) NOT NULL,
    userid int REFERENCES user_table(userid),
    meetupid integer REFERENCES meetups(meetupid) ON DELETE CASCADE,
    reservedon timestamp);"""

    comment = """CREATE TABLE IF NOT EXISTS comments
    (
    userid int REFERENCES user_table(userid),
    questionid int REFERENCES question(questionid),
    title char(50) NOT NULL,
    body char varying(100),
    comment char varying(100)
    );"""
    query = [users, meetups, question, reserve, comment]
    return query


def drop_table_query():
    """Resource for teardown when am testing"""
    drop_users = """DROP TABLE IF EXISTS user_table CASCADE"""
    drop_meetups = """DROP TABLE IF EXISTS meetups CASCADE"""
    drop_question = """DROP TABLE IF EXISTS question CASCADE"""
    drop_reserve = """DROP TABLE IF EXISTS reserve CASCADE"""
    query = [drop_users, drop_meetups, drop_question, drop_reserve]
    return query
