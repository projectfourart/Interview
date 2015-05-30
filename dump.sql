-- MySQL dump 10.13  Distrib 5.5.43, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: interview
-- ------------------------------------------------------
-- Server version	5.5.43-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `interview`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `interview` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `interview`;

--
-- Table structure for table `Question`
--

DROP TABLE IF EXISTS `Question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `body` text,
  `bals` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Question`
--

LOCK TABLES `Question` WRITE;
/*!40000 ALTER TABLE `Question` DISABLE KEYS */;
INSERT INTO `Question` VALUES (1,'Запитання №1','2.5'),(2,'Запитання №2','2.4'),(3,'Запитання №3','2'),(4,'Запитання №4','2.6'),(5,'Запитання №5','2.2');
/*!40000 ALTER TABLE `Question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Sourses`
--

DROP TABLE IF EXISTS `Sourses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Sourses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` text,
  `interviewter` text,
  `users` text,
  `snipet` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Sourses`
--

LOCK TABLES `Sourses` WRITE;
/*!40000 ALTER TABLE `Sourses` DISABLE KEYS */;
INSERT INTO `Sourses` VALUES (1,'Python','4','1:5:','Python-interpritation programing language. This cources by people who want learned Python.'),(2,'HTML/CSS','2','1:5:','HTML/CSS-This course is designed for those who wish to do frontend . Create web pages and sites.'),(3,'PHP','2',NULL,'PHP-server programming language designed for writing backend applications, creating and conducting various inquiries.'),(4,'JavaScript','4',NULL,'JavaScript- scripting programming language for reviving static HTML- documents.');
/*!40000 ALTER TABLE `Sourses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Users` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `name` text,
  `surname` text,
  `email` text,
  `password` text,
  `login` text,
  `visible` text,
  `status` text,
  `type` text,
  `quesition` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES (1,'Олександр','Ковальчук','sasha-kovalchuk7@mail.ru','x7liruk','mjs','true','true','user','1 : 2 : 4 : '),(2,'Віка ','Мартинюк','malecha@mail.ru','1234','vika','true','false','interviewer',NULL),(3,'Оксана','Мамчич','oksana@mail.ru','1234','Oksana','true','false','user',NULL),(4,'Ігор','Кирийчук','igor@gmail.ru','1234','Kirias','true','false','interviewer',NULL),(5,'test','test','test@test.com','1234','test','true','false','user',NULL);
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-05-30  0:19:33
