CREATE DATABASE `cancheros` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
SELECT * FROM cancheros.tipo_deporte;

CREATE TABLE `cancha` (
  `id_cancha` int(11) NOT NULL,
  `cancha_zonal` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_cancha`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

CREATE TABLE `cancha_reserva` (
  `id_cancha_reserva` int(11) NOT NULL,
  `id_cancha` int(11) DEFAULT NULL,
  `id_reserva` int(11) NOT NULL,
  PRIMARY KEY (`id_cancha_reserva`),
  KEY `id_cancha_idx` (`id_cancha`),
  KEY `fk_reserva` (`id_reserva`),
  CONSTRAINT `fk_cancha` FOREIGN KEY (`id_cancha`) REFERENCES `cancha` (`id_cancha`),
  CONSTRAINT `fk_reserva` FOREIGN KEY (`id_reserva`) REFERENCES `reserva` (`id_reserva`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

CREATE TABLE `reserva` (
  `id_reserva` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `num_jugadores` int(11) DEFAULT NULL,
  `petos` int(11) DEFAULT NULL,
  `balones` int(11) DEFAULT NULL,
  `id_deporte` int(11) DEFAULT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  `arbitraje` tinyint(1) DEFAULT NULL,
  `color_uniforme` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_reserva`),
  KEY `id_deporte` (`id_deporte`),
  KEY `fkusuarioreserva` (`id_usuario`),
  CONSTRAINT `fkdeoirtereserva` FOREIGN KEY (`id_deporte`) REFERENCES `tipo_deporte` (`id_deporte`),
  CONSTRAINT `fkusuarioreserva` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

CREATE TABLE `rol` (
  `id_rol` int(11) NOT NULL,
  `nombre_rol` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_rol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

CREATE TABLE `tipo_deporte` (
  `id_deporte` int(11) NOT NULL,
  `nombre_deporte` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_deporte`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

CREATE TABLE `tipo_documento` (
  `id_documento` int(11) NOT NULL,
  `nombre_tipo_documento` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_documento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `nombres` varchar(100) DEFAULT NULL,
  `apellidos` varchar(100) DEFAULT NULL,
  `telefono` int(11) DEFAULT NULL,
  `correo` varchar(45) DEFAULT NULL,
  `numero_documento` int(11) DEFAULT NULL,
  `id_rol` int(11) DEFAULT NULL,
  `id_documento` int(11) DEFAULT NULL,
  `clave` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`),
  KEY `id_rol` (`id_rol`),
  KEY `fk_usuario_tipodocumento` (`id_documento`),
  CONSTRAINT `FkRolUser` FOREIGN KEY (`id_rol`) REFERENCES `rol` (`id_rol`),
  CONSTRAINT `fk_usuario_tipodocumento` FOREIGN KEY (`id_documento`) REFERENCES `tipo_documento` (`id_documento`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
















