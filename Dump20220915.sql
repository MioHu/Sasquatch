CREATE DATABASE  IF NOT EXISTS `sasquatch` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `sasquatch`;
-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: sasquatch
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `sightings`
--

DROP TABLE IF EXISTS `sightings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sightings` (
  `id` int NOT NULL AUTO_INCREMENT,
  `location` varchar(45) DEFAULT NULL,
  `happen` text,
  `date` date DEFAULT NULL,
  `num` int DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` int NOT NULL,
  `user_fname` varchar(45) DEFAULT NULL,
  `user_lname` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`,`user_id`),
  KEY `fk_sightings_users_idx` (`user_id`),
  CONSTRAINT `fk_sightings_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sightings`
--

LOCK TABLES `sightings` WRITE;
/*!40000 ALTER TABLE `sightings` DISABLE KEYS */;
INSERT INTO `sightings` VALUES (1,'Bluff Creek','happen1','1967-10-20',1,'2022-08-17 09:49:03','2022-08-17 09:49:03',1,'Jingwen','Hu'),(2,'Provo Canyon','happen2','2012-10-18',3,'2022-08-17 09:49:03','2022-08-17 09:49:03',2,'Mercy','Hu'),(5,'Blue Mountains','happened something','1994-08-19',2,'2022-08-17 11:03:58','2022-08-17 11:03:58',1,'Jingwen','Hu'),(6,'Allegheny Forest','what happened??? IDK lol','2007-05-06',133,'2022-08-17 11:04:53','2022-08-17 11:04:53',3,'Tracer','Hu'),(7,'Mercer Court D','I\'m so restless, why the AWS cannot work???','2022-08-18',133,'2022-08-18 10:14:53','2022-08-18 10:14:53',4,'Ana','Hu');
/*!40000 ALTER TABLE `sightings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `skeptics`
--

DROP TABLE IF EXISTS `skeptics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `skeptics` (
  `user_id` int NOT NULL,
  `sighting_id` int NOT NULL,
  PRIMARY KEY (`user_id`,`sighting_id`),
  KEY `fk_users_has_sightings_sightings1_idx` (`sighting_id`),
  KEY `fk_users_has_sightings_users1_idx` (`user_id`),
  CONSTRAINT `fk_users_has_sightings_sightings1` FOREIGN KEY (`sighting_id`) REFERENCES `sightings` (`id`),
  CONSTRAINT `fk_users_has_sightings_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skeptics`
--

LOCK TABLES `skeptics` WRITE;
/*!40000 ALTER TABLE `skeptics` DISABLE KEYS */;
INSERT INTO `skeptics` VALUES (1,1),(2,1),(3,1),(3,5),(1,6),(3,6);
/*!40000 ALTER TABLE `skeptics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `pw` char(60) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Jingwen','Hu','jwhu@uw.edu','$2b$12$Fw6CPS4iA33USIUatY30lO9ApLDp/d4SCTi6/RS5FRTFIaQjU1Sly','2022-08-17 09:21:15','2022-08-17 09:21:15'),(2,'Mercy','Hu','mercy@gmail.com','$2b$12$qRPYZP.jDpjMtbZj7go95.yLuODByP4Eq2Qu.NjdBhrnRSx54Yn1.','2022-08-17 09:22:36','2022-08-17 09:22:36'),(3,'Tracer','Hu','tracer@gmail.com','$2b$12$O/B5.AngEqsX0OziI3hoIOaKDQFbsqG.qY75plFjytACLK4Ex4h7e','2022-08-17 09:23:06','2022-08-17 09:23:06'),(4,'Ana','Hu','ana@gmail.com','$2b$12$4h5J3tFQz208qWXonhhYb.eTm6vt25ZBep9Y1BAuAkyIVZm1txDCq','2022-08-18 10:13:27','2022-08-18 10:13:27');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-15 12:36:56
