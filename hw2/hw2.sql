CREATE TABLE CIS3368.gem (
id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
gemtype varchar(30) NOT NULL,
gemcolor varchar(30) NOT NULL,
carat float,
price float
);

INSERT INTO gem(gemtype, gemcolor, carat, price)
VALUES ('beryl','red',1,19.3);
INSERT INTO gem(gemtype, gemcolor, carat, price)
VALUES ('chrysoberyl','blue',1.2,1.3);
INSERT INTO gem(gemtype, gemcolor, carat, price)
VALUES ('corundum','black',1.5,192.3);
INSERT INTO gem(gemtype, gemcolor, carat, price)
VALUES ('diamond','brown',2,129.3);
INSERT INTO gem(gemtype, gemcolor, carat, price)
VALUES ('feldspar','red',3,119.3);