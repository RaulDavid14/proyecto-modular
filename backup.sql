/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-11.5.2-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: catalogos
-- ------------------------------------------------------
-- Server version	11.5.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add content type',4,'add_contenttype'),
(14,'Can change content type',4,'change_contenttype'),
(15,'Can delete content type',4,'delete_contenttype'),
(16,'Can view content type',4,'view_contenttype'),
(17,'Can add session',5,'add_session'),
(18,'Can change session',5,'change_session'),
(19,'Can delete session',5,'delete_session'),
(20,'Can view session',5,'view_session'),
(21,'Can add Ingreso',6,'add_catingresos'),
(22,'Can change Ingreso',6,'change_catingresos'),
(23,'Can delete Ingreso',6,'delete_catingresos'),
(24,'Can view Ingreso',6,'view_catingresos'),
(25,'Can add Situacion Laboral',7,'add_catsituacionlaboral'),
(26,'Can change Situacion Laboral',7,'change_catsituacionlaboral'),
(27,'Can delete Situacion Laboral',7,'delete_catsituacionlaboral'),
(28,'Can view Situacion Laboral',7,'view_catsituacionlaboral'),
(29,'Can add user model',8,'add_usermodel'),
(30,'Can change user model',8,'change_usermodel'),
(31,'Can delete user model',8,'delete_usermodel'),
(32,'Can view user model',8,'view_usermodel'),
(33,'Can add Estado cívil',9,'add_catestadocivil'),
(34,'Can change Estado cívil',9,'change_catestadocivil'),
(35,'Can delete Estado cívil',9,'delete_catestadocivil'),
(36,'Can view Estado cívil',9,'view_catestadocivil'),
(37,'Can add Nivel educativo',10,'add_catniveleducativo'),
(38,'Can change Nivel educativo',10,'change_catniveleducativo'),
(39,'Can delete Nivel educativo',10,'delete_catniveleducativo'),
(40,'Can view Nivel educativo',10,'view_catniveleducativo'),
(41,'Can add Población',11,'add_catpoblacion'),
(42,'Can change Población',11,'change_catpoblacion'),
(43,'Can delete Población',11,'delete_catpoblacion'),
(44,'Can view Población',11,'view_catpoblacion'),
(45,'Can add Sexo',12,'add_catsexo'),
(46,'Can change Sexo',12,'change_catsexo'),
(47,'Can delete Sexo',12,'delete_catsexo'),
(48,'Can view Sexo',12,'view_catsexo'),
(49,'Can add pregunta model',13,'add_preguntamodel'),
(50,'Can change pregunta model',13,'change_preguntamodel'),
(51,'Can delete pregunta model',13,'delete_preguntamodel'),
(52,'Can view pregunta model',13,'view_preguntamodel');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cat_ingreso`
--

DROP TABLE IF EXISTS `cat_ingreso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cat_ingreso` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) NOT NULL,
  `abreviacion` varchar(5) NOT NULL,
  `descripcion` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cat_ingreso`
--

LOCK TABLES `cat_ingreso` WRITE;
/*!40000 ALTER TABLE `cat_ingreso` DISABLE KEYS */;
INSERT INTO `cat_ingreso` VALUES
(1,'menos de $5,000','','Menos de $5,000 pesos'),
(2,'$5000 a $9,999','','De $5,000 a $9,999 pesos'),
(3,'$10,000 a $19,999','','De $10,000 a 19,999 pesos'),
(4,'$20,000 a $29,999','','De $20,000 a $29,999 pesos'),
(5,'$30,000 a $39,999','','De $30,000 a $39,999 pesos'),
(6,'$40,000 a $49,999','','De $40.000 a $49.999 pesos'),
(7,'$50,000 a $59,999','','De $50,000 a $59,999 pesos'),
(8,'$60,000 a $69,999','','De $60.000 a $69.999 pesos'),
(9,'$70,000 a $79,999','','De $70.000 a $79.999 pesos'),
(10,'$80,000 a $89,999','','De $80.000 a $89.999 pesos'),
(11,'$90,000 a $99,999','','De $90.000 a 99.999 pesos'),
(12,'$100,000 a $149,000','','De $100,000 a $149,999 pesos'),
(13,'más de $150,000','','$150,000 pesos o más');
/*!40000 ALTER TABLE `cat_ingreso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cat_situacion_laboral`
--

DROP TABLE IF EXISTS `cat_situacion_laboral`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cat_situacion_laboral` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) NOT NULL,
  `abreviacion` varchar(5) NOT NULL,
  `descripcion` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cat_situacion_laboral`
--

LOCK TABLES `cat_situacion_laboral` WRITE;
/*!40000 ALTER TABLE `cat_situacion_laboral` DISABLE KEYS */;
INSERT INTO `cat_situacion_laboral` VALUES
(1,'empleado','empl','Persona que tiene un empleo remunerado'),
(2,'desempleado','desem','Persona que está buscando empleo o no tiene trabajo actualmente'),
(3,'estudiante','estud','Persona que se dedica a estudiar en una institución educativa'),
(4,'jubilado','jubi','Persona que se ha retirado del mercado laboral tras cumplir con los requisitos de jubilación');
/*!40000 ALTER TABLE `cat_situacion_laboral` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `catalogo_estado_civil`
--

DROP TABLE IF EXISTS `catalogo_estado_civil`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `catalogo_estado_civil` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_largo` varchar(30) NOT NULL,
  `abreviacion` varchar(5) NOT NULL,
  `descripcion` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `catalogo_estado_civil`
--

LOCK TABLES `catalogo_estado_civil` WRITE;
/*!40000 ALTER TABLE `catalogo_estado_civil` DISABLE KEYS */;
INSERT INTO `catalogo_estado_civil` VALUES
(1,'soltero','solt','Persona no casada que no ha tenido una unión formal'),
(2,'casado','casa','Persona unida en matrimonio'),
(3,'viudo','viudo','Persona cuya pareja ha fallecido'),
(4,'unión libre','unlib','Persona en una relación de convivencia sin matrimonio formal'),
(5,'separado/divorciado','se_di','Persona que ha terminado una relación matrimonial o de unión formal');
/*!40000 ALTER TABLE `catalogo_estado_civil` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `catalogo_nivel_educativo`
--

DROP TABLE IF EXISTS `catalogo_nivel_educativo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `catalogo_nivel_educativo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_largo` varchar(30) NOT NULL,
  `abreviacion` varchar(5) NOT NULL,
  `descripcion` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `catalogo_nivel_educativo`
--

LOCK TABLES `catalogo_nivel_educativo` WRITE;
/*!40000 ALTER TABLE `catalogo_nivel_educativo` DISABLE KEYS */;
INSERT INTO `catalogo_nivel_educativo` VALUES
(7,'primaria','prim','Persona que ha completado o está cursando el nivel educativo de primaria'),
(8,'secundaria','secu','Persona que ha completado o está cursando el nivel educativo de secundaria'),
(9,'preparatoria','prepa','Persona que ha completado o está cursando el nivel educativo de preparatoria o bachillerato'),
(10,'universidad','univ','Persona que ha completado o está cursando estudios universitarios o técnicos'),
(11,'posgrado','posgr','Persona que ha completado estudios de nivel posgrado (maestría o doctorado)'),
(12,'ninguno','none','Persona que no ha completado ningún nivel educativo formal');
/*!40000 ALTER TABLE `catalogo_nivel_educativo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `catalogo_poblacion`
--

DROP TABLE IF EXISTS `catalogo_poblacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `catalogo_poblacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_largo` varchar(30) NOT NULL,
  `abreviacion` varchar(5) NOT NULL,
  `descripcion` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `catalogo_poblacion`
--

LOCK TABLES `catalogo_poblacion` WRITE;
/*!40000 ALTER TABLE `catalogo_poblacion` DISABLE KEYS */;
INSERT INTO `catalogo_poblacion` VALUES
(1,'rural','rural','Persona que reside en una zona o comunidad rural'),
(2,'urbana','urban','Persona que reside en una zona o ciudad urbana');
/*!40000 ALTER TABLE `catalogo_poblacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `catalogo_sexo`
--

DROP TABLE IF EXISTS `catalogo_sexo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `catalogo_sexo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_largo` varchar(30) NOT NULL,
  `abreviacion` varchar(5) NOT NULL,
  `descripcion` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `catalogo_sexo`
--

LOCK TABLES `catalogo_sexo` WRITE;
/*!40000 ALTER TABLE `catalogo_sexo` DISABLE KEYS */;
INSERT INTO `catalogo_sexo` VALUES
(1,'Hombre','H','Genero masculino'),
(2,'Mujer','M','Genero femenino');
/*!40000 ALTER TABLE `catalogo_sexo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cuestionario_preguntamodel`
--

DROP TABLE IF EXISTS `cuestionario_preguntamodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cuestionario_preguntamodel` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `texto` longtext NOT NULL,
  `sig_pregunta` int(11) NOT NULL,
  `tipo_respuesta` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cuestionario_preguntamodel`
--

LOCK TABLES `cuestionario_preguntamodel` WRITE;
/*!40000 ALTER TABLE `cuestionario_preguntamodel` DISABLE KEYS */;
/*!40000 ALTER TABLE `cuestionario_preguntamodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_usuario_usermodel_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_usuario_usermodel_id` FOREIGN KEY (`user_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(9,'catalogos','catestadocivil'),
(10,'catalogos','catniveleducativo'),
(11,'catalogos','catpoblacion'),
(12,'catalogos','catsexo'),
(4,'contenttypes','contenttype'),
(13,'cuestionario','preguntamodel'),
(6,'datos_socioeconomicos','catingresos'),
(7,'datos_socioeconomicos','catsituacionlaboral'),
(5,'sessions','session'),
(8,'usuario','usermodel');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES
(1,'contenttypes','0001_initial','2024-10-14 02:20:41.631943'),
(2,'contenttypes','0002_remove_content_type_name','2024-10-14 02:20:41.668762'),
(3,'auth','0001_initial','2024-10-14 02:20:41.805950'),
(4,'auth','0002_alter_permission_name_max_length','2024-10-14 02:20:41.836450'),
(5,'auth','0003_alter_user_email_max_length','2024-10-14 02:20:41.849631'),
(6,'auth','0004_alter_user_username_opts','2024-10-14 02:20:41.861388'),
(7,'auth','0005_alter_user_last_login_null','2024-10-14 02:20:41.873801'),
(8,'auth','0006_require_contenttypes_0002','2024-10-14 02:20:41.879748'),
(9,'auth','0007_alter_validators_add_error_messages','2024-10-14 02:20:41.888080'),
(10,'auth','0008_alter_user_username_max_length','2024-10-14 02:20:41.898821'),
(11,'auth','0009_alter_user_last_name_max_length','2024-10-14 02:20:41.932434'),
(12,'auth','0010_alter_group_name_max_length','2024-10-14 02:20:41.952042'),
(13,'auth','0011_update_proxy_permissions','2024-10-14 02:20:41.961464'),
(14,'auth','0012_alter_user_first_name_max_length','2024-10-14 02:20:41.966690'),
(15,'usuario','0001_initial','2024-10-14 02:20:42.146424'),
(16,'admin','0001_initial','2024-10-14 02:20:42.261627'),
(17,'admin','0002_logentry_remove_auto_add','2024-10-14 02:20:42.280092'),
(18,'admin','0003_logentry_add_action_flag_choices','2024-10-14 02:20:42.296830'),
(20,'sessions','0001_initial','2024-10-14 02:20:42.392479'),
(21,'usuario','0002_alter_usermodel_options_alter_usermodel_table','2024-10-14 02:22:30.132908'),
(24,'catalogos','0001_initial','2024-10-20 15:50:28.443678'),
(25,'datos_socioeconomicos','0001_initial','2024-10-20 16:20:47.927595'),
(26,'cuestionario','0001_initial','2024-10-20 16:46:25.381260');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES
('yot1fiby42phl88fbuienqb0kd0t8nn3','.eJxVjEEOgjAQRe_StWmAdix16Z4zkJnOjKCmTSisjHdXEha6_e-9_zIjbus0blWWcWZzMa05_W6E6SF5B3zHfCs2lbwuM9ldsQetdigsz-vh_h1MWKdvHUBRzh0yswtRut5HJe8aiQReXEuEzvfYQ1IG5aQQm9gpYEiBPal5fwAE_TkH:1t0B1s:x6UEdxrCy4Gy_64a9374hqxWKLIraEHai3rSIOVnLqE','2024-10-28 02:41:52.533374');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuarios` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `second_name` varchar(30) DEFAULT NULL,
  `third_name` varchar(30) DEFAULT NULL,
  `last_name_maternal` varchar(30) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES
(1,'pbkdf2_sha256$870000$FTQo7bT1wOagjkHLwjfNQB$HfuzylWOeDNDKZ0ylE3lPU7HYZVIoBtAZcDYmoUgBr0=','2024-10-14 02:41:52.529419',0,'JOSE','DAVID','rauldavidc14@gmail.com','RAUL',NULL,'CORONA','2000-12-14',1,0);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios_groups`
--

DROP TABLE IF EXISTS `usuarios_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuarios_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `usermodel_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario_usermodel_groups_usermodel_id_group_id_20007749_uniq` (`usermodel_id`,`group_id`),
  KEY `usuario_usermodel_groups_group_id_b7b598f8_fk_auth_group_id` (`group_id`),
  CONSTRAINT `usuario_usermodel_gr_usermodel_id_cdb79583_fk_usuario_u` FOREIGN KEY (`usermodel_id`) REFERENCES `usuarios` (`id`),
  CONSTRAINT `usuario_usermodel_groups_group_id_b7b598f8_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios_groups`
--

LOCK TABLES `usuarios_groups` WRITE;
/*!40000 ALTER TABLE `usuarios_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuarios_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios_user_permissions`
--

DROP TABLE IF EXISTS `usuarios_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuarios_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `usermodel_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario_usermodel_user_p_usermodel_id_permission__35e7aa3d_uniq` (`usermodel_id`,`permission_id`),
  KEY `usuario_usermodel_us_permission_id_a7aca6f4_fk_auth_perm` (`permission_id`),
  CONSTRAINT `usuario_usermodel_us_permission_id_a7aca6f4_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `usuario_usermodel_us_usermodel_id_9288dc98_fk_usuario_u` FOREIGN KEY (`usermodel_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios_user_permissions`
--

LOCK TABLES `usuarios_user_permissions` WRITE;
/*!40000 ALTER TABLE `usuarios_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuarios_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2024-10-23 21:25:28
