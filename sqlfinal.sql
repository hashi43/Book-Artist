/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - program_announcer
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`program_announcer` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `program_announcer`;

/*Table structure for table `artist_panel` */

DROP TABLE IF EXISTS `artist_panel`;

CREATE TABLE `artist_panel` (
  `panel_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  `pincode` int(11) DEFAULT NULL,
  `logo` varchar(250) DEFAULT NULL,
  `latitude` varchar(50) DEFAULT NULL,
  `longitude` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT 'pending',
  `est_year` date DEFAULT NULL,
  PRIMARY KEY (`panel_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `artist_panel` */

insert  into `artist_panel`(`panel_id`,`login_id`,`name`,`email`,`phone`,`place`,`post`,`district`,`pincode`,`logo`,`latitude`,`longitude`,`status`,`est_year`) values 
(1,12,'Thaikkudam Bridge','thaikkudam@gmail.com',9854253655,'Kochi','Mattancherry','Ernakulam',682002,'/static/artist/thaii.jpg','152.155.13.12','455.155.15.15','artist','2013-06-20');

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `book_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `user_lid` int(11) DEFAULT NULL,
  `program_id` int(11) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `bdate` date DEFAULT NULL,
  `location` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `booking` */

insert  into `booking`(`book_id`,`date`,`user_lid`,`program_id`,`status`,`bdate`,`location`) values 
(1,'2023-04-06',24,1,'Approved','2023-04-12','pmna'),
(2,'2023-04-06',24,2,'pending','2023-04-16','cpy'),
(3,'2023-04-06',24,2,'Rejected','2023-04-09',''),
(4,'2023-04-06',24,1,'pending','2023-04-22','bu hn'),
(5,'2023-04-06',30,1,'pending','2023-04-22','trivandrum ');

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `program_id` int(11) NOT NULL AUTO_INCREMENT,
  `program_name` varchar(50) DEFAULT NULL,
  `photo` varchar(250) DEFAULT NULL,
  `artist_panel_lid` int(11) DEFAULT NULL,
  `description` varchar(250) DEFAULT NULL,
  `budget` int(11) DEFAULT NULL,
  PRIMARY KEY (`program_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`program_id`,`program_name`,`photo`,`artist_panel_lid`,`description`,`budget`) values 
(1,'MUSIC BAND','/static/category/thaii 1.jpg',12,'is a famous music band in kerala',15000),
(2,'Carol','/static/category/A-Christmas-Carol-1024x576.jpg',12,'carol team for christhmas',12500);

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `from_id` int(11) DEFAULT NULL,
  `to_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `message` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`chat_id`,`from_id`,`to_id`,`date`,`message`) values 
(1,15,26,'2022-12-30','hi'),
(2,26,15,'2022-12-30','dfhh'),
(3,26,1,'2022-12-30','hi'),
(4,26,1,'2022-12-30','hello'),
(5,26,1,'2022-12-30','dfhh'),
(6,26,1,'2022-12-30','xcvv'),
(7,1,26,'2022-12-30','fds'),
(8,15,26,'2022-12-30','hello'),
(9,26,15,'2022-12-30','hi'),
(10,26,15,'2022-12-30','hi'),
(11,26,15,'2022-12-30','hi'),
(12,26,15,'2022-12-30','hi'),
(13,26,15,'2022-12-30','hi'),
(14,15,26,'2022-12-30','hello'),
(15,15,26,'2023-01-20','how are you'),
(16,24,15,'2023-03-05','hi'),
(17,26,15,'2023-04-02','iam fine'),
(18,26,15,'2023-04-02','thank you for asking'),
(19,15,14,'2023-04-06','hi');

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaints_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `user_lid` int(11) DEFAULT NULL,
  `complaint` varchar(250) DEFAULT NULL,
  `reply` varchar(250) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`complaints_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `feedback` varchar(250) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `user_lid` int(11) DEFAULT NULL,
  `rating` int(11) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`feedback`,`date`,`user_lid`,`rating`) values 
(1,'this app is change your life','2022-12-08',16,5),
(2,'tu ubibbuyg v g','2022-12-30',26,3),
(3,'tu ubibbuyg v g','2022-12-30',26,3),
(4,'tu ubibbuyg v g','2022-12-30',26,3),
(5,'tu ubibbuyg v g','2022-12-30',26,3),
(6,'tu ubibbuyg v g','2022-12-30',26,3),
(7,'tu ubibbuyg v g','2022-12-30',26,3),
(8,'tu ubibbuyg v g','2022-12-30',26,3),
(9,'tu ubibbuyg v g','2022-12-30',26,3),
(10,'tu ubibbuyg v g','2022-12-30',26,3),
(11,'tu ubibbuyg v g','2022-12-30',26,3),
(12,'tu ubibbuyg v g','2022-12-30',26,3),
(13,'tu ubibbuyg v g','2022-12-30',26,3),
(14,'tu ubibbuyg v g','2022-12-30',26,3),
(15,'tu ubibbuyg v g','2022-12-30',26,3),
(16,'tu ubibbuyg v g','2022-12-30',26,3),
(17,'tu ubibbuyg v g','2022-12-30',26,3),
(18,'tu ubibbuyg v g','2022-12-30',26,3),
(19,'tu ubibbuyg v g','2022-12-30',26,3),
(20,'tu ubibbuyg v g','2022-12-30',26,3),
(21,'tu ubibbuyg v g.','2022-12-30',26,3),
(22,'tu ubibbuyg v g.','2022-12-30',26,3),
(23,'tu ubibbuyg v g.','2022-12-30',26,3),
(24,'tu ubibbuyg v g.','2022-12-30',26,3),
(25,'tu ubibbuyg v g.','2022-12-30',26,3),
(26,'tu ubibbuyg v g.','2022-12-30',26,3),
(27,'tu ubibbuyg v g.','2022-12-30',26,3),
(28,'tu ubibbuyg v g.','2022-12-30',26,3),
(29,'tu ubibbuyg v g.','2022-12-30',26,3),
(30,'tu ubibbuyg v g.','2022-12-30',26,3),
(31,'tu ubibbuyg v g.','2022-12-30',26,3),
(32,'tu ubibbuyg v g.','2022-12-30',26,3),
(33,'tu ubibbuyg v g.','2022-12-30',26,3),
(34,'tu ubibbuyg v g.','2022-12-30',26,3),
(35,'tu ubibbuyg v g.','2022-12-30',26,3),
(36,'tu ubibbuyg v g.','2022-12-30',26,3),
(37,'tu ubibbuyg v g.','2022-12-30',26,3),
(38,'tu ubibbuyg v g.','2022-12-30',26,3),
(39,'tu ubibbuyg v g.','2022-12-30',26,3),
(40,'tu ubibbuyg v g.','2022-12-30',26,3),
(41,'tu ubibbuyg v g.','2022-12-30',26,3),
(42,'tu ubibbuyg v g.','2022-12-30',26,3),
(43,'tu ubibbuyg v g.','2022-12-30',26,3),
(44,'tu ubibbuyg v g.','2022-12-30',26,3),
(45,'tu ubibbuyg v g.','2022-12-30',26,3),
(46,'tu ubibbuyg v g.','2022-12-30',26,3),
(47,'farzan vaazha','2022-12-30',26,5),
(48,'farzan vaazha','2022-12-30',26,5),
(49,'farzan vaazha','2022-12-30',26,5),
(50,'farzan vaazha','2022-12-30',26,5),
(51,'farzan vaazha','2022-12-30',26,5),
(52,'farzan vaazha','2022-12-30',26,5),
(53,'farzan vaazha','2022-12-30',26,5),
(54,'farzan vaazha','2022-12-30',26,5),
(55,'ok','2022-12-30',26,3),
(56,'good one','2022-12-30',26,3),
(57,'ffhhhg','2022-12-30',26,3);

/*Table structure for table `highlights` */

DROP TABLE IF EXISTS `highlights`;

CREATE TABLE `highlights` (
  `highlight_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `description` varchar(250) DEFAULT NULL,
  `photo_1` varchar(250) DEFAULT NULL,
  `photo_2` varchar(250) DEFAULT NULL,
  `program_id` int(11) DEFAULT NULL,
  `artist_panel_lid` int(11) DEFAULT NULL,
  PRIMARY KEY (`highlight_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `highlights` */

insert  into `highlights`(`highlight_id`,`name`,`description`,`photo_1`,`photo_2`,`program_id`,`artist_panel_lid`) values 
(1,'NAVARASAM','On Diwali, the Cochin-based band Thaikkudam Bridge made an accusation of plagiarism, on social media, against the recent hit Kannada film Kantara. The creative team, the band said, has lifted their 2015 song for the film','/static/highlights/thaii highlightt1.jpg','/static/highlights/navarasam1.jpg',1,12);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`type`) values 
(1,'admin@gmail.com','admin','admin'),
(12,'thaikkudam@gmail.com','Thaikkudampass','artist'),
(13,'rajesh@gmail.com','9564856528','pending'),
(14,'hashi@gmail.com','Hashi@gmail.com','user'),
(15,'mithunraju@gmail.com','123','team leader'),
(16,'danishkkoori47@gmail.com','Dani@123','user'),
(17,'himanshugola@gmail.com','9856475622','pending'),
(18,'himanshugola@gmail.com','9856475622','pending'),
(19,'hashi@gmail.com','Hashi@123','user'),
(21,'hashi@gmail.com','Hashi@123','user'),
(24,'farsan@gmail.com','Farsan@123','user'),
(26,'farsan123@gmail.com','Farsan@123','user'),
(28,'midlaj123@gmail.com','Midlaj@123','user'),
(29,'stn123@gmail.com','stn123','user'),
(30,'nivin123@gmail.com','nivin123','user');

/*Table structure for table `member` */

DROP TABLE IF EXISTS `member`;

CREATE TABLE `member` (
  `member_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  `pincode` int(11) DEFAULT NULL,
  `photo` varchar(250) DEFAULT NULL,
  `artist_panel_lid` int(11) DEFAULT NULL,
  `member_lid` int(11) DEFAULT NULL,
  `program_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `member` */

insert  into `member`(`member_id`,`name`,`email`,`phone`,`place`,`gender`,`post`,`district`,`pincode`,`photo`,`artist_panel_lid`,`member_lid`,`program_id`) values 
(1,' Govind P Menon',' Govindmenon@gmail.com',9564856528,'Kochi','male','Mattancherry','Ernakulam',682002,'/static/member/20221207-154531.jpg',12,13,1),
(2,'Mithun Raju','mithunraju@gmail.com',9685962545,'Kochi','male','Mattancherry','Ernakulam',682019,'/static/member/mithun.jpg',12,15,1),
(3,'Himanshu Gola','himanshugola@gmail.com',9856475622,'Mumbai','male','Dharaavi','mazgaon',400010,'/static/member/Himanshu Gola.jpg',12,17,3);

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `account_no` varchar(50) DEFAULT NULL,
  `cvv` int(11) DEFAULT NULL,
  `book_id` int(11) DEFAULT NULL,
  `bank_name` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`date`,`account_no`,`cvv`,`book_id`,`bank_name`,`status`,`amount`) values 
(1,'2023-03-20','7538282-18',637,1,'sbi','Approved','15000'),
(6,'2023-04-06','145363',1553,NULL,'Baroda ',NULL,NULL),
(7,'2023-04-06','36363',13,NULL,'federal ',NULL,NULL),
(8,'2023-04-06','1442',32,0,'fafaf',NULL,NULL),
(9,'2023-04-06','#553',4,NULL,'fhdj',NULL,NULL),
(10,'2023-04-06','134',34,NULL,'txuf',NULL,NULL),
(11,'2023-04-06','63662',2562,NULL,'jaa',NULL,NULL),
(12,'2023-04-06','1452',2552,NULL,'fajam',NULL,NULL),
(13,'2023-04-06','',0,0,'','Paid',''),
(14,'2023-04-06','57853',413,NULL,'federal ',NULL,NULL),
(15,'2023-04-06','2565',432,1,'federal ','Paid','com.google.android.material.textview.MaterialTextV'),
(16,'2023-04-06','5262',3663,1,'gsjkal','Paid','com.google.android.material.textview.MaterialTextV'),
(17,'2023-04-06','5363',6362,1,'7373','Paid','15000');

/*Table structure for table `review` */

DROP TABLE IF EXISTS `review`;

CREATE TABLE `review` (
  `review_id` int(11) NOT NULL AUTO_INCREMENT,
  `review` varchar(250) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `program_id` int(11) DEFAULT NULL,
  `user_lid` int(11) DEFAULT NULL,
  PRIMARY KEY (`review_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `review` */

insert  into `review`(`review_id`,`review`,`date`,`program_id`,`user_lid`) values 
(8,'execellent program','2022-12-31',1,26),
(9,'i like it ','2022-12-31',1,26),
(10,'good program','2023-03-05',1,24),
(11,'ol afufojan','2023-03-20',1,24),
(12,'fgg','2023-04-06',1,24),
(13,'hh','2023-04-06',2,24);

/*Table structure for table `team_leader` */

DROP TABLE IF EXISTS `team_leader`;

CREATE TABLE `team_leader` (
  `team_leader_id` int(11) NOT NULL AUTO_INCREMENT,
  `member_lid` int(11) DEFAULT NULL,
  `panel_lid` int(11) DEFAULT NULL,
  PRIMARY KEY (`team_leader_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `team_leader` */

insert  into `team_leader`(`team_leader_id`,`member_lid`,`panel_lid`) values 
(2,15,12);

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  `pincode` int(11) DEFAULT NULL,
  `photo` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`name`,`email`,`phone`,`place`,`post`,`district`,`pincode`,`photo`) values 
(1,14,'Danish','danishkkoori47@gmail.com',9539548288,'Perinthalmanna ','Thazhekkod ','Palakkad',679341,''),
(2,16,'Danish','danishkkoori47@gmail.com',9539548265,'pmna','Thazhekkod ','Palakkad',679341,''),
(3,19,'Danish','danishkkoori47@gmail.com',9539548288,'Perinthalmanna ','Thazhekkod ','Palakkad',679341,''),
(4,20,'Danish','danishkkoori47@gmail.com',9539548288,'Perinthalmanna ','Thazhekkod ','Palakkad',679341,''),
(5,21,'Danish','danishkkoori47@gmail.com',9539548288,'Perinthalmanna ','Thazhekkod ','Palakkad',679341,''),
(6,22,'Danish','danishkkoori47@gmail.com',9539548288,'Perinthalmanna ','Thazhekkod ','Palakkad',679341,''),
(8,24,'Farsan','farsan@gmail.com',7907349255,'Cherpulassery ','Cherpulassery ','Palakkad',679506,'/static/user/20221208_173042.jpg'),
(10,26,'Farsan','farsan123@gmail.com',7907349255,'Cherpulassery ','Cherpulassery ','Palakkad',678909,'/static/user/20221208_173851.jpg'),
(11,27,'Midlan','midlaj123@gmail.com',6798645798,'palakkad','palakkad','Palakkad',679488,'/static/user/20230402_180157.jpg'),
(12,28,'Midlaj','midlaj123@gmail.com',6798645798,'palakkad','palakkad','Palakkad',679488,'/static/user/20230402_180206.jpg'),
(13,29,'Stn','stn123@gmail.com',6798334567,'palakkad','palakkad','Palakkad',678385,'/static/user/20230406_144542.jpg'),
(14,30,'nivin','nivin123@gmail.com',8736784567,'aluva','aluva','Ernamkulam',879367,'/static/user/20230406_144900.jpg');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
