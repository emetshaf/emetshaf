-- Drop database
DROP DATABASE IF EXISTS emetshaf_dev_db;

-- Create database + user if doesn't exist
CREATE DATABASE IF NOT EXISTS emetshaf_dev_db DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci;
CREATE USER IF NOT EXISTS 'emetshaf_dev'@'localhost' IDENTIFIED BY 'emetshaf_dev_pwd';
GRANT ALL PRIVILEGES ON emetshaf_dev_db.* TO 'emetshaf_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'emetshaf_dev'@'localhost';
FLUSH PRIVILEGES;