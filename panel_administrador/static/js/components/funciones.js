function cargarPreguntas(page, size, apiUrl) {
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
                        <a href="${pregunta.url}" class="btn btn-outline-info d-block">
                            <i class="bi bi-pencil"></i> 
                        </a>
                        <a href="#" class="btn btn-outline-danger d-block">
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
