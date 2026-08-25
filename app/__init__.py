#===========================================================
# PROJECT NAME HERE
# By YOUR NAME HERE
#===========================================================

from flask import Flask, request, session, render_template, flash, redirect, send_file, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from os import getenv
from io import BytesIO
import html
from app.helpers import *


# Create the app
app = Flask(__name__)


#===========================================================
# App Routes Handlers
#===========================================================

#-----------------------------------------------------------
# Home page - Show all notes
#-----------------------------------------------------------
@app.get("/configuration")
def show_config():
    with connect_db() as db:
        sql = """
            SELECT 
                configurations.name AS con_name,
                configurations.cost AS con_cost,
                cpus.name           AS cpu_name,
                motherboards.name   AS motherboard_name,
                harddrives.name     AS harddrive_name,
                soliddrives.name    AS soliddrive_name,
                ram.name            AS ram_name,
                gpus.name           AS gpu_name,
                cases.name          AS case_name,
                coolers.name        AS cooler_name,
                powersupply.name    AS psu_name,
                os.name             AS os_name

            FROM configurations WHERE id = 1
            JOIN cpus ON configurations.cpu = cpus.id
            JOIN motherboards ON configurations.motherboard = motherboards.id
            LEFT JOIN harddrives ON configurations.hard_drive = harddrives.id
            JOIN soliddrives ON configurations.solid_drive = soliddrives.id
            JOIN ram ON configurations.ram = ram.id
            LEFT JOIN gpus ON configurations.gpu = gpus.id
            JOIN cases ON configurations.`case` = cases.id
            JOIN coolers ON configurations.cooler = coolers.id
            JOIN networkcard ON configurations.network_card = networkcard.id
            JOIN powersupply ON configurations.psu = powersupply.id
            JOIN os ON configurations.os = os.id

        """
        params = ()
        configs = db.execute(sql, params).fetchall()

        

        return render_template("pages/configurations.jinja", configs=configs)


#===========================================================
# Configure the app
#===========================================================
load_dotenv()
app.config.from_prefixed_env()
init_logging(app)
init_text_filters(app)
init_date_filters(app)
init_error_handlers(app)
init_database()
register_commands(app)

