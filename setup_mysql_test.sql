-- prepares a MySQL server
-- Grant usage on hbnb_test_db to hbnb_test
-- Grant priveleges to the user  for the date base
-- Grant SELECT privileges on performance_schema database

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
