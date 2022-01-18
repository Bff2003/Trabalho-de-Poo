-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 23-Nov-2021 às 01:02
-- Versão do servidor: 10.4.21-MariaDB
-- versão do PHP: 8.0.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `sensors`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `alert`
--

CREATE TABLE `alert` (
  `idAlert` int(11) NOT NULL,
  `idSensor` int(11) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `description` varchar(45) NOT NULL,
  `cleared` bit(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `location`
--

CREATE TABLE `location` (
  `idLocation` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `description` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `location`
--

INSERT INTO `location` (`idLocation`, `name`, `description`) VALUES
(1, 'Prometheus Server', 'Prometheus Server @ lab. 163 / ISE /UAlg'),
(3, 'Ualg Server', 'Ualg Server @ lab. 167 / ISE /UAlg'),
(7, 'ESEC Server', 'ESEC Server @ lab. 167 / ISE /UAlg'),
(8, 'ISE Server', 'ISE Server @ lab. 167 / ISE /UAlg');

-- --------------------------------------------------------

--
-- Estrutura da tabela `reading`
--

CREATE TABLE `reading` (
  `idReading` int(11) NOT NULL,
  `idSensor` int(11) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `value` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `reading`
--

INSERT INTO `reading` (`idReading`, `idSensor`, `timestamp`, `value`) VALUES
(63, 5, '2021-11-23 00:00:57', 21.9),
(64, 5, '2021-11-23 00:00:58', 13.9),
(65, 5, '2021-11-23 00:00:59', 10),
(66, 5, '2021-11-23 00:01:00', 14.8),
(67, 5, '2021-11-23 00:01:01', 12.2),
(68, 5, '2021-11-23 00:01:02', 12.7),
(69, 5, '2021-11-23 00:01:03', 10.6),
(70, 5, '2021-11-23 00:01:04', 10.5),
(71, 5, '2021-11-23 00:01:05', 13.3),
(72, 5, '2021-11-23 00:01:06', 14.2),
(73, 5, '2021-11-23 00:01:07', 11.5),
(74, 5, '2021-11-23 00:01:08', 14.6),
(75, 5, '2021-11-23 00:01:09', 11.5),
(76, 5, '2021-11-23 00:01:10', 9.4),
(77, 5, '2021-11-23 00:01:11', 9.9),
(78, 5, '2021-11-23 00:01:13', 12.1),
(79, 5, '2021-11-23 00:01:14', 13.6),
(80, 5, '2021-11-23 00:01:15', 13),
(81, 5, '2021-11-23 00:01:16', 19.6),
(82, 5, '2021-11-23 00:01:17', 18);

-- --------------------------------------------------------

--
-- Estrutura da tabela `sensor`
--

CREATE TABLE `sensor` (
  `idSensor` int(11) NOT NULL,
  `idLocation` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `unit` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `sensor`
--

INSERT INTO `sensor` (`idSensor`, `idLocation`, `name`, `unit`) VALUES
(5, 1, 'cpu_sensor_01', 'percent');

-- --------------------------------------------------------

--
-- Estrutura da tabela `unit`
--

CREATE TABLE `unit` (
  `unit` varchar(45) NOT NULL,
  `description` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `unit`
--

INSERT INTO `unit` (`unit`, `description`) VALUES
('percent', 'percentage of usage');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `alert`
--
ALTER TABLE `alert`
  ADD PRIMARY KEY (`idAlert`),
  ADD KEY `fk_Alert_Sensor1_idx` (`idSensor`);

--
-- Índices para tabela `location`
--
ALTER TABLE `location`
  ADD PRIMARY KEY (`idLocation`),
  ADD UNIQUE KEY `name_UNIQUE` (`name`);

--
-- Índices para tabela `reading`
--
ALTER TABLE `reading`
  ADD PRIMARY KEY (`idReading`),
  ADD KEY `fk_Reading_Sensor1_idx` (`idSensor`);

--
-- Índices para tabela `sensor`
--
ALTER TABLE `sensor`
  ADD PRIMARY KEY (`idSensor`),
  ADD UNIQUE KEY `uniq_loc_vs_sensor` (`idLocation`,`name`),
  ADD KEY `fk_Sensor_Location_idx` (`idLocation`),
  ADD KEY `fk_Sensor_Units1_idx` (`unit`);

--
-- Índices para tabela `unit`
--
ALTER TABLE `unit`
  ADD PRIMARY KEY (`unit`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `alert`
--
ALTER TABLE `alert`
  MODIFY `idAlert` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `location`
--
ALTER TABLE `location`
  MODIFY `idLocation` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de tabela `reading`
--
ALTER TABLE `reading`
  MODIFY `idReading` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=83;

--
-- AUTO_INCREMENT de tabela `sensor`
--
ALTER TABLE `sensor`
  MODIFY `idSensor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `alert`
--
ALTER TABLE `alert`
  ADD CONSTRAINT `fk_Alert_Sensor1` FOREIGN KEY (`idSensor`) REFERENCES `sensor` (`idSensor`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limitadores para a tabela `reading`
--
ALTER TABLE `reading`
  ADD CONSTRAINT `fk_Reading_Sensor1` FOREIGN KEY (`idSensor`) REFERENCES `sensor` (`idSensor`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limitadores para a tabela `sensor`
--
ALTER TABLE `sensor`
  ADD CONSTRAINT `fk_Sensor_Location` FOREIGN KEY (`idLocation`) REFERENCES `location` (`idLocation`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_Sensor_Units1` FOREIGN KEY (`unit`) REFERENCES `unit` (`unit`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
