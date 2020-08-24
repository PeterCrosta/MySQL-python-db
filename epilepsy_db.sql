CREATE DATABASE /*!32312 IF NOT EXISTS*/`epilepsy_db` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `epilepsy_db`;

/*Table structure for table `authors` */

DROP TABLE IF EXISTS `patients`;

CREATE TABLE `patients` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(40) NOT NULL,
  `last_name` varchar(40) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=128 DEFAULT CHARSET=latin1;

/*Data for the table `authors` */

insert  into `patients`(`id`,`first_name`,`last_name`) values (1,'Herbert','Methley'),(2,'Peter','Crosta'),(3,'Hyunmi','Choi'), (4,'Nahal','Heydari'), (5,'Colin','McKinney');

/*Table structure for table `books` */

DROP TABLE IF EXISTS `drugs`;

CREATE TABLE `drugs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=84 DEFAULT CHARSET=latin1;

/*Data for the table `books` */

insert  into `drugs`(`id`,`name`) values (1,'Levetiracetam'),(2,'Lamotrigine'),(3,'Gabapentin'),(4,'Zonisamide'),(5,'Clonazepam');

/*Table structure for table `book_author` */

DROP TABLE IF EXISTS `regimens`;

CREATE TABLE `regimens` (
  `pt_id` int(11) NOT NULL,
  `drug_id` int(11) NOT NULL,
  KEY `drug_id` (`drug_id`),
  KEY `pt_id` (`pt_id`),
  CONSTRAINT `ba_fk1` FOREIGN KEY (`drug_id`) REFERENCES `drugs` (`id`) ON DELETE CASCADE,
  CONSTRAINT `ba_fk2` FOREIGN KEY (`pt_id`) REFERENCES `patients` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `book_author` */

insert  into `regimens`(`pt_id`,`drug_id`) values (1,1),(1,2), (1,3),(2,2),(3,5),(4,2),(4,4),(5,5);


/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
