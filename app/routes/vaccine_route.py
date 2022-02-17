from flask import Blueprint
from app.controllers import vaccine_controller

bp = Blueprint("vaccine", __name__, url_prefix="/vaccinations")

bp.post("")(vaccine_controller.create_vaccine_card)
bp.get("")(vaccine_controller.get_vaccine_cards)