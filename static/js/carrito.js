function disminuirCantidad() {
    let inputCantidad = document.getElementById("inputCantidad")
    // Decrementar el valor del input de tipo number
    inputCantidad.stepDown()
}

function aumentarCantidad() {
    let inputCantidad = document.getElementById("inputCantidad")
    // Incrementar el valor del input de tipo number
    inputCantidad.stepUp()
}

// La función DOMContentLoaded es un evento en JavaScript que se dispara cuando el DOM de una página web ha sido completamente cargado y parseado
document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('disminuir').addEventListener('click', disminuirCantidad);
    document.getElementById('aumentar').addEventListener('click', aumentarCantidad);
});

