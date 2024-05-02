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
  `fotolink` varchar(2048) DEFAULT NULL,
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
INSERT INTO `behuizing` VALUES (1,'Obsidian 1000D',4,'100x100x40',34,149.99,1,'https://tweakers.net/i/T_ExRH7dyARulcwakGjwRJsqHPs=/fit-in/656x/filters:strip_exif()/i/2001967595.png?f=imagenormal');
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
  `fotolink` varchar(2048) DEFAULT NULL,
  PRIMARY KEY (`CPUID`),
  KEY `LevInCpu_idx` (`LeverancierID`),
  CONSTRAINT `LevInCpu` FOREIGN KEY (`LeverancierID`) REFERENCES `leverancier` (`LeverancierID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cpu`
--

LOCK TABLES `cpu` WRITE;
/*!40000 ALTER TABLE `cpu` DISABLE KEYS */;
INSERT INTO `cpu` VALUES (1,'i9-13900K','5,2GHz',24,'1700',19,675.95,2,'https://barakacomputer.net/wp-content/uploads/2023/12/13900k.webp'),(2,'i9-14900K','6,0GHz',24,'1700',9,639,2,'https://esp-tech.com/cdn/shop/files/23-057-UNIV-K-N13840_1200x1200.png?v=1698086888'),(3,'i7-14700K','5,6 GHz',20,'1700',6,459,2,'https://tweakers.net/i/IUBEdypgH1XHLOrXCeAZBuYGils=/fit-in/656x/filters:strip_exif()/i/2006164056.png?f=imagenormal');
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
  `fotolink` varchar(2048) DEFAULT NULL,
  PRIMARY KEY (`GPUID`),
  KEY `LevInGpu_idx` (`LeverancierID`),
  CONSTRAINT `LevInGpu` FOREIGN KEY (`LeverancierID`) REFERENCES `leverancier` (`LeverancierID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gpu`
--

LOCK TABLES `gpu` WRITE;
/*!40000 ALTER TABLE `gpu` DISABLE KEYS */;
INSERT INTO `gpu` VALUES (1,'Nvidia GeForce RTX 4080','2535 MHz','16GB','6X',17,1479,6,'https://www.nvidia.com/content/dam/en-zz/Solutions/geforce/news/geforce-rtx-40-series-ultra-efficient-beyond-fast/nvidia-geforce-rtx-4080-ogimage.png'),(2,'Arc A770 CL 16GO','2150 MHz','16GB','6',61,420.99,2,'https://www.asrock.com/Graphics-Card/photo/Intel%20Arc%20A770%20Challenger%2016GB%20OC(M1).png'),(3,'GeForce RTX 4090','2520 MHz','24GB','6X',10,1999,6,'https://images.nvidia.com/aem-dam/Solutions/geforce/ada/news/rtx-40-series-graphics-cards-announcements/geforce-rtx-4090-product-photo-002-850px.png');
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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leverancier`
--

LOCK TABLES `leverancier` WRITE;
/*!40000 ALTER TABLE `leverancier` DISABLE KEYS */;
INSERT INTO `leverancier` VALUES (1,'Corsair'),(2,'Intel'),(3,'GIGABYTE'),(4,'ASUS'),(5,'SAMSUNG'),(6,'NVIDIA'),(7,'Lexar');
/*!40000 ALTER TABLE `leverancier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `MessageID` int NOT NULL AUTO_INCREMENT,
  `UserID` int NOT NULL,
  `IDList` varchar(45) NOT NULL,
  `Naam` varchar(45) NOT NULL,
  PRIMARY KEY (`MessageID`),
  UNIQUE KEY `MessageID_UNIQUE` (`MessageID`),
  KEY `UserID_idx` (`UserID`),
  CONSTRAINT `FKUID` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
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
  `fotolink` varchar(2048) DEFAULT NULL,
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
INSERT INTO `moederbord` VALUES (1,'ROG STRIX B760-F GAMING','1700',5,'6X',0,269,4,'https://dlcdnwebimgs.asus.com/gain/69159885-AADB-444B-B17B-C1809F91A343/w250');
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
  `fotolink` varchar(2048) DEFAULT NULL,
  PRIMARY KEY (`OpslagID`),
  KEY `TypeID_idx` (`TypeID`),
  KEY `LeverancierIDinOpslag_idx` (`LeverancierID`),
  CONSTRAINT `LeverancierIDinOpslag` FOREIGN KEY (`LeverancierID`) REFERENCES `leverancier` (`LeverancierID`),
  CONSTRAINT `TypeID` FOREIGN KEY (`TypeID`) REFERENCES `type` (`TypeID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `opslag`
--

LOCK TABLES `opslag` WRITE;
/*!40000 ALTER TABLE `opslag` DISABLE KEYS */;
INSERT INTO `opslag` VALUES (1,'990 Pro',1,'2TB',10,190,5,'https://images.samsung.com/is/image/samsung/p6pim/be/mz-v9p2t0bw/gallery/be-990pro-nvme-m2-ssd-mz-v9p2t0bw-533691431?$650_519_PNG$'),(2,'NM790',1,'4TB',29,249.45,7,'https://m.media-amazon.com/images/S/aplus-media-library-service-media/e74ea14b-d1b9-454e-969a-813e87f99427.__CR0,0,300,300_PT0_SX300_V1___.png');
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
  `Naam` varchar(400) DEFAULT NULL,
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
INSERT INTO `prebuilt` VALUES (1,1,1,1,1,2,1,1,'Robby\'s Prebuilt');
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
  `fotolink` varchar(2048) DEFAULT NULL,
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
INSERT INTO `psu` VALUES (1,'RM1000e V2 PSU',1000,2,14,144.9,1,'https://assets.corsair.com/image/upload/f_auto/q_auto/v1680204879/products/Power-Supply-Units/base-rme-series-2023-psu-config/Content/RM1000e_ATX3_image.png');
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
  `fotolink` varchar(2048) DEFAULT NULL,
  PRIMARY KEY (`RAMID`),
  KEY `LevInRam_idx` (`LeverancierID`),
  CONSTRAINT `LevInRam` FOREIGN KEY (`LeverancierID`) REFERENCES `leverancier` (`LeverancierID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ram`
--

LOCK TABLES `ram` WRITE;
/*!40000 ALTER TABLE `ram` DISABLE KEYS */;
INSERT INTO `ram` VALUES (1,'Vengeance LPX','4000MHz','16GB',4,28,99.8,1,'https://tweakers.net/i/vumoBZGZf4ogrHCfUSB1NKBrjxI=/i/2003077380.png'),(2,'Vengeance LPX','6800MHz','32GB',5,19,152.9,1,'https://assets.corsair.com/image/upload/c_pad,q_auto,h_1024,w_1024,f_auto/products/Memory/vengeance-ddr5-blk-config/Gallery/VENGEANCE_DDR5_BLK_01_2up.webp'),(3,'Vengeance RGB','7200MHz','32GB',5,13,199.95,1,'https://esp-tech.com/cdn/shop/products/CorsairVengeanceRGBDDR51_e0dea24b-908e-4d7e-9684-1d13703ff0ea_300x300.png?v=1679402671');
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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (18,'admin','a15a80a3d51b2d4fef427803191341bee161377dc63242b305414bdeb079b72b','Admin','AdminStreet',95275.7,1,'9²tÂ»üÅ:N\'\Z÷ÈzxÜmèc°Þ'),(19,'robbyvgaming','7a0c62479b7264d99d400181518afca60cb2d1a874a63caaf8e07c15f58b5750','Robbert Groffi','Halingenstraat 32, Velm 3806',918,0,']TzK×Y2^è¼mÄ	¦õg»Ô²ÖÔY¶'),(20,'victoria','45027579fbb86c7982ca78d43667ef3c7f0c7818410ff8abb10af20a4ea1f745','Victoria Crauwels','Neger is de poepstraat 32',NULL,0,'¸hÞñÙÄµÈ9%kø¥Ëçz&/¶Ã\0äg%N');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-02 21:58:51
