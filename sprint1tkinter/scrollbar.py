import tkinter as tk

root = tk.Tk()
root.title("Ejercicio 10 - Scrollbar")
root.geometry("400x300")

texto = tk.Text(root, wrap="word")
texto.pack(side="left", fill="both", expand=True)

scroll = tk.Scrollbar(root, command=texto.yview)
scroll.pack(side="right", fill="y")

texto.config(yscrollcommand=scroll.set)

texto.insert("1.0", """LIONEL ANDRÉS MESSI CUCCITTINI:

Lionel Andrés Messi Cuccittini (Rosario, 24 de junio de 1987), conocido como Leo Messi, es un futbolista argentino que juega como delantero o centrocampista. Desde 2023, integra el plantel del Inter Miami de la MLS canadoestadounidense. Es también internacional con la selección de Argentina, de la que es capitán.

Con el Fútbol Club Barcelona, al que estuvo ligado más de veinte años, ganó 35 títulos, entre ellos,diez de La Liga, cuatro de la Liga de Campeones de la UEFA y siete de la Copa del Rey.

Considerado con frecuencia el mejor jugador del mundo y uno de los mejores de todos los tiempos,[10]​ es el único en la historia que ha ganado, entre otras distinciones, ocho veces el Balón de Oro, ocho premios de la FIFA al mejor jugador del mundo, seis Botas de Oro y dos Balones de Oro de la Copa Mundial de Fútbol. En 2020, se convirtió en el primer futbolista y el primer argentino en recibir un premio Laureus y fue incluido en el Dream Team del Balón de Oro.

Tiene, entre otros, los récords por más goles en una temporada,[11]​ en un mismo club y en un año calendario. Es, además, el máximo goleador histórico del Barcelona y de la selección argentina, de La Liga, la Supercopa de España, la Supercopa de Europa y el jugador no europeo con más goles en la Liga de Campeones de la UEFA.

Nacido y criado en la ciudad de Rosario, a los 13 años se radicó en España, donde el Barcelona accedió a pagar el tratamiento de la enfermedad hormonal que le habían diagnosticado de niño. Después de una rápida progresión por la Academia juvenil del Barcelona, hizo su debut oficial con el primer equipo en octubre de 2004, a los diecisiete años. A pesar de haber sido propenso a lesiones en los inicios de su carrera, ya en 2006 se estableció como jugador fundamental para el club. Su primera temporada ininterrumpida fue la 2008-09, en la que el Barcelona alcanzó el primer triplete del fútbol español. Por su estilo de juego de pequeño driblador zurdo,[12]​ pronto se lo comparó con su compatriota Diego Maradona quien, en 2007, lo declaró su «sucesor».

En 2009, a los veintidós años, ganó su primer Balón de Oro y el premio al Jugador Mundial de la FIFA del año. Siguieron tres temporadas exitosas, en las que ganó cuatro Balones de Oro de forma consecutiva, hecho que no tenía precedentes. Hasta el momento, su mejor campaña personal fue en 2011-12, cuando estableció el récord de más goles en una temporada, tanto en La Liga como en otras competiciones europeas. Durante las dos siguientes temporadas, también sufrió lesiones y, en 2014, perdió el Balón de Oro frente a Cristiano Ronaldo, a quien se considera su rival. Recuperó su mejor forma durante la campaña 2014-15, en la que superó los registros de máximo goleador absoluto en La Liga y la Liga de Campeones y logró con el Barcelona un histórico segundo triplete, además de ganar su quinto Balón de Oro. Volvería a ganarlo en 2019, 2021 y 2023.

Como internacional argentino, ha representado a su país en catorce torneos mayores. A nivel juvenil, en 2005 participó con la selección sub-20 en el Sudamericano de Colombia y ganó la Copa Mundial de Países Bajos, torneo en el que finalizó como mejor jugador y máximo goleador y, con la sub-23, recibió la medalla de oro en los Juegos Olímpicos de 2008. Después de debutar en la selección mayor en agosto de 2005, en el Mundial de Alemania 2006 se convirtió en el argentino más joven en jugar y en marcar en un mundial. Al año siguiente, en la Copa América, fue nombrado mejor jugador joven del torneo. Como capitán desde agosto de 2011, llegó con su equipo a las finales del Mundial de Brasil 2014, de la Copa América 2015 y de la Copa América Centenario, además de ganar la Copa América 2021 ante Brasil en el Maracaná, la Finalissima 2022 frente a Italia en Wembley, el Mundial de Catar 2022 contra Francia en el estadio Lusail y la Copa América 2024 ante Colombia en el Hard Rock Stadium.

Orígenes y formación

Casa de la infancia de Messi en Rosario
Lionel Andrés Messi nació el 24 de junio de 1987 en el Hospital Italiano Garibaldi de la ciudad de Rosario, en la provincia de Santa Fe. Es el tercer hijo de Jorge Horacio Messi y Celia María Cuccittini. Tiene dos hermanos mayores, Rodrigo y Matías, y una hermana menor, María Sol.[13]​ Su familia paterna es originaria del municipio italiano de Recanati, de donde su bisabuelo, Angelo Messi, emigró a Argentina en 1883.[14]​ Fue su abuela materna, Celia, la que lo alentó a dedicarse al fútbol, por lo que él le agradece señalando al cielo con las dos manos tras convertir un gol.[13]​[15]​ Dos de sus primos (Maximiliano y Emanuel Biancucchi) son también futbolistas.[13]​ Estudió en la escuela primaria N° 66 "Gral. Las Heras".[13]​

Con apenas cuatro años, comenzó a practicar fútbol con Salvador Aparicio en el club Abanderado Grandoli, ubicado en el barrio Grandoli, a pocas cuadras de su casa.[13]​[16]​ En 1994, empezó a entrenarse en las divisiones inferiores de Newell's Old Boys.[13]​ En 1995, jugó un torneo no oficial con Central Córdoba.[17]​

A la edad de ocho años, le diagnosticaron una deficiencia de la hormona de crecimiento,[18]​ por lo que debió hacer un tratamiento de 900 dólares mensuales que, durante un año y medio, cubrieron su obra social y Acindar, siderúrgica en la que trabajaba su padre.[13]​

En 1999, quiso ficharlo el equipo italiano Como, pero finalmente no lo hizo por las dificultades que representaba la mudanza de la familia.[19]​ Al año siguiente, dio su primera entrevista a un medio de comunicación en el suplemento "Pasión Rojinegra" del diario La Capital de Rosario, publicada el 3 de septiembre. A los trece años, tras haber sido reclutado por Federico Vairo en Rosario, fue a Buenos Aires a probarse a River Plate. Eduardo Abrahamian, encargado de las divisiones infantiles del club, pidió su incorporación, pero esta nunca se concretó.[20]​ El jugador dio su versión de por qué no lo aceptaron en una entrevista a Fox Sports Radio el 31 de mayo de 2019:

Yo estaba en Newell's y fui a probarme a la escuela de River, en Rosario. Uno de los chicos que iba me dijo de ir y dije que sí. Después me trajeron a Buenos Aires. Eran categoría 85, todos más grandes. Yo jugué quince o veinte minutos. Me dijeron que vuelva en diez días con mi categoría. Volví e hice tres o cuatro goles y me dijeron que me tenía que quedar, que tenía que llevar el pase. Se iban a hacer cargo del tratamiento. Newell's nunca me bancó en ese sentido, nunca me lo pagó (...) En River me dijeron que llevara el pase, y cuando fui a Newell's me sacaron cagando. Peleamos y peleamos pero el pase nunca me lo dieron. Nunca me dieron el pase. Después salió todo lo del Barcelona.[20]​
Dos ojeadores de Buenos Aires, enterados de su paso por River, se pusieron en contacto con su socio en Barcelona, Horacio Gaggioli, quien a su vez se comunicó con el agente Josep María Minguella. Minguella decidió llamar a Carles Rexach para pedirle que lo probaran.[21]​

El 17 de septiembre de 2000, Messi llegó con su padre a El Prat, el aeropuerto de Barcelona, donde los esperaba Gaggioli para llevarlos al hotel, justo delante del Camp Nou.[22]​ Joaquín Rifé, entrenador de juveniles, lo citó para un entrenamiento con niños de su categoría, entre los que estaban Cesc Fábregas y Gerard Piqué.[23]​ En uno de esos entrenamientos, que se prolongaron dos semanas,[19]​ marcó seis goles y, según Joan Lacueva, ejecutivo responsable del fútbol base del club, "a la media parte tuvieron que cambiarle de equipo para equilibrar el amistoso".[22]​ Sin embargo, el club seguía sin contratarlo, porque esperaban el regreso de Rexach de los Juegos Olímpicos de Sídney. A su vuelta, se organizó una prueba el 2 de octubre en el campo 3,[23]​ y cuando Rexach lo vio jugar, resolvió la situación: «Llegué con el partido empezado y no me dio tiempo a sentarme. Tenía claro que, si no le fichábamos, nos arrepentiríamos», recordó años después.[21]​

Era muy bajito, casi no hablaba y nadie podía imaginar la que nos iba a liar.
—Gerard Piqué, uno de los compañeros de Messi en La Masia.[22]​
A pesar de que algunos técnicos no aprobaban su contratación,[24]​ el 14 de diciembre Rexach se reunió en el restaurante del Club Tenis Pompeia con Gaggioli y Minguella y redactó un principio de acuerdo sobre una servilleta de papel, en el que se comprometía a su fichaje y firmaron todas las partes implicadas.[21]​

En Barcelona, a 14 de diciembre del 2000 y en presencia de los Sres. Minguella y Horacio (Gaggioli), Carles Rexach, secretario técnico del F.C.B., se compromete bajo su responsabilidad y a pesar de algunas opiniones en contra a fichar al jugador Lionel Messi siempre y cuando nos mantengamos en las cantidades acordadas.
Texto de la servilleta, conservada en el Museo del Fútbol Club Barcelona.
Finalmente, el 8 de enero de 2001, firmaron un documento en el que se aseguraban un trabajo para el padre de Messi en el fútbol base (como forma de encubrir el fichaje del adolescente) y el pago del tratamiento hormonal.[25]​ Al mes siguiente, la familia se instaló en Barcelona, primero en un hotel y luego en un departamento en Les Corts. La madre y los hermanos regresaron a Rosario poco después.[26]​[27]​

Categorías inferiores
Newell's Old Boys (1994-1999)
Messi jugó en las inferiores de Newell's entre 1994 y 1999.[28]​ Integraba la categoría 1987, conocida como "La Máquina '87", dirigida por Ernesto Vecchio.[29]​ Debutó ante Pablo VI el 9 de abril, en un encuentro que Newell's ganó 6-0 con cuatro tantos suyos.[28]​ El club recibió, entre otros títulos, la Copa de la Amistad de Perú en 1997, después de convertirle diez goles (nueve de Messi) al Callao,[30]​ y en 1998 ganó el torneo Ciudad de Balcarce, en la provincia de Buenos Aires, en el que Messi marcó quince goles en seis partidos.[31]​ En este período, Messi convirtió 234 goles, con un promedio de 1,32 por partido.[32]​ En una entrevista realizada en 2014, Vecchio comentó: "Verlo jugar a Leo con tan corta edad realmente era impresionante. Uno no podía creer (…) ver un chico con esa virtud, esa calidad, y tan menudito, chiquitito, que haga tantas cosas con la pelota".[cita requerida]

Equipo	Año	Partidos	Goles	Promedio
Newell`s "A"
(Categoría ‘87)
Argentina	1994	29	40	1.38
1995	30	36	1.2
1996	27	36	1.33
1997	36	40	1.11
1998	25	27	1.08
1999	29	55	1.9
Total*[32]​	176	234	1.33
F. C. Barcelona (2000-2005)

La Masia
En 2001, Messi comenzó a entrenar con el Infantil A de Rodolfo Borrell, pero luego lo pasaron al Infantil B, dirigido por Xavi Llorens,[33]​ donde jugaba como media punta o extremo izquierdo. Al ser extranjero, no podía participar en partidos oficiales, pero sí en amistosos. Jugó por primera vez en marzo, de visitante ante el Amposta, y anotó un gol, pero en el siguiente partido, contra el Ebre Escola Esportiva el 21 de abril, se fracturó el peroné izquierdo, por lo que no pudo jugar hasta junio. Poco después, al bajar una escalera, se distendió los ligamentos del tobillo izquierdo y se perdió el resto de la temporada 2000-2001.[34]​[23]​ Volvió a entrenar con el Infantil A en la temporada 2001-2002, pero pronto lo ascendieron al Cadete B de Tito Vilanova, donde marcó nueve goles en diez partidos. En la temporada 2002-2003 integró el Cadete A, entrenado por Álex García, con el que jugó 31 partidos y anotó 38 goles. El Cadete A fue campeón de la Liga y la Copa Cataluña,[33]​ después de ganarle 4-1 al Espanyol con un doblete de Messi.[35]​

Comenzó la pretemporada 2003-2004 el 8 de agosto en el Juvenil B, en el marco de la Toyota U17 Club World Cup, con el Feyenoord como rival, al que los españoles vencieron 3-1. Jugó los 90 minutos y dio una asistencia a Franck Songo'o.[36]​ Juan Carlos Pérez Rojo, entrenador del Juvenil A, lo pidió para un partido de la Liga de la División de Honor Juvenil contra el Hércules que el Barcelona ganó 3-0.[33]​ Messi pasó entonces a integrar el Juvenil A y, el 14 de octubre, firmó su primer contrato como profesional.[33]​[37]​ El 26 de octubre, ante el Gimnastic de Tarragona, marcó cuatro goles en un partido para el 0-7 del Barcelona y, dos semanas después, un hat trick en el 8-1 a Granollers.[38]​

Frank Rijkaard, entrenador del primer equipo, convocó a Messi y a otros canteranos para jugar un partido de exhibición ante el Fútbol Club Oporto, entrenado por José Mourinho, en la inauguración del Estádio do Dragão de Oporto.[39]​ Así, el 16 de noviembre de 2003, a los dieciséis años y 145 días,[33]​ y cuando todavía no había pasado por el Barça B,[40]​ Messi debutó con el primer equipo. Fue, en ese momento, el tercero más joven en hacerlo.[41]​ El 29 de noviembre, jugó con el Barcelona C frente al Europa de la tercera división.[33]​

El 18 de febrero de 2004, lo llamaron para otro amistoso del primer equipo contra el FC Shakhtar Donetsk.[42]​ Después de once partidos con el Barcelona C, el 6 de marzo jugó por primera vez con el Barcelona B de Pere Gratacós contra el Mataró en la Segunda División B.[33]​ Hacia el final de la temporada, jugó seis veces con el Barcelona B y también disputó partidos con el Barcelona C y los Juveniles A y B. El 15 de mayo, con el Juvenil A, en el partido de vuelta de octavos de final de la Copa del Rey Juvenil frente al Sevilla, convirtió su segundo poker.[43]​ Ese año, jugó en cinco categorías en cuatro meses, en los que pasó de los juveniles al equipo profesional.[2]​ Marcó, en total, 35 goles en 37 partidos oficiales con el Juvenil B, el Juvenil A, Barça C y Barça B.[33]​

En la temporada 2004-2005, alternó partidos en Segunda División B y Primera División: jugó diecisiete con el Barcelona B, en los que marcó seis goles, y nueve en el primer equipo, con el que anotó una vez.[33]​

Club	División	Temporada	Partidos	Goles	Promedio
F. C. Barcelona
Bandera de España España	Infantil B	2000-01	2	1	0.5
Cadete B	2001-02	10	9	0.9
Cadete A	2002-03	31	38	1.23
Juvenil B	2003-04	3	1	0.57
Juvenil A	19	29	1.48
Barcelona C	10	5	0.5
Barcelona B	5	0	0
2004-05	17	6	0.35
Total*[33]​	97	89	0.98
Trayectoria
Fútbol Club Barcelona
Artículo principal: Lionel Messi en el Fútbol Club Barcelona
Primeros años

Messi en un partido ante el Málaga en 2005
Comenzó la pretemporada 2004-2005 jugando amistosos con el primer equipo: ante el Banyoles, el Figueres, el Palamós, el Hércules y el Olympique de Marsella, donde fue titular por primera vez.[44]​ Contra el Palamós el 20 de julio en el Camp Nou, en el minuto '74, anotó su primer gol, que puso el 0-4 parcial de un partido que el Barcelona ganó 0-6.[45]​ Participó también en el On Tour Asia, una gira promocional del club por Corea, China y Japón en la que se jugaron cuatro amistosos. Convirtió un gol el 1 de agosto en el 5-0 ante el Kashima Antlers.[46]​

Aunque sabía que podía funcionar como atacante en cualquier posición, Rikjaard lo hizo jugar como extremo derecho, puesto que tenía Giuly.[47]​ Messi jugó su primer partido oficial el 16 de octubre, el derby barcelonés contra el Espanyol en el estadio Olímpico Lluís Companys, cuando sustituyó a Deco ocho minutos antes de terminar el encuentro. Con diecisiete años, tres meses y veintidós días, se convirtió en uno de los canteranos más jóvenes en debutar en La Liga.[48]​ El 27 de octubre, ante el Gramenet, jugó por primera vez en la Copa del Rey y el 7 de diciembre en la Liga de Campeones 2004-2005 frente al FC Shakhtar Donetsk en el Donbass Arena.[49]​[50]​ Hacia fines de ese año, el diario El País lo señalaba como "la gran promesa".[2]​

En un partido de La Liga contra el Albacete Balompié el 1 de mayo de 2005, tras asistencia de Ronaldinho, Messi anotó, de vaselina, su primer gol oficial, después de que le anularan otro parecido por estar en offside.[51]​ Con diecisiete años, 10 meses y 7 días, se convirtió en el jugador más joven del Barcelona en hacer un gol en ese torneo, marca que superó Bojan Krkić en 2007.[52]​ Luego de cinco temporadas sin conseguir el título, el 14 de mayo el Barcelona empató 1-1 contra el Levante y fue campeón de La Liga tres jornadas antes de la finalización del torneo.[53]​

Nunca olvidaré que Rijkaard me puso en marcha. Que confió en mí con tan solo diecisiete años de edad.
Messi sobre de su ex-entrenador.[54]​
En junio, Messi firmó su primer contrato como jugador del primer equipo, que lo vinculaba con el club hasta 2010 y tenía una cláusula de rescisión de 150 millones de euros, similar a las de Ronaldinho y Samuel Eto'o, jugadores ya establecidos en el plantel.[55]​

Titularidad y consagración en la élite
A pesar de que Rijkaard lo había llevado como suplente para el partido de ida de la Supercopa de España contra el Betis el 13 de agosto,[56]​ Messi no pudo jugar por estar ya cubierto el cupo de extranjeros. El Barcelona ganó 3-0 y, una semana después, perdió 2-1, resultado con el que obtuvo el primer título de la temporada.[57]​ Messi, entretanto, obtuvo la nacionalidad española el 1 de octubre, por lo que tampoco pudo participar en las cinco primeras jornadas de La Liga.[58]​ El 24 de agosto, fue titular en el Trofeo Joan Gamper ante la Juventus en el Camp Nou. Pese a que el Barcelona perdió 2-4 en la tanda de penaltis tras un empate 2-2, su desempeño fue tan bueno que, por primera vez, lo ovacionaron cuando fue sustituido y Fabio Capello, DT de la Juventus, le pidió a Rijkaard si no se lo cedía, además de decir en la conferencia de prensa posterior que "Nunca había visto a un jugador con tanta calidad a esta edad y con esa personalidad con una camiseta tan importante".[59]​[60]​[61]​ En Mundo Deportivo, Andrés Astruells escribió que para Messi, a quien definió como "pequeño, incisivo" y con "un endiablado cambio de ritmo", el Trofeo había sido "su gran noche" y Santi Nolla afirmó que lo había "catapultado".[62]​ En el reporte del partido de El País, se señalaba que "El Gamper de anoche pasará a la historia por haber entronizado a un futbolista magistral que ofreció un recital",[63]​ mientras que otros periodistas españoles lo describieron como un momento bisagra en su carrera.[59]​[60]​[61]​[64]​ Después del torneo, el club decidió que no volvería a jugar con los juveniles y sería parte del primer equipo.[65]​

Debido al interés que había despertado en otros clubes europeos, como el escocés Glasgow Rangers, por su desempeño en el Mundial sub-20 y en el Joan Gamper, el 16 de septiembre el presidente Joan Laporta decidió aumentarle el sueldo y prolongar su contrato hasta 2014, con la misma cláusula de rescisión.[66]​[67]​[68]​

Como no podía jugar por ser extranjero, el Barcelona recurrió a la Real Federación Española de Fútbol para que lo considerara asimilado pero, el 19 de septiembre, la Comisión Delegada de la Liga Profesional rechazó esa concesión. Messi, por lo tanto, no podía participar en competiciones españolas (tampoco con el Barcelona B), aunque sí en la Liga de Campeones.[68]​[69]​ El club, entonces, decidió acelerar su nacionalización, que obtuvo el 26 del mismo mes.[70]​ Al día siguiente, Messi jugó en la Liga de Campeones 2005-2006 frente al Udinese, y los aficionados en el Camp Nou, lo ovacionaron antes del partido y después de su sustitución.[71]​

Messi pudo jugar en La Liga el 1 de octubre, en el empate 2-2 con el Zaragoza, donde entró en el minuto '66 en lugar de Giuly.[72]​ El Alavés y el Deportivo La Coruña denunciaron ante el Comité de Competición su inclusión en la plantilla, por considerar que se le había dado la licencia como juvenil y no como profesional. El Comité, sin embargo, declaró improcedente la denuncia, ya que el jugador conservaba la licencia de juvenil y era ciudadano español.[73]​ El 2 de noviembre, Messi convirtió su primer gol en Liga de Campeones ante el Panathinaikos, al que el Barcelona le ganó 5-0.[74]​ El 19, por un encuentro de La Liga en el estadio Santiago Bernabéu, fue titular en su primer Clásico, que perdió el Real Madrid 0-3 y en el que Ronaldinho recibió aplausos de la afición rival. Dio el pase a Eto'o para el primer gol, superó el marcaje de Roberto Carlos y aceleró el juego de su equipo, por momentos lento y que desaprovechaba ocasiones de gol.[75]​[76]​

El 29 de enero de 2006, en un partido de Liga ante el Mallorca en el Son Moix, marcó, en dieciocho minutos, su primer doblete para el 3-0 del Barcelona.[77]​[78]​


Messi en 2007
En octavos de final de la Liga de Campeones 2005-2006, el 22 de febrero en Stamford Bridge ante el Chelsea de Mourinho, Messi pateó cinco veces a puerta, todas entre los tres palos, en una victoria por 2-1 del Barcelona.[79]​ En El País, Santiago Segurola comentó que, pese a sus dieciocho años y sus pocos partidos como titular, Messi había dominado el encuentro "a una distancia sideral de los demás" y se había establecido como "una gran estrella".[80]​ Otros diarios también destacaron su actuación,[81]​ a la vez que Diego Maradona, en una entrevista con la BBC, lo señaló como quien "ocuparía su lugar" en el fútbol argentino.[82]​ En el partido de vuelta, jugado en el Camp Nou el 7 de marzo, se rompió el músculo femoral izquierdo, lo que le impidió jugar los siguientes diecisiete encuentros.[83]​ El 3 de mayo, el Barcelona ganó la Liga y fue campeón de Europa el 17, tras ganarle al Arsenal en el Stade de France.[84]​[85]​ A pesar de haber jugado sólo veinticinco partidos en los que marcó ocho goles, esa temporada se constituyó en la figura emergente del equipo.[86]​

En mayo, fue nominado al Premio Laureus al Deportista Revelación del Año,[87]​ pero perdió ante Rafael Nadal.[88]​ A mediados de la temporada 2005-06, comenzaron a señalarlo como el jugador revelación del año: en septiembre, recibió en Italia el premio Eurochampion, que distingue al mejor jugador joven del mundo,[89]​ en noviembre, el diario El Mundo hablaba de un duelo entre Messi y Robinho, fichado por el Real Madrid ese mismo año, a quienes consideraba las futuras estrellas de La Liga y,[90]​ en diciembre, recibió el premio Golden Boy, entregado por la revista italiana Tuttosport al mejor jugador joven de Europa. Messi, con 225 puntos sobre 300, superó a Wayne Rooney (127) y a Lukas Podolski (74).[91]​

En la temporada 2006-07, se estableció en el cuadro titular.[92]​ El 17 y 20 de agosto, jugó su primera final con el primer equipo, la Supercopa de España, que el Barcelona le ganó al Espanyol 1-0 y 3-0,[93]​[58]​ y participó el 25 en la final de la Supercopa de Europa, que ganó el Sevilla en el Stade Louis II de Mónaco. No anotó goles en ninguna de las dos competiciones.[93]​[94]​

En las dos primeras jornadas de Liga, el 28 de agosto anotó uno de los tres goles del 3-2 del Barcelona ante el Celta de Vigo y,[95]​ el 9 de septiembre, otro en el 3-0 contra el Osasuna.[96]​

En el segundo partido del Barcelona en la Liga de Campeones 2006-2007, el 27 de septiembre ante el Werder Bremen, entró en el segundo tiempo en lugar de Giuly y, siete minutos antes de terminar el partido, marcó el gol del empate 1-1.[97]​

En noviembre, recibió el premio Mejor Jugador Joven, otorgado por FIFPro,[98]​ que volvería a ganar los dos años siguientes.[99]​

En un partido de Liga contra el Zaragoza el 12 de noviembre, se quebró el metatarso izquierdo y no pudo jugar por tres meses.[100]​ Se recuperó de su lesión en Argentina y regresó el 11 de febrero de 2007 en el segundo tiempo contra el Racing de Santander.[101]​[102]​

En enero de 2007, se le aumentó la paga a tres millones de euros por año y se le extendió el contrato hasta 2014.[66]​[103]​

El 10 de marzo, con un triplete ante el Real Madrid, que fue un empate 3-3 con diez hombres en su equipo,[104]​ se convirtió en el jugador más joven en haber anotado en El Clásico. Desde Romario en 1994, ningún otro jugador del Barcelona había marcado un hat trick en el derby español y nadie lo había hecho desde Iván Zamorano en 1995.[104]​[105]​

El 18 de abril, en el 5-2 por semifinales de la Copa del Rey 2006-2007 contra el Getafe FC, Messi anotó dos goles, el primero muy parecido al llamado Gol del Siglo de Maradona contra Inglaterra en la Copa del Mundo de 1986.[106]​ Corrió casi la misma distancia (62 metros) y eludió al mismo número de jugadores (seis, incluido el portero), para anotar desde una posición muy similar, después de correr hacia el banderín de esquina.[107]​ Distintas personas ligadas al fútbol y la prensa internacional lo compararon con el 10 argentino y el periódico español Marca lo llamó "Messidona".[108]​[109]​ En el partido de vuelta el 10 de mayo, el Getafe ganó 4-0 y eliminó al Barcelona del torneo.[110]​

El 9 de junio, en el derby barcelonés, Messi convirtió un gol similar al de "La Mano de Dios", anotado por Maradona contra Inglaterra en cuartos de final del Mundial 86. Se adelantó al portero Carlos Kameni y quiso cabecear pero, como no llegó, empujó el balón con la mano. A pesar de las protestas de los jugadores del Espanyol y repeticiones que demostraron la falta evidente, el gol fue validado.[111]​ El 15 de agosto, con gol de Messi en el 1-0 contra el Bayern Múnich, el Barcelona ganó la primera edición de la Copa Beckenbauer.[112]​ Hacia el final de la Liga, Messi empezó a marcar más que al inicio de la temporada (11 de sus 14 goles los hizo en los últimos trece partidos).[113]​ Sumó un total de diecisiete goles en treinta y seis partidos (14 en La Liga, 1 en Champions y 2 en Copa del Rey).[92]​

En noviembre, se convirtió en el primer argentino que recibió el Trofeo Bravo, entregado por Guerin Sportivo a los mejores futbolistas menores de veintiún años.[114]​ El 4 de diciembre, quedó en tercer lugar en la votación del Balón de Oro, detrás de Kaká y Cristiano Ronaldo,[115]​ y el 16 fue incluido por primera vez en el FIFA FIFPro World XI en la categoría de delantero.[116]​[117]​

El 15 de diciembre, en un partido contra el Valencia, se lesionó el bíceps femoral izquierdo, por lo que estuvo más de un mes sin jugar.[118]​ Regresó el 20 de enero del año siguiente frente al Racing de Santander.[119]​

El 29 de abril de 2008, el Barcelona fue eliminado por el Manchester United en semifinales de la Liga de Campeones 2007-2008, después de un empate sin goles el 23 en el Camp Nou y perder 1-0 en Old Trafford.[120]​[121]​ Al final de la temporada, Messi había hecho dieciséis goles y diez asistencias en cuarenta partidos.[86]​

Era dorada del club: el "Pep Team"
2008-09: Triplete histórico

Messi en el Clásico en el que el Barcelona le ganó 6-2 al Real Madrid en el estadio Santiago Bernabéu.
Después de dos temporadas sin éxito, el Barcelona necesitaba una reforma,[122]​ lo que provocó la salida de Rijkaard y la llegada de Pep Guardiola como entrenador, por decisión unánime de la comisión delegada del club, apoyada por la junta directiva.[123]​ Tras la marcha de Ronaldinho, Messi recibió la camiseta número 10.[124]​ En junio de 2008, firmó su cuarto contrato por un salario de entre 10 y 14 millones de euros que lo convirtió en el mejor pagado del club.[125]​

De cara a la nueva temporada, una de las principales preocupaciones seguía siendo sus frecuentes lesiones musculares, que lo habían dejado al margen durante un total de ocho meses entre 2006 y 2008.[126]​ Para solucionar el problema, se implementaron nuevos regímenes de nutrición y sueño y el Barcelona aceptó que eligiera un kinesiólogo y un fisioterapeuta personales, que serían supervisados por el plantel médico del club.[127]​ Como resultado, permaneció prácticamente libre de lesiones los siguientes cuatro años.[128]​

A fines de julio, participó en la gira por Escocia en la que el Barcelona jugó contra el Hibernians y el Dundee United.[129]​ El 27 de julio, ante el Dundee, anotó un hat-trick y fue capitán por primera vez.[130]​ Marcó, entre los dos partidos, cuatro de los once goles de su equipo.[131]​[132]​

Hacia fines de año, en la prensa ya se hablaba de "Messidependencia" para referirse a su papel fundamental en el equipo,[133]​ aunque Laporta y Guardiola negaran que fuera así.[134]​ Ya en julio, después de la repercusión por su desempeño en Escocia, el entrenador había dicho "No quiero que Messi lo resuelva todo. A Messi hay que ayudarlo porque él también nos ayuda" y que no creía que hubiera "dos Barças, uno con Messi y otro sin él".[131]​[132]​

En diciembre, Messi se ubicó en el segundo puesto en el Balón de Oro y, en enero de 2009, en el premio al Jugador Mundial de la FIFA, en ambas ocasiones detrás de Cristiano Ronaldo.[135]​[136]​

El 6 de enero, en el partido de ida de octavos de final de la Copa del Rey, hizo un hat trick en el 3-1 frente al Atlético de Madrid, a pesar de que en su equipo faltaron siete titulares. La afición rival festejó su segundo gol y lo aplaudió cuando fue sustituido.[137]​[138]​ El 1 de febrero, en un partido de La Liga contra el Racing de Santander, donde entró en el segundo tiempo, marcó el gol del empate y otro para el 2-1 final, que fue el número 5000 del Barcelona en ese torneo.[139]​

El 8 de abril, en el partido de ida de cuartos de final de la Liga de Campeones, hizo dos goles y dos asistencias en el 4-0 ante el Bayern Múnich.[140]​

El 2 de mayo, por un partido de Liga, con un doblete de Messi el Barcelona le ganó 6-2 al Real Madrid, en lo que fue su mayor goleada en el Santiago Bernabéu.[141]​ Fue ése el primer partido en el que Messi marcó un gol en ese estadio y jugó como falso nueve, después de que Guardiola decidiera que ya no jugaría de extremo y establecerlo como el eje del juego del equipo.[142]​[143]​

Frente al Chelsea, el 6 de mayo en el partido de vuelta por semifinales en Champions, asistió a Andrés Iniesta en el gol que permitió el empate 1-1 en el minuto 92 y el pase a la final.[144]​

El 13 de mayo, en un clásico contra el Athletic de Bilbao por Copa del Rey, anotó su primer gol en una final con el primer equipo y asistió en el segundo para el 4-1 del Barcelona, que ganó el torneo después de once años.[93]​[145]​ Tres días más tarde, el club fue campeón de La Liga sin necesidad de jugar las últimas tres jornadas.[146]​

El 27 de mayo, en la final de la Liga de Campeones ante el Manchester United en el estadio Olímpico de Roma, Messi convirtió de cabeza el segundo gol del Barcelona, que ganó 2-0 y recibió su tercera Copa de Europa,[147]​ con lo que consiguió el primer triplete del fútbol español y el quinto de la historia, detrás del Celtic, el Ajax, el PSV y el Manchester United.[148]​ En una entrevista con el canal argentino TyC Sports en 2019, el jugador eligió ese gol como el más importante de su carrera.[149]​

En su primera campaña ininterrumpida,[83]​ Messi hizo 18 asistencias y 38 goles en 62 partidos, nueve de ellos en la Liga de Campeones,[150]​ lo que lo hizo el máximo goleador y mejor delantero de esa edición.[151]​[152]​ Por otra parte, sus tantos, sumados a los de Eto'o (36) y Thierry Henry (26), dieron un total de 100 goles en todas las competiciones.[143]​ De esos cien, 70 fueron anotados en La Liga, con lo que rompieron el récord de 66 goles establecido por Ferenc Puskás (28), Alfredo Di Stéfano (21) y Luis del Sol (17) para el Real Madrid en la temporada 1960-1961.[153]​ El Barcelona, además, superó su propia marca de más goles en una temporada (158),[154]​ en los que Messi tuvo una incidencia del 35,4 %.[150]​

En julio, Messi recibió el Trofeo Alfredo Di Stéfano, que se otorga al mejor jugador de la primera división española. Antes de entregarle el premio, Di Stéfano dijo que era el mejor del mundo.[155]​

2009-2010: sextete y primer Balón de Oro
El 23 de agosto, frente al Athletic de Bilbao, Messi anotó por primera vez en la Supercopa de España. Marcó dos de los tres goles de su equipo, que salió campeón.[58]​ El 28, le dio un pase a Pedro, que hizo el gol con que el Barcelona ganó 1-0 la Supercopa de Europa ante el Shakhtar Donetsk.[156]​

El 27 de ese mes, la UEFA lo reconoció como Mejor Delantero y Jugador del Año,[157]​ además de Jugador de Club del Año.[158]​

Después de no participar en el primer partido del Barcelona en La Liga, convirtió en las tres jornadas siguientes y consiguió un promedio de un gol cada 37 minutos, pese a haber jugado sólo un partido completo.[159]​ El 12 de septiembre, ante el Getafe, entró en el segundo tiempo y anotó el segundo gol del 2-0 del Barcelona.[160]​ Hizo un doblete en el 5-2 frente al Atlético de Madrid el 20, cuando jugó los noventa minutos,[161]​[159]​ y otro en el 4-1 ante el Racing de Santander.[162]​

En septiembre, se le renovó el contrato hasta 2016, por una suma que el club nunca había ofrecido a otro jugador.[103]​[163]​ Así, con un salario de once millones de euros y una cláusula de rescisión de 250 millones, pasó a ser el futbolista mejor pagado del mundo.[103]​[66]​ En octubre, fue elegido Mejor Jugador de la temporada 2008-09 en la primera entrega de los premios LFP.[164]​

El 2 de diciembre, ganó su primer Balón de Oro y el premio al Jugador Mundial de la FIFA, en ambas ocasiones por el mayor margen de votación en la historia de cada trofeo.[165]​[166]​

En la semifinal de la Copa Mundial de Clubes, jugada el 16 de diciembre, marcó un gol en el 3-1 contra el Atlante dos minutos después de haber ingresado.[167]​ Dos días más tarde, en la final contra Estudiantes de La Plata anotó con el pecho el 2-1 en tiempo suplementario.[168]​ El Barcelona ganó el torneo por primera vez y se convirtió en el primer club en lograr un sextete.[169]​ Messi recibió el Balón de Oro y el premio Toyota.[168]​

El 10 de enero de 2010, en un partido de Liga ante el Tenerife, anotó un hat trick en el 5-0 del Barcelona y,[170]​ en la jornada siguiente, un doblete en el 4-0 contra el Sevilla. Con el primero de los dos goles, superó la marca de Mariano Martín como jugador del Barcelona más joven (veintidós años y medio) en anotar cien goles en partidos oficiales.[171]​ El 14 de marzo, frente al Valencia, marcó su cuarto hat-trick con el club, que ganó 3-0.[172]​ Por el último de sus goles fue candidato al premio Puskás,[173]​ pero perdió ante Hamit Altintop.[174]​ Una semana después, consiguió un penalti y anotó otro triplete en el 4-2 ante el Zaragoza, por lo que fue el autor de nueve de los últimos diez goles de su equipo.[175]​[176]​ Su desempeño volvió a ser destacado por la prensa internacional, en notas donde, además de comparárselo con Maradona, se lo señalaba como el mejor futbolista del mundo.[177]​[176]​

El 5 de abril, en la vuelta de cuartos de final de la Liga de Campeones, el Barcelona venció 4-1 al Arsenal con goles todos de Messi que, con ocho tantos, fue máximo goleador del torneo.[178]​[179]​ El jugador recibió por ese poker elogios de distintos diarios del mundo.[180]​[181]​ El 28 de abril, el Barcelona quedó eliminado en semifinales por el Inter de Milán y, el 16 de mayo, al ganarle 4-0 al Valladolid con dos goles de Messi, fue campeón de La Liga.[182]​[183]​

Messi finalizó la temporada con 47 goles, 34 de ellos en La Liga, número que no alcanzaba un jugador del Barcelona desde Ronaldo en la temporada 1996-1997.[15]​ Recibió el trofeo Pichichi (máximo goleador de La Liga) y la Bota de Oro.[184]​[185]​

2010-2011: quinta Liga y tercera Liga de Campeones

Messi ante el Arsenal FC en la Liga de Campeones 2010-2011
El 14 de septiembre, en la Liga de Campeones, convirtió un gol en el 5-1 frente al Panathinakós y pasó a ser, con 27 tantos, el máximo goleador histórico del Barcelona en ese torneo.[186]​

El 30 de octubre, tras una derrota en el partido de ida por la Supercopa de España, anotó un hat-trick en el 4-0 sobre el Sevilla en el partido de vuelta, con lo que el Barcelona ganó su primer trofeo de la campaña 2010-11.[187]​[188]​

El 20 de noviembre, en un partido de La Liga contra el Almería, anotó otro hat-trick en el 8-0 del Barcelona, una diferencia de goles que no se registraba en ese torneo desde 1959.[189]​ El 29 dio dos asistencias a David Villa en el Clásico, el primero con Mourinho a cargo del Real Madrid, al que el Barcelona ganó 5-0 en otra histórica goleada.[190]​ Hizo otro triplete en el 3-0 contra el Atlético de Madrid el 5 de febrero de 2011. El Barcelona, así, ganó dieciséis partidos seguidos en La Liga y rompió el récord del Madrid de Di Stéfano de la temporada 1960-1961.[191]​ Guardiola comentó que Messi había sido determinante para alcanzar esa cantidad de partidos ganados.[192]​

El 8 de marzo, Messi hizo dos de los goles en el 3-1 al Arsenal en octavos de final de la Liga de Campeones.[193]​ Por su primer gol quedó seleccionado para el premio Puskás, pero perdió ante Neymar.[194]​ Volvió a convertir un doblete en el partido de ida de semifinales, un 2-0 contra el Real Madrid, el 27 de abril.[195]​ En la final ante el Manchester United el 28 de mayo en el estadio de Wembley, fue determinante en el juego de su equipo, no sólo por su gol, sino también por sus pases, caños y regates. El Barcelona ganó 3-1 y consiguió su cuarta Copa de Europa.[196]​ Nuevamente, el desempeño de Messi fue destacado por varios diarios de distintos países.[197]​

Con 53 goles y 24 asistencias en todo el curso,[198]​ se convirtió en el máximo goleador de todos los tiempos del Barcelona en una temporada.[199]​ Por otra parte, con doce tantos, fue el máximo goleador en la Liga de Campeones, lo que le permitió igualar el récord de Ruud van Nistelrooy de 2002-2003 y pasar a ser, tras Gerd Müller y Jean-Pierre Papin, el tercero en ostentar ese título tres veces consecutivas.[151]​

El 10 de enero de 2011, recibió el Balón de Oro inaugural de la FIFA, una combinación del Balón de Oro de France Football y el premio al Jugador Mundial de la FIFA, aunque se lo criticó por haber recibido ese premio, debido a que con la selección argentina había llegado sólo a cuartos de final en el Mundial de Sudáfrica 2010.[200]​

2011-2012: una temporada récord

Messi y Neymar en la final de la Copa Mundial de Clubes de 2011.
En el partido de ida de la Supercopa de España contra el Real Madrid el 14 de agosto, dio una asistencia e hizo un gol en el empate 2-2.[201]​ En la vuelta, el 17, en el 5-4 con el que el Barcelona fue campeón,[202]​ marcó dos goles, por lo que llegó a los ocho y superó a Raúl (7) como máximo goleador de esa competición.[203]​ El 26, con un gol y asistencia suyos, el Barcelona le ganó 2-0 al Porto la Supercopa de Europa.[204]​

El 25 de agosto, Messi recibió el premio inaugural al Mejor Jugador en Europa y, en octubre, lo eligieron segundo mejor jugador de los últimos veinte años de la Champions League.[205]​[206]​

El 18 de diciembre, el Barcelona ganó 4-0 la final de la Copa Mundial de Clubes contra el Santos con un doblete de Messi, que recibió el Balón de Oro del torneo.[207]​

Hacia fin de año, ganó su primer Olimpia de Oro y,[208]​ el 9 de enero de 2012, con casi el 50 % de los votos, volvió a recibir el Balón de Oro y pasó a ser el cuarto jugador en la historia en ganarlo en tres ocasiones, después de Johan Cruyff, Michel Platini y Marco van Basten.[209]​ Para entonces, ya era ampliamente considerado uno de los mejores futbolistas de la historia, junto a jugadores como Maradona y Pelé.[210]​

El 18 de febrero, en un partido de La Liga contra el Valencia que el Barcelona ganó 5-1, marcó cuatro goles.[3]​ Volvió a anotar esa cantidad (dos de penalti) el 5 de mayo, en la anteúltima fecha ante Espanyol, que el Barcelona ganó 4-0 y fue el último partido dirigido por Guardiola.[211]​ Con su segundo poker de la temporada, llegó a los 50 goles en esa competición y superó el récord en un torneo liguero europeo, establecido por Dudu Georgescu con el Dinamo de Bucarest (47) en la temporada 1976-1977.[212]​

El 7 de marzo, al anotar cinco veces en el 7-1 frente al Bayer Leverkusen en el partido de vuelta por los octavos de final de la Liga de Campeones, se convirtió en el primer jugador que marcó esa cantidad de goles en un solo partido en la historia de esa competición.[213]​

El 20 de marzo, ante el Granada en el Camp Nou, alcanzó con un hat-trick los 234 goles y desplazó a César (232) como máximo goleador histórico del Barcelona en partidos oficiales.[214]​

El 3 de abril, en el partido de vuelta por cuartos de final, el Barcelona le ganó 3-1 al Milan con dos penaltis de Messi y pasó a la quinta semifinal consecutiva de su historia.[215]​ El jugador, por su parte, marcó su gol número 14 en esa edición y el 50 en Champions, con lo que igualó a Raúl, van Nistelrooy y Thierry Henry en cantidad total de tantos y alcanzó el récord de José Altafini de la temporada 1962-1963,[216]​ que sería superado por Cristiano Ronaldo (17) en 2013-2014.[217]​ Fue, además, máximo goleador por cuarta vez consecutiva, con lo que igualó el récord de Gerd Müller de los años 1972-1977.[151]​

Durante la temporada 2011-12, a medida que se convirtió en una combinación de un número 8 (un creador), un 9 (anotador) y un 10 (asistente), aumentó su capacidad goleadora en todas las competiciones de clubes,[218]​ en las que realizó siete hat-tricks, dos pokers y un repoker.[219]​ Con 50 goles en 31 partidos, fue máximo goleador de La Liga y jugador con mejor promedio de gol (1,61) en una temporada, dos récords,[220]​[221]​ mientras que sus 73 goles en todas las competiciones (14 en Champions, 3 en la Copa del Rey, 2 en el Mundial de Clubes, 3 en la Supercopa de España y 1 en la Supercopa de Europa) superaron los 67 de Gerd Müller en la temporada 1972-73 de la Bundesliga, por lo que pasó a ser el máximo goleador en competiciones oficiales y máximo goleador absoluto en una temporada.[222]​ A los anotados con el Barcelona, se agregaron nueve con la selección argentina, por lo que fue, con 82 goles, máximo goleador histórico en una temporada en competiciones oficiales.[223]​

La Messidependencia
2012-2013: con Tito Vilanova
Bajo la dirección del nuevo entrenador Tito Vilanova, durante la segunda mitad de 2012 el Barcelona tuvo su mejor comienzo de temporada en la Liga, con 55 puntos acumulados en la mitad de la competencia, un récord en el fútbol español.[224]​

A fines de marzo, Messi había anotado en diecinueve partidos consecutivos de La Liga, algo sin precedentes en esa competición.[225]​ Al convertir un doblete el 9 de diciembre contra el Betis, alcanzó 192 goles en La Liga y 86 (74 en su club y 12 con la selección) en el año. Rompió así dos récords históricos: el de César Rodríguez de 190 goles en La Liga, por lo que pasó a ser el máximo goleador de todos los tiempos del Barcelona en esa competición (192 en 228 partidos), y el de más goles en un año calendario de Müller, que en 1972 marcó 85 con el Bayern Múnich (72) y Alemania Occidental (13).[226]​ El jugador alemán, en una entrevista con el canal Sport1, lo felicitó por haber batido su récord de cuarenta años y Messi, en reconocimiento, le envió una camiseta del Barcelona con el número 10, en la que se leía "Para Gerd Müller/Mi respeto y admiración/Un abrazo".[227]​[228]​ Con esos 86 tantos, ingresó en el Guinness World Records por el número de goles (club y selección) marcados en un año calendario,[229]​ aunque la FIFA alegó problemas de verificabilidad y no reconoció el logro.[230]​ Messi amplió ese resultado en los últimos partidos de La Liga y Copa del Rey (dos ante Córdoba Club de Fútbol, dos contra el Real Madrid y uno frente al Valladolid), de manera que terminó el año con 91 goles, de los que 79 fueron con su club (59 en la Liga, 13 en la Champions, 5 en la Copa del Rey y 2 en la Supercopa), lo que lo convirtió en el máximo goleador absoluto en un año natural del Barcelona.[222]​ Entre esos goles, 25 fueron internacionales (13 en la Liga de Campeones y 12 en su selección), con lo que igualó el récord de Vivian John Woodward de 1909.[222]​[231]​

Como favorito, volvió a recibir el Balón de Oro, por lo que es el único jugador en ganar ese premio en cuatro ocasiones seguidas.[232]​ Lo incluyeron, además, en el FIFA/FIFPro World XI por sexto año consecutivo.[233]​

En diciembre, renovó su contrato hasta 2018, con un sueldo neto de 13 millones de euros.[66]​[103]​

El 27 de enero de 2013, anotó su cuarto poker en el 5-1 como local ante el Osasuna.[219]​ El 17 de marzo, llevó el brazalete de capitán por primera vez, en un partido de Liga ante el Rayo Vallecano; para entonces, se había convertido en el punto focal táctico del equipo en un grado que solo se comparaba con los exjugadores del Barcelona Josep Samitier, László Kubala y Cruyff.[234]​ El 5 de mayo contra el Betis, entró en el segundo tiempo y, en cinco minutos, desempató el partido que el Barcelona ganó 4-2.[235]​ Anotó así en veintiún encuentros consecutivos, lo que le permitió alcanzar un nuevo récord mundial de mayor seguidilla de partidos anotando,[236]​ que hasta ese momento pertenecía a Josef Bican.[237]​

Desde su evolución a un falso nueve tres años antes,[238]​ su participación en el ataque del equipo había aumentado: del 36,1 % de los goles (2009-10) al 40,5 % (2012-13). Esta dependencia del Barcelona del jugador argentino fue señalada tanto por Evarist Murtra, exdirectivo del club,[239]​ como por su compañero Iniesta.[240]​ En la misma línea, Piqué comentó que "su presencia en el campo de juego es suficiente para levantarnos la moral y el nivel de juego".[241]​

2013-2014: con el Tata Martino
Messi tuvo un inicio irregular de la temporada con el nuevo entrenador Gerardo Martino.[242]​

El 10 de noviembre, en un partido contra el Betis, sufrió la tercera lesión de la temporada cuando se lastimó el bíceps femoral izquierdo, lo que lo dejó fuera de juego por dos meses.[243]​ Quedó en segundo lugar en la votación del Balón de Oro, lo que terminó su ventaja de cuatro años seguidos sobre Cristiano Ronaldo.[244]​

El 13 de marzo de 2014, el Barcelona le ganó 4-3 al Real Madrid con un hat-trick de Messi, que sumó así 21 goles y superó a Di Stéfano (18) como goleador histórico de El Clásico.[214]​

Por primera vez en cinco años, el Barcelona terminó la temporada sin un gran trofeo: el 9 de abril, quedó eliminado en cuartos de final de la Liga de Campeones tras perder 1-0 contra el Atlético de Madrid,[245]​ fue derrotado 2-1 el 16 de abril en la final de la Copa del Rey por el Real Madrid y, el 17 de mayo, perdió la Liga al empatar 1-1 en el último partido ante el Atlético de Madrid.[246]​[247]​ En los dos primeros partidos, Messi jugó muy por debajo de su nivel.[248]​

Tras prolongadas especulaciones sobre su futuro con el club,[249]​ en mayo renovó su contrato hasta 2018, que aumentó su paga a 20 millones de euros brutos anuales, el salario más alto en el fútbol.[103]​

La MSN
2014-2015: segundo triplete

Messi celebra un gol ante el Granada en octubre de 2014.
Con Luis Enrique como nuevo entrenador, el 15 de febrero en un partido de La Liga ante el Rayo Vallecano, anotó dos goles en el 6-0 del Barcelona. Alcanzó así los 337 tantos con su club, por lo que superó a Telmo Zarra (335 en el Athletic Club) como máximo goleador de un club español en los distintos torneos.[250]​ El 16 de marzo, con un doblete en el 7-0 contra el Osasuna, llegó a los 371 goles (344 en partidos oficiales y 27 en amistosos), y pasó a ser el máximo goleador absoluto del Barcelona, marca que pertenecía a Paulino Alcántara (142 oficiales y 227 en amistosos) desde 1917.[251]​

Con un hat-trick ante el Sevilla el 22 de noviembre, se convirtió en el máximo goleador de todos los tiempos en La Liga ya que, con 253 goles, superó tras cincuenta y nueve años el récord de 251 de Zarra.[252]​ El 24 de noviembre, en un partido de Liga de Campeones contra el APOEL en Chipre, alcanzó con otro hat-trick los 74 goles, por lo que pasó a ser el máximo goleador histórico de ese torneo y de la Copa de Europa. Logró ese récord en 91 partidos, mientras que el anterior titular, Raúl, había necesitado 142 para marcar 71 tantos.[253]​ Con un tercer hat-trick en el 5-1 ante el Espanyol el 7 de diciembre, superó los doce goles de César como máximo goleador del derby barcelonés.[254]​


Aficionados con pancartas de la "MSN" en la Breitscheidplatz de Berlín antes de la Final de la Liga de Campeones en 2015
A principios de 2015, se percibía que el Barcelona tendría otra mala temporada y en los medios de comunicación se especulaba con que Messi abandonaría el club.[255]​ El jugador, por su parte, venía de un año en el que había sido centro de críticas porque su rendimiento no había sido el mejor.[256]​ Sin embargo, el 11 de enero, en el 3-1 sobre el Atlético de Madrid, cada uno de los integrantes del tridente de ataque formado por Messi, Luis Suárez y Neymar, apodado "MSN", anotó un gol, lo que marcó el comienzo de una etapa de gran éxito.[257]​

Después de cinco años jugando como falso nueve, Messi regresó a su antigua posición en la banda derecha a fines del año anterior.[258]​ A partir de ahí, recuperó su mejor forma, posiblemente la mejor de su carrera, mientras que Suárez y Neymar terminaron con la dependencia ofensiva del equipo de su jugador estrella.[259]​ Con 58 goles y 31 asistencias de Messi, el trío marcó un total de 122 goles en todas las competiciones de esa temporada, un récord en el fútbol español.[260]​

El 28 de abril, Messi convirtió dos goles en el 6-0 al Getafe,[261]​ el segundo de penalti, el primero que marcó a lo Panenka.[262]​ En una entrevista con RAC1, Antonin Panenka describió ese tiro como el "mejor que he visto nunca".[263]​ El 17 de mayo, el Barcelona ganó La Liga, con un gol de Messi en la victoria a domicilio 1-0 sobre el Atlético de Madrid.[264]​ En la final de la Copa del Rey el 30 de mayo, Messi anotó un doblete en el 3-1 sobre el Athletic de Bilbao. Comenzó su primer su gol como extremo derecho cerca de la mitad de cancha y regateó a cuatro defensores antes anotar en un espacio reducido.[265]​ El tanto fue elegido el mejor de su carrera en una encuesta realizada por el diario Sport,[266]​ mientras que en La Vanguardia se lo describió como un "gol imposible" que "pasará a los anales de la historia de la competición".[256]​ Messi fue nominado al premio Puskás, pero quedó en segundo lugar.[267]​ El club consiguió el sexto doblete de su historia.[268]​

En octavos, cuartos de final y semifinales de la Liga de Campeones, Messi fue decisivo en el juego de su equipo.[256]​ El 6 de mayo, en el partido de ida de semifinales como local, hizo dos de los tres goles con que el Barcelona le ganó 3-0 al Bayern Múnich.[269]​ Su segundo tanto, convertido de vaselina tras eludir a Jerôme Boateng, fue elegido en una votación organizada por la UEFA como el mejor de la competición.[270]​ En la final el 6 de junio en Berlín, al derrotar a la Juventus 3-1, el Barcelona ganó su segundo triplete y se convirtió en el primer equipo de la historia en hacerlo.[271]​ En la cuarta Champions que ganó,[272]​ Messi, máximo asistidor (6) y, junto con Neymar y Cristiano Ronaldo, goleador (10) del torneo,[273]​ recibió por segunda vez el premio al Mejor Jugador en Europa por amplia mayoría de votos (49, contra tres para Luis Suárez y dos para Cristiano Ronaldo).[256]​

2015-2016: éxito doméstico
El 11 de agosto, el Barcelona ganó su quinta Supercopa de la UEFA en el estadio Borís Paichadze, tras vencer 4-5 al Sevilla en tiempo suplementario. Messi, con un doblete,[274]​ alcanzó los tres goles en ese torneo y pasó a ser máximo goleador, junto con Oleh Blokhin, Radamel Falcao, Arie Haan, Terry McDermott, Gerd Müller, Rob Rensenbrink, David Fairclough y François Van der Elst.[275]​ Además, al ganar su vigésimo sexto trofeo, superó a Di Stéfano como jugador argentino con más títulos.[276]​

El 17 de agosto, el Barcelona perdió la Supercopa de España contra el Athletic de Bilbao, después de una derrota 4-0 el partido de ida y un empate 1-1 en la vuelta, con gol de Messi.[277]​

El 26 de septiembre, en un partido ante Las Palmas, se rompió el ligamento colateral tibial izquierdo, lo que le impidió jugar por casi dos meses.[278]​ Volvió en un encuentro de fase de grupos de la Liga de Campeones contra Roma, que el Barcelona ganó 6-1 con dos goles suyos,[279]​ uno de los que fue elegido Gol de la Temporada.[280]​

El 11 de enero, ganó su quinto Balón de Oro, un récord.[281]​ En la conferencia de prensa previa a la entrega, había dicho: "Prefiero un Mundial a los cinco Balones de Oro. Los trofeos colectivos están por encima de los individuales. Sería lo más ganar un Mundial".[282]​

El 23 de febrero, en octavos de final de la Liga de Campeones, anotó, en los últimos veinte minutos de juego, un gol y un penalti con los que su equipo le ganó 2-0 al Arsenal. Fue la primera vez que el Barcelona pudo ganar en el Emirates Stadium y que Messi le convirtió a Petr Čech, después de habérselo cruzado en seis partidos.[283]​ Sobre esto, el portero había dicho: "Es fantástico, no muchos pueden decir que hayan jugado tantas veces contra Messi y que no haya encontrado la manera de hacerle gol".[284]​

El 22 de mayo, le dio un pase a Jordi Alba y el Barcelona consiguió su segundo doblete nacional consecutivo al ganar 2-0 en tiempo suplementario la final de la Copa del Rey 2016 contra el Sevilla.[285]​ Esa temporada, Messi superó su marca de 2012 de mejor comienzo goleador en un año natural (hacia mediados de marzo, había hecho 24),[286]​ anotó 41 goles y brindó 23 asistencias, mientras que el trío de ataque del Barcelona, con 131 goles, batió su propio récord del curso anterior.[260]​

2016-2017: cuarta Bota de Oro

Messi ante el Al-Ahli FC en diciembre de 2016
El 14 de agosto, en el partido de ida de la Supercopa de España, Messi participó en el gol de Munir en el 2-0 sobre el Sevilla y, en el partido de vuelta el 17, dio una asistencia a Arda Turan y convirtió un gol en el 3-0.[287]​[288]​ Fue su séptima Supercopa y la primera en la que alzó el trofeo como capitán en ausencia de Iniesta, que se encontraba lesionado.[289]​

El 13 de septiembre, en fase de grupos de la Liga de Campeones 2016-2017, anotó un triplete en el 7-0 ante el Celtic, en lo que fue la mayor goleada del Barcelona en la historia de ese torneo.[290]​ Llegó así a los 515 goles entre club y selección, por lo que superó a Di Stéfano como máximo goleador argentino de la historia.[291]​

El 21 de septiembre, en un partido de La Liga contra el Atlético de Madrid, se desgarró el muslo derecho y estuvo tres semanas sin jugar.[278]​ Regresó contra el Manchester City el 19 de octubre y anotó otro hat-trick.[292]​ El 23, en el partido de vuelta con el Celtic, convirtió un tanto y un penalti (su gol número 100 en campeonatos internacionales con el club), con los que su equipo ganó 2-0 y pasó a octavos de final. Ramon Besa, en El País, lo describió como un "jugador total" cuyo "protagonismo es últimamente tan absoluto que cuestiona no solo el fútbol del contrario sino del propio Barcelona".[293]​

El 11 de enero de 2017, tras ganarle 3-1 al Athletic con goles de cada uno de los integrantes de la MSN, el Barcelona pasó a cuartos de final de la Copa del Rey 2016-2017.[294]​ El 26, Messi anotó un penalti en el 5-2 en el partido de vuelta ante el Real Sociedad y volvió a convertir el 1 de febrero, en el partido de ida de semifinales ante el Atlético de Madrid.[295]​[296]​ Aunque no marcó en el partido de vuelta, fue el mejor de su equipo y su remate a puerta, rechazado por Miguel Ángel Moyá, lo aprovechó Luis Suárez para anotar el primer gol del 1-1.[297]​

El 14 de febrero, el Barcelona perdió 0-4 en el Parque de los Príncipes por octavos de final ante el Paris Saint-Germain,[298]​ pero el 8 de marzo, en el partido de vuelta en el Camp Nou, ganó 6-1, un hecho sin precedentes en la historia de la máxima competición europea.[299]​ Pasó así a cuartos de final y se convirtió en el único equipo español que aún podía alcanzar el triplete.[300]​ Sin embargo, fue eliminado por la Juventus tras perder 3-0 el partido de ida y empatar sin goles el 19 de abril en el Camp Nou, donde Messi jugó por debajo de su nivel.[301]​

En un Clásico de Liga el 23 de abril, fue el eje del juego de su equipo, además de anotar un doblete en el 3-2 del Barcelona.[302]​ Tras ganarle 4-2 al Eibar con dos goles de Messi, el Barcelona fue subcampeón de La Liga el 21 de mayo y el 27 ganó la Copa del Rey al vencer 3-1 en la final al Deportivo Alavés, con un gol y asistencia de Messi.[303]​[304]​ Fue el partido despedida de Luis Enrique como entrenador y el último partido oficial jugado en el Vicente Calderón.[304]​[305]​ Messi terminó la temporada con 54 goles y 19 asistencias,[260]​ ganó su cuarta Bota de Oro y, por sus 37 goles en La Liga, su tercer pichichi.[306]​[184]​

Dominio local con Ernesto Valverde y años difíciles en Champions
2017-2018: doblete doméstico y quinta Bota de Oro
El 12 de septiembre, en el primer partido de Liga de Campeones 2017-2018, Messi realizó un doblete en el 3-0 contra la Juventus y por primera vez pudo convertirle a Gianluigi Buffon.[307]​

El 19 de septiembre, en un partido de La Liga ante el Eibar que el Barcelona ganó 6-1, anotó su cuarto poker en esa competición y superó su propia marca de la temporada 2011-2012 de más goles convertidos (9) en los primeros cinco partidos.[308]​[309]​

Tras la partida de Neymar al PSG en agosto,[310]​ se disolvió la MSN, que sumó, en tres temporadas, 364 goles y 211 asistencias.[272]​

El 18 de octubre, contra el Olympiacos en la Liga de Campeones, Messi llegó a su gol número 100 en todas las competiciones de clubes de la UEFA. Fue el primer jugador no europeo en lograrlo y el segundo detrás de Cristiano Ronaldo, aunque lo hizo en veintiún partidos menos.[311]​

El 25 de noviembre, renovó hasta 2021 su contrato con el Barcelona, que estipulaba un sueldo bruto de 55 millones de euros y aumentó la cláusula de rescisión a 700 millones.[312]​[103]​

El 23 de diciembre, anotó un gol en un Clásico de La Liga que el Barcelona ganó 3-0.[313]​

El 14 de marzo de 2018, en el 3-0 de cuartos de final ante el Chelsea,[314]​ llegó con un doblete a los cien goles en Champions. Nuevamente, se ubicó detrás de Cristiano Ronaldo, pero hizo los tantos en 123 partidos, mientras que el portugués necesitó 144.[315]​

El 21 de abril, en el 5-0 sobre el Sevilla en la final de la Copa del Rey 2018, marcó el segundo gol del equipo y luego asistió en el segundo de Suárez y en el de Iniesta. El Barcelona ganó su cuarto título consecutivo y trigésimo en total.[316]​ El 29 de abril, en un partido de La Liga, Messi, con un hat-trick en el 4-2 a domicilio sobre el Deportivo de La Coruña, llegó a su gol número 30 de la temporada, por lo que pasó a ser el primer jugador de la historia de la Liga en anotar al menos 30 goles en siete ediciones distintas.[317]​[318]​ Con este resultado, y a cuatro fechas de terminar el torneo, el Barcelona consiguió su vigésimo quinta Liga.[319]​ El 6 de mayo, en un empate 2-2 en La Liga, Messi anotó el que sería su último gol en el Clásico, ya que no convirtió ninguno en los siguientes siete encuentros que jugaron.[320]​ El 9 de mayo, marcó en el 5-1 contra el Villarreal y el Barcelona llegó así a 43 partidos consecutivos sin perder,[321]​ un récord en la historia de La Liga.[322]​

Al final de la temporada, con 34 goles, Messi recibió el Pichichi y ganó, además, su quinta Bota de Oro.[323]​

2018-2019: capitanía, décima Liga y sexta Bota de Oro

Messi ante el Real Valladolid, en la segunda jornada de La Liga 2018-2019
Tras la salida de Iniesta en mayo, fue nombrado capitán del equipo para la siguiente temporada.[324]​ El 12 de agosto, tras el 2-1 sobre el Sevilla, levantó su primer título como capitán, la Supercopa de España.[325]​

El 2 de septiembre, por un partido de La Liga 2018-2019 ante el Huesca que el Barcelona ganó 8-2, hizo un doblete y dio tres asistencias.[326]​

El 18 de septiembre, en la fase de grupos de la Liga de Campeones 2018-2019, en el partido que el Barcelona le ganó 4-0 al PSV, marcó un triplete, el número 42 con su club y su octavo en Champions, que le permitió establecer un nuevo récord en ese torneo.[327]​[328]​ El 28 de noviembre, el Barcelona venció 2-1 al PSV con un gol de Piqué y otro de Messi, quien pasó a ser el jugador con más goles con un mismo equipo (106) en esa competición.[329]​[330]​

El 20 de octubre, asistió a Philippe Coutinho y anotó un gol en el 4-2 en casa sobre el Sevilla, pero tuvo que retirarse en el minuto 26 tras fracturarse en una caída el hueso radial derecho, lo que le impidió jugar durante aproximadamente tres semanas.[331]​ El 16 de diciembre, en el 5-0 del Barcelona contra el Levante, asistió a Luis Suárez en el primer gol y, al marcar su hat trick número 31 en La Liga,[332]​[333]​ pasó a ser el jugador del Barcelona con más hat-tricks y pokers (31 y 5) en ese torneo.[222]​

Terminó el año con 51 goles en 54 partidos (club y selección), por lo que la UEFA lo nombró máximo goleador de Europa de 2018.[334]​

El 17 de marzo de 2019, anotó un triplete en el 4-1 sobre el Betis.[335]​ Por uno de esos goles, fue candidato al premio Puskás, pero perdió ante Daniel Zsóri.[336]​

El 16 de abril, después de seis años sin anotar en cuartos de final de la Liga de Campeones, convirtió un doblete para el 3-0 frente al Manchester United.[337]​

El 27 de abril, ante el Levante, entró en el segundo tiempo y marcó el único gol en la victoria en casa 1-0, que le permitió al Barcelona conseguir su vigésimo sexto título de Liga tres fechas antes de que terminara el torneo,[338]​ el primero con Messi como capitán.[339]​ Fue también, con 416 goles en 449 partidos, el máximo goleador histórico del torneo y el jugador con más títulos de Liga (10) en la historia del Barcelona y el segundo del fútbol español: igualó el número de Pirri y quedó por detrás de Paco Gento (12).[221]​

El 30 de abril, le fue concedida la Cruz de Sant Jordi, otorgada por la Generalidad de Cataluña, en reconocimiento a «su fabulosa trayectoria deportiva, que lo ha llevado a ser reconocido como el mejor futbolista de todos los tiempos». Es el tercer deportista en alcanzar esta distinción, tras Gemma Mengual y Johan Cruyff.[340]​

El 1 de mayo, en el partido de ida de las semifinales de la Liga de Campeones, anotó un doblete en el 3-0 como local contra el Liverpool. Su segundo gol, de tiro libre, el número 600 con el Barcelona,[341]​ fue elegido por la UEFA como el mejor de la temporada.[342]​ Seis días después, en el partido de vuelta en el estadio Anfield de Liverpool, el Barcelona quedó eliminado después de perder 4-0.[343]​ A pesar de la eliminación de su equipo, Messi, con doce goles, fue elegido Delantero de la Temporada.[344]​

El 19 de mayo, en el último partido de liga del Barcelona, marcó dos goles en el empate 2-2 a domicilio contra el Eibar (sus goles 49 y 50 de la temporada en todas las competiciones). Así, con 36 goles en 34 apariciones, recibió su sexto Pichichi.[345]​ El 25, marcó un gol en la derrota 2-1 ante el Valencia en la final de la Copa del Rey. Fue la sexta final de Copa en la que anotó.[346]​

2019-2020: sexto Balón de Oro y Premio Laureus
El 5 de agosto, se anunció que Messi no participaría de la gira del Barcelona por Estados Unidos, ya que se había lesionado la pantorrilla derecha. A fines de ese mes, como aún no se había recuperado, tampoco jugó el primer partido de la temporada.[347]​

El 23 de septiembre ganó el premio The Best 2019,[348]​ el 16 de octubre, su sexta Bota de Oro (la tercera consecutiva, un récord),[349]​ el 25 de noviembre, la UEFA lo incluyó en el mejor equipo del siglo xxi y el 1 de diciembre se convirtió en el primer futbolista en recibir seis veces el Balón de Oro.[350]​[351]​

Me hubiera gustado jugar con Messi
—Pelé en una entrevista con La Gazzetta dello Sport en noviembre de 2019 para conmemorar los cincuenta años de su gol número mil.[352]​
En un partido de La Liga 2019-2020 el 7 de diciembre ante el Mallorca en el Camp Nou, anotó su trigésimo quinto hat-trick, con lo que superó a Cristiano Ronaldo como jugador con más tripletes en la primera división española.[353]​ Hasta esa fecha, había generado hasta un 64 % de los goles del equipo, por lo que su incidencia en el juego colectivo era mucho mayor que la de los años anteriores.[354]​

Como local en el 4-1 contra el Alavés el 21, llegó por novena vez y sexta consecutiva a los 50 goles (45 con el club y 5 con la selección) en un año calendario.[355]​[356]​

El 9 de enero de 2020, en las semifinales de la Supercopa de España, se convirtió en el jugador con más partidos jugados en esa competición, además de alcanzar su gol número 14.[357]​

Con Quique Setién como nuevo entrenador, Messi retrasó su posición en el campo y pasó a jugar más de 10 que de falso 9, lo que supuso una disminución en cantidad de goles y un aumento de asistencias.[358]​ Anotó en el 1-0 contra el Granada el 19 de enero, día del debut de Setién,[359]​ pero no volvió a hacerlo hasta el 22 de febrero, cuando convirtió el sexto y más rápido poker de su carrera en un partido ante el Eibar.[360]​[361]​

El 17 de febrero, luego de seis nominaciones,[362]​ se convirtió en el primer futbolista y el primer argentino en recibir el Premio Laureus al mejor deportista del año.[363]​

En el empate 2-2 contra el Real Madrid el 30 de junio, marcó de penalti su gol 700 (630 con su club y 70 con la selección), cantidad que sólo habían logrado Romario, Bican, Puskás, Pelé, Gerd Müller y Cristiano Ronaldo. El 19 de julio, en el último encuentro de la temporada, tras su doblete en el 5-0 ante el Alavés, fue máximo goleador (25) y mejor proveedor de asistencias (21) en La Liga, con lo que batió el récord de 20, perteneciente a Xavi.[364]​

El 16 de julio, a pesar del empate provisorio de Messi, el Barcelona perdió 2-1 contra el Osasuna. Con este resultado y con la victoria 2-1 del Real Madrid sobre el Villarreal, fue subcampeón de La Liga una jornada antes de que terminara el torneo.[365]​

El 8 de agosto en el Camp Nou, en el partido de vuelta de los octavos de final de la Liga de Campeones 2019-2020 contra el Napoli, marcó dos goles (el segundo, anulado por haber usado la mano) y obtuvo un penalti que ejecutó Luis Suárez.[366]​ Su gol fue elegido por la UEFA el mejor de la temporada.[367]​ Con una victoria 3-1, el Barcelona se clasificó a cuartos de final contra el Bayern Múnich.[366]​ El 15 de agosto, Messi sufrió la peor derrota de toda su carrera cuando el Bayern Múnich aplastó al Barcelona por 8 a 2 en un único partido en Lisboa.[368]​

Deseo de abandonar Barcelona
Tras su creciente descontento con la dirección del Barcelona dentro y fuera del campo,[369]​ el 25 de agosto Messi les comunicó a los abogados del club que rescindiría su contrato amparándose en la cláusula 24, que le permitía irse sin tener que pagar los 700 millones de euros de la cláusula de rescisión. Sin embargo, el Barcelona manifestó que esa cláusula había vencido el 10 de junio, a lo que los abogados del jugador respondieron que, debido a la suspensión de los torneos por la pandemia de COVID, debía considerarse el 23 de agosto como fecha fin de la temporada.[370]​[371]​ La decisión de Messi, además de tener una significativa repercusión en los medios, fue apoyada por compañeros y excompañeros e incluso por el presidente catalán, Quim Torra.[372]​ Al día siguiente, Ramón Planes, director deportivo del Barcelona, reiteró el deseo del club de "construir un equipo alrededor del jugador más importante del mundo" y afirmó que la junta directiva quería, de forma unánime, que se quedara.[373]​ El 30 de agosto, La Liga emitió un comunicado en el que indicaba que el contrato y la cláusula de rescisión aún estaban activos.[374]​El 4 de septiembre, Jorge Messi le envió un comunicado en respuesta, en el que afirmaba que una de las cláusulas del contrato establecía que la "indemnización no aplicará cuando la resolución del contrato por decisión unilateral del jugador tenga efectos a partir de la finalización de la temporada deportiva 2019-20". Momentos después, La Liga reiteró su declaración.[375]​ Esa noche, en una entrevista con Goal, Messi anunció que continuaría hasta el último año de su contrato y que había manifestado su deseo de irse varias veces y que el presidente, Josep Bartomeu, había dicho que podría decidirlo al final de cada temporada pero, como Bartomeu se refería sólo a la cláusula de rescisión, sólo tenía dos opciones: quedarse o ir a juicio, pero afirmó: "Nunca iría a juicio contra el club de mi vida".[376]​

Etapa con Ronald Koeman y despedida del club
2020-2021: máximo goleador histórico de clubes
Messi se incorporó a los entrenamientos de pretemporada con el nuevo técnico, Ronald Koeman, el 7 de septiembre, una semana más tarde de que hubieran empezado.[377]​ Cinco días después, participó en un amistoso ante el Nástic de Tarragona que el Barcelona ganó 3-1.[378]​

El 19 de septiembre, el Barcelona ganó 1-0 ante el Elche el Trofeo Joan Gamper.[379]​ El 26 ante el Villarreal, por la primera fecha de La Liga 2020-2021, Messi igualó la marca de Xavi y Rexach de jugadores con más temporadas en el club (17).[380]​ El 7 de noviembre, por la novena jornada de La Liga ante el Betis en el Camp Nou, entró en el segundo tiempo y marcó dos (uno de penalti) de los cinco goles con que el Barcelona ganó 5-2.[381]​

El 14 de diciembre, fue incluido como extremo derecho en el Dream Team del Balón de Oro, y el 17 en el equipo ideal del año FIFA/FIFPro World XI.[382]​[383]​

El 19, por la decimocuarta fecha de Liga, el Barcelona empató 2-2 como local ante el Valencia.[384]​ Messi, tras errar un penal ante Jaume Doménech, en la misma jugada remató de cabeza y metió el primer gol en el minuto '49, con lo que igualó los 643 goles de Pelé con el Santos.[385]​ El jugador brasileño lo felicitó en Instagram por el logro y por su trayectoria en el club, a la vez que le expresó su admiración.[386]​

El 21 de diciembre, al recibir su séptimo trofeo Pichichi, el cuarto consecutivo, superó a Zarra en cantidad de premios e igualó a Di Stefano y Hugo Sánchez, quienes también lo recibieron en cuatro ediciones seguidas,[387]​ y a Gerd Müller y Eusebio como más veces mejor goleador en sus respectivas ligas.[388]​[389]​

Superó el récord de Pelé como máximo goleador en la historia del fútbol en un mismo club el 22 de diciembre, tras convertir el último gol en el partido que el Barcelona ganó 3-0 como visitante al Valladolid.[390]​

El 1 de enero de 2021, la IFFHS lo ubicó en el segundo puesto de Mejor Goleador del siglo xxi, detrás de Cristiano Ronaldo. Messi había convertido 715 goles oficiales (451 en la liga española, 67 en copas nacionales, 126 en competiciones internacionales de clubes y 71 en la selección argentina),[391]​ lo eligió mejor jugador de 2020 de la Conmebol y mejor creador de juego de la década 2011-2020,[392]​[393]​ además de incluirlo en los mejores equipos mundial y Conmebol de la década 2011-20.[394]​[395]​ El 7 de febrero, lo nombró mejor jugador de la década 2011-2020[396]​

Messi tuvo el segundo mejor arranque liguero de su carrera, con cuatro goles antes del 10 de enero.[397]​El 17 de enero, en la final de la Supercopa de España que ganó 3-2 el Athletic Club, recibió su primera tarjeta roja con el Barcelona tras un cruce con Asier Villalibre.[398]​ Después de cumplir la suspensión de dos partidos, regresó contra el Rayo Vallecano en un partido de Copa del Rey, que el Barcelona ganó 2-1 con un gol suyo.[399]​ Al haber participado en 76 encuentros, superó a Josep Samitier como jugador de su club con más partidos en la historia de ese torneo.[400]​

El 31 de enero, el diario El Mundo publicó su contrato de renovación de 2017, que era, hasta esa fecha, el mayor en la historia del deporte.[401]​

El 16 de febrero, por octavos de final de la Liga de Campeones 2020-2021 en el Camp Nou, Messi convirtió, de penalti, el único gol de los locales, que perdieron 4-1 contra el PSG.[402]​ El 10 de marzo, marcó el gol del empate 1-1 y falló un penalti en el partido de vuelta, en el que el Barcelona quedó eliminado. Sería su último partido en esa competición con el club.[403]​

El 15 de marzo, con dos goles en el 4-1 frente al Huesca, se convirtió en el primer jugador en anotar al menos veinte goles por trece temporadas consecutivas de Liga.[404]​ El 21, contra el Real Sociedad en el Reale Arena, desplazó a Xavi como jugador con más partidos oficiales en la historia del club (768 contra 767) y marcó su gol número 700 en el equipo (663 en partidos oficiales y 37 en amistosos).[405]​[406]​

El 17 de abril, en la final de la Copa del Rey, jugada en el estadio de La Cartuja de Sevilla, el Barcelona superó al Athletic 4-0 con dos goles de Messi, que ganó su primera copa como capitán.[407]​ Fue nombrado mejor jugador del partido, igualó, junto con Piqué y Sergio Busquets, las siete copas ganadas de Piru Gaínza y José María Belauste y, con nueve goles, superó a Zarra (ocho) como máximo goleador en finales de ese torneo,[408]​ además de batir su propio récord de número de finales en las que anotó (siete, de diez jugadas).[409]​[410]​ Se convirtió también en el jugador que marcó más de treinta goles en todas las competiciones por trece temporadas seguidas y el ganador de más títulos (35) en la historia del Barcelona.[411]​[412]​

Contra el Getafe el 22 de abril, con dos goles en el 5-2 del Barcelona, llegó a los 469 en La Liga y superó así a Pelé (468) como máximo goleador en una misma liga.[413]​ Su récord, sin embargo, quedó finalmente en 474 goles,[414]​ cuando marcó, de cabeza, ante el Celta de Vigo el 16 de mayo en el Camp Nou,[415]​ lo que lo llevó a ser el máximo goleador histórico de ese torneo.[222]​ Éste sería su último partido con el Barcelona, el 778, y en el que marcó su gol 672,[416]​ número que le valió ser reconocido por la IFFHS como máximo goleador en la historia en un mismo club.[417]​

El 21 de mayo, Koeman le dio permiso para adelantar sus vacaciones, por lo que no jugó ante el Eibar el último partido de La Liga,[418]​ en la que el Barcelona terminó en tercer lugar.[419]​

Sin haber aclarado si renovaría o no su contrato,[420]​ el 26 de mayo viajó a Argentina para comenzar los entrenamientos para las eliminatorias del Mundial 2022 y la Copa América.[421]​

Fin del contrato
Cuando el 30 de junio venció su contrato, Messi pasó a ser agente libre, pero las negociaciones para continuar en el Barcelona estaban encaminadas.[422]​ El 14 de julio, y aunque aún faltaban ajustar algunos detalles del contrato, trascendió que firmaría por cinco años más y se rebajaría el sueldo a la mitad.[423]​ El 5 de agosto, sin embargo, y a pesar de que La Liga había aprobado el nuevo contrato, Laporta le comunicó a Jorge Messi que, por cuestiones de presupuesto, no podía renovar al jugador,[424]​ y el Barcelona anunció que no podía retenerlo, pues implicaba sobrepasar el tope de gastos previstos por La Liga. Messi dejó el club con treinta y cinco títulos ganados (entre ellos diez Ligas y cuatro Ligas de Campeones).[425]​ En la conferencia de despedida en el Auditori 1899 del Camp Nou, afirmó: "No sé si lo hizo el club, pero yo tengo claro que hice todo lo posible para quedarme. Estaba todo arreglado. Me bajé el sueldo un 50 %. El resto es mentira. Y, después, nadie me pidió nada más".[426]​

Paris Saint-Germain F. C.
2021-2022: octavo Pichichi y séptimo Balón de Oro

Mbappé, Messi y Neymar en el PSG en 2021.
El 10 de agosto, Messi firmó con Paris Saint-Germain un contrato por dos años, con opción de extenderlo una temporada. Se le fijó el salario en 6,5 millones de euros y se le dio el dorsal 30, el mismo con el que había debutado en el Barcelona.[427]​[428]​ Ese día, el club anunció su llegada con un video en sus redes sociales.[429]​

Messi jugó su primer partido el 29 de ese mes, ante el Stade de Reims por la cuarta fecha de la Ligue 1.[430]​ Ingresó en el minuto '65, en sustitución de Neymar, en un partido que acabó 0-2 a favor de su equipo.[431]​ El 28 de septiembre, en la segunda jornada del Grupo A de la Liga de Campeones ante el Manchester City de Guardiola, que el PSG ganó 2-0, marcó su primer gol después de una pared con Mbappé.[432]​ Alcanzó así la marca de Benzema de diecisiete temporadas consecutivas anotando en esa competición.[433]​

El 19 de octubre, en el 3-2 ante el Leipzig en el tercer partido de clasificación en la Liga de Campeones, hizo su primer doblete, el segundo gol, de penal a lo Panenka, después de una falta sobre Mbappé en el área rival.[434]​

Messi será el jugador que más Balones de Oro gane en la historia. Probablemente ganará cinco, seis o siete Balones de Oro, es imparable.
—Johan Cruyff a Olé en 2011[435]​
El 20 de noviembre, por la decimocuarta fecha, anotó su primer gol en la Ligue 1 en el 3-1 ante Nantes.[436]​ El 28, marcó un hat-trick de asistencias frente al Saint-Étienne, dos a Marquinhos y una a Ángel Di María, en el 1-3 de su equipo en el estadio Geoffroy-Guichard.[437]​

Al día siguiente, ganó su octavo Pichichi y su séptimo Balón de Oro.[438]​[439]​ Periodistas, jugadores y exjugadores cuestionaron esa elección,[440]​ a tal punto que France Football decidió modificar los criterios de selección y evaluación del premio.[441]​

El 7 de diciembre, en la última jornada de clasificación para octavos de final de la Liga de Campeones, anotó otro doblete en el 4-1 ante Brujas. En ese partido, igualó a Cristiano Ronaldo como jugador que a más equipos (38) les ha convertido goles en la competición europea y, con 758 goles como profesional, superó a Pelé (757).[442]​

En diciembre, la IFFHS lo incluyó en el equipo Conmebol del año y lo reconoció como mejor jugador y creador de juego de esa confederación.[443]​[444]​

Durante sus vacaciones en Argentina, Messi se contagió coronavirus, por lo que tuvo que aislarse en su casa de Funes desde el 28 de diciembre. Tras dar negativo en una nueva PCR, el 5 de enero pudo volver a París, donde se le realizarían exámenes para descartar secuelas.[445]​ El 22 jugó su primer partido del año, por la vigésimo segunda fecha de la Ligue 1 ante Reims. Entró en la segunda mitad del encuentro, que su equipo ganó 4-0.[446]​

El 17 de enero, fue incluido en el FIFA FIFPro World XI.[447]​

El 31 de enero de 2022, frente a Niza en octavos de final de la Copa de Francia 2021-22, jugó un partido regular, pero anotó en la tanda de penales tras el empate 0-0. El PSG perdió 6-5 y quedó eliminado, después de haber ganado ese torneo en seis de los siete años anteriores.[448]​

El 15 de febrero, en octavos de final de la Champions League 2021-22 ante el Real Madrid, Messi erró un penal en el partido de ida que terminó 1-0 con gol de Mbappé.[449]​ En la vuelta en el Santiago Bernabéu el 9 de marzo, el PSG quedó eliminado tras perder 3-1.[450]​ Algunos medios franceses criticaron el desempeño de Messi en ambos partidos: L'Équipe lo calificó con un 3 en el primero y un 6 en el segundo, para el que Le Parisien le puso un 4.[451]​ En el siguiente encuentro como locales, ante el Bordeaux, los jugadores del PSG fueron abucheados y silbados, especialmente Messi y Neymar.[452]​

Con 125 goles, Messi figuró en el segundo puesto de la lista de Máximos goleadores históricos de la Champions League, por detrás de Cristiano Ronaldo, con 140. Ambos jugadores son los únicos en haber marcado más de cien veces en la historia de ese torneo.[453]​

El 23 de abril, ganó su primer título con el PSG, la Ligue 1.[454]​ Con once goles y catorce asistencias en 33 partidos,[455]​ fue la temporada que menos jugó y anotó, si se exceptúan las dos primeras con el Barcelona.[456]​

2022-2023
El 31 de julio en el Estadio de Bloomfield de Tel Aviv, marcó, con la derecha, el primer gol del 4-0 contra Nantes, resultado con el que el PSG ganó la Supercopa de Francia, su primer título de la temporada.[457]​ El 6 de agosto, en la primera fecha de la Ligue 1, jugada en el Stade Gabriel Montpied contra Clermont Foot, hizo un doblete en el 5-0 de su equipo. El segundo gol, anotado de chilena, fue el primero que marcó de esta forma.[458]​

En enero de 2023, la IFFHS lo reconoció Mejor Goleador Internacional y Mejor Jugador del Mundo, en el segundo caso por una significativa diferencia de votos (275 contra 35 y 30) con Mbappé y Benzema.[459]​[460]​

El 26 de febrero, frente al Olympique de Marsella por la Ligue 1, tras una asistencia de Mbappé, anotó su gol número 700 en clubes.[461]​ Al día siguiente, ganó su segundo premio The Best y, en mayo, otro Laureus.[462]​[463]​

El 8 de abril, con un gol y una asistencia a Sergio Ramos en el 2-0 frente a Niza,[464]​ alcanzó los 702 goles y superó a Cristiano Ronaldo como máximo goleador histórico en clubes de Europa.[465]​ El 27 de mayo, anotó contra Estrasburgo en el Stade de la Meinau y el PSG fue campeón de la Ligue 1 cuando aún faltaba una fecha.[466]​ Fue su gol número 496 en ligas, con lo que se convirtió en el máximo goleador histórico de las cinco grandes ligas de Europa.[467]​

El 1 de junio, el entrenador Christophe Galtier confirmó que Messi jugaría su último partido el 3 de junio ante Clermont porque,[468]​ pese a que el contrato establecía un año opcional, prefirió irse el 1 de julio como agente libre.[469]​ Dejó el club con 32 goles y 35 asistencias en setenta y cinco partidos.[469]​

Inter Miami

Messi con el Inter Miami en la U.S. Open Cup 2023
Luego de que se hablara sobre una posible vuelta a Barcelona y de un fichaje con Al-Hilal, el 7 de junio Messi anunció en una entrevista con Mundo Deportivo que firmaría contrato con el Inter Miami.[470]​ El club lo presentó el 16 de julio en el estadio DRV PNK y anunció que usaría el dorsal número 10.[471]​

El primer partido de Messi fue el 21 de julio ante Cruz Azul por la primera jornada del Grupo 3 de la Zona Sur de la Leagues Cup. Ingresó en el minuto 54 por Benjamin Cremaschi y en el minuto 94 marcó de tiro libre un gol con el que su club ganó 2-1.[472]​ Fue capitán a pesar de ser suplente y, tres días después, Martino anunció que lo había ratificado en el puesto.[473]​ El 19 de agosto, en la final contra Nashville SC, marcó el primer gol y, tras un empate 1-1, anotó en la definición por penales. El Inter Miami ganó 10-9 y consiguió así su primer título.[474]​ Con diez tantos y cuatro asistencias, Messi fue el máximo goleador y MVP del torneo.[475]​[476]​

El 26 de agosto, en el Red Bull Arena contra New York Red Bulls, jugó por primera vez en la MLS. Ingresó a los 15' del segundo tiempo y anotó un gol para el 2-0 de su equipo.[477]​ Terminó la temporada con once goles y cinco asistencias en catorce partidos y fue elegido Jugador más valioso de Inter Miami.[476]​


Messi en Inter Miami en 2025
El 30 de octubre recibió un octavo Balón de Oro y,[478]​ el 19 de diciembre, un cuarto Olimpia de Oro (compartido con Belén Casetta) y un decimosexto Olimpia de Plata, tres nuevos récords.[208]​[479]​ El 15 de enero de 2024 ganó su tercer The Best. A pesar de haber obtenido la misma cantidad de puntos que Erling Haaland, lo ganó porque fue el más votado como primero por los capitanes de selección.[480]​ Diarios noruegos como Verdens Gang y Dagbladet y el británico Manchester Evening News criticaron la elección, ya que Haaland había ganado la Premier League, la Champions League y la FA Cup con Manchester City y sido Bota de Oro europea, máximo goleador de la Premier League y de la Champions, mientras que Messi sólo ganó la Ligue 1 y la Leagues Cup.[481]​[482]​ Por su parte, tanto Marca como Olé publicaron que, dada la diferencia de logros entre uno y otro jugador, la entrega del premio ponía en cuestión la credibilidad de la FIFA y su proceso de votación.[483]​[484]​ Messi también fue incluido en el FIFA FIFPro World XI por decimoséptima vez.[99]​

El 13 de marzo de 2024, anotó un gol y le dio una asistencia a Luis Suárez en el 3-1 contra Nashville SC por la Copa de Campeones de la Concacaf, pero se lesionó el isquiotibial derecho y tuvo que salir a los cuatro minutos del tiempo suplementario.[485]​[486]​ Volvió a jugar el 6 de abril con Colorado Rapids en la MLS, partido en el que ingresó en el segundo tiempo y marcó a los doce minutos.[487]​

El 2 de octubre, convirtió un doblete en el 3-2 contra Columbus Crew y su equipo ganó la Supporters' Shield,[488]​ trofeo que se otorga al mejor equipo de la temporada regular de la MLS. Messi alcanzó así su título número 46.[489]​[490]​

Selección nacional
Categorías inferiores

Placa dedicada a Messi en el Paseo de los Olímpicos de Rosario
En 2002, Jorge Messi le hizo llegar a Hugo Tocalli, responsable de las divisiones juveniles de Argentina, un video compilatorio de las jugadas de su hijo. A pesar de reconocer las cualidades del adolescente, el entrenador le respondió que no podía incorporarlo al plantel, porque ya tenía definido el equipo para el Mundial del año siguiente en Finlandia, pero que lo tendría en cuenta para otra competición.[491]​[492]​ En 2003, sin embargo, y aunque sabía que la Federación Española de Fútbol quería ficharlo para su selección sub-17,[491]​ tampoco lo convocó para el Mundial Sub-20 en Emiratos Árabes.[492]​ El 30 de marzo de 2004, se reunió con el presidente de la AFA Julio Grondona y, por sugerencia de José Pékerman (quien había visto a Messi contra el Alcorcón), le propuso organizar un encuentro amistoso para impedir toda posibilidad de que jugara para España.[19]​[493]​[492]​ En abril, finalmente, Messi recibió una citación por fax para un entrenamiento en junio en el predio de Ezeiza.[492]​ El jugador ya había declinado, alrededor de 2003, reiteradas ofertas de jugar para España, porque quería representar a su país.[494]​[495]​

El 29 de junio de 2004, casi desconocido en Argentina, debutó en el estadio Diego Armando Maradona de Buenos Aires con la categoría sub-20, en un partido amistoso con una sub-22 de Paraguay armada para la ocasión que arbitró Gabriel Brazenas.[492]​ Ingresó en el segundo tiempo por Ezequiel Lavezzi e hizo un gol y dos asistencias en un encuentro que finalizó 8-0 a favor de Argentina.[19]​ El 3 de julio, contra Uruguay en el estadio Suppicci de Colonia, hizo un doblete en otro amistoso que Argentina ganó 4-1.[496]​ Con solo estos dos partidos jugados, a fines de diciembre Tocalli lo convocó para el Sudamericano Sub-20 de principios del año siguiente, aunque, por decisión conjunta con Pékerman, jugaría siempre como suplente.[497]​

Sudamericano Sub-20 2005
En el primer partido de Argentina en el Campeonato Sudamericano Sub-20 de Colombia, el 13 de enero contra Venezuela, Messi entró a los 59 minutos por Lavezzi y anotó el segundo gol del 3-0.[497]​ El 15, convirtió un doblete en el 4-0 a Bolivia.[498]​ Fue titular por primera vez el 17 en el 6-0 ante Perú, donde marcó el quinto gol.[499]​ En el 1-1 con Colombia el 21, volvió a ser suplente y no convirtió.[500]​

En la hexagonal final, Argentina le ganó 1-0 a Venezuela, con gol en contra de José Luis Granados el 25 de enero,[501]​ empató 1-1 con Chile el 27, 0-0 ante Uruguay el 30 y 1-1 con Colombia el 2 de febrero.[502]​[503]​ El 6 de febrero, en el clásico de América contra Brasil, ganó 2-1 con un gol de Messi, quien había ingresado en el minuto 65,[504]​ y se clasificó en tercer lugar al torneo mundialista que tendría lugar en Países Bajos.[505]​ Messi, con cinco tantos, ocupó el segundo puesto en la tabla de goleadores.[506]​

Mundial Sub-20 2005
El 11 de junio, Messi no fue titular en el primer partido de Argentina en el Mundial Sub-20 de Países Bajos contra Estados Unidos, pero sí en los otros seis.[507]​ Como no había querido exigirlo porque tenía una contractura, el DT Francisco Ferraro lo hizo ingresar en el segundo tiempo del encuentro que Argentina perdió 1-0. En el 2-0 contra Egipto el 14, Messi metió un gol y,[508]​ el 18, inició con un centro la jugada del gol de Neri Cardozo en el 1-0 contra Alemania.[509]​ El 22, en octavos de final, puso el 1-1 parcial en el 2-1 contra Colombia,[510]​ en cuartos el 25, dio una asistencia y marcó el último gol en el 3-1 contra España y,[511]​ el 28 en semifinales, anotó el primer gol del 2-1 frente a Brasil. En la final contra Nigeria el 2 de julio, ejecutó dos penales con los que su equipo ganó 2-1.[508]​ Al final del campeonato, recibió la Bota de Oro y el Balón de Oro.[512]​

Su participación en los dos torneos juveniles supuso una mayor repercusión a nivel internacional y también que comenzara a hacerse conocido en Argentina.[513]​[19]​ Hacia fines de ese año, el diario La Nación lo señalaba como la revelación del fútbol argentino y posible sucesor de Maradona,[514]​ mientras que Clarín le otorgó el Clarín de Oro a la Revelación del año y el Círculo de Periodistas Deportivos, el Olimpia de Plata.[91]​[515]​

Juegos Olímpicos 2008
Véase también: Anexo:Torneo masculino de fútbol en los Juegos Olímpicos de Pekín 2008

Messi en semifinales frente a Brasil en los Juegos Olímpicos de Pekín 2008
El 24 de mayo de 2008, Messi jugó por primera vez con la selección sub-23, dirigida por Sergio Batista, en un amistoso contra Cataluña que Argentina ganó 1-0.[516]​

El 17 de junio, el Barcelona le informó a la AFA que no cedería a Messi para los Juegos Olímpicos de Pekín por considerar que, al no ser una competición oficial de la FIFA, la reglamentación no lo obligaba y porque quería contar con "una de las piezas claves del equipo" en las preliminares de la Liga de Campeones.[517]​[518]​ La AFA, entonces, solicitó la intervención de la FIFA, que dictaminó que era obligatorio ceder a los jugadores menores de veintitrés años.[519]​ Por consiguiente, el 3 de julio el técnico lo incluyó en el plantel que jugaría en Beijing,[520]​ con la idea de que fuera su "principal carta ofensiva".[521]​ Como el Barcelona no cejaba en su postura,[522]​ Jacques Rogge, presidente del Comité Olímpico Internacional, anticipó el 19 de julio que, de seguir en su negativa, el club no podría contar con Messi hasta el 24 de agosto,[523]​ mientras que el presidente de la FIFA, Joseph Blatter, demandó cuatro días más tarde que dejara ir al jugador.[522]​ Tras el fallo final de la FIFA a favor de la AFA el 30 de julio, el Barcelona decidió llevar el litigio al Tribunal de Arbitraje Deportivo (TAS),[524]​ que el 6 de agosto anuló la obligatoriedad de liberarlo.[525]​ Messi, mientras tanto, había viajado el 31 de julio a Beijing, porque Batista había dicho que no podía seguir esperándolo.[526]​ Finalmente, el 8 de agosto Txiki Begiristain, secretario técnico del Barcelona, anunció que había acordado con Grondona que se le permitiría al jugador seguir en Beijing, si la AFA costeaba el seguro médico en caso de lesión y no lo convocaba para ningún amistoso de la temporada.[527]​

El 7 de agosto, ante Costa de Marfil, Messi marcó el primer gol y asistió a Lautaro Acosta en el segundo, con el que Argentina ganó 2-1.[528]​ Jugó ante Australia el 10 de agosto,[529]​ pero no el 13 frente a Serbia, ya que Batista había decidido reservarlo para los cuartos de final.[530]​ En cuartos de final contra Países Bajos, metió el primer gol, tras eludir al arquero. Después del empate del contrario, en el último minuto del primer tiempo adicional le dio un pase a Di María, quien convirtió otro gol.[531]​ El 19 de agosto, frente a Brasil, realizó un muy buen partido, que finalizó 3-0 con dos goles de Sergio Agüero y uno de Juan Román Riquelme.[532]​

El 23 de agosto, después de ganarle 1-0 a Nigeria en el Estadio Nacional, con asistencia de Messi para el gol de Di María, los jugadores argentinos recibieron el oro olímpico.[533]​

Selección absoluta
Etapa Pékerman
Primeras convocatorias (2005-2006)

Messi, máximo goleador histórico y capitán por más de diez años de la selección argentina.
El 2 de agosto de 2005, Pékerman convocó por primera vez a Messi para jugar con la selección absoluta.[534]​ El jugador debutó el 17 de agosto en un amistoso con Hungría que Argentina ganó 2-1 en el estadio Ferenc Puskás de Budapest. Ingresó en el minuto 66 y llegó a tocar tres pelotas, pero 1m32s después, fue expulsado por Markus Merk tras un gesto brusco hacia el defensor Vilmos Vanczák, que lo había tironeado de la camiseta.[535]​

Jugó su primer partido oficial el 3 de septiembre, en las eliminatorias del Mundial 2006 contra Paraguay en Asunción. Entró en el minuto '80 del partido que Argentina perdió 1-0. Fue titular el 9 de octubre frente a Perú en el estadio Monumental de Buenos Aires, donde jugó por primera vez en su país natal. A pesar de que aún era poco conocido, los hinchas argentinos lo ovacionaron antes y después del partido, en el que fue la figura.[536]​ En la última fecha de eliminatorias, el 12 de octubre ante Uruguay, ingresó en el segundo tiempo.[537]​

Jugó un amistoso contra Catar el 16 de noviembre, que Argentina ganó 3-0,[538]​ y el 1 de marzo de 2006 metió su primer gol en otro amistoso contra Croacia en el estadio St. Jakob Park de Basilea, que Argentina perdió 3-2.[539]​ También jugó un muy buen partido el 30 de mayo en un amistoso con Angola, ganado 2-1 por Argentina en el estadio Arechi de Salerno.[540]​

Mundial 2006
Véase también: Argentina en la Copa Mundial de Fútbol de 2006
Aunque Messi había jugado sólo tres partidos por eliminatorias,[541]​ el 16 de mayo Pékerman confirmó que lo había incluido en la lista de veintitrés para el Mundial de Alemania aunque,[542]​ como no estaba totalmente recuperado de un desgarro sufrido en marzo y había pasado ochenta y cuatro días inactivo, no había aún decidido si sería o no titular.[541]​[543]​ El jugador, con dieciocho años y 357 días, es el futbolista argentino más joven en participar en un mundial.[544]​ Debutó en el segundo partido de Argentina, ante Serbia y Montenegro. Ingresó en el segundo tiempo, dio una asistencia de gol a Hernán Crespo y marcó el 6-0 final en el minuto 88,[545]​ lo que lo convirtió en el argentino más joven en anotar en una Copa del Mundo.[544]​ Fue titular contra Países Bajos (0-0) y, en octavos de final ante México, entró en el minuto 84 y anotó un gol en el tiempo de descuento que hubiera marcado el desempate, pero se lo anuló el juez de línea. Se debió, entonces, jugar la prórroga, en la que Argentina ganó 2-1.[546]​ Messi no participó en cuartos de final frente a Alemania, que eliminó a Argentina en los penales.[547]​ Buena parte de la prensa y de la opinión general, tanto argentina como española, criticó esa decisión de Pékerman,[548]​[549]​ quien anunció su renuncia en la conferencia post partido.[550]​ Lo sucedió Alfio Basile, que fue nombrado en agosto y asumió el cargo en septiembre.[551]​

Etapa Basile
El 3 de septiembre de 2006, Messi jugó en el partido debut de Basile, un amistoso contra Brasil disputado en Londres que Argentina perdió 3-0.[552]​ Participó también el siguiente amistoso, el 11 de octubre ante España en el estadio Nueva Condominas de Murcia que ganaron 2-1 los locales.[553]​

Copa América 2007
Véase también: Argentina en la Copa América 2007
El 5 de junio de 2007, en un amistoso contra Argelia, Messi convirtió su primer doblete con la selección.[554]​

El 28 de junio, en el 4-1 contra Estados Unidos en la Copa América, jugó 79 minutos y dio una asistencia de gol a Crespo.[555]​ El 2 de julio, ante Colombia, provocó el penal del 1-1 para un 4-2 a favor de Argentina, antes de ser sustituido en el minuto 83.[556]​ Contra Paraguay el 5, entró en el minuto 67 de un encuentro que finalizó 1-0.[557]​

En cuartos de final el 9, convirtió el segundo gol del 4-0 ante Perú.[558]​ El 12, en semifinales ante México, tras pase de Carlos Tévez, marcó un gol de vaselina en el 3-0 de Argentina.[559]​ Después del partido, Basile afirmó: "Sólo los genios son capaces de hacer un gol como el que hizo Messi".[560]​ El 15 de julio, en la final contra Brasil, Argentina perdió 3-0, con un gol de contra de Roberto Ayala.[561]​

Messi fue elegido mejor jugador joven e integrante del "once ideal".[562]​

El 16 de octubre de 2008, después de perder 1-0 ante Chile en las eliminatorias sudamericanas el día anterior, Basile presentó su renuncia.[563]​ Lo sucedió en el cargo Diego Maradona.[564]​

Etapa Maradona
Como el Barcelona había acordado con la AFA que no participaría en amistosos,[565]​ el 19 de noviembre Messi no jugó en el debut de Maradona como entrenador, un partido contra Escocia que ganó Argentina 1-0,[566]​ pero sí lo hizo en el siguiente contra Francia, el 11 de febrero de 2009, donde marcó un gol en el 2-0 de su equipo.[567]​

El 28 de marzo, en su primer partido oficial como DT, la fecha 11 de las eliminatorias ante Venezuela en el estadio Monumental, Maradona decidió darle a Messi la camiseta número 10.[568]​ Messi fue fundamental en el partido que ganó Argentina 4-0: lideró el trío de ataque que conformaba con Tévez y Agüero, convirtió un gol y dio una asistencia para el segundo. Los medios argentinos resaltaron su juego, así como también el interés que generaba la presencia simultánea de los dos "10" en el equipo.[569]​ El 1 de abril, de visitante ante Bolivia, Messi pateó dos veces al arco, pero no pudo anotar en el partido que Argentina perdió 6-1, el primero en el que recibió seis goles desde el Mundial de Suecia de 1958.[570]​

En un amistoso con España el 14 de noviembre marcó, de penal, el momentáneo 1-1 de un partido que Argentina perdió 2-1.[571]​

Mundial 2010
Véase también: Argentina en la Copa Mundial de Fútbol de 2010

Messi ante Alemania en cuartos de final del Mundial 2010
Messi llegó con una gran presión al Mundial de Sudáfrica, debido a que varios lo consideraban el sucesor de Maradona y su campaña en el Barcelona lo perfilaba para ser la gran figura del torneo.[cita requerida]

El 12 de junio, en el 1-0 contra Nigeria, tuvo un muy buen partido y fue, según el periodista Horacio Pagani, "el responsable del 90 % de las maniobras ofensivas".[572]​[573]​ El 17, contra Corea del Sur, a pesar de jugar más retrasado, funcionó como organizador, enganche y delantero y tuvo incidencia en los cuatro goles del 4-1.[574]​ Para el encuentro contra Grecia el 22, y ante la ausencia de Mascherano en el plantel, Maradona designó capitán a Messi que, con veintidós años, se convirtió en el argentino más joven en cumplir ese papel en un mundial. Argentina ganó 2-0 y Messi fue elegido Jugador Budweiser del partido.[575]​[576]​ El 27, en octavos de final frente a México, Argentina ganó 3-1,[573]​ pero fue eliminada el 3 de julio en cuartos de final, tras perder 4-0 contra Alemania.[577]​

El 27 de julio, la AFA anunció que su comité directivo había acordado "por unanimidad" cesar en su cargo a Maradona.[578]​ Lo sucedió Batista quien, después de tres meses como DT interino, fue oficializado el 2 de noviembre.[579]​

Etapa Batista
Messi participó en siete de los once amistosos que comenzó dirigiendo Batista. En el debut del entrenador, el 10 de agosto en el Aviva Stadium de Dublín contra Irlanda, a la que Argentina ganó 1-0, no anotó y fue sustituido a los 58 minutos.[580]​ Contra España como local el 7 de septiembre, convirtió el primer gol del 4-1, después de no haber anotado desde el 14 de noviembre del año anterior.[581]​[582]​ El 11 de noviembre hizo el único tanto en el 1-0 frente a Brasil y, con Japón el 9 de octubre, generó varias ocasiones de gol, pero no fueron aprovechadas y Argentina perdió 1-0.[581]​[583]​ Ya en 2011, el 9 de febrero desempató con un penal el 2-1 ante Portugal y, el 20 de junio, convirtió un tanto y dio dos asistencias en el 4-0 a Albania.[581]​[584]​

Copa América 2011
Véase también: Argentina en la Copa América 2011

Messi frente a Bolivia en el partido inaugural de la Copa América 2011
El 1 de julio de 2011, Argentina, como país anfitrión, jugó contra Bolivia el partido inaugural de la Copa América, que finalizó 1-1.[585]​[586]​ La prensa cuestionó al seleccionado, especialmente a Messi, por el bajo nivel de juego:[585]​ La Nación publicó que no había jugado de nueve y que, "confundido", no se había asociado con ninguno de sus compañeros.[587]​ Olé, por su parte, señaló que no había sido líder y que todo el equipo se había visto superado por un rival "muy inferior".[588]​ El 6 de julio, tras el empate sin goles contra Colombia, los jugadores argentinos se retiraron del campo entre silbidos y a Messi, que había tenido un mal partido,[589]​[590]​ se lo cuestionó por no rendir como en el Barcelona.[591]​ El 11, en el partido contra Costa Rica que Argentina ganó 3-0, Messi asistió en el segundo gol de Agüero y en el de Di María. El público volvió a ovacionar sus jugadas y disminuyeron las críticas hacia él y sus compañeros.[592]​[591]​

En cuartos de final, en el Clásico del Río de la Plata, Pérez marcó el primer gol de Uruguay a los cinco minutos, pero Messi asistió a Gonzalo Higuaín en el tanto del empate. Después de los tiempos extras, Uruguay ganó 4-5 en los penales.[593]​ El equipo argentino fue duramente criticado tras la derrota,[594]​ que fue, además, el último partido de Batista como entrenador.[595]​

A pesar de no haber convertido goles, Messi realizó el mayor número de asistencias (tres) y fue elegido mejor jugador del partido frente a Bolivia y Costa Rica.[562]​[586]​[592]​

Después de que la AFA despidiera a Batista el 25 de julio,[595]​ el 5 de agosto Alejandro Sabella fue nombrado nuevo director técnico.[596]​

Etapa Sabella
Eliminatorias del Mundial 2014
En septiembre de 2011, Sabella designó capitán a Messi en reemplazo de Mascherano.[597]​ El jugador debutó en su nuevo rol el 2 de ese mes en un amistoso contra Venezuela en el estadio Yuba Bharati Krirangan de Calcuta que Argentina ganó 1-0.[598]​

El 7 de octubre, en el primer partido de las eliminatorias del Mundial 2014 contra Chile, marcó el segundo gol del 4-1 a favor su equipo.[599]​ Fue su primer gol en dos años y medio, después de dieciséis partidos oficiales sin convertir.[600]​ El 11 de octubre, de visitante, Argentina perdió 1-0 por primera vez con Venezuela.[601]​


Messi disputa la pelota con Granit Xhaka en un amistoso con Suiza el 29 de febrero de 2012.

Messi en un partido contra Suiza, donde marcaría su primer hat-trick con Argentina.
El 11 de noviembre, después del empate 1-1 con Bolivia, Messi fue, junto con Clemente Rodríguez, el único al que el escaso público argentino no silbó en el Monumental.[602]​ El 15, en el 2-1 contra Colombia, fue la figura del partido, por haber marcado el gol del empate y haber sido fundamental para el segundo tanto, anotado por Agüero.[603]​ Disminuyeron entonces las críticas a Messi, pero se le seguía reprochando que no pudiera brillar jugando para su país como lo hacía en su equipo.[cita requerida]

El 29 de febrero de 2012, hizo su primer hat-trick en la selección en un amistoso con Suiza, que Argentina ganó 3-1 en el Stade de Suisse en Berna.[604]​

El 2 de junio, convirtió un gol en el 4-0 a Ecuador. El 8 de junio, en un amistoso contra la sub-23 de Brasil jugado en Nueva Jersey, marcó su segundo hat-trick con la selección. Su último gol permitió desempatar el 3-3 y Messi se retiró ovacionado del estadio.[605]​[606]​ En otro amistoso contra Alemania el 15 de agosto, anotó un gol en el 3-1 a favor de Argentina.[607]​

El 7 de septiembre, contra Paraguay en el Estadio Mario Alberto Kempes de Córdoba, convirtió su primer gol de tiro libre con Argentina, que ganó 3-1.[557]​ El 11, al igual que sus compañeros, no realizó un buen partido en Lima frente a Perú, que terminó 1-1.[608]​ El 16 de octubre, en el estadio Nacional de Santiago, Argentina le ganó 2-1 a Chile con un gol de Messi,[609]​ que alcanzó el récord de Gabriel Batistuta de doce goles en un año calendario con su selección.[610]​ El 12 de noviembre, contra Uruguay, metió dos goles, el segundo de tiro libre, para un 3-0 final.[611]​ Argentina jugó su último partido el 14 de noviembre, un amistoso con Arabia Saudita empatado sin goles.[612]​

El 22 de marzo de 2013, Messi convirtió un gol e hizo dos asistencias en el 3-0 contra Chile en el estadio Monumental.[613]​ El 26, no jugó un buen partido en el 1-1 frente a Bolivia,[614]​ jugó sólo media hora en el 0-0 contra Colombia el 7 de junio y también fue suplente el 12 en el 1-1 con Ecuador.[615]​[616]​ El 14 de junio, al realizar un triplete en un amistoso frente a Guatemala en el estadio Mateo Flores, llegó a los 35 goles con la selección e igualó a Hernán Crespo como segundo goleador histórico.[617]​ El 10 de septiembre, anotó dos goles de penal y dio una asistencia a Agüero en el partido que Argentina le ganó 2-5 a Paraguay.[618]​ Con este resultado, la selección argentina se clasificó al mundial cuando aún faltaban dos fechas de juego.[619]​ Debido a que se había lesionado el bíceps femoral derecho a fines de septiembre,[128]​ no pudo jugar los encuentros ante Perú y Uruguay.[620]​

La selección argentina quedó en el primer puesto de las eliminatorias de la Conmebol y Messi se ubicó segundo en la tabla de goleadores, junto a Luis Suárez.[621]​[622]​

Mundial 2014
Véase también: Argentina en la Copa Mundial de Fútbol de 2014

Messi disputa el balón con Mats Hummels en la final de Brasil 2014
El 15 de junio, en el primer partido de Argentina en el Mundial de Brasil, contra Bosnia-Herzegovina, Messi anotó el segundo gol, tras una devolución en una pared con Higuaín, para un resultado final 2-1 con gol en contra de Sead Kolašinac.[623]​ El 21, frente a un Irán con una defensa muy poblada durante todo el partido, en el minuto 91 remató desde el borde del área para poner el 1-0.[624]​ En el 3-2 contra Nigeria el 25, convirtió su primer doblete en un mundial: el primer gol en el minuto 3 y el segundo, de tiro libre, en el minuto 45.[625]​


Messi tras perder la final del Mundial 2014
El 1 de julio, tras un empate 0-0 contra Suiza en octavos de final, en el minuto 118 de los tiempos extras, asistió a Di María en el gol.[626]​ Argentina le ganó 1-0 a Bélgica en cuartos de final el 5 de julio.[627]​ El 9 de julio, después de veinticuatro años sin llegar a semifinales, jugó contra Países Bajos. Tras un empate 0-0 en los 90 minutos y los tiempos extras, ganó 4-2 en la tanda de penales, en la que Messi anotó el primero.[628]​ El 13 de julio, en la final con Alemania en el Maracaná, luego de un empate 0-0 se jugó un tiempo suplementario en el que Mario Götze convirtió en el minuto 114. Alemania fue campeón y Argentina, subcampeón.[629]​

Messi, que quedó tercero en la tabla de goleadores, fue elegido Mejor Jugador del Partido contra Bosnia-Herzegovina, Irán, Nigeria y Suiza.[630]​[626]​ Igualó así el récord de Wesley Sneijder de cuatro premios en una misma edición.[631]​ Además, recibió el Balón de Oro, aunque no lo incluyeron en el once ideal. Era la primera vez que la elección recaía en el Grupo de Estudios Técnicos de la FIFA y no en periodistas acreditados para la competición.[632]​ La entrega del premio fue objetada por periodistas, jugadores, exjugadores, directores técnicos y usuarios de redes sociales.[633]​ Algunos afirmaban que se lo habían dado porque su auspiciante, adidas, era el mismo que el del campeonato,[634]​ mientras que otros aludían al peso de Julio Grondona dentro de la FIFA.[635]​ Incluso Blatter, que en un principio dijo sentirse "un poco sorprendido" por la elección de Messi,[632]​ en octubre declaró que había sido "incorrecta".[636]​

El 29 de julio, Sabella presentó su renuncia.[637]​ Bajo su dirección, Messi, con 25 tantos en 32 partidos, fue goleador del equipo, además de superar sus medias de gol con otros entrenadores: 0,78 contra 0,20 (Pékerman), 0,33 (Basile), 0,36 (Batista) y 0,18 (Maradona).[638]​[596]​

Etapa Martino
El 14 de agosto de 2014, Gerardo Martino asumió como nuevo DT. Dirigió su primer partido el 3 de septiembre,[639]​ un amistoso contra Alemania en Düsseldorf, en el que Messi no jugó por estar lesionado.[640]​ Sí participó en los siguientes dos amistosos: el Superclásico de las Américas el 11 de octubre en el Estadio Nacional de Beijing, en el que erró un penal y Argentina perdió 2-0 y el 14 ante Hong Kong en el estadio Hong Kong donde, en apenas media hora de juego, dio una asistencia y marcó dos de los goles del 7-0.[641]​[642]​

En noviembre, Argentina jugó sus dos últimos amistosos del año en Inglaterra. Le ganó 2-1 a Croacia el 12 en el Upton Park de Londres y, seis días más tarde, perdió 1-0 contra Portugal en el Old Trafford. Messi anotó un penal en el primer partido,[643]​ mientras que en el segundo jugó sólo el primer tiempo.[644]​

Copa América 2015
Véase también: Argentina en la Copa América 2015

Messi ejecutando un tiro libre en la Copa América 2015 contra Paraguay
El 13 de junio de 2015, contra Paraguay, Messi anotó en el primer tiempo y puso un momentáneo 2-0 a favor de su equipo, que empató 2-2.[645]​ Cuatro días más tarde, jugó en el 1-0 contra Uruguay. En ambos encuentros fue elegido MVP del partido, aunque sólo lo aceptó en la segunda ocasión.[646]​ El 20 de junio, en el 1-0 contra Jamaica, llegó a los cien partidos con su selección.[647]​ Se convirtió así en uno de los futbolistas argentinos más jóvenes en alcanzar esa marca, junto con Javier Zanetti, Roberto Ayala, Javier Mascherano y Diego Simeone.[648]​[649]​

El 27 de junio, en cuartos de final ante la Colombia de Pékerman, hizo el primero de los penales con los que Argentina ganó 5-4 tras un partido empatado 0-0.[650]​ El 30 de junio, en semifinales contra Paraguay, realizó tres asistencias en un encuentro que Argentina ganó 6-1.[651]​ En la final contra Chile el 4 de julio, jugó bien en el primer tiempo, pero no influyó en el resto del partido. Luego de un empate 0-0 en 120 minutos, Argentina perdió 4-1 en los penales, donde Messi fue el único que no falló.[652]​ Messi fue elegido Mejor Jugador del Torneo, pero se negó a recibir el premio.[562]​

Copa América Centenario
Véase también: Argentina en la Copa América Centenario
El 6 de junio de 2016, Messi no jugó en el 2-1 contra Chile en la Copa América Centenario, porque se había lesionado en un amistoso con Honduras.[653]​ El 10, contra Panamá, entró en el segundo tiempo y, en dieciocho minutos, marcó un hat-trick en un partido que Argentina ganó 5-0.[654]​ También entró en el segundo tiempo el 14 en el 3-0 frente a Bolivia, donde no anotó.[655]​ El 18 de junio, en cuartos de final ante Venezuela, llegó a los 54 goles e igualó a Batistuta como máximo goleador histórico de la selección argentina, aunque lo hizo en más partidos (111 contra 77).[656]​ Superó esa marca tres días después, en la semifinal contra Estados Unidos, donde dio una asistencia a Higuaín y marcó un gol de tiro libre, en un partido que Argentina ganó 4-0.[657]​ Fue nuevamente candidato al premio Puskás por ese gol,[658]​ pero perdió ante Mohd Faiz Subri.[659]​

El 26 de junio, Argentina jugó la final contra Chile en el MetLife Stadium de East Rutherford. Tras un empate sin goles en 120 minutos, ganó la selección chilena 4-2 por penales. A pesar de su muy buen desempeño en toda la competición y de haber jugado un buen partido, Messi, que pateó primero, envió la pelota por encima del travesaño.[660]​[661]​

Renuncia y retorno
A la salida del vestuario, Messi anunció su retiro de la selección argentina, una decisión que ni siquiera les había comunicado a sus compañeros.[662]​[663]​ Hizo referencia a las últimas tres finales perdidas, sobre lo que comentó: "Es increíble, pero no se da. Hoy nos pasó otra vez y otra vez los penales. Son cuatro finales las que me toca perder, las que nos toca perder, tres seguidas... La verdad que es una lástima, pero tiene que ser así. No se da, lo intentamos, lo buscamos, pero ya está. Se terminó para mí la selección".[662]​Sin embargo, el 12 de agosto del mismo año, confirmó en un comunicado de prensa su regreso y que también iba a participar en los partidos de la clasificación para el Mundial 2018.[664]​

Eliminatorias del Mundial 2018
Es un jugador que no se puede describir, sólo hay que verlo, maravillarse y admirarlo. Messi es un jugador con un nivel por encima de todos los demás.
—Óscar Washington Tabárez, entrenador de Uruguay, luego del partido contra Argentina en la Clasificación de Conmebol para la Copa Mundial de Fútbol de 2018.[665]​
Rompiendo con la tradición que imperaba desde hacía años en la AFA, la derrota en la Copa América 2015 no significó la salida de Martino,[666]​ pese a lo que la mayoría de los hinchas y periodistas anunciaban, y se mantuvo una continuidad y su proyecto a largo plazo.[cita requerida] En septiembre, el seleccionado argentino inició una gira por Estados Unidos que serviría como preparación para las eliminatorias del Mundial 2018, que contó con dos amistosos contra Bolivia y México. El 4 de septiembre, ante Bolivia, Messi entró en el segundo tiempo y, en nueve minutos, anotó dos goles: de cabeza el 5-0 parcial y luego el segundo, para un resultado final 7-0. Era la primera vez que le convertía a la selección boliviana,[667]​ y gracias a este doblete pasó a ser el primer jugador argentino en anotarles a todas las selecciones de la Conmebol, una marca con la que solo contaban otros tres jugadores sudamericanos (Zico, Arnoldo Iguarán y Agustín Delgado).[668]​ El 8 de septiembre contra México, a los 90 minutos convirtió el tanto del empate final, después de que Agüero, a los 85, anotara el primer gol cuando Argentina estaba perdiendo 0-2.[669]​ Por una lesión sufrida en un Barcelona-Las Palmas el 26,[278]​ no pudo jugar ante Ecuador y Paraguay, en octubre, y Brasil y Colombia en noviembre.[670]​

El 24 de marzo de 2016 ante Chile, dio una asistencia a Gabriel Mercado en el segundo gol, que le permitió a Argentina ganar 2-1.[671]​ El 29, de penal, convirtió el segundo tanto del 2-0 a Bolivia, que fue su gol número 50 con la selección.[672]​


Messi festeja un gol ante Ecuador, mirando al cielo en agradecimiento a su abuela Celia.
Después de la renuncia de Martino el 5 de julio,[673]​ Edgardo Bauza fue designado nuevo entrenador el 5 de agosto. En su primera conferencia de prensa, dijo que viajaría a España para hablar con Messi, aunque sin intenciones de convencerlo para que volviera.[674]​

En su regreso a la selección, el 1 de septiembre ante Uruguay, Messi guio el juego y marcó el único gol del encuentro, a pesar de que el contrincante había puesto nueve jugadores en la defensa.[675]​ El 6, por una pubalgia, no fue convocado contra Venezuela y,[676]​ como a fines de ese mes se rompió el aductor del muslo derecho, tampoco participó en los partidos contra Perú y Paraguay en octubre.[670]​ El 10 de noviembre, Argentina perdió 3-0 como visitante frente a Brasil.[677]​ El 15 de noviembre, Messi anotó un gol y dio dos asistencias en el 3-0 contra Colombia.[678]​ Su juego, destacado por medios de varios países, fue esencial en la clasificación de Argentina, que apenas había sumado dos puntos en los cuatro partidos previos.[679]​

El 23 de marzo de 2017, Messi ejecutó el penal con que Argentina le ganó 1-0 a Chile en el estadio Monumental.[680]​ Cinco días más tarde, a horas del partido contra Bolivia en La Paz, la FIFA, actuando de oficio, decidió multarlo con 10 000 francos suizos y sancionarlo por cuatro fechas, por haber insultado a Emerson Augusto de Carvalho, árbitro asistente del partido con Chile, a pesar de que ni este ni el árbitro Sandro Ricci lo habían informado en acta. Messi, en consecuencia, no pudo jugar y miró el partido por televisión en el vestuario del estadio Hernando Siles. Argentina perdió 2-0, bajó a la quinta posición y entró en zona de repechaje.[681]​ El 11 de abril, Bauza fue despedido como DT.[682]​

El 5 de mayo, la FIFA levantó la sanción en su totalidad, por lo que Messi pudo participar en los tres siguientes partidos.[683]​

Etapa Sampaoli
El 1 de junio, Jorge Sampaoli fue designado nuevo entrenador de la selección argentina. En la conferencia de prensa, afirmó que Messi era "el mejor jugador del mundo con muchas variantes creativas" y que pensaba juntarlo con "jugadores compatibles".[684]​ Comenzó dirigiendo dos amistosos ese mismo mes. El 9, Messi no realizó un buen partido en el Melbourne Cricket Ground frente a Brasil, que Argentina ganó 1-0,[685]​ y estuvo ausente contra Singapur el 13, cuando Argentina goleó 6-0 en el Estadio Nacional de Singapur.[686]​

En su debut oficial como entrenador, el 31 de agosto de visitante ante Uruguay, Sampaoli planteó un equipo ofensivo, con cuatro jugadores arriba para facilitarle la tarea a Messi. A pesar de haber sido el mejor de su equipo, Messi no pudo convertir y el partido terminó 0-0.[687]​Los dos siguientes encuentros también fueron empates: 1-1 ante Venezuela (con gol en contra de Rolf Feltscher) el 5 de septiembre y,[688]​ un mes más tarde, 0-0 frente a Perú.[689]​ Con estos resultados, Argentina quedó en el sexto puesto y debía ganarle el último partido a Ecuador para no quedar afuera del Mundial. El 10 de octubre, con un hat-trick de Messi, ganó 1-3 en Quito y se clasificó sin necesidad de jugar el repechaje.[690]​ Con 21 goles en eliminatorias sudamericanas, Messi desplazó a Hernén Crespo (19) como máximo goleador argentino en esa competición.[691]​

En sus primeros trece partidos, Argentina consiguió 15 puntos sobre 18 posibles (83 %) en los seis encuentros donde jugó Messi, pero apenas 7 de 21 (33 %) en los siete en que no participó.[692]​

Mundial 2018
Véase también: Argentina en la Copa Mundial de Fútbol de 2018

Messi festeja su gol ante Nigeria en la Copa Mundial de Fútbol de 2018.
El 27 de mayo de 2018, por problemas en los isquiotibiales, Messi no participó en el amistoso contra España que Argentina perdió 6-1.[693]​ Por su ausencia, la AFA perdió 350 000 euros.[694]​ El 29 de mayo, en un amistoso contra Haití en la Bombonera de Buenos Aires, hizo tres de los goles con que Argentina ganó 4-0.[695]​

El 16 de junio, en el primer partido de Argentina en el Mundial, erró un penal en el empate 1-1 ante Islandia.[696]​ Tras perder 0-3 ante Croacia,[697]​ convirtió un gol ante Nigeria, a la que Argentina le ganó 2-1, y en el que fue elegido Jugador del Partido.[698]​ La selección alcanzó el segundo puesto en la clasificación del grupo y pasó a octavos de final, donde fue eliminada por Francia, primera del grupo C, el 30 de junio.[699]​ A pesar de su pobre desempeño en los dos primeros y el último partido,[697]​[699]​ Messi fue candidato al premio Puskás por su gol a Nigeria,[700]​ pero perdió ante Mohamed Salah.[701]​

Etapa Scaloni
El 14 de julio, la AFA anunció en Twitter que Sampaoli había dejado de ser DT.[702]​ De manera provisoria, y para dirigir seis amistosos, tomó el puesto Lionel Scaloni, quien en noviembre fue ratificado hasta la siguiente Copa América y,[703]​ en julio de 2019, hasta el Mundial de Catar.[704]​

Messi acordó no jugar ninguno de esos encuentros en los que,[705]​ por decisión de Scaloni, ningún jugador llevó la camiseta número 10.[706]​ Sin el atractivo de su presencia en el plantel, la AFA perdió hasta 900 000 dólares por partido.[707]​ Regresó el 22 de marzo de 2019, en otro amistoso contra Venezuela en el estadio Wanda Metropolitano de Madrid que Argentina perdió 3-1.[708]​ Tanto el equipo como el jugador recibieron críticas de diversos medios y el excapitán argentino Daniel Passarella le recriminó no demostrar con la selección la misma "actitud" que con su club.[709]​[694]​ Debido a una pubalgia, no participó en el amistoso contra Marruecos el 26 en el estadio Ibn Battouta de Tánger. Su ausencia significó una pérdida de unos 400 000 mil dólares para la AFA, ya que la Real Federación de Fútbol de Marruecos había estipulado por contrato un pago inferior si Messi no jugaba.[710]​

En el último amistoso antes de la Copa América, el 7 de junio contra Nicaragua en el estadio del Bicentenario, anotó su séptimo doblete con Argentina, que ganó 5-1.[711]​

Copa América 2019
Véase también: Argentina en la Copa América 2019
Tras perder 2-0 contra Colombia el primer partido de la fase de grupos de la Copa América el 15 de junio,[712]​ el 19 Argentina, gracias a un penal ejecutado por Messi al inicio del segundo tiempo, empató 1-1 con Paraguay, resultado que la obligaba a ganarle a Catar para pasar a cuartos de final.[713]​ El 23 de junio, aunque no tuvo un muy buen desempeño, Messi contribuyó en el 2-0, con goles de Lautaro Martínez y Agüero.[714]​ Luego de que Argentina le ganara 2-0 a Venezuela el 28, algunos medios criticaron la actuación de Messi,[715]​[716]​ quien reconoció que no había sido su mejor Copa América, a la vez que se quejó de la calidad de los terrenos de juego.[717]​ En ese partido, por otra parte, cantó por primera vez el himno,[718]​ algo por lo que se lo criticaba repetidamente en su país.[719]​ Luego de la derrota 2-0 ante Brasil en semifinales el 2 de julio, cuestionó el arbitraje y alegó que la competición estaba "preparada" para que ganara el país anfitrión.[720]​

Argentina y Chile se enfrentaron por el tercer puesto el 6 de julio en el Arena Corinthians de San Pablo. Messi ejecutó, desde mitad de cancha, el tiro libre que le permitió a Agüero convertir el primer gol en la victoria 2-1 pero, tras un altercado con Gary Medel, fue expulsado en el minuto 37 junto con el capitán chileno. Después del partido, no subió al podio (el premio lo recogió Di María) y dio a entender que había sido expulsado por sus quejas sobre el arbitraje en la semifinal.[721]​[722]​ El 23 de julio, la CONMEBOL lo multó con 1500 dólares y lo sancionó por un encuentro, lo que le impediría disputar el primer partido de la clasificación para el Mundial 2022,[723]​ y el 2 de agosto, le impuso una sanción de tres meses y una multa de 50 000 dólares por sus comentarios sobre las decisiones arbitrales. Debido a esta prohibición, Messi no pudo jugar los amistosos contra Chile, México y Alemania en septiembre y octubre.[724]​

Copa América 2021
Véase también: Argentina en la Copa América 2021
El 14 de junio de 2021, en el primer partido de Argentina en la Copa América en Brasil, Messi marcó de tiro libre en el empate 1-1 contra Chile en el estadio Nilton Santos de Río de Janeiro.[725]​ Con este gol, el décimo en una Copa América, sobrepasó los 56 hechos de tiro libre por Cristiano Ronaldo y se convirtió en el futbolista activo con más goles de esa manera (57). También superó el récord de Batistuta de 38 goles en partidos oficiales con Argentina.[726]​ Contra Uruguay el 18 de junio, asistió a Guido Rodríguez en el gol de cabeza con que Argentina ganó 1-0.[727]​

El 21 de junio, Argentina le ganó 1-0 a Paraguay.[728]​ El 28, en el 4-1 contra Bolivia, Messi dio una asistencia en el primer gol de Papu Gómez y marcó después otros dos, uno de penal y otro de jugada, algo que no hacía desde 2018. Fue su partido número 148 en la selección, por lo que superó el récord de 147 de Mascherano.[729]​ El 3 de julio, dio dos asistencias y marcó de tiro libre el último gol en el 3-0 ante Ecuador en cuartos de final.[730]​ Contra Colombia el 6 de julio, asistió a Lautaro Martínez en el primer gol y, tras el empate 1-1, anotó en la tanda de penales para el 3-2 de Argentina.[731]​

El 10 de julio, en la final contra Brasil en el Maracaná, Argentina ganó 1-0 con gol de Di María. En su quinta final internacional, Messi consiguió su primer título, el primero de Argentina desde la Copa América 1993 y la decimoquinta Copa América en su historia.[732]​ Había participado directamente en nueve de los doce goles marcados por Argentina, con cuatro tantos y cinco asistencias.[733]​[734]​ Fue nombrado mejor jugador y máximo goleador del torneo, premio que compartió con el colombiano Luis Díaz,[735]​ e integrante del Once ideal.[736]​ Además, ascendió al cuarto puesto de goleadores históricos del torneo e igualó dos récords: con treinta y cuatro encuentros disputados, el de 1953 del arquero chileno Sergio Livingstone como jugador presente en más partidos en la historia de la Copa América y, con seis participaciones, se convirtió en el segundo argentino en alcanzar ese número junto con el arquero Américo Tesoriere, quien lo había hecho en 1925.[737]​[738]​[739]​

El 5 de agosto, la IFFHS lo incluyó en la selección argentina ideal de todos los tiempos.[740]​

Eliminatorias del Mundial 2022

Messi frente a México en el Mundial 2022
El 8 de octubre de 2020, en el primer partido de las eliminatorias del Mundial 2022, Messi anotó de penal el 1-0 ante Ecuador.[741]​ De visitante contra Bolivia el 13, jugó un muy buen segundo tiempo, en el que se asoció con Lautaro Martínez para habilitar el gol de Joaquín Correa con el que Argentina ganó 2-1.[742]​ El 13 de noviembre, en el empate 1-1 con Paraguay, le anularon un gol tras consulta con el VAR.[743]​ Después del 2-0 ante Perú el 17, donde tuvo un buen desempeño, pero no marcó, se convirtió en el jugador con más partidos ganados (85) en la historia de su selección.[744]​

El 3 de junio de 2021 frente a Chile, marcó el primer gol del partido y ejecutó dos tiros libres, pero los atajó Claudio Bravo y el encuentro terminó 1-1.[745]​ El 14 de octubre, al igual que sus compañeros, tuvo una actuación regular en el 1-0 contra Perú.[746]​ Tampoco convirtió goles el 8 de junio en el 2-2 contra Colombia, donde David Ospina, que fue la figura del partido, le atajó un tiro libre y una volea.[747]​

En la reanudación de las eliminatorias el 2 de septiembre, no convirtió en el 3-1 ante Venezuela pero,[748]​ después de la suspensión del partido ante Brasil el 6,[749]​ el 9 anotó un hat-trick en el 3-0 contra Bolivia en el estadio Monumental, ya con presencia de público tras las restricciones impuestas por la pandemia de COVID.[750]​ En su partido número 153, alcanzó los 79 goles (43 de jugada, 22 de penal, 8 tiros libres, 5 con el pie derecho y 2 de cabeza) con la absoluta, por lo que superó a Pelé como máximo goleador de selecciones sudamericanas,[751]​ y, con 26 tantos, a Luis Suárez como máximo goleador en eliminatorias Conmebol.[752]​ El desglose de goles por competición es 6 en mundiales, 26 en eliminatorias y 13 en Copa América, más otros 34 en amistosos.[753]​

Luego de un empate sin goles ante Paraguay el 7 de octubre,[754]​ tres días más tarde, Messi anotó el primer tanto del 3-0 contra Uruguay,[755]​ pero no marcó en el 1-0 frente a Perú el 14 ni en el 1-0 con Uruguay el 12 de noviembre, donde jugó sólo los últimos quince minutos.[756]​[757]​[758]​ El 16 de noviembre como local ante Brasil, con un 0-0 final y cuando aún faltaban cuatro fechas, la selección argentina se clasificó matemáticamente para el Mundial. Continuaba invicta en las eliminatorias, después de haber jugado veintisiete partidos entre oficiales y amistosos.[759]​

Scaloni no convocó a Messi para los partidos contra Chile y Colombia en enero y febrero, porque seguía entrenando diferenciado en el PSG por haber tenido COVID y problemas en la rodilla e isquiotibiales izquierdos.[760]​ El 25 de marzo, Messi anotó un gol en el 3-0 contra Venezuela,[761]​ seleccionado frente al que no marcaba desde 2016 y nunca le había convertido a Wuilker Faríñez.[762]​ Al empatar 1-1 con Ecuador el 29, Argentina igualó su récord de 1993 de 31 partidos sin perder.[763]​

El 27 de septiembre, en un amistoso contra Jamaica que Argentina ganó 3-0, Messi convirtió dos goles. Alcanzó así los 90 y se ubicó en el tercer puesto de la lista de máximos goleadores históricos de selecciones, detrás de Cristiano Ronaldo (117) y Ali Daei (109).[764]​

Finalissima 2022
El 1 de junio de 2022, en la Copa de Campeones Conmebol-UEFA (apodada Finalissima), Argentina le ganó 3-0 a Italia en el estadio de Wembley. Messi, que jugó un muy buen partido, asistió en el primer y tercer gol, además de tirar tres veces al arco. Al final del encuentro, fue nombrado MVP.[765]​[766]​

En un amistoso ante Estonia el 5 de junio en el estadio El Sadar de Pamplona, anotó los cinco goles del 5-0 de Argentina. Con 86 tantos en 163 partidos, ascendió al cuarto lugar en la tabla de máximos goleadores históricos de selección, por delante de Puskás y detrás de Cristiano Ronaldo, Ali Daei y Mokhtar Dahari. Además, fue el tercer jugador de su selección en convertir cinco goles en un partido, después de Juan Andrés Marvezy y José Manuel Moreno, quienes lo habían hecho en 1941 y 1942.[767]​[768]​ El 16 de noviembre, en otro amistoso con Emiratos Árabes Unidos, marcó un tanto en otro 5-0 de Argentina.[769]​ Argentina, por su parte, llegó a los 36 partidos sin perder, lo que la posicionó en el segundo lugar de la lista de selecciones con más partidos invictos consecutivos, detrás de Italia (37) y por delante de Brasil (35 en 1993-1996) y España (35 en 2007-2009).[770]​

Mundial 2022
Véase también: Argentina en la Copa Mundial de Fútbol de 2022
El 22 de noviembre, en el partido contra Arabia Saudita que Argentina perdió 2-1, Messi convirtió un penal a los diez minutos de juego y, a los veintidós, un gol que le anularon por estar en offside.[771]​ En el segundo tiempo ante México en el estadio Lusail el 26, anotó el primer gol y dio el pase para el de Enzo Fernández en el 2-0 de Argentina.[772]​ A los 35 años y 155 días, se convirtió en el jugador de mayor edad en hacer un gol y dar una asistencia en un mundial.[773]​ El 30, en el estadio 974 frente a Polonia, a pesar de que Wojciech Szczęsny le atajó un penal y un remate, fue el centro del juego de Argentina, que ganó 2-0. Por otra parte, con veintidós partidos, superó el récord argentino de Maradona (21) de presencias en Copas del Mundo.[774]​


Alineación inicial de Argentina ante México por el grupo C del Mundial de Catar
El 3 de diciembre, en el 2-1 por octavos de final frente a Australia en el estadio Áhmad bin Ali, anotó el primer gol tras asistencia de Nicolás Otamendi. En su partido oficial número mil, convirtió por primera vez más allá de la fase de grupos.[775]​ Para Diego Latorre, exintegrante de la selección argentina, fue su mejor partido en todos los mundiales.[776]​ El 9, en cuartos de final frente a Países Bajos, superó a Maradona como argentino que más veces jugó como capitán.[777]​ Asistió a Nahuel Molina en el primer tanto, anotó un penal y, tras un empate 2-2 incluso en los tiempos extras, marcó uno de los penales con que Argentina ganó 4-3.[778]​ En el 3-0 por semifinales frente a Croacia el 13, marcó de penal el primer gol y asistió en el segundo de Julián Álvarez. Con su decimoprimer gol, quedó en primer lugar de la lista de máximos goleadores argentinos en mundiales, por delante de Batistuta (10), Guillermo Stábile (8) y Maradona (8).[779]​[772]​

El 18 de diciembre, en la final contra Francia en el estadio Lusail, marcó de penal el primer gol y, en los tiempos extras, aprovechó el rebote de un intento de Lautaro Martínez que Hugo Lloris había rechazado para desempatar el 2-2. Como Mbappé anotó el tercero para su equipo, el partido se definió por penales. Messi convirtió el suyo para un 4-2 a favor de Argentina, que ganó el título después de treinta y seis años.[780]​ Al igual que contra México, Australia, Croacia y Países Bajos,[781]​ fue elegido MVP y recibió el Balón de Oro,[780]​[631]​ por lo que pasó a ser el primer jugador reconocido como MVP en once oportunidades y en dos como el mejor del torneo.[782]​ Ganó también la Bota de Plata, quedó cuarto en la lista de máximos goleadores en mundiales y superó otros dos récords de la Copa del Mundo: el de Lothar Matthäus de más partidos (26) y el de más minutos jugados (2314 contra 2217) de Paolo Maldini[783]​[784]​[631]​ Con un total de 26 goles, además, desplazó a Ronaldo (25) como máximo goleador histórico en torneos mayores internacionales.[785]​

Amistosos 2023-2024
En marzo de 2023, marcó un gol de tiro libre en un amistoso contra Panamá y un hat-trick en otro con Curazao, con el que llegó a los cien goles en su selección.[786]​[787]​ En medio de una gira por Asia en junio, anotó el gol más rápido de su carrera (1:19') frente a Australia,[788]​ pero no jugó frente a Indonesia porque había empezado sus vacaciones.[789]​ Tampoco participó en los dos primeros partidos de marzo de 2024, contra El Salvador y Costa Rica, por encontrarse lesionado.[486]​

Por decisión de Scaloni, que quería preservar su estado físico,[790]​ fue suplente en el encuentro con Ecuador el 9 de junio, en el que entró a los diez minutos del segundo tiempo. Aunque impreciso al principio, después dio dos asistencias a Enzo Fernández, que no anotó, además de tratar de marcar una vez desde fuera del área.[791]​ El 14, frente a Guatemala, empató el 1-1 parcial, asistió a Lautaro Martínez e hizo el último gol en el 4-1 de Argentina.[792]​

Copa América 2024
Véase también: Argentina en la Copa América 2024
El 20 de junio, en el partido inaugural de la Copa América 2024 en el Mercedes-Benz Stadium frente a Canadá, Messi le dio un pase a Alexis Mac Allister, que se la dejó a Julián Álvarez para el primer gol, y otro a Lautaro Martínez para el 2-0 final. Además, con treinta y cinco presencias y siete torneos, superó los records de Livingstone y Tesoriere, respectivamente.[793]​[794]​ Frente a Chile, tuvo una molestia en el aductor derecho que le impidió jugar contra Perú.[795]​[796]​ En cuartos de final, frente a Ecuador, falló su tiro en la tanda de penales, que finalizó 4-2 a favor de Argentina.[797]​ En semifinales, nuevamente contra Canadá, convirtió su único gol en el torneo al desviar un remate al arco de Enzo Fernández.[798]​ El 14 de julio, frente a Colombia, jugó la décima final con su selección,[799]​ pero a los 66 minutos tuvo que ser sustituido tras lastimarse el tobillo.[800]​ En el minuto 112' de la prórroga, Lautaro Martínez convirtió el gol con que Argentina ganó su decimosexta Copa y superó así a Uruguay, que tiene quince.[801]​

Perfil de jugador

Un versátil delantero, Messi a veces se desempeña como un enganche.
Estilo de juego
Goleador prolífico, Messi es conocido por su remate, posicionamiento, reacciones rápidas y habilidad para hacer corridas para vencer las líneas defensivas rivales. También puede funcionar en un rol de organizador, debido a su visión y rango de pases.[802]​ Es frecuentemente llamado "mago" por crear situaciones de gol de la nada.[803]​[804]​[805]​ Es, además, un preciso lanzador de tiros libres, que comenzó a mejorar bajo Basile en los entrenamientos de la selección,[806]​ y penales (77,62 % a noviembre de 2022),[807]​[808]​ y uno de los mejores en goles de falta directa: entre 2016 y 2021, anotó 56 goles de ese modo, tres veces más que el resto de los jugadores.[809]​[810]​ Tras su salida del Barcelona, marcó cinco con Argentina, dos con PSG y dos con Inter Miami.[811]​ También suele anotar picando la pelota por encima del arquero.[812]​[813]​

Debido a su habilidad con la pelota y baja estatura, es muy ágil para cambiar rápido de dirección y evadir así las barridas de sus rivales,[814]​ lo que hizo que los medios de España empezaran a llamarlo "La Pulga Atómica", como le había puesto Mario Alberto Kempes.[815]​ A pesar de no ser físicamente imponente, tiene una fuerza significativa en la parte superior del cuerpo, lo que, combinado con su bajo centro de gravedad y equilibrio, lo ayuda a resistir los desafíos físicos de los oponentes. En consecuencia, se distingue por simular poco en un deporte en el que muchos lo hacen.[816]​[817]​ Por sus cortas pero fuertes piernas, puede ejecutar veloces ráfagas de aceleración, mientras que sus rápidos pies le permiten mantener controlada la pelota a gran velocidad.[cita requerida] Guardiola dijo una vez que era "el único jugador más rápido con un balón en los pies que sin balón".[818]​

Messi es un jugador predominantemente zurdo: con la parte exterior del pie izquierdo empieza carreras regateando, mientras que con la parte interna finaliza las jugadas, ya sea con un remate o con una asistencia o pase.[cita requerida] Sin embargo, siempre marcó también con la derecha y, a partir de 2012, comenzó a usar más su pierna menos hábil.[819]​

Su ritmo y habilidad técnica le permiten hacer largas corridas con la pelota hacia el arco, en particular durante contraataques, donde usualmente comienza desde la mitad o el sector derecho del campo.[820]​ Considerado el mejor gambeteador del mundo,[821]​ y uno de los mejores de la historia,[822]​ en 2009, mientras lo entrenaba en la selección, Maradona dijo sobre él: "Tiene la pelota pegada al pie, es parte de su cuerpo. (...) Eso no lo vi en ningún otro y miren que vi jugadores, eh. Vi entrenar a Van Basten, a Careca, a infinidad de jugadores, a Houseman, por ejemplo. (...) Pero ninguno como Messi".[823]​ Más allá de sus cualidades individuales, también es un jugador de equipo completo y trabajador, conocido por sus combinaciones creativas, en particular con los ex-centrocampistas del Barcelona Xavi e Iniesta.[824]​[825]​


Messi suele conectar profundamente con los mediocampistas, organizar las jugadas de ataque y crear oportunidades de gol.
Tácticamente, Messi juega en un rol ofensivo libre. Al ser versátil, puede atacar tanto por el centro del campo como por el sector derecho. Su posición favorita en la infancia era como organizador detrás de dos delanteros, conocido como enganche en Argentina, pero empezó su carrera en el Barcelona como un extremo clásico por izquierda.[826]​ Ya en el primer equipo, Rijkaard lo movió a la banda derecha, posición desde donde podía recortar fácilmente hacia el centro del campo y realizar tiros con efecto al arco con la pierna izquierda, en vez de dedicarse únicamente a lanzarles centros a sus compañeros.[827]​

Bajo Guardiola y los entrenadores siguientes, jugó seguido en el rol de falso nueve, posicionado como un delantero centro, pero que podía merodear el centro del campo, llegando a veces al mediocampo y atrayendo defensores para crear y explotar los espacios que dejaban con pases filtrados, corridas ofensivas de los otros delanteros, sus propias corridas o para combinar con Xavi e Iniesta.[828]​ En la formación 4-3-3 de Luis Enrique, volvió a su posición habitual como delantero derecho, que lo caracterizó tanto en su carrera,[829]​ pero después desarrolló un rol como un organizador libre y más profundo en el campo.[830]​ Con Ernesto Valverde, jugó en una variedad de posiciones: ocasionalmente continuó en un rol más profundo, en el que podía hacer carreras desde atrás hacia el área, o desde la banda derecha o como un falso nueve, también jugó en un rol más central, en formaciones 4-2-3-1 o 4-4-2 como un segundo delantero, donde se le daba la libertad para caer profundo, conectarse con los mediocampistas, orquestar los ataques y crear oportunidades para su compañero de delantera, Luis Suárez.[831]​

A medida que la efectividad de sus gambetas disminuyó lentamente por la edad,[366]​ empezó a dictar su juego en áreas más profundas del campo y se desarrolló como uno de los mejores pasadores y organizadores de todos los tiempos.[832]​ Su trabajo sin pelota y sus responsabilidades defensivas también se hicieron menores a medida que su carrera progresó: al cubrir menos áreas en el campo y conservar su energía para aprovechar más ráfagas de velocidad, mejoró su efectividad, movimiento y juego posicional, además de evitar lesiones musculares, pese a la gran cantidad de partidos que jugaba por temporada.[cita requerida]

Con la selección argentina, estuvo también en diferentes posiciones por el frente de ataque: con distintos entrenadores, ha jugado en la banda derecha, como un falso nueve, un delantero todoterreno, un segundo delantero junto a otro compañero o en un rol más libre y creativo como enganche o mediapunta detrás de los delanteros.[833]​

Uno va creciendo y aprendiendo cosas dentro de la cancha. Antes agarraba la pelota y hacía mi jugada. Hoy intento hacer jugar más al equipo y no ser tan definidor, tan egoísta, entre comillas. Cerca del área buscar siempre una mejor opción, tirarme un poco más atrás y desde ahí intentar manejar el juego. Intento mover más al equipo desde otra posición, de otro lugar. Creo que sigo corriendo igual que lo hice siempre pero de diferente manera
Messi en una entrevista de 2018 con el periodista argentino Luis Majul.[18]​
Estudios estadísticos, señalaron que Messi, en sus últimas temporadas con el Barcelona, "no corría" en determinados momentos del partido.[834]​[835]​ Sin embargo, diferentes análisis televisivos demostraron que esa es una característica típica suya: espera el momento justo y se ubica en la posición exacta para sacar provecho de cada jugada.""")

root.mainloop()
