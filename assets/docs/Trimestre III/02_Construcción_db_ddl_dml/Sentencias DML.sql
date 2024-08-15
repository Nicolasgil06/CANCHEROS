INSERT INTO `cancheros`.`cancha`
VALUES
(`id_cancha`,
`cancha_zonal`);


INSERT INTO `cancheros`.`cancha_reserva`
VALUES
(`id_cancha_reserva`,
`id_cancha`,
`id_reserva`);


INSERT INTO `cancheros`.`reserva`
VALUES
(`id_reserva`,
`fecha`,
`hora`,
`num_jugadores`,
`petos`,
`balones`,
`id_deporte`,
`id_usuario`,
`arbitraje`,
`color_uniforme`);

INSERT INTO `cancheros`.`rol`
VALUES
(`id_rol`,
`nombre_rol`);

INSERT INTO `cancheros`.`tipo_deporte`
VALUES
(`id_deporte`,
`nombre_deporte`);

INSERT INTO `cancheros`.`tipo_documento`
VALUES
(`id_documento`,
`nombre_tipo_documento`);

INSERT INTO `cancheros`.`usuario`
VALUES
(`id_usuario`,
`nombres`,
`apellidos`,
`telefono`,
`correo`,
`numero_documento`,
`id_rol`,
`id_documento`,
`clave`);

SELECT `cancha`.`id_cancha`,
    `cancha`.`cancha_zonal`
FROM `cancheros`.`cancha`;

SELECT `cancha_reserva`.`id_cancha_reserva`,
    `cancha_reserva`.`id_cancha`,
    `cancha_reserva`.`id_reserva`
FROM `cancheros`.`cancha_reserva`;

SELECT `reserva`.`id_reserva`,
    `reserva`.`fecha`,
    `reserva`.`hora`,
    `reserva`.`num_jugadores`,
    `reserva`.`petos`,
    `reserva`.`balones`,
    `reserva`.`id_deporte`,
    `reserva`.`id_usuario`,
    `reserva`.`arbitraje`,
    `reserva`.`color_uniforme`
FROM `cancheros`.`reserva`;

SELECT `rol`.`id_rol`,
    `rol`.`nombre_rol`
FROM `cancheros`.`rol`;

SELECT `tipo_deporte`.`id_deporte`,
    `tipo_deporte`.`nombre_deporte`
FROM `cancheros`.`tipo_deporte`;

SELECT `tipo_documento`.`id_documento`,
    `tipo_documento`.`nombre_tipo_documento`
FROM `cancheros`.`tipo_documento`;

SELECT `usuario`.`id_usuario`,
    `usuario`.`nombres`,
    `usuario`.`apellidos`,
    `usuario`.`telefono`,
    `usuario`.`correo`,
    `usuario`.`numero_documento`,
    `usuario`.`id_rol`,
    `usuario`.`id_documento`,
    `usuario`.`clave`
FROM `cancheros`.`usuario`;

SELECT nombres, fecha
FROM usuario
INNER JOIN reserva
ON usuario.id_usuario = reserva.id_usuario

SELECT nombres, nombre_deporte, nombre_rol, nombre_tipo_documento
FROM reserva
INNER JOIN usuario ON reserva.id_usuario = usuario.id_usuario
INNER JOIN tipo_deporte ON reserva.id_deporte = tipo_deporte.id_deporte
INNER JOIN rol ON usuario.id_rol = rol.id_rol
INNER JOIN tipo_documento ON usuario.id_documento = tipo_documento.id_documento;

SELECT nombres, fecha
FROM usuario
RIGHT JOIN reserva
ON usuario.id_usuario = reserva.id_usuario

SELECT *
FROM reserva
WHERE id_usuario = 1;
