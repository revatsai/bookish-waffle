-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2021-08-22 15:49:04
-- 伺服器版本： 10.4.18-MariaDB
-- PHP 版本： 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `members`
--

-- --------------------------------------------------------

--
-- 資料表結構 `user`
--

CREATE TABLE `user` (
  `UserID` int(11) NOT NULL,
  `UserName` varchar(100) NOT NULL,
  `UserPassword` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `birthday` datetime NOT NULL,
  `height` int(11) NOT NULL,
  `weight` int(11) NOT NULL,
  `CreateTime` datetime NOT NULL,
  `LastModifyTime` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `user`
--

INSERT INTO `user` (`UserID`, `UserName`, `UserPassword`, `gender`, `birthday`, `height`, `weight`, `CreateTime`, `LastModifyTime`) VALUES
(1, '25uy10FE7K', 'NpQ9X77o34', '男', '1958-10-05 00:00:00', 174, 86, '2021-08-22 21:47:15', NULL),
(2, '7845hC4uZg', '3zH80y88RF', '男', '1930-02-20 00:00:00', 172, 55, '2021-08-22 21:47:15', NULL),
(3, 'R5v94P7Df1', 'M4C39w7nB7', '男', '1957-08-14 00:00:00', 172, 66, '2021-08-22 21:47:15', NULL),
(4, 'G08O6sUL88', 'M690NK4g3K', '女', '1992-03-25 00:00:00', 160, 73, '2021-08-22 21:47:15', NULL),
(5, 'y8bY04C69N', 'g8Z00k5dM7', '男', '1941-02-14 00:00:00', 175, 57, '2021-08-22 21:47:15', NULL),
(6, '5wU9I59ge4', 'w31b6Nn9v3', '男', '1917-12-13 00:00:00', 185, 60, '2021-08-22 21:47:15', NULL),
(7, 'Q3ID1v282z', 'TMnb3112H7', '男', '1986-07-06 00:00:00', 152, 81, '2021-08-22 21:47:15', NULL),
(8, 'HVaP696n80', '00I93ZG8tM', '女', '1932-06-13 00:00:00', 151, 77, '2021-08-22 21:47:15', NULL),
(9, '2v11v5j3kD', 'f59tb87W7z', '男', '1988-03-17 00:00:00', 164, 73, '2021-08-22 21:47:16', NULL),
(10, 'k1Z63Ob71c', '7FXuM5s459', '女', '1942-04-29 00:00:00', 147, 59, '2021-08-22 21:47:16', NULL),
(11, 'FdS82W9k44', '051pyY7u8W', '男', '1990-01-06 00:00:00', 175, 89, '2021-08-22 21:47:16', NULL),
(12, 'sX8Qp103e3', '78a3Sz9dq1', '女', '1936-11-26 00:00:00', 156, 39, '2021-08-22 21:47:16', NULL),
(13, '0aD6J0C95e', '2l63aOg6f9', '男', '1924-03-16 00:00:00', 183, 87, '2021-08-22 21:47:16', NULL),
(14, '1t074Pbdy0', '3FOj47iZ49', '女', '2008-01-16 00:00:00', 170, 53, '2021-08-22 21:47:16', NULL),
(15, '11iYH2e71y', 'or3dk6d693', '女', '1961-10-30 00:00:00', 174, 75, '2021-08-22 21:47:16', NULL),
(16, 'a5mAy3426R', 'p74WF8P25A', '男', '1929-06-29 00:00:00', 177, 66, '2021-08-22 21:47:16', NULL),
(17, 'Xnr28X451q', 'bNH5190z0e', '女', '1916-01-25 00:00:00', 174, 60, '2021-08-22 21:47:16', NULL),
(18, 'TMkW84e146', 'e2m28gh48B', '男', '1943-02-20 00:00:00', 166, 83, '2021-08-22 21:47:16', NULL),
(19, 'p62X5kB17y', 'E756ML1h2R', '女', '1979-04-22 00:00:00', 159, 73, '2021-08-22 21:47:16', NULL),
(20, 'v85b0ze9D4', 'f20jl9ve46', '女', '1922-09-12 00:00:00', 167, 39, '2021-08-22 21:47:16', NULL),
(21, '3ezN56YL41', 'PS9Yc694R8', '女', '1960-10-15 00:00:00', 168, 62, '2021-08-22 21:47:16', NULL),
(22, '8i9dgp9r13', 'W7820eIL0M', '男', '1980-01-21 00:00:00', 198, 60, '2021-08-22 21:47:16', NULL),
(23, 'Z5Cy7727Rb', '388E1t9Epx', '男', '1941-06-08 00:00:00', 198, 94, '2021-08-22 21:47:16', NULL),
(24, '8i6z9YJR51', 'KAIc72z513', '男', '2005-10-27 00:00:00', 173, 70, '2021-08-22 21:47:16', NULL),
(25, '4ShoZ09K70', '4148CBEEb2', '女', '1946-07-04 00:00:00', 161, 76, '2021-08-22 21:47:16', NULL),
(26, 'ryD157z1D6', '3IlkLJ3816', '男', '1948-05-24 00:00:00', 185, 77, '2021-08-22 21:47:16', NULL),
(27, 'G4E9EPW131', 'g606VrX1A0', '女', '1917-04-22 00:00:00', 150, 80, '2021-08-22 21:47:16', NULL),
(28, '23DVl0e36z', 'I77p4Xae26', '女', '1981-01-27 00:00:00', 169, 46, '2021-08-22 21:47:16', NULL),
(29, '1Qp6YH456W', '4f1NL8s2b3', '女', '1988-05-15 00:00:00', 154, 77, '2021-08-22 21:47:16', NULL),
(30, '3xP8y989ox', 'Gl29I5xG65', '女', '1913-02-28 00:00:00', 173, 62, '2021-08-22 21:47:16', NULL),
(31, 'Fgf975SD44', 'hK780BA81P', '女', '1960-01-20 00:00:00', 147, 62, '2021-08-22 21:47:16', NULL),
(32, '32iu0B6zz5', '99pFuC32k0', '男', '1995-12-02 00:00:00', 160, 67, '2021-08-22 21:47:16', NULL),
(33, 'peR2149Yp3', 'N083tr9rW7', '男', '1952-10-18 00:00:00', 195, 100, '2021-08-22 21:47:16', NULL),
(34, 'pzr26W79I9', '9F0b39aBQ3', '女', '1925-03-21 00:00:00', 161, 58, '2021-08-22 21:47:16', NULL),
(35, 'pH30S9Ey18', '5r40oO7P9L', '男', '1980-07-25 00:00:00', 184, 86, '2021-08-22 21:47:16', NULL),
(36, '75x1Avz4Q7', '602v92BJXA', '男', '1918-04-10 00:00:00', 176, 63, '2021-08-22 21:47:16', NULL),
(37, '83pC3XA19h', '0S1b63N0BO', '男', '2010-04-30 00:00:00', 162, 68, '2021-08-22 21:47:16', NULL),
(38, '0J273x0EaK', 'c9W3ZK4t47', '女', '1950-02-04 00:00:00', 156, 71, '2021-08-22 21:47:17', NULL),
(39, '3R01u1Ur9r', '7gel07q80W', '女', '1959-08-21 00:00:00', 154, 73, '2021-08-22 21:47:17', NULL),
(40, 'k88oRx449b', '8K83bOX3D9', '女', '1985-11-20 00:00:00', 164, 38, '2021-08-22 21:47:17', NULL),
(41, '63uc7sb7j1', '721zpe3v0m', '女', '1979-11-08 00:00:00', 143, 64, '2021-08-22 21:47:17', NULL),
(42, 'WHy71h913v', 'A74zR00u7N', '男', '2007-06-19 00:00:00', 185, 59, '2021-08-22 21:47:17', NULL),
(43, 'h7Q20jy7B9', '9X3Vu98g2G', '男', '1953-04-10 00:00:00', 193, 71, '2021-08-22 21:47:17', NULL),
(44, '74rrd4wK23', 'uh1D3to721', '男', '1983-03-03 00:00:00', 171, 58, '2021-08-22 21:47:17', NULL),
(45, '4X6V54E5oe', '5XqP3Z27m4', '男', '1995-08-22 00:00:00', 195, 96, '2021-08-22 21:47:17', NULL),
(46, '8t09D79qFw', 'd86uHL2O58', '男', '2003-06-10 00:00:00', 191, 61, '2021-08-22 21:47:17', NULL),
(47, '7uD6LkA121', '1gD08XbJ17', '女', '1954-08-23 00:00:00', 179, 43, '2021-08-22 21:47:17', NULL),
(48, 'd642tlK02v', 'ao7h46P20Y', '男', '1977-09-16 00:00:00', 151, 100, '2021-08-22 21:47:17', NULL),
(49, '9dmHc7H971', '710vH7rB6C', '男', '2000-04-28 00:00:00', 192, 63, '2021-08-22 21:47:17', NULL),
(50, 'Ff7v76g4C9', '64M8a0E9eq', '女', '2010-05-24 00:00:00', 142, 46, '2021-08-22 21:47:17', NULL),
(51, '466J6jh1SF', 'x5d76lu90n', '男', '1983-10-04 00:00:00', 194, 72, '2021-08-22 21:47:17', NULL),
(52, 'D0jOFF4472', 'vWum71x241', '女', '1990-12-25 00:00:00', 144, 60, '2021-08-22 21:47:17', NULL),
(53, '2hy0E4V5y5', '81Io1Rn8f8', '男', '1998-11-26 00:00:00', 162, 94, '2021-08-22 21:47:17', NULL),
(54, '0GmAw2s742', '4xU41q1EZ4', '女', '1995-09-09 00:00:00', 148, 61, '2021-08-22 21:47:17', NULL),
(55, '1v2171qwAS', '12MLa78j2F', '男', '1946-07-14 00:00:00', 153, 67, '2021-08-22 21:47:17', NULL),
(56, 'l68JVj88e9', '4Z74bf4a3P', '男', '2003-08-11 00:00:00', 185, 94, '2021-08-22 21:47:17', NULL),
(57, 'w0936tKU4r', 'aK70s7IV07', '女', '1993-06-08 00:00:00', 160, 59, '2021-08-22 21:47:17', NULL),
(58, '9I3Zy50rb6', '93u6OEdV28', '男', '1968-05-27 00:00:00', 181, 67, '2021-08-22 21:47:17', NULL),
(59, 'HF59O17ZG3', 'FmF66l551y', '女', '1977-09-12 00:00:00', 153, 51, '2021-08-22 21:47:17', NULL),
(60, '771F56fvhg', '80LO8L26Xk', '女', '1946-03-15 00:00:00', 173, 73, '2021-08-22 21:47:17', NULL),
(61, 'Z56t97x5kL', 'lz69nzU011', '男', '2002-03-06 00:00:00', 163, 56, '2021-08-22 21:47:17', NULL),
(62, '91K25khI0l', '6Pg886mT4e', '女', '1956-08-16 00:00:00', 169, 49, '2021-08-22 21:47:17', NULL),
(63, 'rx7H3P2V34', 'vR0739LA0h', '女', '1922-11-11 00:00:00', 149, 60, '2021-08-22 21:47:17', NULL),
(64, 'n18F0qxT82', 'F74p4mO17D', '女', '1915-03-12 00:00:00', 158, 42, '2021-08-22 21:47:17', NULL),
(65, 'z518O73JGB', '0i061EmH9E', '男', '1980-11-01 00:00:00', 187, 78, '2021-08-22 21:47:17', NULL),
(66, 'SaZ1e5673t', 'G6K18kFH93', '男', '1939-08-22 00:00:00', 173, 82, '2021-08-22 21:47:18', NULL),
(67, 'am5JG6Y227', 'T2Tc5r251k', '男', '2010-08-15 00:00:00', 152, 79, '2021-08-22 21:47:18', NULL),
(68, 'iwz82c66j2', 'YK910G4UU6', '男', '2006-04-13 00:00:00', 196, 51, '2021-08-22 21:47:18', NULL),
(69, '3x59wfhp29', '755z9LqL7Y', '女', '1933-12-26 00:00:00', 179, 53, '2021-08-22 21:47:18', NULL),
(70, '6u73iH2H0p', 'W825o2K4TS', '女', '1943-07-12 00:00:00', 160, 44, '2021-08-22 21:47:18', NULL),
(71, 'qN908nb38o', 'xtr8A2984P', '女', '1979-06-22 00:00:00', 147, 42, '2021-08-22 21:47:18', NULL),
(72, 'u73Lwk7n92', '90cV90Y5pQ', '男', '1959-07-06 00:00:00', 188, 95, '2021-08-22 21:47:18', NULL),
(73, 'qJ53P8a64M', 'jG88V7j1a4', '女', '1939-12-01 00:00:00', 158, 66, '2021-08-22 21:47:18', NULL),
(74, '04m04uSMC6', 'a5dQ4V5Z99', '女', '1944-02-04 00:00:00', 180, 57, '2021-08-22 21:47:18', NULL),
(75, '4u85IlIC93', '6ATF863u8i', '女', '1935-09-09 00:00:00', 174, 56, '2021-08-22 21:47:18', NULL),
(76, 'kh259a62lj', '67M92NAuK3', '女', '1973-10-31 00:00:00', 143, 76, '2021-08-22 21:47:18', NULL),
(77, '9s7yC61V7u', '0X7827sFpH', '女', '1962-01-09 00:00:00', 173, 64, '2021-08-22 21:47:18', NULL),
(78, 'd4gR94d8S5', '25U473dxvR', '男', '1965-05-19 00:00:00', 167, 59, '2021-08-22 21:47:18', NULL),
(79, 'Cf395S5M8T', '2566HnvF6V', '男', '1951-01-29 00:00:00', 153, 69, '2021-08-22 21:47:18', NULL),
(80, '3j535uiyj1', 'r859G7y0CD', '男', '1979-12-02 00:00:00', 162, 85, '2021-08-22 21:47:18', NULL),
(81, 'BuSZ217n84', '79O3a2mnc5', '女', '1923-08-01 00:00:00', 140, 66, '2021-08-22 21:47:18', NULL),
(82, 'y08BUc6b16', 'Rpw2z08E05', '男', '1966-03-18 00:00:00', 200, 89, '2021-08-22 21:47:18', NULL),
(83, 'b9j5Y2Y47W', 'uw909zv9Y9', '女', '1970-07-18 00:00:00', 149, 62, '2021-08-22 21:47:18', NULL),
(84, '1Gu49Y0B5q', '4qc0I58S8u', '男', '1941-08-10 00:00:00', 198, 64, '2021-08-22 21:47:18', NULL),
(85, 'b052wC77kk', '595Ak1eW0p', '女', '0000-00-00 00:00:00', 146, 43, '2021-08-22 21:47:18', NULL),
(86, 'wr138O4U7m', 'f5K6nW8e01', '女', '1989-04-21 00:00:00', 166, 36, '2021-08-22 21:47:18', NULL),
(87, 'gc86uX2v01', 'Yu8l458x8g', '男', '1977-01-17 00:00:00', 161, 72, '2021-08-22 21:47:18', NULL),
(88, '88jO9MHU17', '6wCyEJ0651', '女', '1995-05-10 00:00:00', 150, 74, '2021-08-22 21:47:18', NULL),
(89, 'a976tN4Y3g', '51i2KffK16', '女', '1949-07-18 00:00:00', 170, 49, '2021-08-22 21:47:18', NULL),
(90, 'z570ZCEW06', 'x4H2m98V4K', '女', '1931-04-08 00:00:00', 173, 45, '2021-08-22 21:47:18', NULL),
(91, 'j753Qki3t7', '59U4U8EE9t', '男', '1912-05-20 00:00:00', 157, 57, '2021-08-22 21:47:18', NULL),
(92, 'c1Ler6h180', 'c64FA993oS', '女', '2007-01-07 00:00:00', 140, 35, '2021-08-22 21:47:18', NULL),
(93, '80283YdyyU', '9V633p4lmU', '男', '1922-04-23 00:00:00', 157, 93, '2021-08-22 21:47:18', NULL),
(94, 'rz0289Yco5', 'hKkwP21551', '男', '1914-02-17 00:00:00', 189, 70, '2021-08-22 21:47:19', NULL),
(95, 'nv6c8d1t54', 'u1j05F3r9V', '女', '1980-04-01 00:00:00', 161, 38, '2021-08-22 21:47:19', NULL),
(96, '37lf46sM9k', '29B1KG37RR', '男', '1933-01-07 00:00:00', 165, 76, '2021-08-22 21:47:19', NULL),
(97, 'cN149TE69r', 'Fo56587gVV', '女', '1974-01-08 00:00:00', 169, 41, '2021-08-22 21:47:19', NULL),
(98, '3F3O12Ye3O', '119g2FLnE9', '女', '1929-07-05 00:00:00', 171, 79, '2021-08-22 21:47:19', NULL),
(99, '26AO1JJU83', 'b6Y4963Uxt', '男', '1947-12-15 00:00:00', 190, 93, '2021-08-22 21:47:19', NULL),
(100, 'qS020Jm25k', '9qp8D7Zs40', '女', '1918-08-27 00:00:00', 171, 78, '2021-08-22 21:47:19', NULL);

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`UserID`),
  ADD UNIQUE KEY `UserName` (`UserName`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `user`
--
ALTER TABLE `user`
  MODIFY `UserID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
