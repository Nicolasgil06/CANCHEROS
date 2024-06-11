-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-04-2024 a las 03:55:22
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `cancheros`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `canchas`
--

CREATE TABLE `canchas` (
  `id_canchas` varchar(1) NOT NULL,
  `nombre_canchas` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `canchas`
--

INSERT INTO `canchas` (`id_canchas`, `nombre_canchas`) VALUES
('1', 'Cancha_zonal_1'),
('2', 'Cancha_zonal_2');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `horarios`
--

CREATE TABLE `horarios` (
  `Id_Horarios` varchar(20) NOT NULL,
  `Hora` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `horarios`
--

INSERT INTO `horarios` (`Id_Horarios`, `Hora`) VALUES
('1', '7-8'),
('10', '4-5'),
('11', '5-6'),
('12', '6-7'),
('13', '7-8'),
('14', '8-9'),
('15', '9-10'),
('2', '8-9'),
('3', '9-10'),
('4', '10-11'),
('5', '11-12'),
('6', '12-1'),
('7', '1-2'),
('8', '2-3'),
('9', '3-4');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservas`
--

CREATE TABLE `reservas` (
  `Id_Reserva` int(11) NOT NULL,
  `Fecha` varchar(20) DEFAULT NULL,
  `Hora` varchar(5) DEFAULT NULL,
  `Num_Usuarios` varchar(10) DEFAULT NULL,
  `Tipo_deporte` varchar(15) DEFAULT NULL,
  `Petos` varchar(10) DEFAULT NULL,
  `Balones` varchar(10) DEFAULT NULL,
  `Id_canchas` varchar(1) DEFAULT NULL,
  `Id_Usuario` varchar(20) DEFAULT NULL,
  `Id_Horarios` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `reservas`
--

INSERT INTO `reservas` (`Id_Reserva`, `Fecha`, `Hora`, `Num_Usuarios`, `Tipo_deporte`, `Petos`, `Balones`, `Id_canchas`, `Id_Usuario`, `Id_Horarios`) VALUES
(1, '15/04/2024', '7-8 ', '15', 'Rugby', '6', '3', '1', '1', '1'),
(2, '15/04/2024', '8-9 ', '18', 'Futbol', '15', '1', '2', '2', '2'),
(3, '16/04/2024', '9-10 ', '21', 'Futbol', '12', '4', '2', '3', '3'),
(4, '17/04/2024', '10-11', '19', 'Rugby', '8', '2', '1', '1', '4'),
(5, '18/04/2024', '11-12', '22', 'Rugby', '14', '1', '2', '3', '5'),
(6, '18/04/2024', '12-1 ', '14', 'Futbol', '11', '2', '1', '2', '6'),
(7, '19/04/2024', '8-9 ', '19', 'Futbol', '17', '1', '2', '2', '2');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol`
--

CREATE TABLE `rol` (
  `id_rol` varchar(20) NOT NULL,
  `nombre_rol` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `rol`
--

INSERT INTO `rol` (`id_rol`, `nombre_rol`) VALUES
('1', 'usuario'),
('2', 'administrador');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_id`
--

CREATE TABLE `tipo_id` (
  `Id_Tipo_Documento` varchar(20) NOT NULL,
  `nombre_tipodedocumento` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tipo_id`
--

INSERT INTO `tipo_id` (`Id_Tipo_Documento`, `nombre_tipodedocumento`) VALUES
('1', 'Cedula_de_ciudadania'),
('2', 'Tarjeta_de_identidad'),
('3', 'Nit');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id_usuario` varchar(20) NOT NULL,
  `Nombres_y_Apellidos` varchar(20) DEFAULT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `correo` varchar(20) DEFAULT NULL,
  `Numero_Documento` varchar(20) DEFAULT NULL,
  `Id_Rol` varchar(20) DEFAULT NULL,
  `Id_Tipo_Documento` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id_usuario`, `Nombres_y_Apellidos`, `telefono`, `correo`, `Numero_Documento`, `Id_Rol`, `Id_Tipo_Documento`) VALUES
('1', 'carlos_cardona', '3245566776', 'carlospg@gmail.com', '1023344544', '2', '1'),
('2', 'Andrea_Vargas', '3123455776', 'andreavv@gmail.com', '1023321544', '2', '2'),
('3', 'jacobo_contreras', '3003455778', 'andreavv@gmail.com', '1023321678', '2', '1'),
('4', 'Daniel_Santorini', '3214339987', 'dani.santorini@gmail', '9-1014245532', '2', '3');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `canchas`
--
ALTER TABLE `canchas`
  ADD PRIMARY KEY (`id_canchas`);

--
-- Indices de la tabla `horarios`
--
ALTER TABLE `horarios`
  ADD PRIMARY KEY (`Id_Horarios`);

--
-- Indices de la tabla `reservas`
--
ALTER TABLE `reservas`
  ADD PRIMARY KEY (`Id_Reserva`),
  ADD KEY `Id_canchas` (`Id_canchas`),
  ADD KEY `Id_Horarios` (`Id_Horarios`),
  ADD KEY `Id_Usuario` (`Id_Usuario`);

--
-- Indices de la tabla `rol`
--
ALTER TABLE `rol`
  ADD PRIMARY KEY (`id_rol`);

--
-- Indices de la tabla `tipo_id`
--
ALTER TABLE `tipo_id`
  ADD PRIMARY KEY (`Id_Tipo_Documento`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id_usuario`),
  ADD KEY `Id_Rol` (`Id_Rol`),
  ADD KEY `Id_Tipo_Documento` (`Id_Tipo_Documento`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `reservas`
--
ALTER TABLE `reservas`
  MODIFY `Id_Reserva` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `reservas`
--
ALTER TABLE `reservas`
  ADD CONSTRAINT `reservas_ibfk_1` FOREIGN KEY (`Id_canchas`) REFERENCES `canchas` (`id_canchas`),
  ADD CONSTRAINT `reservas_ibfk_2` FOREIGN KEY (`Id_Horarios`) REFERENCES `horarios` (`Id_Horarios`),
  ADD CONSTRAINT `reservas_ibfk_3` FOREIGN KEY (`Id_Usuario`) REFERENCES `usuarios` (`id_usuario`);

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`Id_Rol`) REFERENCES `rol` (`id_rol`),
  ADD CONSTRAINT `usuarios_ibfk_2` FOREIGN KEY (`Id_Tipo_Documento`) REFERENCES `tipo_id` (`id_tipo_documento`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
