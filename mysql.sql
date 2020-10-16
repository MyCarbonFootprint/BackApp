-- Adminer 4.7.7 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

USE `myfingerprint`;

DROP TABLE IF EXISTS `action`;
CREATE TABLE `action` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(254) NOT NULL,
  `description` varchar(2047) NOT NULL,
  `unit` varchar(254) NOT NULL,
  `number` int(11) NOT NULL,
  `impact` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4;

INSERT INTO `action` (`id`, `name`, `description`, `unit`, `number`, `impact`) VALUES
(1,	'Achat sur internet en livraison ',	'Moyenne de l\'impact de la livraison d\'un colis ', 'count', '1',	738),
(2,	'Regarder Netflix',	'Visionnage pendant 30 minutes de contenu Netflix',	'minute', '30',	50),
(3,	'Trajet en voiture Essence',	'équivalent de l\'émission de CO2 par kilomètre en voiture essence pour une seule personne', 'km', '1', 153),
(4,	'Trajet en voiture Gazole',	'équivalent de l\'émission de CO2 par kilomètre en voiture Gazole pour une seule personne',	'km', '1', 145),
(5,	'Trajet en voiture GPL',	'équivalent de l\'émission de CO2 par kilomètre en voiture GPL pour une seule personne',	'km', '1', 133),
(6,	'Trajet en train',	'équivalent de l\'émission de CO2 par kilomètre en train pour une seule personne',	'km', '1', 6),
(7,	'Trajet en avion',	'équivalent de l\'émission de CO2 par kilomètre en avion pour une seule personne',	'km', '1', 146),
(8,	'Trajet à pied ou à vélo',	'',	'km', '1', 0),
(9,	'Lavage au lave-vaisselle à 55°C',	'Un cycle de lave-vaiselle à 55°C',	'count', '1', 770),
(10,	'Lavage au lave-vaisselle à 65°C',	'Un cycle de lave-vaiselle à 65°C',	'count', '1',	990),
(11,	'Lavage vaiselle à la main avec eau-forte et chaude',	'Lavage de la vaisselle à l\'eau chaude et en écoulement prolongé (équivalent d\'un lave-vaiselle rempli)',	'count', '1', 6000),
(12,	'Lavage vaiselle à la main avec eau tiède',	'Lavage de la vaisselle à l\'eau tiède (équivalent d\'un lave-vaiselle rempli)',	'count', '1', 540),
(13,	'Lavage vaiselle à la main avec eau froide',	'Lavage de la vaisselle à l\'eau froide (équivalent d\'un lave-vaiselle rempli)',	'count', '1', 0),
(14,	'Envoi email sans pièce jointe',	'Impact du stockage de l\'email partout dans le monde',	'count', '1',	4),
(15,	'Envoi email avec une pièce jointe',	'Impact du stockage de l\'email partout dans le monde',	'count', '1',	30);

-- 2020-10-10 20:41:02
