INSERT INTO catalogos.catalogo_sexo ('nombre_largo', 'abreviacion', 'descripcion') VALUES
	('Hombre', 'H', 'Genero masculino'),
	('Mujer', 'M', 'Genero femenino');


INSERT INTO 'catalogo_nivel_educativo' ('nombre_largo', 'abreviacion', 'descripcion') VALUES
	('primaria', 'prim', 'Persona que ha completado o está cursando el nivel educativo de primaria'),
	('secundaria', 'secu', 'Persona que ha completado o está cursando el nivel educativo de secundaria'),
	('preparatoria', 'prepa', 'Persona que ha completado o está cursando el nivel educativo de preparatoria o bachillerato'),
	('universidad', 'univ', 'Persona que ha completado o está cursando estudios universitarios o técnicos'),
	('posgrado', 'posgr', 'Persona que ha completado estudios de nivel posgrado (maestría o doctorado)'),
	('ninguno', 'none', 'Persona que no ha completado ningún nivel educativo formal');


INSERT INTO 'catalogo_estado_civil' ('nombre_largo', 'abreviacion', 'descripcion') VALUES
	('soltero', 'solt', 'Persona no casada que no ha tenido una unión formal'),
	('casado', 'casa', 'Persona unida en matrimonio'),
	('viudo', 'viudo', 'Persona cuya pareja ha fallecido'),
	('unión libre', 'unlib', 'Persona en una relación de convivencia sin matrimonio formal'),
	('separado/divorciado', 'se_di', 'Persona que ha terminado una relación matrimonial o de unión formal');



INSERT INTO 'catalogo_poblacion' ('nombre_largo', 'abreviacion', 'descripcion') VALUES
	('rural', 'rural', 'Persona que reside en una zona o comunidad rural'),
	('urbana', 'urban', 'Persona que reside en una zona o ciudad urbana');

