from flask import Blueprint

routes = Blueprint('routes', __name__)

from .city import *
from .index import *
