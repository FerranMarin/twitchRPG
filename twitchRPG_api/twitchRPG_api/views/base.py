from flask import jsonify
from flask import abort
from flask import make_response
from flask import Blueprint

from twitchRPG_core.models import Player, Enemy
from twitchRPG_api.authentication import auth
from .. import filters


base_api = Blueprint('base_api', __name__)


@base_api.route('/', methods=['GET'])
def index():
    msg = {
        'status': 1,
        'msg': "Welcome to TwitchRPG API",
        'ip': filters.get_remote_ip()
    }
    return jsonify(msg)


@base_api.route('/players', methods=['GET'])
def get_players():
    return jsonify(Player().get_players())


@base_api.route('/enemies', methods=['GET'])
def get_enemies():
    return jsonify(Enemy().get_enemies())
