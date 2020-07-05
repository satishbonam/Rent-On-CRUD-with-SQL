# import resprctive blueprints and flask REstful resources
from .blueprint_test import bp
from app.main import api
from app.main.routes.Users import UserRegistration
from app.main.routes.Authentication import Login, Logout
from app.main.routes.Property import Property, EditProperty, DeleteProperty
from app.main.routes.Rented import Rented


def add_resources(app):
    """
    Method to add resources to app context

    Args:
        app (object): object of Flask representing the app in context
    """
    api.add_resource(UserRegistration, '/registration')
    api.add_resource(Login, '/login')
    api.add_resource(Logout, '/logout')
    api.add_resource(Property, '/property')
    api.add_resource(EditProperty, '/edit_property')
    api.add_resource(DeleteProperty, '/delete_property')
    api.add_resource(Rented, '/rented')


def register_blueprints(app):
    """
    Method to add blueprints to app context

    Args:
        app (object): object of Flask representing the app in context
    """
    app.register_blueprint(bp)
