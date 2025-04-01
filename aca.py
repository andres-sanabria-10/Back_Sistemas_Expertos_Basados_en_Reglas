from experta import KnowledgeEngine, Rule, Fact, P
from flask import Flask, request, jsonify
from flask_cors import CORS  # Importar CORS

# Definir la base de conocimiento
class SistemaExperto(KnowledgeEngine):
    # Regla 1: Condiciones con predicados (P)
    @Rule(
        Fact(region="R1"),  # Condición 1: Región Caribe
        Fact(piso_termico="Pt1"),  # Condición 2: Piso térmico cálido
        Fact(tipo_suelo="Ts4"),  # Condición 3: Tipo de suelo franco
        Fact(precipitacion_anual=P(lambda x: 500 <= x <= 4000)),  # Condición 4: Precipitación entre 500 y 4000 mm
        Fact(proposito_cultivo="Pc1")  # Condición 5: Propósito consumo personal
    )
    def recomendacion_caribe(self):
        print("¡La regla 1 se ha activado!")
        print("Recomendación para la región Caribe:")
        cultivos = [
            "Arveja_R1", "Frijol_R1", "Maiz_Amarillo_R1", "Maiz_Blanco_R1",
            "Soya_R1", "Tomate_R1", "Yuca_R1"
        ]
        print("Cultivos recomendados:", cultivos)
        self.declare(Fact(cultivos_recomendados=cultivos))

    # Regla 2: Nueva regla para suelos arcillosos y exportación
    @Rule(
        Fact(region="R1"),  # Condición 1: Región Caribe
        Fact(piso_termico="Pt1"),  # Condición 2: Piso térmico cálido
        Fact(tipo_suelo="Ts1"),  # Condición 3: Tipo de suelo arcilloso
        Fact(precipitacion_anual=P(lambda x: 500 <= x <= 4000)),  # Condición 4: Precipitación entre 500 y 4000 mm
        Fact(proposito_cultivo="Pc3")  # Condición 5: Propósito exportación
    )
    def recomendacion_exportacion(self):
        print("¡La regla 2 se ha activado!")
        print("Recomendación para exportación en la región Caribe:")
        cultivos = [
            "Banano_R1", "Cacao_R1", "Cafe_R1", "Aguacate_R1"
        ]
        print("Cultivos recomendados:", cultivos)
        self.declare(Fact(cultivos_recomendados=cultivos))

    # Regla 3: Suelos arenosos y venta local
    @Rule(
        Fact(region="R1"),  # Condición 1: Región Caribe
        Fact(piso_termico="Pt1"),  # Condición 2: Piso térmico cálido
        Fact(tipo_suelo="Ts2"),  # Condición 3: Tipo de suelo arenoso
        Fact(precipitacion_anual=P(lambda x: 500 <= x <= 4000)),  # Condición 4: Precipitación entre 500 y 4000 mm
        Fact(proposito_cultivo="Pc2")  # Condición 5: Propósito venta local
    )
    def recomendacion_venta_local(self):
        print("¡La regla 3 se ha activado!")
        print("Recomendación para venta local en la región Caribe:")
        cultivos = [
            "Hortalizas_Fruto_R1", "Hortalizas_Hoja_R1", "Hortalizas_Tallo_R1"
        ]
        print("Cultivos recomendados:", cultivos)
        self.declare(Fact(cultivos_recomendados=cultivos))

    # Regla 4: Piso templado y consumo personal
    @Rule(
        Fact(region="R1"),  # Condición 1: Región Caribe
        Fact(piso_termico="Pt2"),  # Condición 2: Piso térmico templado
        Fact(tipo_suelo="Ts4"),  # Condición 3: Tipo de suelo franco
        Fact(precipitacion_anual=P(lambda x: 500 <= x <= 4000)),  # Condición 4: Precipitación entre 500 y 4000 mm
        Fact(proposito_cultivo="Pc1")  # Condición 5: Propósito consumo personal
    )
    def recomendacion_consumo_personal_pt2(self):
        print("¡La regla 4 se ha activado!")
        print("Recomendación para consumo personal en piso templado:")
        cultivos = [
            "Cebolla_Bulbo_R1", "Cebolla_Rama_Larga_R1", "Tomate_R1"
        ]
        print("Cultivos recomendados:", cultivos)
        self.declare(Fact(cultivos_recomendados=cultivos))

    # Regla 5: Región Insular, consumo personal
    @Rule(
        Fact(region="R2"),  # Condición 1: Región Insular
        Fact(piso_termico="Pt1"),  # Condición 2: Piso térmico cálido
        Fact(tipo_suelo="Ts2"),  # Condición 3: Tipo de suelo arenoso
        Fact(precipitacion_anual=P(lambda x: 0 <= x <= 750)),  # Condición 4: Precipitación entre 0 y 750 mm
        Fact(proposito_cultivo="Pc1")  # Condición 5: Propósito consumo personal
    )
    def recomendacion_insular_consumo_personal(self):
        print("¡La regla 5 se ha activado!")
        print("Recomendación para consumo personal en la región Insular:")
        cultivos = [
            "Frijol_R2", "Maiz_Amarillo_R2", "Maiz_Blanco_R2", "Soya_R2", "Tomate_R2", "Yuca_R2"
        ]
        print("Cultivos recomendados:", cultivos)
        self.declare(Fact(cultivos_recomendados=cultivos))

    # Regla 6: Región Insular, venta local
    @Rule(
        Fact(region="R2"),  # Condición 1: Región Insular
        Fact(piso_termico="Pt1"),  # Condición 2: Piso térmico cálido
        Fact(tipo_suelo="Ts4"),  # Condición 3: Tipo de suelo franco
        Fact(precipitacion_anual=P(lambda x: 0 <= x <= 750)),  # Condición 4: Precipitación entre 0 y 750 mm
        Fact(proposito_cultivo="Pc2")  # Condición 5: Propósito venta local
    )
    def recomendacion_insular_venta_local(self):
        print("¡La regla 6 se ha activado!")
        print("Recomendación para venta local en la región Insular:")
        cultivos = [
            "Aguacate_R2", "Banano_R2", "Cacao_R2", "Cafe_R2"
        ]
        print("Cultivos recomendados:", cultivos)
        self.declare(Fact(cultivos_recomendados=cultivos))

    # Regla 7: Región Insular, piso templado, consumo personal
    @Rule(
        Fact(region="R2"),  # Condición 1: Región Insular
        Fact(piso_termico="Pt2"),  # Condición 2: Piso térmico templado
        Fact(tipo_suelo="Ts4"),  # Condición 3: Tipo de suelo franco
        Fact(precipitacion_anual=P(lambda x: 0 <= x <= 750)),  # Condición 4: Precipitación entre 0 y 750 mm
        Fact(proposito_cultivo="Pc1")  # Condición 5: Propósito consumo personal
    )
    def recomendacion_insular_consumo_personal_pt2(self):
        print("¡La regla 7 se ha activado!")
        print("Recomendación para consumo personal en piso templado, región Insular:")
        cultivos = [
            "Cebolla_Bulbo_R2", "Cebolla_Rama_Larga_R2", "Frijol_R2", "Tomate_R2"
        ]
        print("Cultivos recomendados:", cultivos)
        self.declare(Fact(cultivos_recomendados=cultivos))

    # Regla 8: Región Pacífica, consumo personal
    @Rule(
        Fact(region="R3"),  # Condición 1: Región Pacífica
        Fact(piso_termico="Pt1"),  # Condición 2: Piso térmico cálido
        Fact(tipo_suelo="Ts1"),  # Condición 3: Tipo de suelo arcilloso
        Fact(precipitacion_anual=P(lambda x: x > 12700)),  # Condición 4: Precipitación mayor a 12700 mm
        Fact(proposito_cultivo="Pc1")  # Condición 5: Propósito consumo personal
    )
    def recomendacion_pacifico_consumo_personal(self):
        print("¡La regla 8 se ha activado!")
        print("Recomendación para consumo personal en la región Pacífica:")
        cultivos = [
            "Arveja_R3", "Banano_R3", "Cacao_R3", "Platano_R3", "Yuca_R3"
        ]
        print("Cultivos recomendados:", cultivos)
        self.declare(Fact(cultivos_recomendados=cultivos))
        
    # Regla 9: Región Pacífica, suelo franco, exportación
    @Rule(
        Fact(region="R3"),  # Condición 1: Región Pacífica
        Fact(piso_termico="Pt1"),  # Condición 2: Piso térmico cálido
        Fact(tipo_suelo="Ts4"),  # Condición 3: Tipo de suelo franco
        Fact(precipitacion_anual=P(lambda x: x > 12700)),  # Condición 4: Precipitación mayor a 12700 mm
        Fact(proposito_cultivo="Pc3")  # Condición 5: Propósito exportación
    )
    def recomendacion_pacifico_exportacion(self):
        print("¡La regla 9 se ha activado!")
        print("Recomendación para exportación en la región Pacífica:")
        cultivos = [
            "Aguacate_R3", "Cacao_R3", "Cana_Azucar_R3", "Cana_Panelera_R3"
        ]
        print("Cultivos recomendados:", cultivos)
        self.declare(Fact(cultivos_recomendados=cultivos))

    # Regla 10: Región Pacífica, piso templado, venta local
    @Rule(
        Fact(region="R3"),  # Condición 1: Región Pacífica
        Fact(piso_termico="Pt2"),  # Condición 2: Piso térmico templado
        Fact(tipo_suelo="Ts4"),  # Condición 3: Tipo de suelo franco
        Fact(precipitacion_anual=P(lambda x: x > 12700)),  # Condición 4: Precipitación mayor a 12700 mm
        Fact(proposito_cultivo="Pc2")  # Condición 5: Propósito venta local
    )
    def recomendacion_pacifico_venta_local(self):
        print("¡La regla 10 se ha activado!")
        print("Recomendación para venta local en la región Pacífica:")
        cultivos = [
            "Cebolla_Bulbo_R3", "Frijol_R3", "Hortalizas_Fruto_R3",
            "Maiz_Amarillo_R3", "Maiz_Blanco_R3"
        ]
        print("Cultivos recomendados:", cultivos)
        self.declare(Fact(cultivos_recomendados=cultivos))

    # Regla 11: Región Andina, consumo personal
    @Rule(
        Fact(region="R4"),  # Condición 1: Región Andina
        Fact(piso_termico="Pt1"),  # Condición 2: Piso térmico cálido
        Fact(tipo_suelo="Ts4"),  # Condición 3: Tipo de suelo franco
        Fact(precipitacion_anual=P(lambda x: 500 <= x <= 7000)),  # Condición 4: Precipitación entre 500 y 7000 mm
        Fact(proposito_cultivo="Pc1")  # Condición 5: Propósito consumo personal
    )
    def recomendacion_andina_consumo_personal(self):
        print("¡La regla 11 se ha activado!")
        print("Recomendación para consumo personal en la región Andina:")
        cultivos = [
            "Arveja_R4", "Frijol_R4", "Maiz_Amarillo_R4", "Maiz_Blanco_R4",
            "Soya_R4", "Tomate_R4", "Yuca_R4"
        ]
        print("Cultivos recomendados:", cultivos)
        self.declare(Fact(cultivos_recomendados=cultivos))

    # Regla 12: Región Andina, exportación
    @Rule(
        Fact(region="R4"),  # Condición 1: Región Andina
        Fact(piso_termico="Pt1"),  # Condición 2: Piso térmico cálido
        Fact(tipo_suelo="Ts1"),  # Condición 3: Tipo de suelo arcilloso
        Fact(precipitacion_anual=P(lambda x: 500 <= x <= 7000)),  # Condición 4: Precipitación entre 500 y 7000 mm
        Fact(proposito_cultivo="Pc3")  # Condición 5: Propósito exportación
    )
    def recomendacion_andina_exportacion(self):
        print("¡La regla 12 se ha activado!")
        print("Recomendación para exportación en la región Andina:")
        cultivos = [
            "Banano_R4", "Cacao_R4", "Cafe_R4", "Cana_Azucar_R4", "Cana_Panelera_R4"
        ]
        print("Cultivos recomendados:", cultivos)
        self.declare(Fact(cultivos_recomendados=cultivos))

    # Regla 13: Región Andina, piso templado, consumo personal
    @Rule(
        Fact(region="R4"),  # Condición 1: Región Andina
        Fact(piso_termico="Pt2"),  # Condición 2: Piso térmico templado
        Fact(tipo_suelo="Ts4"),  # Condición 3: Tipo de suelo franco
        Fact(precipitacion_anual=P(lambda x: 500 <= x <= 7000)),  # Condición 4: Precipitación entre 500 y 7000 mm
        Fact(proposito_cultivo="Pc1")  # Condición 5: Propósito consumo personal
    )
    def recomendacion_andina_consumo_personal_pt2(self):
        print("¡La regla 13 se ha activado!")
        print("Recomendación para consumo personal en piso templado, región Andina:")
        cultivos = [
            "Cebolla_Bulbo_R4", "Cebolla_Rama_Larga_R4", "Frijol_R4",
            "Papa_R4", "Tomate_R4"
        ]
        print("Cultivos recomendados:", cultivos)
        self.declare(Fact(cultivos_recomendados=cultivos))

    # Regla 14: Región Andina, piso templado, exportación
    @Rule(
        Fact(region="R4"),  # Condición 1: Región Andina
        Fact(piso_termico="Pt2"),  # Condición 2: Piso térmico templado
        Fact(tipo_suelo="Ts3"),  # Condición 3: Tipo de suelo limoso
        Fact(precipitacion_anual=P(lambda x: 500 <= x <= 7000)),  # Condición 4: Precipitación entre 500 y 7000 mm
        Fact(proposito_cultivo="Pc3")  # Condición 5: Propósito exportación
    )
    def recomendacion_andina_exportacion_pt2(self):
        print("¡La regla 14 se ha activado!")
        print("Recomendación para exportación en piso templado, región Andina:")
        cultivos = [
            "Cafe_R4", "Aguacate_R4"
        ]
        print("Cultivos recomendados:", cultivos)
        self.declare(Fact(cultivos_recomendados=cultivos))

    # Regla 15: Región Andina, piso frío, consumo personal
    @Rule(
        Fact(region="R4"),  # Condición 1: Región Andina
        Fact(piso_termico="Pt3"),  # Condición 2: Piso térmico frío
        Fact(tipo_suelo="Ts4"),  # Condición 3: Tipo de suelo franco
        Fact(precipitacion_anual=P(lambda x: 500 <= x <= 7000)),  # Condición 4: Precipitación entre 500 y 7000 mm
        Fact(proposito_cultivo="Pc1")  # Condición 5: Propósito consumo personal
    )
    def recomendacion_andina_consumo_personal_pt3(self):
        print("¡La regla 15 se ha activado!")
        print("Recomendación para consumo personal en piso frío, región Andina:")
        cultivos = [
            "Cebolla_Bulbo_R4", "Frijol_R4", "Papa_R4", "Haba_R4"
        ]
        print("Cultivos recomendados:", cultivos)
        self.declare(Fact(cultivos_recomendados=cultivos))

    # Regla 16: Región Andina, páramo, consumo personal
    @Rule(
        Fact(region="R4"),  # Condición 1: Región Andina
        Fact(piso_termico="Pt4"),  # Condición 2: Piso térmico páramo
        Fact(tipo_suelo="Ts4"),  # Condición 3: Tipo de suelo franco
        Fact(precipitacion_anual=P(lambda x: 500 <= x <= 7000)),  # Condición 4: Precipitación entre 500 y 7000 mm
        Fact(proposito_cultivo="Pc1")  # Condición 5: Propósito consumo personal
    )
    def recomendacion_andina_consumo_personal_pt4(self):
        print("¡La regla 16 se ha activado!")
        print("Recomendación para consumo personal en páramo, región Andina:")
        cultivos = [
            "Cubio_R4", "Ibia_R4"
        ]
        print("Cultivos recomendados:", cultivos)
        self.declare(Fact(cultivos_recomendados=cultivos))
        
    # Regla 17: Región Orinoquía, suelo arenoso, consumo personal
    @Rule(
        Fact(region="R5"),  # Condición 1: Región Orinoquía
        Fact(piso_termico="Pt1"),  # Condición 2: Piso térmico cálido
        Fact(tipo_suelo="Ts2"),  # Condición 3: Tipo de suelo arenoso
        Fact(precipitacion_anual=P(lambda x: 250 <= x <= 1500)),  # Condición 4: Precipitación entre 250 y 1500 mm
        Fact(proposito_cultivo="Pc1")  # Condición 5: Propósito consumo personal
    )
    def recomendacion_orinoquia_consumo_personal(self):
        print("¡La regla 17 se ha activado!")
        print("Recomendación para consumo personal en la región Orinoquía:")
        cultivos = [
            "Frijol_R5", "Hortalizas_Fruto_R5", "Maiz_Amarillo_R5",
            "Maiz_Blanco_R5", "Soya_R5", "Tomate_R5", "Yuca_R5"
        ]
        print("Cultivos recomendados:", cultivos)
        self.declare(Fact(cultivos_recomendados=cultivos))

    # Regla 18: Región Orinoquía, suelo franco, venta local
    @Rule(
        Fact(region="R5"),  # Condición 1: Región Orinoquía
        Fact(piso_termico="Pt1"),  # Condición 2: Piso térmico cálido
        Fact(tipo_suelo="Ts4"),  # Condición 3: Tipo de suelo franco
        Fact(precipitacion_anual=P(lambda x: 250 <= x <= 1500)),  # Condición 4: Precipitación entre 250 y 1500 mm
        Fact(proposito_cultivo="Pc2")  # Condición 5: Propósito venta local
    )
    def recomendacion_orinoquia_venta_local(self):
        print("¡La regla 18 se ha activado!")
        print("Recomendación para venta local en la región Orinoquía:")
        cultivos = [
            "Aguacate_R5", "Banano_R5", "Cacao_R5", "Platano_R5"
        ]
        print("Cultivos recomendados:", cultivos)
        self.declare(Fact(cultivos_recomendados=cultivos))

    # Regla 19: Región Amazónica, suelo arcilloso, consumo personal
    @Rule(
        Fact(region="R6"),  # Condición 1: Región Amazónica
        Fact(piso_termico="Pt1"),  # Condición 2: Piso térmico cálido
        Fact(tipo_suelo="Ts1"),  # Condición 3: Tipo de suelo arcilloso
        Fact(precipitacion_anual=P(lambda x: 1000 <= x <= 1500)),  # Condición 4: Precipitación entre 1000 y 1500 mm
        Fact(proposito_cultivo="Pc1")  # Condición 5: Propósito consumo personal
    )
    def recomendacion_amazonica_consumo_personal(self):
        print("¡La regla 19 se ha activado!")
        print("Recomendación para consumo personal en la región Amazónica:")
        cultivos = [
            "Arveja_R6", "Frijol_R6", "Hortalizas_Fruto_R6",
            "Maiz_Amarillo_R6", "Maiz_Blanco_R6", "Papa_R6", "Yuca_R6"
        ]
        print("Cultivos recomendados:", cultivos)
        self.declare(Fact(cultivos_recomendados=cultivos))

    # Regla 20: Región Amazónica, suelo franco, exportación
    @Rule(
        Fact(region="R6"),  # Condición 1: Región Amazónica
        Fact(piso_termico="Pt1"),  # Condición 2: Piso térmico cálido
        Fact(tipo_suelo="Ts4"),  # Condición 3: Tipo de suelo franco
        Fact(precipitacion_anual=P(lambda x: 1000 <= x <= 1500)),  # Condición 4: Precipitación entre 1000 y 1500 mm
        Fact(proposito_cultivo="Pc3")  # Condición 5: Propósito exportación
    )
    def recomendacion_amazonica_exportacion(self):
        print("¡La regla 20 se ha activado!")
        print("Recomendación para exportación en la región Amazónica:")
        cultivos = [
            "Aguacate_R6", "Banano_R6", "Cacao_R6"
        ]
        print("Cultivos recomendados:", cultivos)
        self.declare(Fact(cultivos_recomendados=cultivos))
# Crear la aplicación Flask
app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas

@app.route('/api/recomendacion', methods=['POST'])
def obtener_recomendacion():
    # Obtener datos de la solicitud JSON
    datos = request.json
    try:
        region = datos.get('region')
        piso_termico = datos.get('piso_termico')
        tipo_suelo = datos.get('tipo_suelo')
        precipitacion_anual = int(datos.get('precipitacion_anual'))
        proposito_cultivo = datos.get('proposito_cultivo')
        # Validar que todos los datos necesarios estén presentes
        if not all([region, piso_termico, tipo_suelo, proposito_cultivo]):
            return jsonify({"error": "Faltan datos requeridos"}), 400
        # Crear una instancia del motor de inferencia
        motor = SistemaExperto()
        motor.reset()
        # Declarar los hechos iniciales
        motor.declare(
            Fact(region=region),
            Fact(piso_termico=piso_termico),
            Fact(tipo_suelo=tipo_suelo),
            Fact(precipitacion_anual=precipitacion_anual),
            Fact(proposito_cultivo=proposito_cultivo)
        )
        # Ejecutar el motor de inferencia
        motor.run()
        # Obtener las recomendaciones
        recomendaciones = None
        for fact in motor.facts.values():  # Iterar sobre los valores de los hechos
            if isinstance(fact, dict) and "cultivos_recomendados" in fact:
                recomendaciones = fact["cultivos_recomendados"]
                break
        if recomendaciones:
            return jsonify({
                "success": True,
                "datos_entrada": {
                    "region": region,
                    "piso_termico": piso_termico,
                    "tipo_suelo": tipo_suelo,
                    "precipitacion_anual": precipitacion_anual,
                    "proposito_cultivo": proposito_cultivo
                },
                "cultivos_recomendados": recomendaciones
            })
        else:
            return jsonify({
                "success": False,
                "mensaje": "No se encontraron recomendaciones para los parámetros proporcionados."
            })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Ruta de información
@app.route('/api/info', methods=['GET'])
def obtener_info():
    return jsonify({
        "sistema": "Sistema Experto de Recomendación de Cultivos",
        "regiones": ["R1 (Caribe)", "R2 (Insular)", "R3 (Pacífica)", "R4 (Andina)", "R5 (Orinoquía)", "R6 (Amazónica)"],
        "pisos_termicos": ["Pt1 (Cálido)", "Pt2 (Templado)", "Pt3 (Frío)", "Pt4 (Páramo)"],
        "tipos_suelo": ["Ts1 (Arcilloso)", "Ts2 (Arenoso)", "Ts3 (Limoso)", "Ts4 (Franco)"],
        "propositos_cultivo": ["Pc1 (Consumo Personal)", "Pc2 (Venta Local)", "Pc3 (Exportación)"]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
