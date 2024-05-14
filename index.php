<?php
    require_once "models/DataBase.php";
    $prueba = Database::connection();
    require_once "controllers/Users.php";
    $controller = new Users;
    $controller->main();
?>