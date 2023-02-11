DROP DATABASE IF EXISTS emetshaf;
CREATE DATABASE IF NOT EXISTS emetshaf;
CREATE USER IF NOT EXISTS 'emetshaf_admin'@'localhost' IDENTIFIED BY 'emetshaf_admin_pwd';
GRANT ALL ON emetshaf.* TO 'emetshaf_admin'@'localhost';
GRANT SELECT ON performance_schema.* TO 'emetshaf_admin'@'localhost';
FLUSH PRIVILEGES;
USE hbnb_dev_db;