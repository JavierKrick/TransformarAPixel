from PIL import Image
import numpy as np


from PIL import Image


## volver pixles
# Cargar la imagen original
imagen = Image.open("/home/javier/Desktop/PixelArt/Cabra.png")

## Elegir tamaño
## por ejemplo 25 / 50 un personaje
## o 342 / 192 un paisaje en deadcells


# Reducir la resolución
imagen_pequeña = imagen.resize((209, 250), Image.NEAREST)



# Escalar la imagen de nuevo a su tamaño original para visualizar los píxeles
imagen_pixel_art = imagen_pequeña.resize(imagen.size, Image.NEAREST)





# Convertir un color hexadecimal a RGB
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
  
# Definir la paleta de 8 colores en formato hexadecimal
#Propia
hex_palette1 =[  
    "#193342", "#223D52", "#2A526D", "#386A6C", "#2A8559", "#43AA53", "#5BB74C",
    "#95CA60", "#64DC70", "#F1F37C", "#FFFFFF", "#40183E", "#5F2645", "#7A2940", 
    "#8E2642", "#B33036", "#D53A39", "#E65B32", "#F57B3A", "#FF9A3B", "#FFC159", 
    "#182231", "#3B6791", "#337FBD", "#3C91D6", "#3BABD3", "#45DAE8", "#5BF3E6", 
    "#7EFCDA", "#A8FBD6", "#CBFFE2", "#1A0631", "#200E39", "#36154F", "#571B69", 
    "#85268A", "#AA318F", "#C73C9E", "#DB50A0", "#DB5B95", "#F582A3", "#FCA1A1", 
    "#1C2929", "#263536", "#334848", "#4E625A", "#658383", "#8EA0A2", "#9D8080", 
    "#BACFCF", "#E2E9EA"
]

# Apollo
hex_palette2 =[  
    "#172038", "#253a5e", "#3c5e8b", "#4f8fba", "#73bed3", "#a4dddb",
    "#19332d", "#25562e", "#468232", "#75a743", "#a8ca58", "#d0da91",
    "#4d2b32", "#7a4841", "#ad7757", "#c09473", "#d7b594", "#e7d5b3",
    "#341c27", "#602c2c", "#884b2b", "#be772b", "#de9e41", "#e8c170",
    "#241527", "#411d31", "#752438", "#a53030", "#cf573c", "#da863e",
    "#1e1d39", "#402751", "#7a367b", "#a23e8c", "#c65197", "#df84a5",
    "#090a14", "#10141f", "#151d28", "#202e37", "#394a50", "#577277",
    "#819796", "#a8b5b2", "#c7cfcc", "#ebede9"
]


hex_palette = hex_palette1 + hex_palette2


# Convertir la paleta de colores hexadecimales a RGB
palette = [hex_to_rgb(color) for color in hex_palette]

def find_closest_color(pixel, palette):
    # Calcular la distancia entre el píxel y cada color en la paleta
    distances = [np.linalg.norm(np.array(pixel) - np.array(color)) for color in palette]
    # Devolver el color de la paleta más cercano
    return palette[np.argmin(distances)]

def apply_palette(image, palette):
    # Convertir la imagen a un array numpy
    img_array = np.array(image)
    # Crear un array vacío para la nueva imagen
    new_img_array = np.zeros_like(img_array)
    
    # Recorrer cada píxel y encontrar el color más cercano en la paleta
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            new_img_array[i, j] = find_closest_color(img_array[i, j], palette)
    
    # Convertir de nuevo a imagen
    return Image.fromarray(new_img_array.astype('uint8'), 'RGB')

# Abrir la imagen original
image = imagen_pixel_art.convert('RGB')

# Aplicar la paleta de colores
new_image = apply_palette(image, palette)

# Guardar la nueva imagen
new_image.save("CabraPixel.png")
