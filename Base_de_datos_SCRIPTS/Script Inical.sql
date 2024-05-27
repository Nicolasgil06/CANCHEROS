CREATE SCHEMA IF NOT EXISTS `cancheros` DEFAULT CHARACTER SET utf8 ;
USE `cancheros` ;

-- -----------------------------------------------------
-- Table `cancheros`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cancheros`.`Usuario` (
  `id_usuario` INT NOT NULL,
  `nombre_apellido` VARCHAR(45) NULL,
  `telefono` INT NULL,
  `correo` VARCHAR(45) NULL,
  `id_documento` INT NULL,
  `numero_documento` INT NULL,
  `id_rol` INT NULL,
  `id_reserva` INT NULL,
  PRIMARY KEY (`id_usuario`),
  INDEX `id_documento` (`id_documento` ASC) INVISIBLE,
  INDEX `id_rol` (`id_rol` ASC) INVISIBLE,
  INDEX `id_reserva` (`id_reserva` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cancheros`.`Rol`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cancheros`.`Rol` (
  `id_rol` INT NOT NULL,
  `nombre_rol` VARCHAR(45) NULL,
  PRIMARY KEY (`id_rol`),
  CONSTRAINT `id_rol`
    FOREIGN KEY (`id_rol`)
    REFERENCES `cancheros`.`Usuario` (`id_rol`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cancheros`.`Cancha`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cancheros`.`Cancha` (
  `id_cancha` INT NOT NULL,
  `cancha_zonal` VARCHAR(45) NULL,
  PRIMARY KEY (`id_cancha`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cancheros`.`Reserva`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cancheros`.`Reserva` (
  `id_reserva` INT NOT NULL,
  `fecha` DATE NULL,
  `hora` DATETIME NULL,
  `num_jugadores` INT NULL,
  `petos` INT NULL,
  `balones` INT NULL,
  `id_usuario` INT NULL,
  `id_deporte` INT NULL,
  PRIMARY KEY (`id_reserva`),
  INDEX `id_deporte` (`id_deporte` ASC) VISIBLE,
  CONSTRAINT `id_reserva`
    FOREIGN KEY (`id_reserva`)
    REFERENCES `cancheros`.`Usuario` (`id_reserva`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cancheros`.`cancha_reserva`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cancheros`.`cancha_reserva` (
  `id_cancha_reserva` INT NOT NULL,
  `id_reserva` INT NULL,
  `id_cancha` INT NULL,
  PRIMARY KEY (`id_cancha_reserva`),
  INDEX `id_cancha_idx` (`id_cancha` ASC) VISIBLE,
  CONSTRAINT `fk_reserva`
    FOREIGN KEY (`id_reserva`)
    REFERENCES `cancheros`.`Reserva` (`id_reserva`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cancha`
    FOREIGN KEY (`id_cancha`)
    REFERENCES `cancheros`.`Cancha` (`id_cancha`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cancheros`.`tipo _documento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cancheros`.`tipo _documento` (
  `id_documento` INT NOT NULL,
  `nombre_tipo_documento` VARCHAR(45) NULL,
  PRIMARY KEY (`id_documento`),
  CONSTRAINT `id_documento`
    FOREIGN KEY (`id_documento`)
    REFERENCES `cancheros`.`Usuario` (`id_documento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cancheros`.`tipo_deporte`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cancheros`.`tipo_deporte` (
  `id_deporte` INT NOT NULL,
  `nombre_deporte` VARCHAR(45) NULL,
  PRIMARY KEY (`id_deporte`),
  CONSTRAINT `id_deporte`
    FOREIGN KEY (`id_deporte`)
    REFERENCES `cancheros`.`Reserva` (`id_deporte`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
