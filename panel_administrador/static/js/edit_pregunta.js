$(document).ready(function() {
    $('#tipo-pregunta').change(function() {
        if ($(this).val() == '2') {
            $('#imagenes').show();
            
        } 
        else {
            $('#imagenes').hide();
        }
    });
});