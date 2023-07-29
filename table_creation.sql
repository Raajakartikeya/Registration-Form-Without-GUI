USE RAAJA;

CREATE TABLE regform(
	
    id INT PRIMARY KEY,
    name VARCHAR(30),
    mobileno BIGINT,
    email VARCHAR(50),
    department VARCHAR(6),
    college VARCHAR(100),
    age INT
);
ALTER TABLE regform
MODIFY COLUMN id INT AUTO_INCREMENT ;
describe regform;

select * from regform ;


