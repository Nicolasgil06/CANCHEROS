<?php
require_once "models/User.php";
class Users{
    public function main(){

        // Objeto01 Rol
        $rol = new User;
        $rol->setRolCode("01");
        echo "Código Rol: ", $rol->getRolCode(), "<hr>";
        $rol->setRolName("admin");
        echo "Nombre Rol: ", $rol->getRolName(), "<hr>";

        // Objeto02 Usuario
        $user = new User;
        $user->setUserCode("user_123");
        echo "Código Usuario: ", $user->getUserCode(), "<hr>";
        $user->setUserName("Pepito");
        echo "Nombre Usuario: ", $user->getUserName(), "<hr>";
        $user->setUserLastName("Perez");
        echo "Apellido Usuario: ", $user->getUserLastName(), "<hr>";
        $user->setUserId(123456789);
        echo "Identificación Usuario: ", $user->getUserId(), "<hr>";
        $user->setUserEmail("pepito@perez.com");
        echo "Correo Usuario: ", $user->getUserEmail(), "<hr>";
        $user->setUserPass(12345);
        echo "Contraseña Usuario: ", $user->getUserPass(), "<hr>";
        $user->setUserState(True);
        echo "Estado Usuario: ", $user->getUserState(), "<hr>";
        echo "<hr>";

        // Objeto03 Constructor 09 Parámetros
        $userconst = new User(
            "02",
            "customer",
            "user_567",
            "Marinita",
            "García",
            "987654321",
            "marinita@garcia.com",
            sha1("12345"),
            True
        );
        print_r($userconst);
        echo "<hr>";

        // Objeto04 Constructor 02 Parámetros
        $user_login = new User("rodrigo@lara.com",md5("12345"));
        print_r($user_login);
        echo "<hr>";

    }
}
?>