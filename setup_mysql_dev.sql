-- Create daba base for development hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
Create USER IF NOT EXISTS hbnb_dev@localhost password 'hbnb_dev_pwd';
GRANT ALL ON hbnb_dev_db.* TO hbnb_dev@localhost;
GRANT SELECT ON performance_schema.* TO hbnb_dev@localhost;
FLUSH PRIVILEGES;