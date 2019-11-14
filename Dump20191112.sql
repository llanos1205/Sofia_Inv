-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	8.0.17

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
-- Dumping data for table `area`
--

LOCK TABLES `area` WRITE;
/*!40000 ALTER TABLE `area` DISABLE KEYS */;
INSERT INTO `area` VALUES (1,'Soporte Tecnico','',1,1),(2,'IT','',1,1),(3,'Desarollo Interno','',1,1),(4,'Caja chica','',2,1),(5,'Caja Grande','',2,1),(6,'Auditoria Contable','',2,1),(7,'Procesos legales','',3,1),(8,'Asesoria Legal','',3,1);
/*!40000 ALTER TABLE `area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `asociacion`
--

LOCK TABLES `asociacion` WRITE;
/*!40000 ALTER TABLE `asociacion` DISABLE KEYS */;
INSERT INTO `asociacion` VALUES (1,'2019-10-31',NULL,'asdasd',1,5,1,1);
/*!40000 ALTER TABLE `asociacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `atributo`
--

LOCK TABLES `atributo` WRITE;
/*!40000 ALTER TABLE `atributo` DISABLE KEYS */;
INSERT INTO `atributo` VALUES (1,'Puerto',1),(2,'El Toner',1);
/*!40000 ALTER TABLE `atributo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auditoria`
--

LOCK TABLES `auditoria` WRITE;
/*!40000 ALTER TABLE `auditoria` DISABLE KEYS */;
/*!40000 ALTER TABLE `auditoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `cargo`
--

LOCK TABLES `cargo` WRITE;
/*!40000 ALTER TABLE `cargo` DISABLE KEYS */;
INSERT INTO `cargo` VALUES (1,'pasante de sistemas','pasante del area de sistemas',1),(2,'Presidente','gefe de todo',1),(3,'gerente de x','asdjalkdj',1);
/*!40000 ALTER TABLE `cargo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `cuenta`
--

LOCK TABLES `cuenta` WRITE;
/*!40000 ALTER TABLE `cuenta` DISABLE KEYS */;
INSERT INTO `cuenta` VALUES (1,'practicantegst','123',1),(2,'gerneciaprincpal','da6s5d4as6d5',1);
/*!40000 ALTER TABLE `cuenta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `departamento`
--

LOCK TABLES `departamento` WRITE;
/*!40000 ALTER TABLE `departamento` DISABLE KEYS */;
INSERT INTO `departamento` VALUES (1,'Departamento de Sistemas','',1),(2,'Departamento de Contabilidad','',1),(3,'Departamento Legal','',1);
/*!40000 ALTER TABLE `departamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `empresa`
--

LOCK TABLES `empresa` WRITE;
/*!40000 ALTER TABLE `empresa` DISABLE KEYS */;
INSERT INTO `empresa` VALUES (1,'Sofia LTDA.','emrpesa principal',1),(2,'Indatta','empresa de desarollo',1),(3,'Despachos','sub empresa encargad de envios',1);
/*!40000 ALTER TABLE `empresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `equipo`
--

LOCK TABLES `equipo` WRITE;
/*!40000 ALTER TABLE `equipo` DISABLE KEYS */;
INSERT INTO `equipo` VALUES (1,'dell','inpirion 15 7550','13246579','31654987','127.0.0.0','ninguna',1),(3,'samsung','ration 2080v2','987465','964132','12.3.3.3','ninguna',1),(4,'asdasd','qrqwe','34534','54651','132164','ninguna',1),(5,'epson','aptr4511','a6s5d1a3s','968as4d1a6s','155.65.66.98','ññññ',1),(6,'sony','pavliaosd541','a65sd4a96','as16532asd','159.65.65.3','ass',1);
/*!40000 ALTER TABLE `equipo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `gerencia`
--

LOCK TABLES `gerencia` WRITE;
/*!40000 ALTER TABLE `gerencia` DISABLE KEYS */;
INSERT INTO `gerencia` VALUES (1,'GST','gerencia ssitemas',1),(2,'GADM','gerencia administrativa',1),(3,'GL','gerencia legal',1);
/*!40000 ALTER TABLE `gerencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `impresora`
--

LOCK TABLES `impresora` WRITE;
/*!40000 ALTER TABLE `impresora` DISABLE KEYS */;
INSERT INTO `impresora` VALUES (5,'laserdisc','a84sd9');
/*!40000 ALTER TABLE `impresora` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `licencia`
--

LOCK TABLES `licencia` WRITE;
/*!40000 ALTER TABLE `licencia` DISABLE KEYS */;
INSERT INTO `licencia` VALUES (1,'Ofice 653',1),(2,'Photoshop',1);
/*!40000 ALTER TABLE `licencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `ordenador`
--

LOCK TABLES `ordenador` WRITE;
/*!40000 ALTER TABLE `ordenador` DISABLE KEYS */;
INSERT INTO `ordenador` VALUES (1,'laptop','5as68d4a+6sd','s65df41sd65f1','intel core i7','16bg','2tb','ssd',3),(4,'laptop','1sad','6sd4a96d8','6asd4a6','17gb','1tb','hdd',1);
/*!40000 ALTER TABLE `ordenador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `ordenador_has_licencia`
--

LOCK TABLES `ordenador_has_licencia` WRITE;
/*!40000 ALTER TABLE `ordenador_has_licencia` DISABLE KEYS */;
INSERT INTO `ordenador_has_licencia` VALUES (1,'asd-asd-asd-asd','2017',1,1,'2017-02-27'),(2,'as65d4a65d46a4d','version nueva',2,1,'2018-11-10'),(3,'asd7-987-987-78','spy 15',2,4,'1998-08-15'),(4,'asd7-987-987-78','spy 15',2,1,'2011-11-15');
/*!40000 ALTER TABLE `ordenador_has_licencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `os`
--

LOCK TABLES `os` WRITE;
/*!40000 ALTER TABLE `os` DISABLE KEYS */;
INSERT INTO `os` VALUES (1,'windows 10','service pack 10','x84',1),(2,'Ubuntu','lts 19','x64',1),(3,'macos','v12','x64',1);
/*!40000 ALTER TABLE `os` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `otro_dispositivo`
--

LOCK TABLES `otro_dispositivo` WRITE;
/*!40000 ALTER TABLE `otro_dispositivo` DISABLE KEYS */;
INSERT INTO `otro_dispositivo` VALUES (6,'televisor',NULL);
/*!40000 ALTER TABLE `otro_dispositivo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `otro_dispositivo_has_atributo`
--

LOCK TABLES `otro_dispositivo_has_atributo` WRITE;
/*!40000 ALTER TABLE `otro_dispositivo_has_atributo` DISABLE KEYS */;
INSERT INTO `otro_dispositivo_has_atributo` VALUES (1,6,1,'tiene 20 puertos');
/*!40000 ALTER TABLE `otro_dispositivo_has_atributo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `permiso`
--

LOCK TABLES `permiso` WRITE;
/*!40000 ALTER TABLE `permiso` DISABLE KEYS */;
INSERT INTO `permiso` VALUES (1,'Full',1),(2,'Solo Usb',1),(3,'Solo Archivos compartidos',1),(4,'Solo internet',1);
/*!40000 ALTER TABLE `permiso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `regional`
--

LOCK TABLES `regional` WRITE;
/*!40000 ALTER TABLE `regional` DISABLE KEYS */;
INSERT INTO `regional` VALUES (1,'Sana Cruz de la Sierra',1),(2,'Tarija',1),(3,'Argentina',1);
/*!40000 ALTER TABLE `regional` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `tablet`
--

LOCK TABLES `tablet` WRITE;
/*!40000 ALTER TABLE `tablet` DISABLE KEYS */;
INSERT INTO `tablet` VALUES (3,'16 gb','2 gbv3','d65ad16ad841','entel','13x16','cualcore i9','17 pulgadas');
/*!40000 ALTER TABLE `tablet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `ubicacion`
--

LOCK TABLES `ubicacion` WRITE;
/*!40000 ALTER TABLE `ubicacion` DISABLE KEYS */;
INSERT INTO `ubicacion` VALUES (1,'Cuarto Anillo Roca y Coronado','Edificio administrativo',1),(2,'Cuarto Anillo Av. Paragua','Edificio Parque Industrial',1);
/*!40000 ALTER TABLE `ubicacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `usuario_ad`
--

LOCK TABLES `usuario_ad` WRITE;
/*!40000 ALTER TABLE `usuario_ad` DISABLE KEYS */;
INSERT INTO `usuario_ad` VALUES (1,'Diego Alejandro','Llanos Gareca','8257165',1,1,2,2,2,2,2,1),(2,'ana patricia','mendoza montealaegre','1846302',3,3,2,1,2,NULL,3,1),(3,'rene alfredo','ovando barba','849562',7,3,1,3,2,NULL,2,1),(4,'sfsdfsdf','asdfdghrfg','6541651',4,2,3,2,2,1,2,1),(5,'alejandro','montero melgar','1324698',3,1,1,1,2,1,1,1);
/*!40000 ALTER TABLE `usuario_ad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `usuario_ad_has_permiso`
--

LOCK TABLES `usuario_ad_has_permiso` WRITE;
/*!40000 ALTER TABLE `usuario_ad_has_permiso` DISABLE KEYS */;
INSERT INTO `usuario_ad_has_permiso` VALUES (1,1),(3,2),(5,2),(3,3),(2,4),(4,4);
/*!40000 ALTER TABLE `usuario_ad_has_permiso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `usuario_correo`
--

LOCK TABLES `usuario_correo` WRITE;
/*!40000 ALTER TABLE `usuario_correo` DISABLE KEYS */;
INSERT INTO `usuario_correo` VALUES (1,'dsfjdfgerfgewfw@gmail.com','1321321','ACESS',1,1),(2,'adasdasd@lsjkdflsd.vm','a2sd4as6d5','ACCESS',3,1);
/*!40000 ALTER TABLE `usuario_correo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-12 19:54:26
