CREATE DATABASE  IF NOT EXISTS `prebuiltdb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `prebuiltdb`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: prebuiltdb
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `behuizing`
--

DROP TABLE IF EXISTS `behuizing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `behuizing` (
  `BehuizingID` int NOT NULL AUTO_INCREMENT,
  `Naam` varchar(45) DEFAULT NULL,
  `AantalFans` int DEFAULT NULL,
  `Afmetingen` varchar(45) DEFAULT NULL,
  `Stock` int DEFAULT NULL,
  `Prijs` float DEFAULT NULL,
  `LeverancierID` int DEFAULT NULL,
  PRIMARY KEY (`BehuizingID`),
  KEY `LeverancierID_idx` (`LeverancierID`),
  CONSTRAINT `LeverancierID` FOREIGN KEY (`LeverancierID`) REFERENCES `leverancier` (`LeverancierID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `behuizing`
--

LOCK TABLES `behuizing` WRITE;
/*!40000 ALTER TABLE `behuizing` DISABLE KEYS */;
INSERT INTO `behuizing` VALUES (1,'Big Tower',4,'100x100x40',2,149.99,1);
/*!40000 ALTER TABLE `behuizing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cpu`
--

DROP TABLE IF EXISTS `cpu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cpu` (
  `CPUID` int NOT NULL AUTO_INCREMENT,
  `Naam` varchar(45) DEFAULT NULL,
  `Clock` varchar(45) DEFAULT NULL,
  `Cores` int DEFAULT NULL,
  `Socket` varchar(45) DEFAULT NULL,
  `Stock` int DEFAULT NULL,
  `Prijs` float DEFAULT NULL,
  `LeverancierID` int DEFAULT NULL,
  PRIMARY KEY (`CPUID`),
  KEY `LevInCpu_idx` (`LeverancierID`),
  CONSTRAINT `LevInCpu` FOREIGN KEY (`LeverancierID`) REFERENCES `leverancier` (`LeverancierID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cpu`
--

LOCK TABLES `cpu` WRITE;
/*!40000 ALTER TABLE `cpu` DISABLE KEYS */;
INSERT INTO `cpu` VALUES (1,'I9 13900K','5,2GHz',24,'1700',5,675.95,2);
/*!40000 ALTER TABLE `cpu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gpu`
--

DROP TABLE IF EXISTS `gpu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gpu` (
  `GPUID` int NOT NULL AUTO_INCREMENT,
  `Naam` varchar(45) DEFAULT NULL,
  `Clock` varchar(45) DEFAULT NULL,
  `VramCap` varchar(45) DEFAULT NULL,
  `GDDR` varchar(45) DEFAULT NULL,
  `Stock` int DEFAULT NULL,
  `Prijs` float DEFAULT NULL,
  `LeverancierID` int DEFAULT NULL,
  PRIMARY KEY (`GPUID`),
  KEY `LevInGpu_idx` (`LeverancierID`),
  CONSTRAINT `LevInGpu` FOREIGN KEY (`LeverancierID`) REFERENCES `leverancier` (`LeverancierID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gpu`
--

LOCK TABLES `gpu` WRITE;
/*!40000 ALTER TABLE `gpu` DISABLE KEYS */;
INSERT INTO `gpu` VALUES (1,'Nvidia GeForce RTX 4080','2535MHz','16GB','6X',1,1479,3);
/*!40000 ALTER TABLE `gpu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `leverancier`
--

DROP TABLE IF EXISTS `leverancier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `leverancier` (
  `LeverancierID` int NOT NULL AUTO_INCREMENT,
  `Naam` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`LeverancierID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leverancier`
--

LOCK TABLES `leverancier` WRITE;
/*!40000 ALTER TABLE `leverancier` DISABLE KEYS */;
INSERT INTO `leverancier` VALUES (1,'Corsair'),(2,'Intel'),(3,'GIGABYTE'),(4,'ASUS'),(5,'SAMSUNG');
/*!40000 ALTER TABLE `leverancier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `moederbord`
--

DROP TABLE IF EXISTS `moederbord`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `moederbord` (
  `MomID` int NOT NULL AUTO_INCREMENT,
  `Naam` varchar(45) DEFAULT NULL,
  `Socket` varchar(45) DEFAULT NULL,
  `DDR` int DEFAULT NULL,
  `GDDR` varchar(45) DEFAULT NULL,
  `Stock` int DEFAULT NULL,
  `Prijs` float DEFAULT NULL,
  `LeverancierID` int DEFAULT NULL,
  PRIMARY KEY (`MomID`),
  KEY `LevInMom_idx` (`LeverancierID`),
  CONSTRAINT `LevInMom` FOREIGN KEY (`LeverancierID`) REFERENCES `leverancier` (`LeverancierID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `moederbord`
--

LOCK TABLES `moederbord` WRITE;
/*!40000 ALTER TABLE `moederbord` DISABLE KEYS */;
INSERT INTO `moederbord` VALUES (1,'ROG STRIX B760-F GAMING','1700',5,'6X',8,269,4);
/*!40000 ALTER TABLE `moederbord` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `opslag`
--

DROP TABLE IF EXISTS `opslag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `opslag` (
  `OpslagID` int NOT NULL AUTO_INCREMENT,
  `Naam` varchar(45) DEFAULT NULL,
  `TypeID` int DEFAULT NULL,
  `Capaciteit` varchar(45) DEFAULT NULL,
  `Stock` int DEFAULT NULL,
  `Prijs` float DEFAULT NULL,
  `LeverancierID` int DEFAULT NULL,
  PRIMARY KEY (`OpslagID`),
  KEY `TypeID_idx` (`TypeID`),
  KEY `LeverancierIDinOpslag_idx` (`LeverancierID`),
  CONSTRAINT `LeverancierIDinOpslag` FOREIGN KEY (`LeverancierID`) REFERENCES `leverancier` (`LeverancierID`),
  CONSTRAINT `TypeID` FOREIGN KEY (`TypeID`) REFERENCES `type` (`TypeID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `opslag`
--

LOCK TABLES `opslag` WRITE;
/*!40000 ALTER TABLE `opslag` DISABLE KEYS */;
INSERT INTO `opslag` VALUES (1,'990 Pro',1,'2TB',4,190,5);
/*!40000 ALTER TABLE `opslag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prebuilt`
--

DROP TABLE IF EXISTS `prebuilt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prebuilt` (
  `PrebuiltID` int NOT NULL AUTO_INCREMENT,
  `BehuizingID` int DEFAULT NULL,
  `OpslagID` int DEFAULT NULL,
  `CPUID` int DEFAULT NULL,
  `GPUID` int DEFAULT NULL,
  `RAMID` int DEFAULT NULL,
  `PSUID` int DEFAULT NULL,
  `MomID` int DEFAULT NULL,
  PRIMARY KEY (`PrebuiltID`),
  KEY `psuid_idx` (`PSUID`),
  KEY `ramid_idx` (`RAMID`),
  KEY `motid_idx` (`MomID`),
  KEY `opslagid_idx` (`OpslagID`),
  KEY `gpuid_idx` (`GPUID`),
  KEY `cpuid_idx` (`CPUID`),
  KEY `behID_idx` (`BehuizingID`),
  CONSTRAINT `behID` FOREIGN KEY (`BehuizingID`) REFERENCES `behuizing` (`BehuizingID`),
  CONSTRAINT `cpuid` FOREIGN KEY (`CPUID`) REFERENCES `cpu` (`CPUID`),
  CONSTRAINT `gpuid` FOREIGN KEY (`GPUID`) REFERENCES `gpu` (`GPUID`),
  CONSTRAINT `motid` FOREIGN KEY (`MomID`) REFERENCES `moederbord` (`MomID`),
  CONSTRAINT `opslagid` FOREIGN KEY (`OpslagID`) REFERENCES `opslag` (`OpslagID`),
  CONSTRAINT `psuid` FOREIGN KEY (`PSUID`) REFERENCES `psu` (`PSUID`),
  CONSTRAINT `ramid` FOREIGN KEY (`RAMID`) REFERENCES `ram` (`RAMID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prebuilt`
--

LOCK TABLES `prebuilt` WRITE;
/*!40000 ALTER TABLE `prebuilt` DISABLE KEYS */;
INSERT INTO `prebuilt` VALUES (1,1,1,1,1,2,1,1);
/*!40000 ALTER TABLE `prebuilt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `psu`
--

DROP TABLE IF EXISTS `psu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `psu` (
  `PSUID` int NOT NULL AUTO_INCREMENT,
  `Naam` varchar(45) DEFAULT NULL,
  `Watt` int DEFAULT NULL,
  `TypeID` int DEFAULT NULL,
  `Stock` int DEFAULT NULL,
  `Prijs` float DEFAULT NULL,
  `LeverancierID` int DEFAULT NULL,
  PRIMARY KEY (`PSUID`),
  KEY `LevInPsu_idx` (`LeverancierID`),
  KEY `TypInPsu_idx` (`TypeID`),
  CONSTRAINT `LevInPsu` FOREIGN KEY (`LeverancierID`) REFERENCES `leverancier` (`LeverancierID`),
  CONSTRAINT `TypInPsu` FOREIGN KEY (`TypeID`) REFERENCES `type` (`TypeID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `psu`
--

LOCK TABLES `psu` WRITE;
/*!40000 ALTER TABLE `psu` DISABLE KEYS */;
INSERT INTO `psu` VALUES (1,'RM1000e V2 PSU',1000,2,4,144.9,1);
/*!40000 ALTER TABLE `psu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ram`
--

DROP TABLE IF EXISTS `ram`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ram` (
  `RAMID` int NOT NULL AUTO_INCREMENT,
  `Naam` varchar(45) DEFAULT NULL,
  `Clock` varchar(45) DEFAULT NULL,
  `Capaciteit` varchar(45) DEFAULT NULL,
  `DDR` int DEFAULT NULL,
  `Stock` int DEFAULT NULL,
  `Prijs` float DEFAULT NULL,
  `LeverancierID` int DEFAULT NULL,
  PRIMARY KEY (`RAMID`),
  KEY `LevInRam_idx` (`LeverancierID`),
  CONSTRAINT `LevInRam` FOREIGN KEY (`LeverancierID`) REFERENCES `leverancier` (`LeverancierID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ram`
--

LOCK TABLES `ram` WRITE;
/*!40000 ALTER TABLE `ram` DISABLE KEYS */;
INSERT INTO `ram` VALUES (1,'Vengeance','4000MHz','16GB',4,3,99.8,1),(2,'Vengeance','6800MGh','32GB',5,7,152.9,1);
/*!40000 ALTER TABLE `ram` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `type`
--

DROP TABLE IF EXISTS `type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `type` (
  `TypeID` int NOT NULL AUTO_INCREMENT,
  `Naam` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`TypeID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `type`
--

LOCK TABLES `type` WRITE;
/*!40000 ALTER TABLE `type` DISABLE KEYS */;
INSERT INTO `type` VALUES (1,'M.2'),(2,'Modulair');
/*!40000 ALTER TABLE `type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `UserID` int NOT NULL AUTO_INCREMENT,
  `Gebruikersnaam` varchar(45) NOT NULL,
  `Passwoord` varchar(200) NOT NULL,
  `Naam` varchar(45) DEFAULT NULL,
  `Adres` varchar(45) DEFAULT NULL,
  `Uitgegeven` float DEFAULT NULL,
  `IsAdmin` tinyint DEFAULT NULL,
  `Salt` varchar(200) NOT NULL,
  PRIMARY KEY (`UserID`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Robbert','f65d2de7cedb039b61524a007564702218ccf74ea3b9cbb74d745be661eedff8','Robbert Groffi','Halingenstraat 32',3061.74,1,'³LRÖÞº\n­Q$ÿjLó<B<ÉÄ5YäÃQÊ'),(16,'Robbyvgaming','2e9e4e019dd50a05b4b80d7e5d59a25aeabae28b88ded3334266e3d510ff0c76',NULL,NULL,NULL,NULL,'­¾:F\"Ò¡Ê¼Ì$¿\nÞÆï\"&\ZK c\r');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'prebuiltdb'
--
/*!50003 DROP PROCEDURE IF EXISTS `get_items_from` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_items_from`(IN _leverancier_id INT)
BEGIN
    -- Behuizing table
    SELECT BehuizingID AS ID, Naam FROM behuizing WHERE LeverancierID = _leverancier_id

    UNION

    -- CPU table
    SELECT CPUID AS ID, Naam FROM cpu WHERE LeverancierID = _leverancier_id

    UNION

    -- GPU table
    SELECT GPUID AS ID, Naam FROM gpu WHERE LeverancierID = _leverancier_id

    UNION

    -- Moederbord table
    SELECT MomID AS ID, Naam FROM moederbord WHERE LeverancierID = _leverancier_id

    UNION

    -- Opslag table
    SELECT OpslagID AS ID, Naam FROM opslag WHERE LeverancierID = _leverancier_id

    UNION

    -- PSU table
    SELECT PSUID AS ID, Naam FROM psu WHERE LeverancierID = _leverancier_id

    UNION

    -- RAM table
    SELECT RAMID AS ID, Naam FROM ram WHERE LeverancierID = _leverancier_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_stock` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_stock`(IN _id INT, IN _table VARCHAR(45))
BEGIN
    -- Find the primary key column
    SELECT COLUMN_NAME INTO @primary_key
    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
    WHERE TABLE_SCHEMA = 'prebuiltdb'
      AND TABLE_NAME = _table
      AND CONSTRAINT_NAME = 'PRIMARY';

    -- Check if primary key column is found
    IF @primary_key IS NOT NULL THEN
        SET @sql = CONCAT('
            SELECT Stock
            FROM ', _table, '
            WHERE ', @primary_key, ' = ', _id, ';
        ');

        PREPARE stmt FROM @sql;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
    ELSE
        SELECT 'Primary key column not found for table: ', _table AS Message;
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_total_price` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_total_price`(
    IN _prebuilt_id INT
)
BEGIN
    -- Initialize variable for total sum
    DECLARE total_price FLOAT;

    -- Calculate total sum for all tables
    SELECT 
        SUM(Prijs) INTO total_price
    FROM (
        SELECT Prijs FROM behuizing WHERE BehuizingID = (SELECT BehuizingID FROM prebuilt WHERE PrebuiltID = _prebuilt_id)
        UNION ALL
        SELECT Prijs FROM cpu WHERE CPUID = (SELECT CPUID FROM prebuilt WHERE PrebuiltID = _prebuilt_id)
        UNION ALL
        SELECT Prijs FROM gpu WHERE GPUID = (SELECT GPUID FROM prebuilt WHERE PrebuiltID = _prebuilt_id)
        UNION ALL
        SELECT Prijs FROM moederbord WHERE MomID = (SELECT MomID FROM prebuilt WHERE PrebuiltID = _prebuilt_id)
        UNION ALL
        SELECT Prijs FROM opslag WHERE OpslagID = (SELECT OpslagID FROM prebuilt WHERE PrebuiltID = _prebuilt_id)
        UNION ALL
        SELECT Prijs FROM psu WHERE PSUID = (SELECT PSUID FROM prebuilt WHERE PrebuiltID = _prebuilt_id)
        UNION ALL
        SELECT Prijs FROM ram WHERE RAMID = (SELECT RAMID FROM prebuilt WHERE PrebuiltID = _prebuilt_id)
    ) AS combined_tables;

    -- Return the total sum in a single column
    SELECT total_price AS TotalPrice;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_user` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_user`(in _id INT)
BEGIN
	SELECT *
    FROM user
    WHERE UserID = _id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_userID` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_userID`(IN p_Gebruikersnaam VARCHAR(255), OUT p_userID INT)
BEGIN
    SELECT userID INTO p_userID
    FROM user
    WHERE Gebruikersnaam = p_Gebruikersnaam;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_user_account` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_user_account`(in _gebruikersnaam varchar(45), in _passwoord varchar(200), in _salt varchar(200))
BEGIN
	INSERT INTO user(Gebruikersnaam, Passwoord, Salt)
    VALUES(_gebruikersnaam, _passwoord, _salt);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-21 14:03:09
