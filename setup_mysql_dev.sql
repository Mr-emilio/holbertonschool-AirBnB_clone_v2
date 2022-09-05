-- Create daba base for development hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;
Create USER 'hbnb_dev'@'localhost' IDENTIFIED password 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;