class Respuesta():
    
    def __init__(self, abreviacion_cuestionario, pregunta, respuestas):
        self.abreviacion_cuestionario = abreviacion_cuestionario
        self.pregunta = pregunta
        self.template = pregunta.tipo_respuesta
        self.id_pregunta = pregunta.id
        self.imagen_grupal = pregunta.imagen_grupal
        self.texto_pregunta = pregunta.texto
        self.respuestas = respuestas

    def get_pregunta(self):
        return {
            'id_pregunta' : self.id_pregunta
            ,'cuestionario' : self.abreviacion_cuestionario
            ,'template' : self.template
            ,'texto_pregunta' : self.texto_pregunta
            ,'imagen_grupal' : self.imagen_grupal
            ,'respuestas' : self.repsuesta_list()
        }
    
    def repsuesta_list(self):
        respuestas = []
        dictRespuesta = {}
        
        if self.template == 1:
            for respuesta in self.respuestas['respuestas']():
                respuestas.append({
                    'id_respuesta' : respuesta.id
                    ,'texto_respuesta' : respuesta.nombre_largo
                })
            
            return respuestas
        else:
            if not self.imagen_grupal:

                for respuesta, imagen in zip(self.respuestas['respuestas'](), self.pregunta.imagenes_preguntas.all()):
                    respuestas.append(
                        {
                            'id_respuesta' : respuesta.id
                            ,'texto_respuesta' : respuesta.nombre_largo
                            ,'url_imagen' : imagen.url
                        }
                    )
                dictRespuesta['respuestas'] = respuestas
                                        
                return dictRespuesta
            else:
                for imagen in self.pregunta.imagenes_preguntas.all():
                    dictRespuesta['imagen'] = imagen.url
                
                for respuesta in self.respuestas['respuestas']():
                    respuestas.append({
                        'id_respuesta' : respuesta.id
                        ,'texto_respuesta' : respuesta.nombre_largo
                    })
                
                dictRespuesta['respuestas'] = respuestas    

                return dictRespuesta