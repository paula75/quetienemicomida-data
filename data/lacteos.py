
'''
 COLUMNAS = ['Marca', 'Tipo', 'Energía', 'Proteinas', 'Grasas', 'Hidratos de carbono', 'Grasas saturadas', 'Colesterol', 'Azúcar total', 'Sodio', 'Ingredientes', 'imagen']

'''
PATH_IMAGES_LECHE = './images/leche'
PATH_IMAGES_YOGURT = './images/yogurt'


leches = [
    ['Colun', 'Descremada', 32, 3.3, 0.05, 4.7, 0.03, 0.16, 4.7, 32, 'Leche fluida natural', PATH_IMAGES_LECHE + '/colun_descremada.png'],
    ['Soprole', 'Entera', 58, 3, 3.1, 4.6, 2, 9.6, 4.6, 38, 'Leche fluida natural entera', PATH_IMAGES_LECHE + '/soprole_entera.png'],
    ['Colun', 'Semidescremada chocolate', 78, 3.1, 1.6, 12.8, 1.02, 5, 11.6, 61, 'Leche natural parcialmente descremada, Azúcar, Cacao, Lecitina de soya, Cloruro de sodio, Celulosa microcristalina, Carboximetilcelulosa, Carragenina, Vitamina a, Vitamina d, Vitamina e', PATH_IMAGES_LECHE + '/colun_semidescremadachocolate.png'],
    ['Loncoleche', 'Descremada', 33, 3.3, 0.1, 4.8, None, None, 4.8, 32, 'Leche fluida natural descremada', PATH_IMAGES_LECHE + '/loncoleche_descremada.png'],
    ['Loncoleche', 'Semidescremada sin lactosa', 45, 3.2, 1.5, 4.6, 1, 6, 4.6, 40, 'Leche fluida natural semidescremada, Enzima lactasa', PATH_IMAGES_LECHE + '/loncoleche_semidescremadasinlactosa.png'],
    ['Surlat', 'Descremada sin lactosa', 33, 3.1, 0.1, 4.9, None, None, 4.8, 40, 'Leche natural descremada, Enzima lactasa, Vitamina a, Vitamina d, Vitamina e', PATH_IMAGES_LECHE + '/surlat_descremadasinlactosa.png']
]

yogurts = [
    ['Danone', 'Oikos', 98, 4.6, 6, 6.5, 4, 19.7, 5.7, 59, 'Leche fluida entera, Sólidos lácteos, Almidón de maíz modificado, Concentrado de proteína de leche, Gelatina, Sorbato de potasio, Concentrado de tocoferoles mixtos, L. bulgaricus, S. thermophilus', PATH_IMAGES_YOGURT + '/danone_oikos.png'],
    ['Soprole', 'Protein', 68, 6.6, 1.8, 6.3, 1.34, 11.4, 6.3, 65, 'Leche fluida descremada, Leche fluida entera, Concentrado de proteína de leche, Gelatina, Lactasa, Cepa de yoghurt l. bulgaricus, Cepa de yoghurt s. thermophilus, Sorbato de potasio, Sucralosa, Estevia', PATH_IMAGES_YOGURT + '/soprole_protein.png'],
    ['Soprole', 'Natural', 70, 3.6, 3.1, 6.9, 2.2, 10.6, 6.9, 55, 'Leche entera fluida, Leche en polvo descremada, Gelatina, Sorbato de potasio, Cepa de yoghurt l. bulgaricus, Cepa de yoghurt s. thermophilus', PATH_IMAGES_YOGURT + '/soprole_natural.png'],
    ['Nestle', 'Griego sin endulzar', 99, 3.7, 5.3, 9, 3.3, 19, 6.2, 87, 'Crema de leche, Almidón modificado de maíz, Concentrado de proteína de leche, Gelatina, Sorbato de potasio, Cultivos lácteos, Leche descremada reconstituida, Leche entera reconstituida', PATH_IMAGES_YOGURT + '/nestle_griegosinendulzar.png'],
    ['Soprole', 'Sin azúcar', 54, 3.5, 1, 7.7, None, None, 4.5, 61, 'Leche descremada, Crema de leche, Almidón de maíz modificado, Leche en polvo descremada, Polidextrosa, Gelatina, Lactasa, Sorbato de potasio, Cepa de yoghurt l. bulgaricus, Cepa de yoghurt s. thermophilus, Sucralosa, Estevia, Saborizante idéntico a natural, Colorante natural cúrcuma, Colorante natural annato', PATH_IMAGES + '/soprole_sinazucarvainilla.png']
]