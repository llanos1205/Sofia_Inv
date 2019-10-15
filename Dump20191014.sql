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
INSERT INTO `area` VALUES (1,'Soporte','Area destiana al soporte tecnico',1,0),(2,'Desarollo','Area destiana al desarollo de aplicaciones moviles',1,0),(3,'Caja chica','Area pequeña contable',2,1),(4,'Caja Grande','Area donde converjen todos los registros contables',2,1),(5,'Archivos','Area de almacenamiento de documentacion contable',2,1),(6,'Front Office','oficina frontal',3,1),(7,'Middle Office','Oficina media',3,1);
/*!40000 ALTER TABLE `area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `asociacion`
--

LOCK TABLES `asociacion` WRITE;
/*!40000 ALTER TABLE `asociacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `asociacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `atributo`
--

LOCK TABLES `atributo` WRITE;
/*!40000 ALTER TABLE `atributo` DISABLE KEYS */;
INSERT INTO `atributo` VALUES (1,'Pantalla',1),(2,'Puertos',1),(3,'Lector de DVD',1),(4,'LED',1);
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
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add area',7,'add_area'),(26,'Can change area',7,'change_area'),(27,'Can delete area',7,'delete_area'),(28,'Can view area',7,'view_area'),(29,'Can add atributo',8,'add_atributo'),(30,'Can change atributo',8,'change_atributo'),(31,'Can delete atributo',8,'delete_atributo'),(32,'Can view atributo',8,'view_atributo'),(33,'Can add auditoria',9,'add_auditoria'),(34,'Can change auditoria',9,'change_auditoria'),(35,'Can delete auditoria',9,'delete_auditoria'),(36,'Can view auditoria',9,'view_auditoria'),(37,'Can add auth group',10,'add_authgroup'),(38,'Can change auth group',10,'change_authgroup'),(39,'Can delete auth group',10,'delete_authgroup'),(40,'Can view auth group',10,'view_authgroup'),(41,'Can add auth group permissions',11,'add_authgrouppermissions'),(42,'Can change auth group permissions',11,'change_authgrouppermissions'),(43,'Can delete auth group permissions',11,'delete_authgrouppermissions'),(44,'Can view auth group permissions',11,'view_authgrouppermissions'),(45,'Can add auth permission',12,'add_authpermission'),(46,'Can change auth permission',12,'change_authpermission'),(47,'Can delete auth permission',12,'delete_authpermission'),(48,'Can view auth permission',12,'view_authpermission'),(49,'Can add auth user',13,'add_authuser'),(50,'Can change auth user',13,'change_authuser'),(51,'Can delete auth user',13,'delete_authuser'),(52,'Can view auth user',13,'view_authuser'),(53,'Can add auth user groups',14,'add_authusergroups'),(54,'Can change auth user groups',14,'change_authusergroups'),(55,'Can delete auth user groups',14,'delete_authusergroups'),(56,'Can view auth user groups',14,'view_authusergroups'),(57,'Can add auth user user permissions',15,'add_authuseruserpermissions'),(58,'Can change auth user user permissions',15,'change_authuseruserpermissions'),(59,'Can delete auth user user permissions',15,'delete_authuseruserpermissions'),(60,'Can view auth user user permissions',15,'view_authuseruserpermissions'),(61,'Can add cargo',16,'add_cargo'),(62,'Can change cargo',16,'change_cargo'),(63,'Can delete cargo',16,'delete_cargo'),(64,'Can view cargo',16,'view_cargo'),(65,'Can add cuenta',17,'add_cuenta'),(66,'Can change cuenta',17,'change_cuenta'),(67,'Can delete cuenta',17,'delete_cuenta'),(68,'Can view cuenta',17,'view_cuenta'),(69,'Can add departamento',18,'add_departamento'),(70,'Can change departamento',18,'change_departamento'),(71,'Can delete departamento',18,'delete_departamento'),(72,'Can view departamento',18,'view_departamento'),(73,'Can add django admin log',19,'add_djangoadminlog'),(74,'Can change django admin log',19,'change_djangoadminlog'),(75,'Can delete django admin log',19,'delete_djangoadminlog'),(76,'Can view django admin log',19,'view_djangoadminlog'),(77,'Can add django content type',20,'add_djangocontenttype'),(78,'Can change django content type',20,'change_djangocontenttype'),(79,'Can delete django content type',20,'delete_djangocontenttype'),(80,'Can view django content type',20,'view_djangocontenttype'),(81,'Can add django migrations',21,'add_djangomigrations'),(82,'Can change django migrations',21,'change_djangomigrations'),(83,'Can delete django migrations',21,'delete_djangomigrations'),(84,'Can view django migrations',21,'view_djangomigrations'),(85,'Can add django session',22,'add_djangosession'),(86,'Can change django session',22,'change_djangosession'),(87,'Can delete django session',22,'delete_djangosession'),(88,'Can view django session',22,'view_djangosession'),(89,'Can add empresa',23,'add_empresa'),(90,'Can change empresa',23,'change_empresa'),(91,'Can delete empresa',23,'delete_empresa'),(92,'Can view empresa',23,'view_empresa'),(93,'Can add equipo',24,'add_equipo'),(94,'Can change equipo',24,'change_equipo'),(95,'Can delete equipo',24,'delete_equipo'),(96,'Can view equipo',24,'view_equipo'),(97,'Can add gerencia',25,'add_gerencia'),(98,'Can change gerencia',25,'change_gerencia'),(99,'Can delete gerencia',25,'delete_gerencia'),(100,'Can view gerencia',25,'view_gerencia'),(101,'Can add licencia',26,'add_licencia'),(102,'Can change licencia',26,'change_licencia'),(103,'Can delete licencia',26,'delete_licencia'),(104,'Can view licencia',26,'view_licencia'),(105,'Can add os',27,'add_os'),(106,'Can change os',27,'change_os'),(107,'Can delete os',27,'delete_os'),(108,'Can view os',27,'view_os'),(109,'Can add permiso',28,'add_permiso'),(110,'Can change permiso',28,'change_permiso'),(111,'Can delete permiso',28,'delete_permiso'),(112,'Can view permiso',28,'view_permiso'),(113,'Can add regional',29,'add_regional'),(114,'Can change regional',29,'change_regional'),(115,'Can delete regional',29,'delete_regional'),(116,'Can view regional',29,'view_regional'),(117,'Can add ubicacion',30,'add_ubicacion'),(118,'Can change ubicacion',30,'change_ubicacion'),(119,'Can delete ubicacion',30,'delete_ubicacion'),(120,'Can view ubicacion',30,'view_ubicacion'),(121,'Can add usuario ad',31,'add_usuarioad'),(122,'Can change usuario ad',31,'change_usuarioad'),(123,'Can delete usuario ad',31,'delete_usuarioad'),(124,'Can view usuario ad',31,'view_usuarioad'),(125,'Can add usuario correo',32,'add_usuariocorreo'),(126,'Can change usuario correo',32,'change_usuariocorreo'),(127,'Can delete usuario correo',32,'delete_usuariocorreo'),(128,'Can view usuario correo',32,'view_usuariocorreo'),(129,'Can add equipo has atributo',33,'add_equipohasatributo'),(130,'Can change equipo has atributo',33,'change_equipohasatributo'),(131,'Can delete equipo has atributo',33,'delete_equipohasatributo'),(132,'Can view equipo has atributo',33,'view_equipohasatributo'),(133,'Can add impresora',34,'add_impresora'),(134,'Can change impresora',34,'change_impresora'),(135,'Can delete impresora',34,'delete_impresora'),(136,'Can view impresora',34,'view_impresora'),(137,'Can add ordenador',35,'add_ordenador'),(138,'Can change ordenador',35,'change_ordenador'),(139,'Can delete ordenador',35,'delete_ordenador'),(140,'Can view ordenador',35,'view_ordenador'),(141,'Can add os has ordenador',36,'add_oshasordenador'),(142,'Can change os has ordenador',36,'change_oshasordenador'),(143,'Can delete os has ordenador',36,'delete_oshasordenador'),(144,'Can view os has ordenador',36,'view_oshasordenador'),(145,'Can add otro dispositivo',37,'add_otrodispositivo'),(146,'Can change otro dispositivo',37,'change_otrodispositivo'),(147,'Can delete otro dispositivo',37,'delete_otrodispositivo'),(148,'Can view otro dispositivo',37,'view_otrodispositivo'),(149,'Can add Token',38,'add_token'),(150,'Can change Token',38,'change_token'),(151,'Can delete Token',38,'delete_token'),(152,'Can view Token',38,'view_token');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `cargo`
--

LOCK TABLES `cargo` WRITE;
/*!40000 ALTER TABLE `cargo` DISABLE KEYS */;
INSERT INTO `cargo` VALUES (1,'Pasante','pasante',1),(2,'Gerente','Administrador del area',1),(3,'Empaquetador','se encarga de guardar las cosas',1),(4,'Subgerente','El segundo al mando',1);
/*!40000 ALTER TABLE `cargo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `cuenta`
--

LOCK TABLES `cuenta` WRITE;
/*!40000 ALTER TABLE `cuenta` DISABLE KEYS */;
INSERT INTO `cuenta` VALUES (1,'practicantegst','avicola1',1),(2,'practicantecnt','avicola1',1),(3,'GerenteADM','avicola1',1);
/*!40000 ALTER TABLE `cuenta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `departamento`
--

LOCK TABLES `departamento` WRITE;
/*!40000 ALTER TABLE `departamento` DISABLE KEYS */;
INSERT INTO `departamento` VALUES (1,'Sistemas','Departamento de sistemas',1),(2,'Contabilidad','Departamento contable',1),(3,'Administracion','Departamento administrativo',1);
/*!40000 ALTER TABLE `departamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(38,'authtoken','token'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'Sofia_App','area'),(8,'Sofia_App','atributo'),(9,'Sofia_App','auditoria'),(10,'Sofia_App','authgroup'),(11,'Sofia_App','authgrouppermissions'),(12,'Sofia_App','authpermission'),(13,'Sofia_App','authuser'),(14,'Sofia_App','authusergroups'),(15,'Sofia_App','authuseruserpermissions'),(16,'Sofia_App','cargo'),(17,'Sofia_App','cuenta'),(18,'Sofia_App','departamento'),(19,'Sofia_App','djangoadminlog'),(20,'Sofia_App','djangocontenttype'),(21,'Sofia_App','djangomigrations'),(22,'Sofia_App','djangosession'),(23,'Sofia_App','empresa'),(24,'Sofia_App','equipo'),(33,'Sofia_App','equipohasatributo'),(25,'Sofia_App','gerencia'),(34,'Sofia_App','impresora'),(26,'Sofia_App','licencia'),(35,'Sofia_App','ordenador'),(27,'Sofia_App','os'),(36,'Sofia_App','oshasordenador'),(37,'Sofia_App','otrodispositivo'),(28,'Sofia_App','permiso'),(29,'Sofia_App','regional'),(30,'Sofia_App','ubicacion'),(31,'Sofia_App','usuarioad'),(32,'Sofia_App','usuariocorreo');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'Sofia_App','0001_initial','2019-10-14 23:02:54.689080'),(2,'contenttypes','0001_initial','2019-10-14 23:02:54.781832'),(3,'auth','0001_initial','2019-10-14 23:02:55.035485'),(4,'admin','0001_initial','2019-10-14 23:02:55.836344'),(5,'admin','0002_logentry_remove_auto_add','2019-10-14 23:02:55.992973'),(6,'admin','0003_logentry_add_action_flag_choices','2019-10-14 23:02:56.011875'),(7,'contenttypes','0002_remove_content_type_name','2019-10-14 23:02:56.210396'),(8,'auth','0002_alter_permission_name_max_length','2019-10-14 23:02:56.305060'),(9,'auth','0003_alter_user_email_max_length','2019-10-14 23:02:56.413883'),(10,'auth','0004_alter_user_username_opts','2019-10-14 23:02:56.425772'),(11,'auth','0005_alter_user_last_login_null','2019-10-14 23:02:56.530862'),(12,'auth','0006_require_contenttypes_0002','2019-10-14 23:02:56.535802'),(13,'auth','0007_alter_validators_add_error_messages','2019-10-14 23:02:56.553793'),(14,'auth','0008_alter_user_username_max_length','2019-10-14 23:02:56.661509'),(15,'auth','0009_alter_user_last_name_max_length','2019-10-14 23:02:56.763193'),(16,'auth','0010_alter_group_name_max_length','2019-10-14 23:02:56.857941'),(17,'auth','0011_update_proxy_permissions','2019-10-14 23:02:56.885865'),(18,'authtoken','0001_initial','2019-10-14 23:02:56.954728'),(19,'authtoken','0002_auto_20160226_1747','2019-10-14 23:02:57.228985'),(20,'sessions','0001_initial','2019-10-14 23:02:57.270873');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `empresa`
--

LOCK TABLES `empresa` WRITE;
/*!40000 ALTER TABLE `empresa` DISABLE KEYS */;
INSERT INTO `empresa` VALUES (1,'Sofia Ltda.','empresa principal',1),(2,'Indatta','empresa secundaria de bases de datos',1),(3,'Google','Empresa que controla todo lo controlable',1);
/*!40000 ALTER TABLE `empresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `equipo`
--

LOCK TABLES `equipo` WRITE;
/*!40000 ALTER TABLE `equipo` DISABLE KEYS */;
INSERT INTO `equipo` VALUES (1,'hp','mx2510','132465789','987654321','127.0.0.0','prueba v7',1),(2,'dell','inspirion 15 5570','8495623','15487945','195.165.23.2','sin observaciones',1),(3,'asus','xpms465','111111','222222','321.654.987.321','todas',1),(4,'samsung','asdert15','888888','999999','11.20.22.35','imprsora observation',1),(7,'samsung','xpms54','654','654','6486','4',1);
/*!40000 ALTER TABLE `equipo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `gerencia`
--

LOCK TABLES `gerencia` WRITE;
/*!40000 ALTER TABLE `gerencia` DISABLE KEYS */;
INSERT INTO `gerencia` VALUES (1,'GST','gerencia de sistemas',1),(2,'GAM','gerencia administrativa',1),(3,'GCT','gerencia contable',1);
/*!40000 ALTER TABLE `gerencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `impresora`
--

LOCK TABLES `impresora` WRITE;
/*!40000 ALTER TABLE `impresora` DISABLE KEYS */;
INSERT INTO `impresora` VALUES (1,'laser','no usa tinta'),(4,'laser','sin tinta');
/*!40000 ALTER TABLE `impresora` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `licencia`
--

LOCK TABLES `licencia` WRITE;
/*!40000 ALTER TABLE `licencia` DISABLE KEYS */;
/*!40000 ALTER TABLE `licencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `ordenador`
--

LOCK TABLES `ordenador` WRITE;
/*!40000 ALTER TABLE `ordenador` DISABLE KEYS */;
INSERT INTO `ordenador` VALUES (2,'desktop','654987654321','practicantegst','intel core i9','16gb','2tb','ssd',1),(3,'laptop','ASD:ASD:ASD:ASD','practicantegst','ryzen v7','16gb','1tb','ssd',4);
/*!40000 ALTER TABLE `ordenador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `ordenador_has_licencia`
--

LOCK TABLES `ordenador_has_licencia` WRITE;
/*!40000 ALTER TABLE `ordenador_has_licencia` DISABLE KEYS */;
/*!40000 ALTER TABLE `ordenador_has_licencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `os`
--

LOCK TABLES `os` WRITE;
/*!40000 ALTER TABLE `os` DISABLE KEYS */;
INSERT INTO `os` VALUES (1,'Windows10','Service pack10','x86',1),(2,'Windows10','Service pack10','x86',1),(3,'Ubuntu 19','LTS','x64',1),(4,'Macos','v13','x64',1);
/*!40000 ALTER TABLE `os` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `otro_dispositivo`
--

LOCK TABLES `otro_dispositivo` WRITE;
/*!40000 ALTER TABLE `otro_dispositivo` DISABLE KEYS */;
INSERT INTO `otro_dispositivo` VALUES (7,'televisor',NULL);
/*!40000 ALTER TABLE `otro_dispositivo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `otro_dispositivo_has_atributo`
--

LOCK TABLES `otro_dispositivo_has_atributo` WRITE;
/*!40000 ALTER TABLE `otro_dispositivo_has_atributo` DISABLE KEYS */;
INSERT INTO `otro_dispositivo_has_atributo` VALUES (7,1,'4k'),(7,2,'20 puertos');
/*!40000 ALTER TABLE `otro_dispositivo_has_atributo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `permiso`
--

LOCK TABLES `permiso` WRITE;
/*!40000 ALTER TABLE `permiso` DISABLE KEYS */;
INSERT INTO `permiso` VALUES (1,'Full',1),(2,'Uso de USB',1),(3,'Uso de carpetas compartidas',1),(4,'Acceso a internet',1);
/*!40000 ALTER TABLE `permiso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `regional`
--

LOCK TABLES `regional` WRITE;
/*!40000 ALTER TABLE `regional` DISABLE KEYS */;
INSERT INTO `regional` VALUES (1,'Santa cruz de la sierra',1),(2,'Tarija',1),(3,'Argentina',1);
/*!40000 ALTER TABLE `regional` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `tablet`
--

LOCK TABLES `tablet` WRITE;
/*!40000 ALTER TABLE `tablet` DISABLE KEYS */;
/*!40000 ALTER TABLE `tablet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `ubicacion`
--

LOCK TABLES `ubicacion` WRITE;
/*!40000 ALTER TABLE `ubicacion` DISABLE KEYS */;
INSERT INTO `ubicacion` VALUES (1,'4to anillo roca y coronado','Edificio Administrativo',1),(2,'calle padre melgar N6','Casa blanca',1),(3,'4to anillo paragua','Upsa',1);
/*!40000 ALTER TABLE `ubicacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `usuario_ad`
--

LOCK TABLES `usuario_ad` WRITE;
/*!40000 ALTER TABLE `usuario_ad` DISABLE KEYS */;
INSERT INTO `usuario_ad` VALUES (1,'Diego Alejandro','LLanos Gareca','8257165',1,1,1,1,1,1,1,1),(2,'Ana','Mendoza','1234567',2,1,1,1,1,NULL,4,1),(3,'Ricardo','suarez','987654',5,2,1,1,2,NULL,2,1),(4,'Flavia','Martinez','3247165',6,2,2,2,1,NULL,2,1),(5,'Juan','Justiniano','8795643',3,2,3,2,2,NULL,4,1);
/*!40000 ALTER TABLE `usuario_ad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `usuario_ad_has_permiso`
--

LOCK TABLES `usuario_ad_has_permiso` WRITE;
/*!40000 ALTER TABLE `usuario_ad_has_permiso` DISABLE KEYS */;
INSERT INTO `usuario_ad_has_permiso` VALUES (3,1),(4,1),(2,3),(5,4);
/*!40000 ALTER TABLE `usuario_ad_has_permiso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `usuario_correo`
--

LOCK TABLES `usuario_correo` WRITE;
/*!40000 ALTER TABLE `usuario_correo` DISABLE KEYS */;
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

-- Dump completed on 2019-10-14 23:46:32
