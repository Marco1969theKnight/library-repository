from mysql import connector

class Model:
    """
    ********************************************
    * A data model with MySQL for a library DB *
    ********************************************
    """
    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d
    
    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close()

    """
    ****************
    * Book methods *
    ****************
    """

    def create_books(self, b_name, b_amonunt, b_status):
        try:
            sql = 'INSERT INTO books (`b_name`, `b_amonunt`, `b_status`) VALUES (%s, %s, %s)'
            vals = (b_name, b_amonunt, b_status)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_books(self, book):
        try:
            sql = 'SELECT * FROM books WHERE b_name = %s'
            vals = (book,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_books(self):
        try:
            sql = 'SELECT * FROM books'
            self.cursor.execute(sql)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_books_amonunt(self, amonunt):
        try:
            sql = 'SELECT * FROM books WHERE b_amonunt = %s'
            vals = (amonunt,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def read_books_status(self, status):
        try:
            sql = 'SELECT * FROM books WHERE b_status = %s'
            vals = (status,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def update_books(self, b_name, b_amonunt, b_status):
        try:
            fields = []
            vals = []
        except connector.Error as err:
            return err

    """
    ****************
    * User methods *
    ****************
    """

    def create__users(self, u_fname, u_sname1, u_sname2, u_email):
        try:
            sql = 'INSERT INTO _users (`u_fname`, `u_sname1`, `u_sname2`, `u_email`) VALUES (%s, %s, %s, %s)'
            vals = (u_fname, u_sname1, u_sname2, u_email)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a__users(self, fname, sname1, sname2):
        try:
            sql = 'SELECT * FROM _users WHERE u_fname = %s AND u_sname1 = %s AND u_sname2 = %s'
            vals = (fname, sname1, sname2)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all__users(self):
        try:
            sql = 'SELECT * FROM _users'
            self.cursor.execute(sql)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read__users_fname(self, fname):
        try:
            sql = 'SELECT * FROM _users WHERE u_fname = %s'
            vals = (fname,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err
    
    def read__users_sname1(self, sname1):
        try:
            sql = 'SELECT * FROM _users WHERE u_sname1 = %s'
            vals = (sname1,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def read__users_sname2(self, sname2):
        try:
            sql = 'SELECT * FROM _users WHERE u_sname2 = %s'
            vals = (sname2,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def read__users_email(self, email):
        try:
            sql = 'SELECT * FROM _users WHERE u_email = %s'
            vals = (email,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def update__users(self, u_fname, u_sname1, u_sname2, u_email):
        try:
            fields = []
            vals = []
        except connector.Error as err:
            return err

    """
    ************************
    * Book details methods *
    ************************
    """

    def create_books_details(self, book, bd_description, db_pages, db_autor):
        try:
            sql = 'INSERT INTO books_details (`id_db`, `bd_description`, `db_pages`, `db_autor`) VALUES (%s, %s, %s, %s)'
            vals = (book, bd_description, db_pages, db_autor)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_books_details(self, book):
        try:
            sql = 'SELECT * FROM books_details WHERE id_db = %s'
            vals = (book,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_books_details(self):
        try:
            sql = 'SELECT * FROM books_details'
            self.cursor.execute(sql)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_books_details_description(self, description):
        try:
            sql = 'SELECT * FROM books_details WHERE bd_description = %s'
            vals = (description,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def read_books_details_pages(self, pages):
        try:
            sql = 'SELECT * FROM books_details WHERE db_pages = %s'
            vals = (pages,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def read_books_details_autor(self, autor):
        try:
            sql = 'SELECT * FROM books_details WHERE db_autor = %s'
            vals = (autor,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def update_books_details(self, book, bd_description, db_pages, db_autor):
        try:
            fields = []
            vals = []
        except connector.Error as err:
            return err

    """
    ****************
    * Loan methods *
    ****************
    """

    def create_loan(self, user, book, l_date, l_status):
        try:
            sql = 'INSERT INTO loan (`id_user`, `id_book`, `l_date`, `l_status`) VALUES (%s, %s, %s, %s)'
            vals = (user, book, l_date, l_status)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_loan(self, user, book):
        try:
            sql = 'SELECT * FROM loan WHERE id_user = %s AND id_book =  %s'
            vals = (user, book)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_loan(self):
        try:
            sql = 'SELECT * FROM loan'
            self.cursor.execute(sql)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_loan_user(self, user):
        try:
            sql = 'SELECT * FROM loan WHERE id_user = %s'
            vals = (user,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def read_loan_book(self, book):
        try:
            sql = 'SELECT * FROM loan WHERE id_book = %s'
            vals = (book,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def read_loan_l_date(self, l_date):
        try:
            sql = 'SELECT * FROM loan WHERE l_date = %s'
            vals = (l_date,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err
    
    def read_loan_l_status(self, l_status):
        try:
            sql = 'SELECT * FROM loan WHERE l_status = %s'
            vals = (l_status,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def update_loan(self, user, book, l_date, l_status):
        try:
            fields = []
            vals = []
        except connector.Error as err:
            return err
