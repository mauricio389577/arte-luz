from flask import Flask, render_template_string

app = Flask(__name__)

# Datos de muestra
obras = [
    {"titulo": "Constelación Urbana", "imagen": "https://source.unsplash.com/400x300/?light,art", "descripcion": "Una instalación inmersiva en el centro de Santiago."},
    {"titulo": "Reflejo Croma", "imagen": "https://source.unsplash.com/400x300/?neon,light", "descripcion": "Juego de espejos y luces LED multicolores."},
    {"titulo": "Bruma Solar", "imagen": "https://source.unsplash.com/400x300/?installation,light", "descripcion": "Luz y niebla en movimiento."}
]

@app.route("/")
def inicio():
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Arte de Luz</title>
        <style>
            body {
                margin: 0;
                font-family: 'Segoe UI', sans-serif;
                background-color: #111;
                color: #f1f1f1;
            }
            header {
                background: linear-gradient(90deg, #6e3ff2, #9f72f9);
                padding: 1rem;
                text-align: center;
            }
            h1 {
                margin: 0;
            }
            .galeria {
                display: flex;
                flex-wrap: wrap;
                gap: 20px;
                justify-content: center;
                padding: 2rem;
            }
            .obra {
                background-color: #222;
                border-radius: 10px;
                overflow: hidden;
                width: 300px;
                box-shadow: 0 0 10px #6e3ff2;
                transition: transform 0.2s;
            }
            .obra:hover {
                transform: scale(1.03);
            }
            .obra img {
                width: 100%;
                display: block;
            }
            .obra-info {
                padding: 1rem;
            }
            .obra-info h3 {
                margin: 0 0 0.5rem 0;
                color: #cfaeff;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Galería Arte de Luz</h1>
        </header>
        <div class="galeria">
            {% for obra in obras %}
            <div class="obra">
                <img src="{{ obra.imagen }}" alt="Obra de luz">
                <div class="obra-info">
                    <h3>{{ obra.titulo }}</h3>
                    <p>{{ obra.descripcion }}</p>
                </div>
            </div>
            {% endfor %}
        </div>
    </body>
    </html>
    """
    return render_template_string(html, obras=obras)

if __name__ == "__main__":
    app.run(debug=True)
