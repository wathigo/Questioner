class Tables():
    """ Class to create tables """
    def table_queries(self):
        """ Create user registration table"""
        users = """CREATE TABLE IF NOT EXISTS users
        (
        FirstName char(50) NOT NULL,
        LastName char(50) NOT NULL,
        Email char(50) NOT NULL,
        Password char(30) NOT NULL
        )"""
        self.query = [users]
        return self.query
