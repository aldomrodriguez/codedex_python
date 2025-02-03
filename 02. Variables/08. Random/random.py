import random



respuestas = [
    'Sí, definitivamente.', 'Definitivamente es así.', 'Sin duda.',
    'Respuesta confusa, inténtalo de nuevo.', 'Vuelve a preguntar más tarde.',
    'Mejor no te lo digo ahora.', 'Mis fuentes dicen que no.',
    'Las perspectivas no son muy buenas.', 'Muy dudoso.',
    'Por supuesto.', 'No tengo dudas.', 'Es bastante probable.',
    'Claro que sí.', 'Eso parece cierto.', 'Es cierto.',
    'Todo apunta a que sí.', 'Lo veo claro como el agua.',
    'Definitivamente no.', 'Ni lo sueñes.', 'No cuentes con ello.',
    'Mis fuentes dicen que sí.', 'Probablemente.',
    'Es muy incierto.', 'No puedo responder eso ahora.',
    'Déjame pensarlo un poco más.', 'Todo indica que sí.',
    'No lo creo.', 'Lo dudo mucho.', 'Imposible.',
    'Casi seguro.', 'Puede ser.', 'Pregunta más tarde.',
    'No estoy seguro.', 'Prefiero no responder eso.',
    'Todo indica que no.', 'No tengo información suficiente.',
    'Confuso, intenta de nuevo.', 'Es complicado.',
    'No te lo puedo garantizar.', 'Mis datos son confusos.',
    'Consulta a alguien más.', 'Tal vez sí, tal vez no.',
    'Hay un 50/50.', 'Es incierto.', 'Vuelve a intentarlo.',
    'La respuesta está nublada.', 'Parece prometedor.',
    'La suerte está de tu lado.', 'Lo dudo.',
    'Mis predicciones no son claras.', 'Un momento, déjame pensar.',
    '¡Claro que no!', 'Sin señales claras.',
    'Un rotundo no.', 'No lo veo probable.',
    'La balanza se inclina a sí.', 'Diría que sí.',
    'El universo dice que sí.', 'No apuestes por ello.',
    '¡Definitivamente sí!', 'Absolutamente.',
    'No tengo certeza.', 'Mis cálculos dicen que no.',
    'Los astros no están alineados.', 'La magia no lo ve claro.',
    'No cuentes con ello.', 'Posiblemente sí.',
    'El destino lo decidirá.', 'Lo siento, no sé.',
    'Mis predicciones dicen que sí.', 'No puedo verlo claro.',
    'Es una posibilidad.', 'Parece poco probable.',
    'Quizás en otro momento.', 'No veo por qué no.',
    'No parece que sea así.', 'Es un gran misterio.',
    'No tengo una respuesta clara.', 'Depende de muchos factores.',
    'Las probabilidades son bajas.', 'Inténtalo de nuevo más tarde.',
    'No puedo predecirlo ahora.', 'Eso es un enigma.',
    'No puedo ayudarte con eso.', 'Tal vez sí, tal vez no.',
    'Todo depende.', 'Eso parece improbable.',
    'Mi respuesta es no.', 'Mi respuesta es sí.',
    'Quizás.', 'No estoy seguro ahora.', 'Sin señales claras.',
    'Eso es difícil de decir.', 'Confía en tu instinto.',
    'El futuro es incierto.', 'Haz otra pregunta.',
    'Esa respuesta está fuera de mi alcance.',
    'Consúltalo más tarde.', 'No puedo decirlo con certeza.',
    'La suerte no está contigo.', 'Parece que sí.',
    'Definitivamente tal vez.', 'Eso parece lógico.',
    'Mi consejo es que no.', 'No creo que suceda.',
    'Parece bastante posible.', 'Podría ser.',
    'Eso no parece correcto.', 'Pregunta a alguien más.',
    'Haz caso a tu intuición.', 'Es un misterio.',
    'Eso no está claro.', 'No tengo una idea clara.',
    'La respuesta es ambigua.', 'Eso parece dudoso.',
    'Es demasiado pronto para decirlo.', 'Diría que sí, pero no estoy seguro.',
    'Mis datos son inconclusos.', 'No tengo una respuesta concreta.',
    'Todo depende de tu perspectiva.', 'Haz la pregunta de otra forma.',
    'El resultado es incierto.', 'Eso está en tus manos.',
    'Tal vez en el futuro.', 'No parece que sea posible.',
    'Eso parece muy improbable.', 'Confuso, vuelve a intentarlo.',
    'La suerte no está de tu lado.', 'La respuesta es afirmativa.',
    'Definitivamente no lo creo.', 'Eso parece una buena idea.',
    'No puedo verlo ahora.', 'Eso no parece correcto.',
    'Es mejor que no lo sepas.', 'Todo apunta a que no.',
    'Parece una mala idea.', 'Todo depende del contexto.',
    'Eso está fuera de mi control.', 'No lo sé.',
    'Es una pregunta difícil.', 'Quizás sí, pero no estoy seguro.',
    'Todo está en movimiento, espera.', 'El destino no está escrito.',
    'No tengo una respuesta exacta.', 'Es demasiado complicado.',
    'Eso parece poco probable.', 'Las probabilidades no están a tu favor.',
    'Eso no es algo que pueda responder.', 'La respuesta es incierta.',
    'Depende de las circunstancias.', 'Todo es posible.',
    'No parece posible.', 'Eso es un rotundo tal vez.',
    'La respuesta está en tu corazón.', 'No tengo idea.',
    'Podría ser una posibilidad.', 'Mis cálculos son inciertos.',
    'Eso parece prometedor.', 'Es posible, pero no seguro.',
    'No tengo suficiente información.', 'La respuesta es nebulosa.',
    'Eso no parece lógico.', 'Eso es incierto.',
    'Todo depende del universo.', 'Eso es una incógnita.',
    'Quizás deberías intentarlo.', 'No lo creo posible.',
    'Parece que sí, pero no lo garantizo.', 'Todo indica que es probable.',
    'No tengo una respuesta para eso.', 'Es poco probable, pero posible.',
    'Eso está fuera de mi entendimiento.', 'Eso depende de ti.',
    'Es un gran tal vez.', 'Eso parece improbable.',
    'Las probabilidades están en tu contra.', 'Eso no está claro ahora.',
    'Eso no parece ser verdad.', 'Confuso, intenta más tarde.',
    'Eso parece positivo.', 'Es mejor no saberlo.',
    'No puedo asegurarlo.', 'Las señales son mixtas.',
    'Eso no tiene respuesta.', 'Eso depende de cómo lo mires.',
    'Eso es incierto.', 'Eso parece una posibilidad.',
    'Eso no es concluyente.', 'No tengo una predicción para eso.',
    'No parece tener sentido.', 'Eso es poco probable.',
    'Eso es muy posible.', 'Eso no parece realista.',
    'Eso es ambiguo.', 'Eso no tiene sentido.',
    'Eso es un gran tal vez.', 'Eso no parece correcto.',
    'Eso parece una mala idea.', 'Eso está fuera de lugar.',
    'Eso no tiene solución.', 'Eso parece improbable.',
    'Eso no es seguro.', 'Eso no parece factible.',
    'Eso es cuestionable.', 'Eso no tiene fundamento.',
    'Eso no tiene lógica.', 'Eso no tiene respuesta clara.',
    'Eso no es lógico.', 'Eso no tiene base.',
    'Eso no es posible.', 'Eso no parece probable.',
    'Eso no tiene explicación.', 'Eso no parece real.',
    'Eso no tiene sentido ahora.', 'Eso no parece tener solución.',
    'Eso no tiene fundamento ahora.', 'Eso no parece correcto.',
    'Eso no parece tener base lógica.', 'Eso no tiene lógica en este momento.',
    'Eso no parece tener lógica ahora.', 'Eso no tiene sentido lógico.',
    'Eso no parece tener lógica clara.', 'Eso no tiene explicación lógica.',
    'Eso no parece tener una respuesta lógica.', 'Eso no tiene lógica clara.',
    'Eso no parece tener una solución lógica.', 'Eso no tiene lógica razonable.',
    'Eso no parece tener una base razonable.', 'Eso no tiene lógica razonable en este momento.',
    'Eso no parece tener una base razonable en este momento.', 'Eso no tiene lógica razonable en este contexto.',
    'Eso no parece tener una base razonable en este contexto.', 'Eso no tiene lógica razonable en este marco.',
    'Eso no parece tener una base razonable en este marco.', 'Eso no tiene lógica razonable en este ámbito.',
    'Eso no parece tener una base razonable en este ámbito.', 'Eso no tiene lógica razonable en este plano.',
    'Eso no parece tener una base razonable en este plano.', 'Eso no tiene lógica razonable en este entorno.',
    'Eso no parece tener una base razonable en este entorno.', 'Eso no tiene lógica razonable en esta situación.',
    'Eso no parece tener una base razonable en esta situación.', 'Eso no tiene lógica razonable en esta condición.',
    'Eso no parece tener una base razonable en esta condición.', 'Eso no tiene lógica razonable en estas circunstancias.',
    'Eso no parece tener una base razonable en estas circunstancias.', 'Eso no tiene lógica razonable en este caso.',
    'Eso no parece tener una base razonable en este caso.', 'Eso no tiene lógica razonable en este supuesto.',
    'Eso no parece tener una base razonable en este supuesto.', 'Eso no tiene lógica razonable en esta hipótesis.',
    'Eso no parece tener una base razonable en esta hipótesis.', 'Eso no tiene lógica razonable en este experimento.',
    'Eso no parece tener una base razonable en este experimento.', 'Eso no tiene lógica razonable en este ensayo.',
    'Eso no parece tener una base razonable en este ensayo.', 'Eso no tiene lógica razonable en esta prueba.',
    'Eso no parece tener una base razonable en esta prueba.', 'Eso no tiene lógica razonable en este análisis.',
    'Eso no parece tener una base razonable en este análisis.', 'Eso no tiene lógica razonable en esta evaluación.',
    'Eso no parece tener una base razonable en esta evaluación.', 'Eso no tiene lógica razonable en este diagnóstico.',
    'Eso no parece tener una base razonable en este diagnóstico.', 'Eso no tiene lógica razonable en esta consideración.',
    'Eso no parece tener una base razonable en esta consideración.', 'Eso no tiene lógica razonable en esta decisión.',
    'Eso no parece tener una base razonable en esta decisión.', 'Eso no tiene lógica razonable en esta elección.',
    'Eso no parece tener una base razonable en esta elección.', 'Eso no tiene lógica razonable en esta determinación.',
    'Eso no parece tener una base razonable en esta determinación.', 'Eso no tiene lógica razonable en esta resolución.',
    'Eso no parece tener una base razonable en esta resolución.', 'Eso no tiene lógica razonable en esta solución.',
    'Eso no parece tener una base razonable en esta solución.', 'Eso no tiene lógica razonable en este resultado.',
    'Eso no parece tener una base razonable en este resultado.', 'Eso no tiene lógica razonable en esta conclusión.',
    'Eso no parece tener una base razonable en esta conclusión.', 'Eso no tiene lógica razonable en este cierre.',
    'Eso no parece tener una base razonable en este cierre.', 'Eso no tiene lógica razonable en este final.',
    'Eso no parece tener una base razonable en este final.', 'Eso no tiene lógica razonable en este desenlace.',
    'Eso no parece tener una base razonable en este desenlace.', 'Eso no tiene lógica razonable en este término.',
    'Eso no parece tener una base razonable en este término.', 'Eso no tiene lógica razonable en esta conclusión.'
]
num = random.randint(1, len(respuestas)-1)

pregunta = input('Pregunta lo que quieras! ')
print(f'Pregunta: {pregunta} . Respuesta: {respuestas[num]}')