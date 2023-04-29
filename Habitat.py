 class Habitat:
    def __init__(self, tipo_h, id_tipo_h, tipo_dieta_ah, tipo_adecuacion_h, cantidad_ah, tipo_adecu_s), temperatura:
        self.tipo_habitad = tipo_h
        self.id_tipo_habitad = id_tipo_h
        self.tipo_dieta_animales = tipo_dieta_ah
        self.tipo_adecuacion = tipo_adecuacion_h
        self.cantidad_animales_h = 0
        self.vector_animales = []
        self.adecuacion_h = tipo_adecu_s
        self.temperatura = temperatura

    def get_tipo_h(self):
        return self.tipo_habitad

    def get_adecuacion_s(self):
        return self.adecuacion_h

    def set_tipo_h(self, tipo_h):
        self.tipo_habitad = tipo_h

    def get_id_tipo_h(self):
        return self.id_tipo_habitad

    def get_tipo_dieta(self):
        return self.tipo_dieta_animales

    def set_tipo_dieta(self, tipo):
        self.tipo_dieta_animales = tipo

    def get_tipo_adecuacion(self):
        return self.tipo_adecuacion

    def set_tipo_adecuacion(self, tipo):
        self.tipo_adecuacion = tipo

    def get_cantidad_ah(self):
        return self.cantidad_animales_h

    def set_cantidad_ah(self, new_ca):
        if new_ca == 1:
            self.cantidad_animales_h += 1
        else:
            self.cantidad_animales_h -= 1

    def __del__(self):
        for animal in self.vector_animales:
            del animal
        self.vector_animales.clear()

    def agregar_animal_h(self, new_animal):
        ban = 0
        ban_condi = 0
        try:
            # AGREGAR MAS CONDICIONES ANTES DE AGRAGR AL ANIMAL TENER EN CUENTA CARACTERISTICAS DEL ANIMAL Y DEL HABITAD
            # Verifica que Tipo de habitat coincida entre el animal y el habitat
            if self.id_tipo_habitad == new_animal.get_id_tipo_ha():
                # verifica que el tipo de adecuacion del habitad y del animal coincidan
                if self.tipo_adecuacion == new_animal.get_tipo_adap_a():
                    # verifica que los animales dentro del habitat compartan la dieta del nuevo animal
                    if self.tipo_dieta_animales == new_animal.get_tipo_dieta():
                        # Lo ingresa pues no hay animales dentro del habitat
                        if len(self.vector_animales) == 0:
                            self.vector_animales.append(new_animal)
                            ban_condi = 1
                        # verifica que haya espacio para el animal dentro del habitat
                        elif len(self.vector_animales) <= 14:
                            if new_animal.get_tipo_dieta() == 1:
                                if new_animal.get_nombre_especie() == new_animal.get_nombre_especie():
                                    self.vector_animales.append(new_animal)
                                    ban_condi = 1
                                else:
                                    print("La especies carnivoras distintas no pueden convivir juntas ")
                                    print(new_animal.get_nombre_especie() + " y " + new_animal.get_nombre_especie())
                                    print("Es Peligroso tenerlas Juntas intentalo en otro habitat\n")
                            elif new_animal.get_tipo_dieta() == 3:
                                if new_animal.get_nombre_especie() == new
 
    


