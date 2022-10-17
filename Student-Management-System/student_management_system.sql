-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 05, 2020 at 06:07 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `student_management_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `Roll_no` varchar(15) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Father_Name` varchar(55) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `Category` varchar(10) NOT NULL,
  `Branch` varchar(30) NOT NULL,
  `Year` varchar(10) NOT NULL,
  `Contact_no` varchar(10) NOT NULL,
  `Address` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`Roll_no`, `Name`, `Father_Name`, `Gender`, `Category`, `Branch`, `Year`, `Contact_no`, `Address`) VALUES
('19bcs086', 'sanil sarathe', 'mr sarathe ji', 'Male', 'General', 'Compter Science', 'Year 3', '9876556789', 'bhopal		\n\n\n'),
('19bcs082', 'jatin sadhwani', 'jai prakash sadhwani', 'Male', 'General', 'Compter Science', 'Year 3', '7566647818', 'gwalior\n'),
('19bcs083', 'Neeraj kumar', 'Mr Kumar', 'Male', 'General', 'Compter Science', 'Year 3', '9877899876', 'Gwalior Sikandar kampoo lashkatr\n\n');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
