import streamlit as st
import json, io, random
from pathlib import Path

# ---------- Configuración página ----------
st.set_page_config(page_title="Neuropsicología Interactiva (M5–M8)", layout="centered")
st.title("🧠 Neuropsicología Interactiva – Módulos 5 a 8")
st.caption("Conceptos clave, casos prácticos y práctica interactiva para el examen.")

# ---------- Rutas de datos ----------
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
CASOS_PATH = DATA_DIR / "casos.json"
CONCEPTOS_PATH = DATA_DIR / "conceptos.json"

# ---------- Si faltan datos, crear ejemplos mínimos ----------
if not CONCEPTOS_PATH.exists():
    conceptos_seed = {
        "Módulo 5 – Personalidad y Psicopatología": {
            "Corteza prefrontal": "Planificación, control de impulsos, toma de decisiones.",
            "Sistema límbico": "Emoción y motivación (amígdala, hipocampo, hipotálamo).",
            "Amígdala": "Procesa el miedo/amenaza; lesión → desinhibición/agresividad.",
            "Hipocampo": "Memoria episódica; sensible a estrés crónico.",
            "Eje HPA": "Sistema hormonal del estrés; hiperactividad → ansiedad/depresión."
        },
        "Módulo 6 – Evaluación Neuropsicológica": {
            "Baterías neuropsicológicas": "WAIS, Stroop, TMT, WCST; miden dominios cognitivos.",
            "Validez y confiabilidad": "Garantizan medición correcta y consistente.",
            "Neuroimagen estructural/funcional": "RM, RMf, PET; correlato cerebro–conducta.",
            "Electrofisiología": "EEG/ERP; procesos temporales (atención, percepción).",
            "Informe neuropsicológico": "Describe, interpreta y recomienda."
        },
        "Módulo 7 – Intervención y Rehabilitación": {
            "Rehabilitación cognitiva": "Entrenamiento dirigido a restaurar funciones.",
            "Estrategias de compensación": "Apoyos externos/alternativas conductuales.",
            "Plasticidad cerebral": "Reorganización estructural/funcional dependiente de uso.",
            "Principios de plasticidad": "Repetición, intensidad, especificidad, transferencia.",
            "GMT / entrenamiento metacognitivo": "Mejora planificación y control inhibitorio."
        },
        "Módulo 8 – Neuropsicología y Sociedad": {
            "Neuroeducación": "Aplicar ciencia del aprendizaje en el aula.",
            "Ergonomía cognitiva": "Diseño laboral que reduce carga mental/errores.",
            "Salud pública": "Prevención deterioro y promoción de salud mental.",
            "Neuroderecho": "Imputabilidad con evidencia neurocientífica.",
            "Conectividad funcional": "Interacción entre redes durante tareas complejas."
        }
    }
    CONCEPTOS_PATH.write_text(json.dumps(conceptos_seed, ensure_ascii=False, indent=2), "utf-8")

if not CASOS_PATH.exists():
    casos_seed = [
        {
            "modulo": "Módulo 5 – Personalidad y Psicopatología",
            "titulo": "Desinhibición orbitofrontal",
            "vigneta": "Varón 35 a., desinhibido y agresivo verbal. RM: lesión OFC.",
            "pregunta": "Funciones alteradas y manifestaciones esperadas.",
            "respuesta_guia": [
                "Inhibición de respuestas; valoración de consecuencias",
                "Desinhibición social, impulsividad, pobre empatía"
            ],
            "opciones": [
                "Déficit de memoria semántica",
                "Desinhibición y pobre control de impulsos",
                "Apraxia constructiva"
            ],
            "correcta": 1
        },
        {
            "modulo": "Módulo 6 – Evaluación Neuropsicológica",
            "titulo": "Quejas de memoria no amnésicas",
            "vigneta": "Mujer 60 a. falla en atención sostenida y memoria de trabajo; memoria semántica ok; RM normal.",
            "pregunta": "Hipótesis y pruebas complementarias.",
            "respuesta_guia": [
                "DCL no amnésico (perfil ejecutivo/atencional)",
                "Profundizar ejecutivas (Stroop, TMT-B, n-back); cribado ánimo/sueño"
            ],
            "opciones": ["Amnesia episódica pura", "Perfil ejecutivo/atencional", "Afasia de conducción"],
            "correcta": 1
        },
        {
            "modulo": "Módulo 7 – Intervención y Rehabilitación",
            "titulo": "TCE y control inhibitorio",
            "vigneta": "Joven con TCE moderado; impulsividad y mala planificación; memoria intacta.",
            "pregunta": "Intervención y principio de plasticidad.",
            "respuesta_guia": [
                "GMT, manejo ambiental, contratos conductuales, ayudas externas",
                "Plasticidad uso-dependiente; repetición e intensidad"
            ],
            "opciones": ["Entrenamiento auditivo", "GMT y manejo ambiental", "Solo psicoeducación"],
            "correcta": 1
        },
        {
            "modulo": "Módulo 8 – Neuropsicología y Sociedad",
            "titulo": "Hurto impulsivo con daño frontal",
            "vigneta": "Hombre con lesión frontal comete hurto impulsivo; es llamado perito.",
            "pregunta": "Rol del neuropsicólogo y elementos para imputabilidad.",
            "respuesta_guia": [
                "Evaluar comprensión de ilicitud y capacidad de autodeterminación",
                "Pruebas ejecutivas, control de simulación, neuroimagen; límites del peritaje"
            ],
            "opciones": ["Dictar sentencia", "Aportar perfil y límites periciales", "Diagnóstico psiquiátrico final"],
            "correcta": 1
        }
    ]
    CASOS_PATH.write_text(json.dumps(casos_seed, ensure_ascii=False, indent=2), "utf-8")

# ---------- Carga de datos ----------
conceptos = json.loads(CONCEPTOS_PATH.read_text("utf-8"))
casos = json.loads(CASOS_PATH.read_text("utf-8"))

# ---------- Estado del usuario ----------
if "score" not in st.session_state: st.session_state.score = 0
if "respondidos" not in st.session_state: st.session_state.respondidos = 0

# ---------- Sidebar: progreso ----------
st.sidebar.header("Progreso")
st.sidebar.metric("Puntaje", st.session_state.score)
st.sidebar.metric("Preguntas", st.session_state.respondidos)

# ---------- Tabs ----------
tab1, tab2, tab3, tab4 = st.tabs(["📚 Conceptos", "🧪 Casos", "⬆️ Cargar/Editar", "📥 Descargas"])

# ===== Tab 1: Conceptos (con buscador) =====
with tab1:
    st.subheader("Conceptos clave por módulo")
    q = st.text_input("🔎 Buscar concepto/definición")
    modulo_sel = st.selectbox("📘 Módulo", list(conceptos.keys()))
    for nombre, definicion in conceptos[modulo_sel].items():
        if not q or q.lower() in nombre.lower() or q.lower() in definicion.lower():
            with st.expander(nombre):
                st.write(definicion)

# ===== Tab 2: Casos interactivos =====
with tab2:
    st.subheader("Casos prácticos con retroalimentación")
    filtro = st.selectbox("Filtrar por módulo", ["Todos"] + list(conceptos.keys()))
    pool = [c for c in casos if filtro == "Todos" or c["modulo"] == filtro]
    if not pool:
        st.info("No hay casos para ese módulo.")
    else:
        caso = random.choice(pool)
        st.markdown(f"**{caso['titulo']}** · _{caso['modulo']}_")
        st.write(caso["vigneta"])
        st.markdown(f"**Pregunta:** {caso['pregunta']}")

        idx = st.radio("Selecciona la mejor respuesta:", list(range(len(caso["opciones"]))),
                       format_func=lambda i: caso["opciones"][i], index=None)

        if st.button("Evaluar"):
            st.session_state.respondidos += 1
            if idx is None:
                st.warning("Selecciona una opción.")
            else:
                if idx == caso["correcta"]:
                    st.session_state.score += 1
                    st.success("✅ ¡Correcto!")
                else:
                    st.error(f"❌ Incorrecto. Correcta: {caso['opciones'][caso['correcta']]}")
                with st.expander("💡 Pauta/Análisis"):
                    for r in caso["respuesta_guia"]:
                        st.markdown(f"- {r}")
        st.caption("Sugerencia: cambia el filtro o recarga para otro caso.")

# ===== Tab 3: Cargar/Editar =====
with tab3:
    st.subheader("Sube más casos (JSON) o edita conceptos")
    up = st.file_uploader("Sube un archivo JSON con casos", type=["json"])
    if up:
        nuevos = json.load(up)
        if isinstance(nuevos, list):
            casos.extend(nuevos)
            CASOS_PATH.write_text(json.dumps(casos, ensure_ascii=False, indent=2), "utf-8")
            st.success(f"Se agregaron {len(nuevos)} casos.")
            st.json(nuevos[:1])
        else:
            st.error("El JSON debe ser una lista de casos.")
    st.markdown("— O descarga y edita los archivos locales `data/casos.json` y `data/conceptos.json`.")

# ===== Tab 4: Descargas =====
with tab4:
    st.subheader("Descargar definiciones y casos")
    raw_def = json.dumps(conceptos, ensure_ascii=False, indent=2).encode("utf-8")
    raw_cas = json.dumps(casos, ensure_ascii=False, indent=2).encode("utf-8")
    st.download_button("📥 Definiciones (JSON)", io.BytesIO(raw_def), file_name="definiciones_modulos.json")
    st.download_button("📥 Casos (JSON)", io.BytesIO(raw_cas), file_name="casos.json")

st.divider()
st.caption("© Material educativo para estudio – Módulos 5–8 Neuropsicología.")

