use db;

CREATE TABLE students(
    StudantID int not null AUTO_INCREMENT,
    FirstName varchar(100) NOT NULL,
    Mensagem varchar(100) NOT NULL,
    PRIMARY KEY (StudantID)
);

INSERT INTO students(FirstName, mensagem)
VALUES("Lucas","Ola Mundo");