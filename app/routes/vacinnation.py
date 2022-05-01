from flask import Blueprint
from app.controllers.vacinnation_controller import post_vaccination, get_vaccination

bp_vacinnation = Blueprint("vaccination",__name__,url_prefix="/vaccination")
bp_vacinnation.post("")(post_vaccination)
bp_vacinnation.get("")(get_vaccination)