DROP DATABASE IF EXISTS emetshaf_prod_db;

CREATE DATABASE IF NOT EXISTS emetshaf_prod_db;
CREATE USER IF NOT EXISTS 'emetshaf_prod'@'localhost' IDENTIFIED BY 'emetshaf_prod_pwd';
GRANT ALL ON emetshaf_prod_db.* TO 'emetshaf_prod'@'localhost';
GRANT SELECT ON performance_schema.* TO 'emetshaf_prod'@'localhost';
FLUSH PRIVILEGES;