$(document).ready(function() {
    $('#enviar-respuesta').click(function() {
        alert('Respuesta enviada'); 
    });
    // Paginación de preguntas
    let currentPage = 1;
    const size = 5;  
    const apiUrl = document.getElementById("config").getAttribute("data-api-url"); 
    // agregar url para reidirigir a la vista de editar pregunta. 
    function cargarPreguntas(page) {
        $.ajax({
            url: apiUrl,
            type: "GET",
            data: { page: page, size: size },
            dataType: "json",
            success: function(response) {
                let preguntasHtml = "";
                response.preguntas.forEach(function(pregunta) {
                    preguntasHtml += `<tr>
                        <td>${pregunta.id}</td>
                        <td>${pregunta.texto}</td>
                        <td>
                            <a href="#" class="btn btn-primary d-block">
                                <i class="bi bi-pencil"></i> 
                            </a>
                            <a href="#" class="btn btn-danger d-block">
                                <i class="bi bi-trash"></i>
                            </a>
                        </td>
                    </tr>`;
                });

                $("#preguntas-lista").html(preguntasHtml);
                $("#page-info").text(`Página ${response.page} de ${response.pages}`);

                $("#prev-btn").prop("disabled", !response.has_previous);
                $("#next-btn").prop("disabled", !response.has_next);

                currentPage = response.page;
            },
            error: function() {
                alert("Error al cargar los datos.");
            }
        });
    }

    $("#prev-btn").click(function() {
        if (currentPage > 1) {
            cargarPreguntas(currentPage - 1);
        }
    });

    $("#next-btn").click(function() {
        cargarPreguntas(currentPage + 1);
    });

    cargarPreguntas(currentPage);

});
