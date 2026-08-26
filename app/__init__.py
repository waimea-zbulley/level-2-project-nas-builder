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
@app.get("/")
def main_page():
    return render_template("pages/homepage.jinja")

@app.get("/configurations")
def configurations():
    with connect_db() as db:
        sql = """
            SELECT
                configurations.name,
                configurations.id,
                configurations.cost
            
            FROM configurations
        """
        params = ()
        configs = db.execute(sql, params).fetchall()
        
        return render_template("pages/configurations.jinja", configs=configs)

@app.get("/configuration/<int:id>")
def show_config(id):
    with connect_db() as db:
        sql = """
            SELECT 
                configurations.id   AS con_id,
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

            FROM configurations
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
            JOIN os ON configurations.os = os.id WHERE configurations.id = ?

        """
        params = (id,)
        configs = db.execute(sql, params).fetchone()

        return render_template("pages/configuration.jinja", config=configs)

@app.get("/configuration/new")
def new_config():
    with connect_db() as db:
        sql_cpu = """
            SELECT name, cost, id
            FROM cpus
        """
        sql_mb = """
            SELECT name, cost, id
            FROM motherboards
        """
        sql_hdd = """
            SELECT name, cost, id
            FROM harddrives
        """
        sql_ssd = """
            SELECT name, cost, id
            FROM soliddrives
        """
        sql_ram = """
            SELECT name, cost, id
            FROM ram
        """
        sql_gpu = """
            SELECT name, cost, id
            FROM gpus
        """
        sql_case = """
            SELECT name, cost, id
            FROM cases
        """
        sql_cooler = """
            SELECT name, cost, id
            FROM coolers
        """
        sql_nwcard = """
            SELECT name, cost, id
            FROM networkcard
        """
        sql_psu = """
            SELECT name, cost, id
            FROM powersupply
        """
        sql_os = """
            SELECT name, cost, id
            FROM os
        """

        params = ()
        cpus = db.execute(sql_cpu, params).fetchall()
        mbs = db.execute(sql_mb, params).fetchall()
        hdds = db.execute(sql_hdd, params).fetchall()
        ssds = db.execute(sql_ssd, params).fetchall()
        ram = db.execute(sql_ram, params).fetchall()
        gpus = db.execute(sql_gpu, params).fetchall()
        cases = db.execute(sql_case, params).fetchall()
        coolers = db.execute(sql_cooler, params).fetchall()
        nwcards = db.execute(sql_nwcard, params).fetchall()
        psus = db.execute(sql_psu, params).fetchall()
        os = db.execute(sql_os, params).fetchall()
    return render_template("pages/new_configuration.jinja", cpus=cpus, mbs=mbs, hdds=hdds, ssds=ssds, ram=ram, gpus=gpus, cases=cases, coolers=coolers, nwcards=nwcards, psus=psus, os=os)

@app.post("/configuration/new/finish")
def finish_config():

    name = request.form.get("name", "unknown").strip()
    cost = request.form.get("cost", "unknown").strip()
    cpu = request.form.get("cpu", "unknown").strip()
    mb = request.form.get("mb", "unknown").strip()
    hdd = request.form.get("hdd", "unknown").strip()
    hddqty = request.form.get("hddqty", "unknown").strip()
    ssd = request.form.get("ssd", "unknown").strip()
    ssdqty = request.form.get("ssdqty", "unknown").strip()
    ram = request.form.get("ram", "unknown").strip()
    ramqty = request.form.get("ramqty", "unknown").strip()
    gpu = request.form.get("gpu", "unknown").strip()
    case = request.form.get("case", "unknown").strip()
    cooler = request.form.get("cooler", "unknown").strip()
    nwcard = request.form.get("nwcard", "unknown").strip()
    psu = request.form.get("psu", "unknown").strip()
    os = request.form.get("os", "unknown").strip()

    #Connect with DB
    with connect_db() as db:

        sql = """
            INSERT INTO configurations (name, cost, cpu, motherboard, hard_drive, hard_drive_qty, solid_drive, solid_drive_qty, ram, ram_qty, gpu, `case`, cooler, network_card, psu, os)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        params = (name, cost, cpu, mb, hdd, hddqty, ssd, ssdqty, ram, ramqty, gpu, case, cooler, nwcard, psu, os)

        db.execute(sql, params)

        return redirect("/configurations") 

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

