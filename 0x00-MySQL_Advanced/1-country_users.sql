--- creates a table users
--- id int not null auto increment and primary
--- email varchar(255) not null and unique
--- name varchar(255)
--- country encruments of countries US,CO, TN not null
--- default country is US
CREATE TABLE IF NOT EXISTS users (
       id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
       email VARCHAR(255) NOT NULL UNIQUE,
       name VARCHAR(255),
       country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);