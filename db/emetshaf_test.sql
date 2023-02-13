-- Active: 1676182256969@@127.0.0.1@3306
DROP DATABASE IF EXISTS emetshaf_test_db;

CREATE DATABASE IF NOT EXISTS emetshaf_test_db;
CREATE USER IF NOT EXISTS 'emetshaf_test'@'localhost' IDENTIFIED BY 'emetshaf_test_pwd';
GRANT ALL ON emetshaf_test_db.* TO 'emetshaf_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'emetshaf_test'@'localhost';
FLUSH PRIVILEGES;