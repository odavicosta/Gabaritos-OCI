CREATE DATABASE  IF NOT EXISTS `oci` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `oci`;
-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: oci
-- ------------------------------------------------------
-- Server version	8.0.42

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
-- Table structure for table `alunos`
--

DROP TABLE IF EXISTS `alunos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alunos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(60) DEFAULT NULL,
  `cpf` char(11) DEFAULT NULL,
  `id_escola` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_escola` (`id_escola`),
  CONSTRAINT `alunos_ibfk_1` FOREIGN KEY (`id_escola`) REFERENCES `escolas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alunos`
--

LOCK TABLES `alunos` WRITE;
/*!40000 ALTER TABLE `alunos` DISABLE KEYS */;
/*!40000 ALTER TABLE `alunos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `escolas`
--

DROP TABLE IF EXISTS `escolas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `escolas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) DEFAULT NULL,
  `estado` char(2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `escolas`
--

LOCK TABLES `escolas` WRITE;
/*!40000 ALTER TABLE `escolas` DISABLE KEYS */;
/*!40000 ALTER TABLE `escolas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gabaritos`
--

DROP TABLE IF EXISTS `gabaritos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gabaritos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome_arquivo` varchar(100) DEFAULT NULL,
  `leitura` varchar(50) DEFAULT NULL,
  `nota` decimal(4,2) DEFAULT NULL,
  `erro` tinyint unsigned DEFAULT NULL,
  `acertos` int DEFAULT NULL,
  `id_prova` int DEFAULT NULL,
  `id_alunos` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_prova` (`id_prova`),
  KEY `id_alunos` (`id_alunos`),
  CONSTRAINT `gabaritos_ibfk_1` FOREIGN KEY (`id_prova`) REFERENCES `provas` (`id`),
  CONSTRAINT `gabaritos_ibfk_2` FOREIGN KEY (`id_alunos`) REFERENCES `alunos` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gabaritos`
--

LOCK TABLES `gabaritos` WRITE;
/*!40000 ALTER TABLE `gabaritos` DISABLE KEYS */;
/*!40000 ALTER TABLE `gabaritos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `provas`
--

DROP TABLE IF EXISTS `provas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `provas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `modalidade` varchar(30) NOT NULL,
  `fase` tinyint unsigned NOT NULL,
  `data_prova` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `provas`
--

LOCK TABLES `provas` WRITE;
/*!40000 ALTER TABLE `provas` DISABLE KEYS */;
/*!40000 ALTER TABLE `provas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questoes`
--

DROP TABLE IF EXISTS `questoes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questoes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `numero` tinyint unsigned NOT NULL,
  `resposta` char(1) NOT NULL,
  `id_prova` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_prova` (`id_prova`,`numero`),
  CONSTRAINT `questoes_ibfk_1` FOREIGN KEY (`id_prova`) REFERENCES `provas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questoes`
--

LOCK TABLES `questoes` WRITE;
/*!40000 ALTER TABLE `questoes` DISABLE KEYS */;
/*!40000 ALTER TABLE `questoes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `respostas`
--

DROP TABLE IF EXISTS `respostas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `respostas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `resposta` char(1) DEFAULT NULL,
  `corretude` tinyint(1) DEFAULT NULL,
  `id_gabarito` int DEFAULT NULL,
  `id_questao` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_gabarito` (`id_gabarito`,`id_questao`),
  KEY `id_questao` (`id_questao`),
  CONSTRAINT `respostas_ibfk_1` FOREIGN KEY (`id_gabarito`) REFERENCES `gabaritos` (`id`),
  CONSTRAINT `respostas_ibfk_2` FOREIGN KEY (`id_questao`) REFERENCES `questoes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `respostas`
--

LOCK TABLES `respostas` WRITE;
/*!40000 ALTER TABLE `respostas` DISABLE KEYS */;
/*!40000 ALTER TABLE `respostas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-14 14:55:53
