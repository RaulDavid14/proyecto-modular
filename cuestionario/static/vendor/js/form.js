let isSubmitting = false;
let isNavigating = false;

document.getElementById('formulario').addEventListener('submit', function() {
    isSubmitting = true;
});

document.getElementById('anterior').addEventListener('click', function() {
    isNavigating = true;
});

window.addEventListener('beforeunload', function (e) {
    if (isSubmitting || isNavigating) {
        return;
    }

    var mensaje = "¿Estás seguro de que deseas salir del formulario?";
    e.returnValue = mensaje;
    return mensaje;
});
