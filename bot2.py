import random
import discord
import os
from bot_logic import get_duck_image_url
from bot_logic import gen_pass
from discord.ext import commands


# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix='¿', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')
    
@bot.command()
async def tipos(ctx):
    await ctx.send("Los residuos son materiales descartados tras cumplir su función principal. Una adecuada clasificación y gestión de estos permite minimizar su impacto ambiental, fomentar el reciclaje y aprovechar recursos valiosos. Cada tipo de residuo tiene características específicas que determinan su tratamiento y potencial reutilización. A continuación, se presentan los principales tipos de residuos:\n 1. electronicos\n 2. organicos\n 3. inorganicos\n 4.vidrio\n 5. metales\n 6. plasticos\n 7. papel y cartón\n De cual deseas aprender? para obtener la info escribe el comando ¿(tipo de residuo))\n\nRECUERDA QUE TAMBIEN PUEDO ACONSEJARTE, DARTE ESTADISTICAS Y RECOMENDARTE TIPS, UTILIZA EL COMANDO HELP PARA VER LOS COMANDOS")
    
@bot.command()
async def electronicos(ctx):
    desc_1 = ["Los desechos electrónicos, o e-waste, son residuos de dispositivos eléctricos en desuso, como celulares, computadoras y baterías. Contienen materiales valiosos y sustancias tóxicas, por lo que es crucial gestionarlos adecuadamente para evitar daños ambientales y riesgos para la salud, aprovechando además sus recursos reciclables.","Los desechos electrónicos son residuos de equipos eléctricos y electrónicos obsoletos, como teléfonos o computadoras. Contienen metales valiosos y sustancias tóxicas, lo que hace esencial su reciclaje para reducir riesgos ambientales y aprovechar sus materiales reutilizables.",]
    await ctx.send(random.choice(desc_1))
    electronics = os.listdir("electros")
    electrico = random.choice(electronics)
    with open(f"electros/{electrico}","rb") as f:
        
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def organicos(ctx):
    desc_1o = ["Los residuos orgánicos son desechos de origen biológico, como restos de comida, cáscaras de frutas y hojas. Son biodegradables y pueden transformarse en compost o abono, reduciendo su impacto ambiental y fomentando la fertilidad del suelo.","Los residuos orgánicos provienen de materia viva, como restos de alimentos y podas de jardín. Su descomposición natural permite reutilizarlos en procesos como el compostaje, ayudando a reducir basura y a generar recursos sostenibles para la agricultura."]
    await ctx.send(random.choice(desc_1o))
    organics = os.listdir("organicocs")
    organico = random.choice(organics)
    with open(f"organicocs/{organico}","rb") as f:
        
        picture = discord.File(f)
    await ctx.send(file=picture)
    
@bot.command()
async def inorganicos(ctx):
    desc_1in = ["Los residuos inorgánicos son desechos no biodegradables que provienen de materiales como vidrio, plástico, metales y papel. Aunque no se descomponen naturalmente, muchos son reciclables, lo que permite reducir su impacto ambiental y reutilizar sus componentes en nuevos productos.","Los residuos inorgánicos incluyen materiales artificiales o minerales como plásticos, metales y vidrios. Debido a su lenta descomposición, requieren un manejo adecuado que priorice el reciclaje y evite su acumulación en el medio ambiente."]
    await ctx.send(random.choice(desc_1in))
    inorganics = os.listdir("organicocs")
    inorganico = random.choice(inorganics)
    with open(f"inorganicocs/{inorganico}","rb") as f:
        
        picture = discord.File(f)
    await ctx.send(file=picture)
    
@bot.command()
async def vidrio(ctx):
    desc_1v = ["Los residuos de vidrio son desechos provenientes de objetos como botellas, frascos y ventanas. Son 100% reciclables y pueden reutilizarse infinitamente sin perder calidad, lo que los convierte en un recurso valioso para la economía circular.","El vidrio como residuo incluye envases y objetos rotos que no se degradan naturalmente. Su reciclaje contribuye a reducir el consumo de energía y materias primas, promoviendo un manejo sostenible y eficiente de este material."]
    await ctx.send(random.choice(desc_1v))
    vidrioz = os.listdir("vidriocs")
    vidrios = random.choice(vidrioz)
    with open(f"vidriocs/{vidrios}","rb") as f:
        
        picture = discord.File(f)
    await ctx.send(file=picture)
    
@bot.command()
async def metales(ctx):
    desc_1m = ["Los residuos metálicos incluyen desechos como latas, cables, herramientas y restos de construcción hechos de materiales como aluminio, acero y cobre. Son altamente reciclables y su reutilización reduce el consumo de recursos naturales y energía.","Los metales como residuo provienen de productos industriales y domésticos, como latas y electrodomésticos. Su reciclaje es esencial para disminuir la extracción minera, ya que se pueden fundir y reutilizar sin perder sus propiedades originales."]
    await ctx.send(random.choice(desc_1m))
    metalez = os.listdir("metalecs")
    metales = random.choice(metalez)
    with open(f"metalecs/{metales}","rb") as f:
        
        picture = discord.File(f)
    await ctx.send(file=picture)
       
@bot.command()
async def plasticos(ctx):
    desc_1p = ["Los residuos plásticos provienen de envases, bolsas, botellas y otros productos fabricados con polímeros sintéticos. Aunque muchos son reciclables, su descomposición tarda siglos, lo que los convierte en una de las principales amenazas para el medio ambiente si no se gestionan adecuadamente.","El plástico como residuo incluye materiales de un solo uso y duraderos, como empaques y utensilios. Su correcto manejo mediante reciclaje o reutilización ayuda a reducir la contaminación, especialmente en ecosistemas marinos, donde tiene un impacto devastador."]
    await ctx.send(random.choice(desc_1p))
    plasticoz = os.listdir("plasticocs")
    plasticos = random.choice(plasticoz)
    with open(f"plasticocs/{plasticos}","rb") as f:
        
        picture = discord.File(f)
    await ctx.send(file=picture)   
    
@bot.command()
async def papel_carton(ctx):
    desc_1pc = ["Los residuos de papel y cartón incluyen materiales como hojas, periódicos, cajas y embalajes. Son reciclables y, al reutilizarlos, se reduce la tala de árboles y el consumo de agua y energía en su producción.","El papel y el cartón son residuos biodegradables provenientes de fibras vegetales. Su reciclaje es clave para disminuir la generación de basura, ya que pueden convertirse en nuevos productos como cuadernos, empaques o papel higiénico."]
    await ctx.send(random.choice(desc_1pc))
    papelz = os.listdir("papelecs")
    papeles = random.choice(papelz)
    with open(f"papelecs/{papeles}","rb") as f:
        
        picture = discord.File(f)
    await ctx.send(file=picture)   
    
@bot.command()
async def consejos(ctx):
    text = "mira, acá te doy un consejo :D\n\n"
    consejos = ["Vidrio: Separa el vidrio por colores (verde, ámbar y transparente) antes de llevarlo al reciclaje para facilitar su procesamiento.","Orgánicos: Coloca los restos de comida y cáscaras en un compostador para crear abono natural.","Plásticos: Aplasta las botellas para ahorrar espacio y revisa el símbolo de reciclaje para identificar su tipo.","Metales: Limpia las latas antes de reciclarlas para evitar contaminación en los centros de acopio.","Papel y cartón: Evita reciclar papel o cartón que esté mojado o grasoso, ya que afecta su reutilización.","Electrónicos: Lleva tus dispositivos obsoletos a un punto limpio para extraer materiales reutilizables.","Pilas y baterías: No las tires en la basura común; busca centros especializados que las recojan.","Ropa: Dona prendas en buen estado o busca programas de reciclaje textil en tu ciudad.","Aceite usado: Nunca lo viertas en el fregadero; deposítalo en puntos de recolección para reciclaje.","Tetra Pak: Lávalos, aplástalos y asegúrate de que tu centro de reciclaje los acepte."]  
    await ctx.send(text + random.choice(consejos))

@bot.command()
async def est(ctx):
    text1 = "Sabías que:\n\n"
    est = ["Reciclar una tonelada de vidrio ahorra más de 1 tonelada de recursos naturales como arena y caliza.","Cada tonelada de papel reciclado salva 17 árboles y reduce el consumo de 26,500 litros de agua.","Reciclar una lata de aluminio puede ahorrar suficiente energía para hacer funcionar un televisor durante 3 horas.","Por cada kilogramo de plástico reciclado, se ahorran aproximadamente 2 kilogramos de emisiones de CO2.","El reciclaje de cartón reduce el consumo de petróleo necesario para producir papel nuevo.","Reutilizar residuos orgánicos como compost reduce hasta el 50% de los desechos domésticos enviados a vertederos.","Por cada tonelada de acero reciclado, se ahorran 1,100 kilogramos de mineral de hierro.","Reciclar una botella de plástico PET puede ahorrar suficiente energía para encender una bombilla durante 3 horas.","Una batería reciclada evita que metales tóxicos contaminen hasta 600,000 litros de agua.","Cada tonelada de electrónicos reciclados recupera aproximadamente 250 gramos de oro y 9 kilogramos de cobre."]
    await ctx.send(text1 + random.choice(est))
    
@bot.command()
async def recom(ctx):
    text1 = "Y por qué no?\n\n"
    reco = ["En lugar de botellas plásticas, utiliza termos reutilizables hechos de acero inoxidable o vidrio.","Reemplaza bolsas plásticas con bolsas de tela o malla para tus compras diarias.","Opta por cepillos de dientes de bambú en lugar de los tradicionales de plástico.","Cambia los popotes plásticos por opciones de acero inoxidable, bambú o silicona.","Prefiere envases de vidrio para alimentos, ya que son más duraderos y reciclables.","Sustituye los pañales desechables por pañales de tela reutilizables para reducir residuos.","Utiliza toallas de tela o esponjas en lugar de servilletas o toallas de papel.","Compra productos a granel para reducir el uso de empaques plásticos innecesarios.","Usa baterías recargables para disminuir la cantidad de desechos electrónicos.","En vez de utensilios plásticos desechables, elige cubiertos reutilizables de acero o madera."]
    await ctx.send(text1 + random.choice(reco))


bot.run("")
