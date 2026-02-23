import streamlit as st
st.set_page_config(page_title="Proyecto Módulo 1",page_icon="🧵", layout="wide", initial_sidebar_state="expanded")
st.sidebar.title("  ADISA SAC")
st.sidebar.image("logo1.png")
st.sidebar.title("Empresa Textil")


menu = st.sidebar.selectbox(
    "Menú Principal",
    [
        "🏠HOME",
        "📝EJERCICIO 1 - VARIABLES Y CONDICIONALES",
        "📋EJERCICIO 2 - LISTAS Y DICCIONARIOS",
        "🧮EJERCICIO 3 - FUNCIONES Y PROGRAMACIÓN FUNCIONAL",
        "⚙️EJERCICIO 4 - PROGRAMACIÓN ORIENTADA A OBJETOS (POO)"
    ]
)
#----------------------------------------------------------------------
#HOME 

if menu == "🏠HOME":

    st.title("Proyecto Módulo 1 – Fundamentos de Programación")

    st.write("**Nombre:** Stephany Xiomara Pachas Sanchez")
    st.write("**Curso:** Python Fundamentals")
    st.write("**Año:** 2026")

    st.write("""
    Esta aplicación integra los conceptos fundamentales aprendidos
    durante el módulo 1: variables, estructuras de datos,
    condicionales, ciclos, funciones, programación funcional
    y programación orientada a objetos.

    La temática está aplicada al control de producción
    en una planta textil.
    """)

    st.write("**Tecnologías utilizadas:**")
    st.write("**-** Python")
    st.write("**-** Streamlit")
 #---------------------------------------------------------------
    #Ejercicio 1
elif menu == "📝EJERCICIO 1 - VARIABLES Y CONDICIONALES":

    st.subheader("🧵Control de Producción de Hilo Teñido")

    presupuesto = st.number_input("Ingrese los kg de Hilo programados", min_value=100,max_value=100000,step=50) #Presupuesto 
    gasto = st.number_input("Ingrese los kg Hilo producidos", min_value=100,max_value=100000,step=50) #Gasto o utilizado

    if st.button("Evaluar Producción"):

         if gasto <= presupuesto:
            st.success("La producción está dentro del programa.")
         else:
            st.warning("La producción excedió lo programado.")

    diferencia = presupuesto - gasto
    st.write("Diferencia (kg):", diferencia)
 #-----------------------------------------------------------------

    #Ejercicio 2
elif menu == "📋EJERCICIO 2 - LISTAS Y DICCIONARIOS": # ACTIVIDADES FINANCIERAS

    st.subheader("🧵Registro de Procesos Textiles (Hilado -tejido - teñido)")

    if "actividades" not in st.session_state:
        st.session_state.actividades = []

    nombre = st.text_input("Nombre de la Actividad (Hilado-teñido-tejido)")
    tipo = st.selectbox("Tipo de Fibra", ["Algodon Tanguis", "Algodon Pima", "Algodon Upland"])
    presupuesto = st.number_input("Kg programados",  min_value=100,max_value=100000,step=50)
    gasto_real = st.number_input("Kg reales", min_value= 100,max_value=100000,step=50)

    if st.button("Agregar Actividad"):

        actividad = {
            "nombre": nombre,
            "tipo": tipo,
            "presupuesto": presupuesto,
            "gasto_real": gasto_real
        }

        st.session_state.actividades.append(actividad)

    st.write("Lista de actividades registradas:")
    st.dataframe(st.session_state.actividades)

    st.write("Estado de cada actividad:")

    for act in st.session_state.actividades:

        if act["gasto_real"] <= act["presupuesto"]:
            st.write(act["nombre"], "✔ Dentro del presupuesto")
        else:
            st.write(act["nombre"], "❌ Fuera del presupuesto")    
#------------------------------------------------------------------------           
#EJERCICIO 3
elif menu == "🧮EJERCICIO 3 - FUNCIONES Y PROGRAMACIÓN FUNCIONAL":

    st.subheader("🧵Cálculo de Retorno Esperado")

    tasa = st.slider("📈Tasa de retorno (% mensual)", 0.0, 1.0, 0.1)
    meses = st.number_input("⏳Número de meses", 1,24,6)

    def calcular_retorno(actividad, tasa, meses):
        return actividad["presupuesto"] * tasa * meses

    if st.button("Calcular Retornos"):

        if "actividades" in st.session_state and len(st.session_state.actividades) > 0:

            retornos = list(
                map(
                    lambda act: calcular_retorno(act, tasa, meses),
                    st.session_state.actividades
                )
            )

            for i, act in enumerate(st.session_state.actividades):
                st.write(f"{act['nombre']} → Retorno esperado: {retornos[i]}")

        else:
            st.warning("No hay actividades registradas.")
#------------------------------------------------------------------------9           
#EJERCICIO 4
elif menu == "⚙️EJERCICIO 4 - PROGRAMACIÓN ORIENTADA A OBJETOS (POO)":

    st.subheader("🧵Modelado con Clase Actividad")

    class Actividad:

        def __init__(self, nombre, tipo, presupuesto, gasto_real):
            self.nombre = nombre
            self.tipo = tipo
            self.presupuesto = presupuesto
            self.gasto_real = gasto_real

        def esta_en_presupuesto(self):
            return self.gasto_real <= self.presupuesto

        def mostrar_info(self):
            return f"Proceso: {self.nombre} | Tipo: {self.tipo}"

    if "actividades" in st.session_state and len(st.session_state.actividades) > 0:

        for act in st.session_state.actividades:

            obj = Actividad(
                act["nombre"],
                act["tipo"],
                act["presupuesto"],
                act["gasto_real"]
            )

            st.write(obj.mostrar_info())

            if obj.esta_en_presupuesto():
                st.success("Cumple el presupuesto")
            else:
                st.warning("No cumple el presupuesto")

    else:
        st.warning("No hay actividades registradas para convertir en objetos.")