DROP DATABASE IF EXISTS emetshaf_dev_db;

CREATE DATABASE IF NOT EXISTS emetshaf_dev_db;
CREATE USER IF NOT EXISTS 'emetshaf_dev'@'localhost' IDENTIFIED BY 'emetshaf_dev_pwd';
GRANT ALL ON emetshaf_dev_db.* TO 'emetshaf_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'emetshaf_dev'@'localhost';
FLUSH PRIVILEGES;