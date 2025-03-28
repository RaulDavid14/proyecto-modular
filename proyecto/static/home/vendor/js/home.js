$(document).ready(function (){
    $('.btn-outline-primary').click(function(event){
        if(!confirm("¿Seguro que quieres continuar?. Se perderá todo el progreso que realizaste"))
        {
            event.preventDefault();
        }
    });
});