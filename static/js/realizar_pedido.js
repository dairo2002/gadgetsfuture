// Funcion ocultar boton 
function mostrarDireccionLocal() {
    var txtDireccionLocal = document.getElementById('txtDireccionLocal')
    txtDireccionLocal.style.display = 'block'
}

document.querySelectorAll('input[name="metodoPago"]').forEach(function (radio) {
    radio.addEventListener('change', function () {
        // Ocultar todos los contenidos
        document.getElementById('infoTarjeta').style.display = 'none';
        document.getElementById('infoEfectivo').style.display = 'none';
        document.getElementById('infoTransferencia').style.display = 'none';

        // Mostrar el contenido correspondiente a la opción seleccionada
        if (this.value === 'tarjeta') {
            document.getElementById('infoTarjeta').style.display = 'block';
        } else if (this.value === 'efectivo') {
            document.getElementById('infoEfectivo').style.display = 'block';
        } else if (this.value === 'transferencia') {
            document.getElementById('infoTransferencia').style.display = 'block';
        }
    });
});
