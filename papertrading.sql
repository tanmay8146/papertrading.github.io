-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 25, 2023 at 06:32 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `papertrading`
--

-- --------------------------------------------------------

--
-- Table structure for table `tradelog`
--

CREATE TABLE `tradelog` (
  `trade_id` int(20) NOT NULL,
  `id` varchar(11) DEFAULT NULL,
  `trade_date` date DEFAULT NULL,
  `exchange` varchar(8) DEFAULT NULL,
  `instrument` varchar(16) DEFAULT NULL,
  `tradetype` varchar(8) DEFAULT NULL,
  `positiontype` varchar(8) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `lotsize` int(11) DEFAULT NULL,
  `entrypoint` int(11) DEFAULT NULL,
  `target` int(11) DEFAULT NULL,
  `stoploss` int(11) DEFAULT NULL,
  `product` varchar(16) DEFAULT NULL,
  `orderstate` varchar(12) DEFAULT NULL,
  `exitpoint` int(11) DEFAULT NULL,
  `closing` int(11) DEFAULT NULL,
  `comment` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `tradelog`
--

INSERT INTO `tradelog` (`trade_id`, `id`, `trade_date`, `exchange`, `instrument`, `tradetype`, `positiontype`, `quantity`, `lotsize`, `entrypoint`, `target`, `stoploss`, `product`, `orderstate`, `exitpoint`, `closing`, `comment`) VALUES
(31, 'QCF1BFZSBI', '2023-05-15', 'NSE', 'INFY', 'regular', 'short', 100, 0, 1270, 1200, 0, 'mis', 'executed', 1210, 106000, 'close to target, intraday session over'),
(34, 'QCF1BFZSBI', '2023-05-16', 'NSE', 'ITC', 'cover', 'long', 200, 0, 415, 435, 400, 'mis', 'executed', 390, 101000, 'sudden fall'),
(35, 'ZH1Z61OOQY', '2023-05-15', 'NSE', 'BANKNIFTY 44000C', 'cover', 'long', 200, 4, 160, 300, 120, 'mis', 'executed', 280, 1024000, 'trailed stoploss'),
(36, 'ZH1Z61OOQY', '2023-05-16', 'NSE', 'REDINGTON', 'regular', 'short', 500, 0, 177, 170, 180, 'mis', 'executed', 174, 1022500, 'intraday session over'),
(37, 'ZH1Z61OOQY', '2023-05-15', 'NSE', 'LICI', 'regular', 'long', 200, 0, 558, 570, 550, 'mis', 'executed', 573, 1025500, 'target hit'),
(38, 'QCF1BFZSBI', '2023-05-15', 'NSE', 'HCLTECH', 'regular', 'long', 50, 0, 1080, 1110, 1070, 'mis', 'executed', 1110, 102500, 'nice');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` varchar(11) NOT NULL,
  `full_name` varchar(32) NOT NULL,
  `username` varchar(16) NOT NULL,
  `email` varchar(64) NOT NULL,
  `password` varchar(16) NOT NULL,
  `capital` int(11) NOT NULL,
  `broker` varchar(32) NOT NULL,
  `experience` int(11) NOT NULL,
  `reputation_score` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `full_name`, `username`, `email`, `password`, `capital`, `broker`, `experience`, `reputation_score`) VALUES
('QCF1BFZSBI', 'Tanmay Sarkar', 'tanmayxd', 'rv3nom@outlook.com', 'qq46', 102500, 'Zerodha', 4, 0),
('ZH1Z61OOQY', 'Priya Mrug', 'pm81', 'priyamrug@gmail.com', 'priya', 1025500, 'Zerodha', 1, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tradelog`
--
ALTER TABLE `tradelog`
  ADD PRIMARY KEY (`trade_id`),
  ADD KEY `id` (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tradelog`
--
ALTER TABLE `tradelog`
  MODIFY `trade_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tradelog`
--
ALTER TABLE `tradelog`
  ADD CONSTRAINT `tradelog_ibfk_1` FOREIGN KEY (`id`) REFERENCES `user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
