-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 29, 2021 at 01:10 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bibo`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `id` int(11) NOT NULL,
  `firstname` varchar(65) NOT NULL,
  `name` varchar(65) NOT NULL,
  `address` varchar(65) NOT NULL,
  `mobile` varchar(15) NOT NULL,
  `born` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`id`, `firstname`, `name`, `address`, `mobile`, `born`) VALUES
(1, 'Jack', 'Warren', 'P.O. Box 282, 5650 Ac Ave', '+4922813544', '2001-03-23'),
(2, 'Idola', 'Pope', 'P.O. Box 774, 831 Sem Avenue', '+4998895899', '1974-12-09'),
(3, 'Ulysses', 'Riggs', '283-7850 Semper Avenue', '+4937048669', '1979-05-08'),
(4, 'Irene', 'Chase', '9873 Pede. Road', '+4928621006', '1988-11-05'),
(5, 'Jameson', 'Juarez', '695-2946 Tincidunt Avenue', '+4906216050', '1975-10-25'),
(6, 'Joelle', 'Hurley', '2943 Amet St.', '+4956249607', '1985-08-18'),
(7, 'Justina', 'English', 'Ap #517-6575 Lectus, St.', '+4995421508', '1980-04-20'),
(8, 'Ella', 'Gilbert', 'Ap #956-9397 Cursus Ave', '+4930137304', '2002-06-24'),
(9, 'Yuli', 'Pittman', 'P.O. Box 318, 9300 Quis St.', '+4917142660', '1996-10-06'),
(10, 'Miranda', 'Barnes', 'Ap #144-4962 Eu Rd.', '+4964106212', '1996-05-17'),
(11, 'Katell', 'Leach', 'Ap #356-7021 Risus. Avenue', '+4932267748', '1989-12-13'),
(12, 'Blair', 'Grant', 'Ap #254-8240 Vivamus Av.', '+4955740144', '1973-11-27'),
(13, 'Bianca', 'Pennington', '2707 Mus. Rd.', '+4939985587', '1979-10-27'),
(14, 'Emerald', 'Gamble', '3161 Semper Street', '+4917772094', '1989-02-08'),
(15, 'Bernard', 'Welch', 'Ap #672-5030 Adipiscing Ave', '+4942699113', '1991-03-07'),
(16, 'Macaulay', 'Patel', '2357 Donec Av.', '+4961616025', '1998-04-12'),
(17, 'Meghan', 'Stone', '924-8138 Sit Rd.', '+4961615366', '1983-03-18'),
(18, 'Shaeleigh', 'Erickson', '6573 In, Street', '+4921675921', '1998-12-05'),
(19, 'Shad', 'Adkins', 'P.O. Box 434, 3970 Aliquam Av.', '+4914003151', '1972-09-07'),
(20, 'Merritt', 'Guerra', 'Ap #869-117 Dolor. St.', '+4919146277', '1978-03-09'),
(21, 'Myles', 'Pierce', 'P.O. Box 791, 487 Sit Av.', '+4959733107', '1985-07-17'),
(22, 'Leroy', 'Chase', '4491 Massa. Road', '+4907648124', '1985-05-14'),
(23, 'Jillian', 'Herman', '4264 Auctor. Rd.', '+4912323534', '1997-05-12'),
(24, 'Hayfa', 'Wright', '371-1520 Mi St.', '+4956380107', '1988-04-16'),
(25, 'Malik', 'Chase', '153-8880 Aliquam Ave', '+4967440956', '1981-04-12'),
(26, 'Xander', 'Sears', '8853 Aliquet Avenue', '+4943411031', '1976-02-19'),
(27, 'Hermione', 'Cannon', '736-9684 Purus, St.', '+4977219551', '1986-11-17'),
(28, 'Nadine', 'Ortiz', '421-3753 Quis Av.', '+4936669854', '1982-02-21'),
(29, 'Charles', 'Zamora', 'Ap #254-7409 Orci Street', '+4935055071', '2000-12-29'),
(30, 'Aimee', 'Castillo', '177-3948 Semper Av.', '+4978850504', '1991-12-14'),
(31, 'Lareina', 'Wilder', '197-3949 Risus Ave', '+4949372555', '1972-10-31'),
(32, 'Leroy', 'Noble', 'Ap #984-8154 Pharetra Road', '+4994373875', '2001-12-23'),
(33, 'Cally', 'Sharpe', '327-1139 Ac St.', '+4902481144', '1996-02-09'),
(34, 'Aiko', 'Lynch', '776-4491 Metus Avenue', '+4903787550', '1989-02-07'),
(35, 'Sybil', 'Harrell', 'P.O. Box 581, 786 Enim, Road', '+4968719675', '2000-08-22'),
(36, 'Ivory', 'Barry', '4221 Sociis Rd.', '+4940556063', '1974-07-22'),
(37, 'Jordan', 'Orr', 'P.O. Box 498, 8163 Mauris Street', '+4901662198', '1994-07-04'),
(38, 'Dustin', 'Frank', '143-8590 Netus Av.', '+4915543202', '1977-03-06'),
(39, 'Lamar', 'Floyd', '2116 Luctus, Av.', '+4981997859', '1984-05-10'),
(40, 'Delilah', 'Shepherd', 'P.O. Box 518, 8871 Erat, St.', '+4915882628', '1986-08-14'),
(41, 'Juliet', 'Winters', 'P.O. Box 717, 2117 Quam Avenue', '+4913209714', '1990-05-30'),
(42, 'Jayme', 'Lucas', '248-9602 Lectus Ave', '+4921024691', '1987-05-28'),
(43, 'Zephr', 'Vargas', 'P.O. Box 139, 5750 Tincidunt, St.', '+4916140773', '1970-10-05'),
(44, 'Anika', 'Walsh', 'Ap #889-2880 Eget Rd.', '+4903518436', '1986-11-05'),
(45, 'Wynne', 'Castro', 'P.O. Box 244, 499 Neque St.', '+4939339024', '1975-08-14'),
(46, 'Matthew', 'Joseph', '931-4282 Ultrices. Ave', '+4954595053', '1989-12-31'),
(47, 'Herrod', 'Ellison', 'Ap #558-2539 Mattis Road', '+4908127960', '2000-12-20'),
(48, 'Reese', 'Sampson', '9090 Sit Street', '+4921617366', '1986-03-14'),
(49, 'Odette', 'Henry', '9299 At, St.', '+4954837148', '1998-01-28'),
(50, 'Sigourney', 'Farmer', 'P.O. Box 381, 4684 Lacinia Av.', '+4919891884', '2001-05-30'),
(51, 'Katell', 'Stephenson', '541-4708 Nec, Rd.', '+4941094399', '1991-02-07'),
(52, 'Ryan', 'Campos', '8784 Amet Rd.', '+4952306568', '2001-11-03'),
(53, 'Nathan', 'Rodriguez', 'Ap #913-8691 Nisi Rd.', '+4946589614', '1981-07-22'),
(54, 'Illiana', 'Valenzuela', 'Ap #118-6955 Lorem, Street', '+4985739104', '1987-08-05'),
(55, 'Grant', 'Cotton', '534 Mi Avenue', '+4932636387', '1988-08-18'),
(56, 'Hashim', 'Branch', '552-7932 Ipsum Ave', '+4929976772', '1985-12-27'),
(57, 'Craig', 'Rios', '2187 Elementum Rd.', '+4915276906', '1991-10-28'),
(58, 'Sara', 'Bennett', '728-2057 Laoreet Av.', '+4922547923', '1984-02-14'),
(59, 'Xaviera', 'Newton', '6904 Suspendisse Rd.', '+4953851467', '1986-08-31'),
(60, 'Fiona', 'Matthews', '8429 Rutrum, Street', '+4905663635', '1973-10-24'),
(61, 'Curran', 'Cole', '9303 Gravida Rd.', '+4908160920', '1999-09-13'),
(62, 'Wylie', 'Weiss', '406-9964 Cursus Rd.', '+4932837129', '1998-05-13'),
(63, 'Kiona', 'Cummings', 'Ap #288-4035 Diam Avenue', '+4943148303', '1974-08-01'),
(64, 'Mikayla', 'Perry', 'Ap #715-2742 Eros. St.', '+4955394714', '1992-08-04'),
(65, 'Wang', 'Kirk', '722-4459 Eu Rd.', '+4913013587', '1977-10-08'),
(66, 'Colby', 'Huffman', 'P.O. Box 590, 8482 Mauris Rd.', '+4972194721', '1989-06-28'),
(67, 'Igor', 'Soto', 'Ap #968-4555 Sed Avenue', '+4938997480', '1991-04-02'),
(68, 'Amelia', 'Duke', 'P.O. Box 959, 524 Luctus Av.', '+4936399632', '1986-08-25'),
(69, 'Phillip', 'Weaver', 'Ap #136-5281 Placerat Street', '+4911124840', '1986-10-05'),
(70, 'Gabriel', 'Taylor', 'P.O. Box 813, 5951 Felis St.', '+4925238728', '1982-04-27'),
(71, 'Yasir', 'Sandoval', '7823 Etiam Ave', '+4925821353', '1953-06-23'),
(72, 'Brielle', 'Carpenter', '6977 Aliquam Ave', '+4962968283', '1991-08-07'),
(73, 'Beatrice', 'Dennis', 'Ap #736-3999 Fames Ave', '+4981403964', '1979-11-08'),
(74, 'Maya', 'Hull', 'Ap #900-3832 Mauris Av.', '+4987095581', '1993-06-22'),
(75, 'Yael', 'Cardenas', '898-3243 Arcu. St.', '+4978378013', '1990-11-22'),
(76, 'Dexter', 'Conner', '409-7897 Donec St.', '+4966123334', '1992-01-28'),
(77, 'Violet', 'Pearson', '468-4125 Quisque Av.', '+4952696330', '1972-06-28'),
(78, 'Kalia', 'Oconnor', '1185 Libero Av.', '+4942873972', '1988-02-02'),
(79, 'Andrew', 'Meyer', '923-9086 Ipsum. Rd.', '+4945974944', '2002-08-09'),
(80, 'Jelani', 'Nicholson', 'Ap #874-8991 Fringilla Avenue', '+4930534890', '1976-02-11'),
(81, 'Judith', 'Mcfadden', '913-2182 Dolor Road', '+4901027403', '1993-06-08'),
(82, 'Plato', 'Fisher', 'P.O. Box 220, 9002 A, Road', '+4939779790', '1947-04-29'),
(83, 'Emi', 'Fischer', 'Ap #153-6744 Pharetra. Ave', '+4930433064', '1977-07-24'),
(84, 'Judah', 'Landry', '631-8419 Sapien. Av.', '+4937977295', '1991-10-03'),
(85, 'Quincy', 'Bernard', 'Ap #194-3857 Sed Av.', '+4902046980', '1982-10-04'),
(86, 'Chandler', 'Singleton', '835-7597 Mauris Av.', '+4952476626', '1999-12-22'),
(87, 'Peter', 'Todd', '519-2304 Mi Street', '+4936725985', '2002-03-17'),
(88, 'Avye', 'Guzman', 'Ap #767-7420 Tincidunt St.', '+4901934114', '1979-04-18'),
(89, 'Delilah', 'Thompson', 'P.O. Box 441, 4097 Eleifend, Street', '+4945077401', '1984-11-09'),
(90, 'Zachery', 'Hubbard', '1923 Semper Avenue', '+4949212853', '2003-11-01'),
(91, 'Jerry', 'Wyatt', 'Ap #835-4483 Suspendisse St.', '+4998284813', '1988-10-06'),
(92, 'Inez', 'Wilder', '9357 In Road', '+4973282456', '1983-10-22'),
(93, 'Halla', 'Becker', 'Ap #935-9315 Donec St.', '+4940044220', '1972-01-10'),
(94, 'Micah', 'Wells', 'P.O. Box 609, 2934 Metus. Road', '+4972301463', '1993-01-21'),
(95, 'Cheryl', 'Mcguire', '8031 Aliquam Street', '+4972835917', '1976-07-25'),
(96, 'Slade', 'Alvarez', '5307 Fringilla Rd.', '+4900747356', '1971-01-06'),
(97, 'Laurel', 'Fleming', '744-4485 Sed St.', '+4926187340', '1973-04-16'),
(98, 'Claire', 'Middleton', '749-4334 Metus. Ave', '+4984128655', '1986-09-13'),
(99, 'Cara', 'Montoya', '8817 Faucibus Ave', '+4920150990', '1991-03-27'),
(100, 'Ignatius', 'Santana', 'P.O. Box 940, 6635 Purus St.', '+4956680516', '1999-08-02');

-- --------------------------------------------------------

--
-- Table structure for table `floor`
--

CREATE TABLE `floor` (
  `id` int(11) NOT NULL,
  `floor` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `floor`
--

INSERT INTO `floor` (`id`, `floor`) VALUES
(1, '1. Etage'),
(2, '2. Etage'),
(3, '3. Etage'),
(4, '4. Etage');

-- --------------------------------------------------------

--
-- Table structure for table `image`
--

CREATE TABLE `image` (
  `id` int(11) NOT NULL,
  `titel` varchar(65) NOT NULL,
  `author` varchar(65) NOT NULL,
  `publisher` varchar(65) NOT NULL,
  `published` date NOT NULL,
  `id_shelf` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `lending`
--

CREATE TABLE `lending` (
  `id` int(11) NOT NULL,
  `id_media` int(11) NOT NULL,
  `id_customer` int(11) NOT NULL,
  `date_output` date NOT NULL,
  `date_input` date NOT NULL,
  `type` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `literature`
--

CREATE TABLE `literature` (
  `id` int(11) NOT NULL,
  `titel` varchar(65) NOT NULL,
  `author` varchar(65) NOT NULL,
  `publisher` varchar(65) DEFAULT NULL,
  `published` date DEFAULT NULL,
  `id_shelf` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `shelf`
--

CREATE TABLE `shelf` (
  `id` int(11) NOT NULL,
  `shelf` varchar(20) NOT NULL,
  `id_floor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `sound`
--

CREATE TABLE `sound` (
  `id` int(11) NOT NULL,
  `titel` varchar(65) NOT NULL,
  `author` varchar(65) NOT NULL,
  `publisher` varchar(65) NOT NULL,
  `published` date NOT NULL,
  `id_shelf` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `floor`
--
ALTER TABLE `floor`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `image`
--
ALTER TABLE `image`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `lending`
--
ALTER TABLE `lending`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `literature`
--
ALTER TABLE `literature`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `shelf`
--
ALTER TABLE `shelf`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sound`
--
ALTER TABLE `sound`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;

--
-- AUTO_INCREMENT for table `floor`
--
ALTER TABLE `floor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `image`
--
ALTER TABLE `image`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `lending`
--
ALTER TABLE `lending`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `literature`
--
ALTER TABLE `literature`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `shelf`
--
ALTER TABLE `shelf`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sound`
--
ALTER TABLE `sound`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
