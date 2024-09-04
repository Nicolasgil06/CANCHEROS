ALTER TABLE cancheros.reserva ADD COLUMN id_usuario INT;

ALTER TABLE cancheros.reserva ADD CONSTRAINT fk_usuario_reserva FOREIGN KEY (id_usuario) REFERENCES cancheros.usuario(id_usuario);


ALTER TABLE cancheros.usuario ADD COLUMN id_documento INT;
ALTER TABLE cancheros.usuario ADD CONSTRAINT fk_usuario_tipodocumento FOREIGN KEY (id_documento) REFERENCES cancheros.tipo_documento(id_documento);

ADD CONSTRAINT fk_usuario_reserva FOREIGN KEY (id_usuario) REFERENCES cancheros.usuario(id_usuario);

ALTER TABLE cancheros.usuario DROP INDEX id_reserva;
ALTER TABLE cancheros.usuario DROP key  id_reserva;
SHOW CREATE TABLE cancheros.reserva;
SHOW CREATE TABLE cancheros.usuario;

SHOW CREATE TABLE cancheros.cancha_reserva;cancha


DROP KEY AID ;

ALTER TABLE cancheros.usuario DROP FOREIGN KEY FkReservaUser;


SELECT
    CONSTRAINT_NAME,
    TABLE_NAME,
    COLUMN_NAME,
    REFERENCED_TABLE_NAME,
    REFERENCED_COLUMN_NAME
FROM
    INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE
    TABLE_SCHEMA = 'cancheros' AND
    REFERENCED_TABLE_NAME IS NOT NULL AND
    REFERENCED_TABLE_NAME = 'usuario' AND
    COLUMN_NAME = 'id_reserva';
    
    
ALTER TABLE cancheros.reserva DROP FOREIGN KEY id_reserva;

RENAME TABLE cancheros.`tipo _documento` TO tipo_documento;

CREATE TABLE cancheros.tipo_documento (
  `id_documento` int NOT NULL,
  `nombre_tipo_documento` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_documento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

