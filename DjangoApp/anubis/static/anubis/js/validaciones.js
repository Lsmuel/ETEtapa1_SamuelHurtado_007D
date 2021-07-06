function validacion(){
    var rut, nombre, email, fono, fechan,contra, direccion;
    rut = document.getElementById('rut').value;
    nombre= document.getElementById('nombre').value;
    email = document.getElementById('email').value; 
    fono = document.getElementById('fono').value;
    contra = document.getElementById('contra').value;
    direccion =document.getElementById('direccion').value;
   
    var emailR = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i;

    if(rut === ""){
        alert("Ingrese su nombre");
        return false
    }
    if(rut >10){
        alert("Rut invalido");
        return false
    }

    if(nombre === ""){
        alert("Ingrese su nombre");
        return false
    }
    if( email === ""){
        alert("Ingrese su email");
        return false
    }
    if(!emailR.test(email)){
        alert("El correo no es válido");
        return false
    }
    
    if(fono === ""){
        alert("Ingrese su telefono");
        return false
    }
    if(fono.length<9){
        alert("Minimo 9 caracteres");
        return false
    }
    if(fono.length>9){
        alert("Max 9 caracteres");
        return false
    }
    if(isNaN(fono)){
        alert("El teléfono ingresado no es un número");
        return false
    }
    
    if( contra === ""){
        alert("Ingrese contraseña");
        return false  
    }
    if(contra.length<6){
        alert("Minimo 6 caracteres");
        return false
    }
    if( direccion === ""){
        alert("Ingrese su direccion");
        return false
    }
 

}

