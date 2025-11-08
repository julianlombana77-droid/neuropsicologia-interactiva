import streamlit as st

st.set_page_config(page_title="Guía Interactiva de Neuropsicología", layout="centered")

st.title("🧠 Guía Interactiva de Neuropsicología – Módulos 5 a 8")
st.markdown("Selecciona un módulo y explora los conceptos clave con su definición o aplicación breve.")

# Diccionario con módulos y conceptos
modulos = {
    "Módulo 5 – Personalidad y Psicopatología": {
        "Corteza prefrontal": "Regula la planificación, el control de impulsos y la toma de decisiones; su lesión causa desinhibición o apatía.",
        "Sistema límbico": "Conjunto (amígdala, hipocampo, hipotálamo) que regula emociones y motivación; alteraciones → ansiedad o depresión.",
        "Amígdala": "Procesa el miedo y las respuestas de amenaza; daño → agresividad o falta de respuesta emocional.",
        "Hipocampo": "Clave para la memoria episódica; vulnerable al estrés crónico y depresión.",
        "Eje HPA": "Sistema hormonal del estrés; su sobreactivación contribuye a ansiedad y deterioro cognitivo.",
        "Trastornos de personalidad": "Alteraciones estables de conducta por disfunciones fronto-límbicas.",
        "Neuroimagen clínica": "Uso de RMf/PET para observar correlatos cerebrales de los trastornos mentales."
    },
    "Módulo 6 – Evaluación Neuropsicológica": {
        "Baterías neuropsicológicas": "Conjuntos de pruebas estandarizadas para medir memoria, atención, lenguaje y funciones ejecutivas.",
        "Validez y confiabilidad": "Propiedades psicométricas que garantizan medición precisa y consistente.",
        "Neuroimagen estructural/funcional": "RM, RMf, PET y EEG permiten correlacionar conducta y actividad cerebral.",
        "Electrofisiología": "Estudia la actividad eléctrica cerebral (EEG, ERP); útil para procesos atencionales rápidos.",
        "Análisis de datos": "Interpretación de resultados mediante puntuaciones z, percentiles o comparación con normas.",
        "Informe neuropsicológico": "Documento que describe, interpreta y recomienda según los hallazgos clínicos."
    },
    "Módulo 7 – Intervención y Rehabilitación": {
        "Rehabilitación cognitiva": "Técnicas para restaurar o mejorar funciones mentales afectadas (memoria, atención, planificación).",
        "Estrategias de compensación": "Apoyos externos o alternativas conductuales que sustituyen la función dañada.",
        "Plasticidad cerebral": "Capacidad del cerebro para reorganizarse estructural y funcionalmente tras una lesión o entrenamiento.",
        "Principios de plasticidad": "Uso dependiente, repetición, intensidad y especificidad de la práctica.",
        "Entrenamiento metacognitivo / GMT": "Programa para mejorar conciencia de errores y planificación ejecutiva.",
        "Apoyo emocional y psicoeducación": "Involucra a la familia y al entorno para mantener la motivación y adherencia."
    },
    "Módulo 8 – Neuropsicología y Sociedad": {
        "Neuroeducación": "Aplica el conocimiento del cerebro al aprendizaje y la enseñanza.",
        "Ergonomía cognitiva": "Diseño de entornos laborales que minimizan carga mental y errores.",
        "Salud pública": "Prevención del deterioro cognitivo y promoción de la salud mental poblacional.",
        "Neuroderecho": "Análisis de imputabilidad y responsabilidad penal desde la evidencia neurocientífica.",
        "Conectividad funcional": "Interacción entre áreas cerebrales durante tareas cognitivas; explica funciones complejas.",
        "Neuroimagen social": "Uso de RMf/EEG para estudiar empatía, moralidad y toma de decisiones sociales."
    }
}

# Selector de módulo
modulo = st.selectbox("📘 Selecciona el módulo:", list(modulos.keys()))

# Mostrar conceptos
st.subheader(f"Conceptos clave del {modulo}")
for concepto, definicion in modulos[modulo].items():
    with st.expander(concepto):
        st.write(definicion)
