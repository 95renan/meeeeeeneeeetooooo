CREATE DATABASE  IF NOT EXISTS `meu_netodb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `meu_netodb`;
-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: meu_netodb
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
-- Table structure for table `agendamento`
--

DROP TABLE IF EXISTS `agendamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `agendamento` (
  `idAgendamento` int NOT NULL AUTO_INCREMENT,
  `idIdoso` int DEFAULT NULL,
  `idPrestador` int DEFAULT NULL,
  `dataInicioPedido` datetime DEFAULT NULL,
  `dataInicioServico` date NOT NULL,
  `horaDisponivel` time DEFAULT NULL,
  `servico` varchar(100) DEFAULT NULL,
  `valor` decimal(10,2) DEFAULT NULL,
  `descricao` varchar(500) DEFAULT NULL,
  `aceito_por` int DEFAULT NULL,
  `status` varchar(20) DEFAULT 'pendente',
  PRIMARY KEY (`idAgendamento`),
  UNIQUE KEY `idAgendamento_UNIQUE` (`idAgendamento`),
  KEY `fk_agendamento_idoso` (`idIdoso`),
  KEY `fk_agendamento_prestador` (`idPrestador`),
  CONSTRAINT `fk_agendamento_idoso` FOREIGN KEY (`idIdoso`) REFERENCES `idoso` (`idIdoso`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_agendamento_prestador` FOREIGN KEY (`idPrestador`) REFERENCES `prestador_de_servico` (`idPrestador`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agendamento`
--

LOCK TABLES `agendamento` WRITE;
/*!40000 ALTER TABLE `agendamento` DISABLE KEYS */;
INSERT INTO `agendamento` VALUES (6,1,NULL,NULL,'2025-02-10','08:00:00','Limpeza da casa',50.00,'Limpeza leve e organização.',1,'pendente'),(7,1,NULL,NULL,'2025-02-12','14:00:00','Acompanhamento médico',70.00,'Preciso de ajuda para ir ao postinho.',25,'concluido'),(8,2,NULL,NULL,'2025-02-11','09:00:00','Cozinhar almoço',40.00,'Almoço simples para duas pessoas.',21,'aceito'),(9,2,NULL,NULL,'2025-02-13','16:00:00','Passeio no parque',30.00,'Caminhada leve.',25,'concluido'),(10,3,NULL,NULL,'2025-02-15','10:30:00','Mercado',25.00,'Comprar itens básicos.',25,'concluido'),(11,3,NULL,NULL,'2025-02-20','07:30:00','Limpeza',60.00,'Limpeza geral.',NULL,'pendente'),(14,5,NULL,NULL,'2025-02-19','08:30:00','Passeio',35.00,'Dar uma volta no quarteirão.',NULL,'pendente'),(15,5,NULL,NULL,'2025-02-25','15:00:00','Medicamentos',20.00,'Buscar remédios na farmácia.',NULL,'pendente'),(16,6,NULL,NULL,'2025-02-11','10:00:00','Cozinhar',40.00,'Preparar refeições para o dia.',NULL,'pendente'),(17,7,NULL,NULL,'2025-02-27','09:45:00','Limpeza da casa',50.00,'Limpeza básica.',NULL,'pendente'),(18,7,NULL,NULL,'2025-02-28','15:00:00','Mercado',30.00,'Compra do mês.',NULL,'pendente'),(19,8,NULL,NULL,'2025-02-14','10:00:00','Passeio',28.00,'Caminhada leve.',NULL,'pendente'),(20,8,NULL,NULL,'2025-02-21','12:30:00','Acompanhamento',55.00,'Passar a tarde.',NULL,'pendente'),(21,9,NULL,NULL,'2025-02-17','08:30:00','Cozinhar',42.00,'Café da manhã e almoço.',NULL,'pendente'),(22,9,NULL,NULL,'2025-02-23','14:00:00','Jardinagem',48.00,'Cuidar das plantas.',NULL,'pendente'),(23,10,NULL,NULL,'2025-02-26','09:00:00','Mercado',30.00,'Lista pronta.',NULL,'pendente'),(24,10,NULL,NULL,'2025-02-28','11:00:00','Limpeza',55.00,'Limpeza rápida.',NULL,'pendente'),(25,10,NULL,NULL,'2025-03-01','16:00:00','Passeio',30.00,'Passeio pela praça.',NULL,'pendente'),(26,4,NULL,'2025-11-17 22:49:37','2025-12-12','09:00:00','compras',100.00,'fazer lista de compras',NULL,'pendente'),(30,4,NULL,'2025-11-17 23:52:31','2025-12-12','05:00:00','companhia',252.00,'sxcvxcvxvcbcnb xcvxvx khgkuygkiuy',NULL,'pendente'),(31,4,NULL,'2025-11-18 00:19:06','2025-12-03','05:00:00','jardinagem',100.00,'asdasdadasd',NULL,'pendente'),(32,4,NULL,'2025-11-18 00:31:25','2025-12-03','05:00:00','jardinagem',100.00,'asdasdadasd',NULL,'pendente'),(33,4,NULL,'2025-11-18 09:49:33','2025-12-12','04:05:00','Companhia e Conversa',100.00,'dsfdfgdsfgsdfgsdfg sdfg sdfg sdg',12,'aceito'),(34,4,NULL,'2025-11-18 09:54:32','2025-12-20','10:00:00','jardinagem',200.00,'poda de arvore de médio porte',12,'concluido'),(36,21,NULL,'2025-12-01 22:26:47','2025-12-08','08:00:00','companhia',150.00,'companhia para ir ao médico',NULL,'pendente'),(37,21,NULL,'2025-12-01 23:19:39','2025-12-12','08:00:00','jardinagem',100.00,'cortar a grama da frente de casa',NULL,'pendente'),(38,20,NULL,'2025-12-01 23:21:24','2025-12-20','07:00:00','limpeza',100.00,'Limpar uma casa de 4 comodos + banheiro social',NULL,'pendente');
/*!40000 ALTER TABLE `agendamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `idoso`
--

DROP TABLE IF EXISTS `idoso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `idoso` (
  `idIdoso` int NOT NULL AUTO_INCREMENT,
  `cpf` varchar(15) NOT NULL,
  `login` varchar(50) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `senha` varchar(100) NOT NULL,
  `telefone` varchar(15) DEFAULT NULL,
  `parentesco` varchar(45) DEFAULT NULL,
  `nascimento` date DEFAULT NULL,
  `endCEP` varchar(9) DEFAULT NULL,
  `endRUA` varchar(100) DEFAULT NULL,
  `endNUMERO` int DEFAULT NULL,
  `endBAIRRO` varchar(100) DEFAULT NULL,
  `endCIDADE` varchar(100) DEFAULT NULL,
  `endUF` char(2) DEFAULT NULL,
  `fotoPERFIL` varchar(255) DEFAULT NULL,
  `perfil` varchar(20) DEFAULT NULL,
  `criadoEm` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idIdoso`),
  UNIQUE KEY `login` (`login`),
  UNIQUE KEY `idIdoso_UNIQUE` (`idIdoso`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `idoso`
--

LOCK TABLES `idoso` WRITE;
/*!40000 ALTER TABLE `idoso` DISABLE KEYS */;
INSERT INTO `idoso` VALUES (1,'0','mariasilva','Maria da Silva','maria@gmail.com','123456','(65)99999-8888',NULL,'1955-10-22','78700-000','Rua das Flores',123,'Centro','Rondonópolis','MT','uploads/maria.jpg',NULL,'2025-11-08 00:58:29'),(2,'12345678912','teste45','teste45','teste45@gmail.com','teste45123','66996239329',NULL,'1995-04-02','78750255','rua das perdizes',2003,'centro','itu','sp',NULL,NULL,'2025-11-08 01:16:18'),(3,'12345678940','teste5','teste5','teste5@gmail.com','teste5123','9969236932',NULL,'1995-05-05','78750500','rua seriema',2011,'centro','itu','SP',NULL,NULL,'2025-11-08 23:19:07'),(4,'05172623124','adm','admin','rgtecsis@gmail.com','adm123','66996239329',NULL,'1995-07-03','78750255','av das perdizes',2011,'Pq Universitário','Rondonópolis','MT',NULL,NULL,'2025-11-13 20:33:10'),(5,'05172623124','teste6','teste6','teste6@gmail.com','teste6123','66996233333',NULL,'1985-11-20','78750000','rua das codornas',2154,'vila olinda','rondonopolis','mt',NULL,NULL,'2025-11-13 21:06:45'),(6,'11111111111','maria01','Maria Aparecida','maria01@email.com','1234','65999990001',NULL,'1950-03-12','78700001','Rua das Flores',120,'Centro','Rondonópolis','MT',NULL,NULL,'2025-11-17 22:46:42'),(7,'22222222222','joao02','João Ferreira','joao02@email.com','1234','65999990002',NULL,'1945-07-09','78700002','Av. Paulista',450,'Centro','Rondonópolis','MT',NULL,NULL,'2025-11-17 22:46:42'),(8,'33333333333','ana03','Ana Souza','ana03@email.com','1234','65999990003',NULL,'1952-10-22','78700003','Rua Sol Nascente',90,'Vila Aurora','Rondonópolis','MT',NULL,NULL,'2025-11-17 22:46:42'),(9,'44444444444','jose04','José Carlos','jose04@email.com','1234','65999990004',NULL,'1955-01-15','78700004','Rua das Palmeiras',321,'Sagrada Família','Rondonópolis','MT',NULL,NULL,'2025-11-17 22:46:42'),(10,'55555555555','cecilia05','Cecília Mendes','cecilia05@email.com','1234','65999990005',NULL,'1948-04-18','78700005','Rua das Acácias',12,'Jardim Atlântico','Rondonópolis','MT',NULL,NULL,'2025-11-17 22:46:42'),(11,'66666666666','marcos06','Marcos Silva','marcos06@email.com','1234','65999990006',NULL,'1951-11-30','78700006','Av. Castelo Branco',980,'Centro','Rondonópolis','MT',NULL,NULL,'2025-11-17 22:46:42'),(12,'77777777777','helena07','Helena Castro','helena07@email.com','1234','65999990007',NULL,'1958-09-02','78700007','Rua Beija Flor',64,'Cidade Alta','Rondonópolis','MT',NULL,NULL,'2025-11-17 22:46:42'),(13,'88888888888','carlos08','Carlos Eduardo','carlos08@email.com','1234','65999990008',NULL,'1954-02-27','78700008','Rua Ipê Roxo',70,'Jardim Iguaçu','Rondonópolis','MT',NULL,NULL,'2025-11-17 22:46:42'),(14,'99999999999','antonia09','Antônia Silva','antonia09@email.com','1234','65999990009',NULL,'1949-12-05','78700009','Rua Do Cedro',88,'Santo Antônio','Rondonópolis','MT',NULL,NULL,'2025-11-17 22:46:42'),(15,'10101010101','paulo10','Paulo Gomes','paulo10@email.com','1234','65999990010',NULL,'1956-06-21','78700010','Av. Bandeirantes',144,'Centro','Rondonópolis','MT',NULL,NULL,'2025-11-17 22:46:42'),(16,'00000000000','admin','Administrador do Sistema','admin@admin.com','123','999999999',NULL,'2000-01-01','00000-000','Centro',100,'Centro','Rondonópolis','MT',NULL,'admin','2025-11-26 21:03:38'),(17,'12345678994','maria123','Maria Aparecida','maria@email.com','maria123','66932369623',NULL,'1960-01-04','78750256','rua das ostras',200,'centro','Rondonopolis','MT',NULL,NULL,'2025-11-27 09:44:43'),(18,'051747892923','rosana','rosana silva','rosana@gmail.com','123','9829278191',NULL,'1978-08-05','95959595','asdasfagags',111,'asasdaf','asdasf','as',NULL,NULL,'2025-11-27 11:20:22'),(19,'1294949929292','andreia','andreia cruz','andreia@GMAIL.COM','123','56959595959',NULL,'1995-12-08','77593251','asffgdfg',154,'dfgdfg','gggdfgdfg','dd',NULL,NULL,'2025-11-27 11:27:16'),(20,'649197863','teste9','teste9','teste9@gmail.com','123','62061651','proprio','2001-04-14','78750202','asfaagfagag',222,'asdasfa','asdasdasgf','aa',NULL,NULL,'2025-11-27 11:32:54'),(21,'12345678942','antonia','Antonia Maria','antonia@gmail.com','123','99669656932','proprio','1965-04-03','78750000','rua 1',250,'Pedra 90','Rondonópolis','MT',NULL,NULL,'2025-12-01 22:24:56');
/*!40000 ALTER TABLE `idoso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prestador_de_servico`
--

DROP TABLE IF EXISTS `prestador_de_servico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prestador_de_servico` (
  `idPrestador` int NOT NULL AUTO_INCREMENT,
  `cpf` varchar(15) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `login` varchar(50) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `senha` varchar(100) NOT NULL,
  `telefone` varchar(15) DEFAULT NULL,
  `nascimento` date DEFAULT NULL,
  `endCEP` varchar(9) DEFAULT NULL,
  `endRUA` varchar(100) DEFAULT NULL,
  `endNUMERO` int DEFAULT NULL,
  `endBAIRRO` varchar(100) DEFAULT NULL,
  `endCIDADE` varchar(100) DEFAULT NULL,
  `endUF` char(2) DEFAULT NULL,
  `fotoPERFIL` varchar(200) DEFAULT NULL,
  `comprovRes` varchar(200) DEFAULT NULL,
  `antecedentes` varchar(200) DEFAULT NULL,
  `serv1` varchar(45) DEFAULT NULL,
  `serv2` varchar(45) DEFAULT NULL,
  `serv3` varchar(45) DEFAULT NULL,
  `perfil` varchar(50) DEFAULT NULL,
  `criadoEm` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idPrestador`),
  UNIQUE KEY `login` (`login`),
  UNIQUE KEY `idPrestador_UNIQUE` (`idPrestador`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prestador_de_servico`
--

LOCK TABLES `prestador_de_servico` WRITE;
/*!40000 ALTER TABLE `prestador_de_servico` DISABLE KEYS */;
INSERT INTO `prestador_de_servico` VALUES (1,'12345678910','teste3','teste3','teste3@gmail.com','teste3123','96296236962','1995-02-01','78750255','av das perdizes',2011,'centro','itu','SP',NULL,'1perfil.jpg','1perfil.jpg','companhia','limpeza','compras',NULL,'2025-11-11 21:20:59'),(2,'11111111000','Lucas Martins','lucas01','lucas01@email.com','1234','65995550001','1998-03-12','78705001','Rua Projetada 1',45,'Centro','Rondonópolis','MT',NULL,'','','Limpeza','Acompanhamento','Cozinhar',NULL,'2025-11-17 22:47:19'),(3,'22222222000','Fernanda Lima','fernanda02','fernanda02@email.com','1234','65995550002','1995-11-02','78705002','Rua Paraná',120,'Vila Operária','Rondonópolis','MT',NULL,'','','Passeio','Acompanhamento','Mercado',NULL,'2025-11-17 22:47:19'),(4,'33333333000','Matheus Oliveira','matheus03','matheus03@email.com','1234','65995550003','1999-07-28','78705003','Rua Amazonas',98,'Centro','Rondonópolis','MT',NULL,'','','Limpeza','Cozinhar','Jardinagem',NULL,'2025-11-17 22:47:19'),(5,'44444444000','Juliana Santos','juliana04','juliana04@email.com','1234','65995550004','1997-05-14','78705004','Rua Goiânia',210,'Centro','Rondonópolis','MT',NULL,'','','Passeio','Medicamentos','Acompanhamento',NULL,'2025-11-17 22:47:19'),(6,'55555555000','Rafael Souza','rafael05','rafael05@email.com','1234','65995550005','1996-10-19','78705005','Rua Porto Alegre',77,'Jardim Atlântico','Rondonópolis','MT',NULL,'','','Mercado','Limpeza','Acompanhamento',NULL,'2025-11-17 22:47:19'),(7,'66666666000','Camila Nunes','camila06','camila06@email.com','1234','65995550006','1994-02-01','78705006','Rua Curitiba',340,'Centro','Rondonópolis','MT',NULL,'','','Cozinhar','Passeio','Limpeza',NULL,'2025-11-17 22:47:19'),(8,'77777777000','Pedro Henrique','pedro07','pedro07@email.com','1234','65995550007','1993-06-06','78705007','Rua Pernambuco',56,'Sagrada Família','Rondonópolis','MT',NULL,'','','Jardinagem','Mercado','Acompanhamento',NULL,'2025-11-17 22:47:19'),(9,'88888888000','Bruna Ferreira','bruna08','bruna08@email.com','1234','65995550008','1998-08-30','78705008','Rua Sergipe',12,'Centro','Rondonópolis','MT',NULL,'','','Limpeza','Passeio','Acompanhamento',NULL,'2025-11-17 22:47:19'),(10,'99999999000','Tiago Ribeiro','tiago09','tiago09@email.com','1234','65995550009','2000-01-15','78705009','Rua Ceará',65,'Jardim Iguaçu','Rondonópolis','MT',NULL,'','','Mercado','Cozinhar','Limpeza',NULL,'2025-11-17 22:47:19'),(11,'10101010000','Larissa Rocha','larissa10','larissa10@email.com','1234','65995550010','1992-09-09','78705010','Rua Bahia',200,'Centro','Rondonópolis','MT',NULL,'','','Acompanhamento','Passeio','Cozinhar',NULL,'2025-11-17 22:47:19'),(12,'12345678910','admin','adm','rgtecsis@gmail.com','adm123','66996239329','1995-07-03','78750255','Av das Perdizes',2011,'Parque Universitário','Rondonópolis','MT',NULL,'profile.jpg','profile.jpg','companhia','compras','tecnologia',NULL,'2025-11-20 22:50:46'),(15,'00000000000','Administrador do Sistema','admin','rgsiqueira95@gmail.com','123','999999999','2000-01-01','00000-000','Centro',100,'Centro','Rondonópolis','MT',NULL,'','','0','0','0','admin','2025-11-26 21:15:14'),(16,'05147856235','Pedro Silva','joao123','joao@gmail.com','joao123','62649341919852','1989-04-02','78750425','Rua Principal',450,'Sao João','Jaciara','MT',NULL,'aula 03 - ihc.pdf','aula 03 - ihc.pdf','limpeza','compras','limpeza',NULL,'2025-11-27 09:47:44'),(17,'05212365478','Sergio Souza','sergio123','sergio@gmail.com','sergio123','6663695623','2001-12-12','78750500','Rua das Codornas',1254,'centro','Rondonopolis','MT',NULL,'profile.jpg','profile.jpg','companhia','limpeza','compras',NULL,'2025-11-27 09:53:16'),(18,'12345678945','mario','mario123','mario@gmail.com','mario123','66123456789','2001-01-01','78750555','rua 1',123,'CENTRO','IYU','SP',NULL,'profile.jpg','profile.jpg','Companhia','Limpeza','Compras',NULL,'2025-11-27 10:21:35'),(19,'1213456789','rogerio','rogerio','rogerio@gmail.com','rogerio123','5629298298292','2002-02-01','78750588','asdasd',1123,'asdasd','asdasd','aa',NULL,'profile.jpg','profile.jpg','Companhia','Limpeza','Compras',NULL,'2025-11-27 10:31:33'),(20,'321651651','teste6','teste6','asdasd@email.com','123','6516516','2002-01-01','99298719','asfasfasf',1115,'asfasf','asfasfasf','as',NULL,'profile.jpg','profile.jpg','Tecnologia','Compras','Companhia',NULL,'2025-11-27 10:35:41'),(21,'555555555','joana','joana','joana@gmail.com','123','656516516165','2003-01-01','784962659','asdasdasd',3,'asdasd','adasdada','aa',NULL,'profile.jpg','profile.jpg','Companhia','Limpeza','Compras',NULL,'2025-11-27 10:47:36'),(22,'19919191919','teste7','teste7','teste7@gmail.com','123','1191959519199','2001-01-01','98978515','asdasdasd',15151,'dasdadad','dsada','aa',NULL,'profile.jpg','profile.jpg','Limpeza','Companhia','Companhia',NULL,'2025-11-27 10:50:02'),(23,'96951951951','teste8','teste8','teste8@gmail.com','123','95951951951','2000-02-02','99899569','asdasdasdad',1515,'asdasdads','asasd','dd',NULL,'profile.jpg','profile.jpg','Companhia','Limpeza','Compras',NULL,'2025-11-27 11:18:26'),(25,'12345678996','José Pestana','ze','ze@gmail.com','123','66966236963','1999-12-12','78750000','Rua 3',120,'CENTRO','Rondonopolis','MT',NULL,'profile.jpg','profile.jpg','Companhia','Limpeza','Compras',NULL,'2025-12-01 22:31:42');
/*!40000 ALTER TABLE `prestador_de_servico` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-01 23:29:50
