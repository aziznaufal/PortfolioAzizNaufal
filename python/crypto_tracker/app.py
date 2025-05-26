from flask import Flask
from routes.router import setup_routes
from middleware.logger import register_middleware
from routes.chart_route import chart_route

app = Flask(__name__)
app.register_blueprint(chart_route)
setup_routes(app)
register_middleware(app)  # ⬅️ Register the middleware here


if __name__ == "__main__":
    app.run(debug=True)
