SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


CREATE TABLE `contact_us` (
  `Phone` bigint(10) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Email` varchar(70) NOT NULL,
  `subject` text NOT NULL,
  `message` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


INSERT INTO `contact_us` (`Phone`, `Name`, `Email`, `subject`, `message`) VALUES
(123, 'abc', 'abc@xyz.com', 'def', 'abc def \r\n');


ALTER TABLE `contact_us`
  ADD PRIMARY KEY (`Phone`);
COMMIT;

