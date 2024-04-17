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
INSERT INTO `behuizing` VALUES (1,'Obsidian 1000D',4,'100x100x40',-4,149.99,1,'https://tweakers.net/i/T_ExRH7dyARulcwakGjwRJsqHPs=/fit-in/656x/filters:strip_exif()/i/2001967595.png?f=imagenormal');
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
INSERT INTO `cpu` VALUES (1,'i9-13900K','5,2GHz',24,'1700',-2,675.95,2,'https://www.alternate.be/p/600x600/7/7/Intel__Core_i9_13900K__3_0_GHz__5_8_GHz_Turbo_Boost__socket_1700_processor@@1865277.jpg'),(2,'i9-14900K','6,0GHz',24,'1700',9,639,2,'https://azerty.nl/media/catalog/product/0/o/0okyo5.5283778_15fb3ae0fc9358f026631170abc11d0a-43235351_1.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=700&width=700&canvas=700:700'),(3,'i7-14700K','5,6 GHz',20,'1700',0,459,2,'https://www.alternate.be/p/600x600/5/7/Intel__Core_i7_14700K__3_4_GHz__5_6_GHz_Turbo_Boost__socket_1700_processor@@100009775.jpg');
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gpu`
--

LOCK TABLES `gpu` WRITE;
/*!40000 ALTER TABLE `gpu` DISABLE KEYS */;
INSERT INTO `gpu` VALUES (1,'Nvidia GeForce RTX 4080','2535 MHz','16GB','6X',-5,1479,3,'https://m.media-amazon.com/images/I/71iaKN6nNrL.jpg'),(2,'Arc A770 CL 16GO','2150 MHz','16GB','6',67,420.99,2,'https://i5.walmartimages.com/asr/84688cb7-74a7-40bf-bc4f-cdbd24cac60d.257b6e8a5ce7d167aa328396039a02d8.jpeg?odnHeight=768&odnWidth=768&odnBg=FFFFFF');
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
INSERT INTO `moederbord` VALUES (1,'ROG STRIX B760-F GAMING','1700',5,'6X',2,269,4,'https://media.ldlc.com/r1600/ld/products/00/06/00/31/LD0006003137.jpg');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `opslag`
--

LOCK TABLES `opslag` WRITE;
/*!40000 ALTER TABLE `opslag` DISABLE KEYS */;
INSERT INTO `opslag` VALUES (1,'990 Pro',1,'2TB',-2,190,5,'https://images.samsung.com/is/image/samsung/p6pim/be/mz-v9p2t0bw/gallery/be-990pro-nvme-m2-ssd-mz-v9p2t0bw-533691431?$650_519_PNG$');
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
  `Name` varchar(400) DEFAULT NULL,
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
INSERT INTO `psu` VALUES (1,'RM1000e V2 PSU',1000,2,-2,144.9,1,'https://cdn.webshopapp.com/shops/330902/files/447022154/1500x1500x2/corsair-corsair-rm1000e-v2-psu-pc-voeding.jpg');
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ram`
--

LOCK TABLES `ram` WRITE;
/*!40000 ALTER TABLE `ram` DISABLE KEYS */;
INSERT INTO `ram` VALUES (1,'Vengeance','4000MHz','16GB',4,3,99.8,1,'https://www.bytesatwork.be/media/catalog/product/cache/926ec4834e42ffe6a495cf71ebadeb46/1/2/1299153_3_6.jpg'),(2,'Vengeance','6800MHz','32GB',5,1,152.9,1,'https://assets.corsair.com/image/upload/c_pad,q_auto,h_1024,w_1024,f_auto/products/Memory/vengeance-ddr5-blk-config/Gallery/VENGEANCE_DDR5_BLK_01_2up.webp');
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
INSERT INTO `user` VALUES (18,'admin','a15a80a3d51b2d4fef427803191341bee161377dc63242b305414bdeb079b72b','Admin','AdminStreet',48352.2,1,'9²tÂ»üÅ:N\'\Z÷ÈzxÜmèc°Þ'),(19,'robbyvgaming','7a0c62479b7264d99d400181518afca60cb2d1a874a63caaf8e07c15f58b5750','Robbert Groffi','Halingenstraat 32, Velm 3806',918,0,']TzK×Y2^è¼mÄ	¦õg»Ô²ÖÔY¶'),(20,'victoria','45027579fbb86c7982ca78d43667ef3c7f0c7818410ff8abb10af20a4ea1f745','Victoria Crauwels','Neger is de poepstraat 32',NULL,0,'¸hÞñÙÄµÈ9%kø¥Ëçz&/¶Ã\0äg%N');
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

-- Dump completed on 2024-04-17 21:53:44
