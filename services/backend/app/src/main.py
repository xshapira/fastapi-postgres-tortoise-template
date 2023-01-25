from src.core.apps import app
from src.database.service import DatabaseService
from src.core.route_manager import mount_routes


DatabaseService.register_app(app=app)
mount_routes(app=app)
