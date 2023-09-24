def clasificar_espectro(frecuencia):
  """
  Clasifica una onda en el espectro electromagnético según su frecuencia.

  Args:
    frecuencia: La frecuencia de la onda en hercios.

  Returns:
    La parte del espectro electromagnético en la que se encuentra la onda.
  """
# Dependiendo el tipo de frecuencia que se digite da una onda diferente

  if frecuencia < 30:
    return "Ondas de radio muy bajas (VLF)"
  elif frecuencia < 300:
    return "Ondas de radio bajas (LF)"
  elif frecuencia < 3000:
    return "Ondas de radio medias (MF)"
  elif frecuencia < 30000:
    return "Ondas de radio altas (HF)"
  elif frecuencia < 300000:
    return "Ondas de radio muy altas (VHF)"
  elif frecuencia < 3000000:
    return "Microondas"
  elif frecuencia < 300000000:
    return "Luz infrarroja"
  elif frecuencia < 300000000000:
    return "Luz visible"
  elif frecuencia < 30000000000000:
    return "Luz ultravioleta"
  elif frecuencia < 300000000000000:
    return "Rayos X"
  else:
    return "Rayos gamma"


if __name__ == "__main__":
  frecuencia = float(input("Ingrese la frecuencia de la onda en Hz: "))
  print(f"La onda se encuentra en el espectro {clasificar_espectro(frecuencia)}.")
