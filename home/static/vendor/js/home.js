$(document).ready(function (){
    $('.btn-outline-primary').click(function(){
        if(confirm("¿Seguro que quieres continuar?. Se perderá todo el progreso que realizaste"))
            window.location.href = $(this).attr('href');
    });
});