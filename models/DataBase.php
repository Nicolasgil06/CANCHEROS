<?php
    class DataBase{
        #  Conexión Local
        public static function connection(){
            $hostname = "localhost";
            $port = "3306";
            $database = "db_tps_nc_iv_2771440";
            $username = "root";
            $password = "";
			$pdo = new PDO("mysql:host=$hostname;port=$port;dbname=$database;charset=utf8",$username,$password);
			$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
			return $pdo;
		}
	}
?>