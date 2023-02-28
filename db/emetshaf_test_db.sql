-- Drop database
DROP DATABASE IF EXISTS emetshaf_test_db;

-- Create database + user if doesn't exist
CREATE DATABASE IF NOT EXISTS emetshaf_test_db DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci;
CREATE USER IF NOT EXISTS 'emetshaf_test'@'localhost' IDENTIFIED BY 'emetshaf_test_pwd';
GRANT ALL PRIVILEGES ON emetshaf_test_db.* TO 'emetshaf_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'emetshaf_test'@'localhost';
FLUSH PRIVILEGES;

USE emetshaf_test_db;