CREATE DATABASE IF NOT EXISTS library_db;

USE library_db;

CREATE TABLE IF NOT EXISTS books(
	id_book INT NOT NULL AUTO_INCREMENT,
    b_name VARCHAR(35) NOT NULL, 
    b_amonunt INT,
    b_status ENUM('EN STOCK','SIN STOCK'),
    PRIMARY KEY(id_book)
) ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS _users(
	id_user INT NOT NULL AUTO_INCREMENT,
    u_fname VARCHAR(35) NOT NULL,
    u_sname1 VARCHAR(35) NOT NULL,
    u_sname2 VARCHAR(35),
    u_email VARCHAR(35),
    PRIMARY KEY (id_user)
)ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS books_details (
	id_db INT,
    bd_description VARCHAR(35) NOT NULL,
    db_pages INT NOT NULL,
    db_autor VARCHAR(125),
    PRIMARY KEY (id_db),
    CONSTRAINT fkbook_db FOREIGN KEY  (id_db)
		REFERENCES books(id_book)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS loan(
	id_user INT,
    id_book INT,
    l_date DATE NOT NULL,
    l_status ENUM('PENDIENTE','ENTREGADO', 'VENCIDO'),
    PRIMARY KEY(id_user, id_book),
    CONSTRAINT fkuser_loan FOREIGN KEY(id_user)
		REFERENCES _users(id_user)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
	CONSTRAINT fkbook_loan FOREIGN KEY (id_book)
		REFERENCES books(id_book)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE=INNODB;