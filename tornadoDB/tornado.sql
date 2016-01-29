set NAMES utf8;
set FOREIGN_KEY_CHECKS=0;
drop table if exists `authors`;
create table `authors` (
`id` int(11) not NULL AUTO_INCREMENT,
`email` text,
`name` text,
PRIMARY KEY (`id`)
)ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
