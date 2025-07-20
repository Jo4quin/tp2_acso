def readlines_mock(path="palabras.txt"):
    with open(path, "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]

def cuenta(palabra, lineas, alto, bajo):
    if bajo > alto:
        raise Exception("explode_bomb: fuera de rango")
    mid = (bajo + alto) // 2
    if mid >= len(lineas):
        raise Exception("explode_bomb: índice fuera de rango")
    linea = lineas[mid]
    c = ord(linea[0])
    if palabra == linea:
        return c
    elif palabra > linea:
        if mid >= alto:
            raise Exception("explode_bomb: derecha")
        return c + cuenta(palabra, lineas, alto, mid + 1)
    else:
        if mid <= bajo:
            raise Exception("explode_bomb: izquierda")
        return c + cuenta(palabra, lineas, mid - 1, bajo)

def buscar_inputs_validos():
    lineas = readlines_mock()
    print(f"{len(lineas)} líneas del archivo")
    encontrados = []
    
    for palabra in lineas:
        try:
            valor = cuenta(palabra, lineas, len(lineas) - 1, 0)
            
            if 401 <= valor <= 799:
                encontrados.append((palabra, valor))
                print(f" {palabra} -> {valor} (VÁLIDO)")
            else:
                print(f"{palabra} -> {valor} (fuera de rango 401-799)")

        except Exception as e:
            print(f"✖️ {palabra} falló: {e}")

    return encontrados

def generar_archivo_resultados(resultados):
    with open("valids.txt", "w") as f:
        f.write("# Combinaciones válidas para la bomba\n")
        for palabra, valor in resultados:
            linea = f"{palabra} {valor}\n"
            f.write(linea)
    
    print(f"{len(resultados)} posibles resultados en valids.txt")

if __name__ == "__main__":
    resultados = buscar_inputs_validos()
    
    if resultados:
        for palabra, valor in resultados:
            print(f"   {palabra} {valor}")
        
        generar_archivo_resultados(resultados)
        
        print(f"\n{len(resultados)} combinaciones válidas")
    else:
        print("No se encontraron combinaciones")