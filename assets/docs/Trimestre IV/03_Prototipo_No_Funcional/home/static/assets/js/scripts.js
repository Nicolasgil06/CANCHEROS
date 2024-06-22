function mostrarFormulario(tipo) {
        // Ocultar todos los formularios
        document.getElementById('formulario-persona-natural').style.display = 'none';
        document.getElementById('formulario-persona-juridica').style.display = 'none';

        // Mostrar el formulario correspondiente al tipo seleccionado
        document.getElementById('formulario-' + tipo).style.display = 'block';
    }
    function guardarVariables(idFormulario) {
        var futbol = document.getElementById("futbol").value;
        var rugby = document.getElementById("rugby").value;
        var si = document.getElementById("si").value;
        var no = document.getElementById("no").value;
        var integrantes = document.getElementById("integrantes").value;
        var colorUniforme = document.getElementById("colorUniforme").value;
        var fechaAlquiler = document.getElementById("fechaAlquiler").value;
        var horaAlquiler = document.getElementById("horaAlquiler").value;            
        var canchaseleccionada = document.getElementById("Cancha").value;

        if (validarCampos(idFormulario)) {

            localStorage.setItem("futbol", futbol);
            localStorage.setItem("rugby", rugby);
            localStorage.setItem("si", si);
            localStorage.setItem("no", no);
            localStorage.setItem("integrantes", integrantes);
            localStorage.setItem("colorUniforme", colorUniforme);
            localStorage.setItem("fechaAlquiler", fechaAlquiler);
            localStorage.setItem("horaAlquiler", horaAlquiler);
            localStorage.setItem("canchaseleccionada", canchaseleccionada);
            window.location.href = "formulario3.html";

        } else {

            swal ( "Oops" ,  "Faltan campos por llenar!" ,  "error" )
            <!-- alert("Por favor, complete todos los campos correctamente."); -->

        }

        function validarCampos(idFormulario) {
            // Aquí puedes implementar la lógica de validación de campos según tus requisitos
            // Por ejemplo, puedes verificar que todos los campos requeridos estén completos
            var formulario = document.getElementById(idFormulario);
            var campos = formulario.getElementsByTagName("input");
            for (var i = 0; i < campos.length; i++) {
                if (campos[i].hasAttribute("required") && campos[i].value.trim() === "") {
                    return false;
                }
            }
            // Si todos los campos requeridos están completos, devolver true
            return true;
        }
        
    }


    function irReserva() {
        window.location.href = "{% url 'reserva' %}";
    }
    function irConsulta() {
        window.location.href = "consultaReserva.html";
    }
    function irCancelar() {
        window.location.href = "cancelarReserva.html";
    }

    // Llenar los campos ocultos con los valores almacenados en localStorage
    document.getElementById("nombre").value = localStorage.getItem("nombre");
    document.getElementById("edad").value = localStorage.getItem("edad");
    document.getElementById("phone").value = localStorage.getItem("phone");
    document.getElementById("email").value = localStorage.getItem("email");
    document.getElementById("doc").value = localStorage.getItem("doc");
    document.getElementById("pass").value = localStorage.getItem("pass");
    document.getElementById("rs").value = localStorage.getItem("rs");
    document.getElementById("phone2").value = localStorage.getItem("phone2");
    document.getElementById("email2").value = localStorage.getItem("email2");
    document.getElementById("pass2").value = localStorage.getItem("pass2");
    document.getElementById("nit").value = localStorage.getItem("nit");
    document.getElementById("deporte").value = localStorage.getItem("deporte");
    document.getElementById("integrantes").value = localStorage.getItem("integrantes");
    document.getElementById("arbibraje").value = localStorage.getItem("arbibraje");
    document.getElementById("colorUniforme").value = localStorage.getItem("colorUniforme");
    document.getElementById("fechaAlquiler").value = localStorage.getItem("fechaAlquiler");
    document.getElementById("horaAlquiler").value = localStorage.getItem("horaAlquiler");
    document.getElementById("canchaseleccionada").value = localStorage.getItem("canchaseleccionada");
    
    // Puedes llenar más campos ocultos si es necesario

    // Borrar los datos de localStorage después de enviar el formulario
    document.getElementById("formularioFinal").addEventListener("submit", function() {
      localStorage.clear();
    });