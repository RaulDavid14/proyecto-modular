$(document).ready(function() {
    let currentPage = 1;
    const size = 5;  
    const apiUrl = document.getElementById("config").getAttribute("data-api-url"); 
    
    $("#prev-btn").click(function() {
        if (currentPage > 1) {
            cargarPreguntas(currentPage - 1, size, apiUrl);
        }
    });

    $("#next-btn").click(function() {
        cargarPreguntas(currentPage + 1, size, apiUrl);
    });

    cargarPreguntas(currentPage, size, apiUrl);
});
