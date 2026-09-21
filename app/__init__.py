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
                networkcard.name    AS networkcard_name,
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

@app.get("/components")
def compnents():
    with connect_db() as db:

        sql_cpu = """
            SELECT *
            FROM cpus
        """
        sql_mb = """
            SELECT *
            FROM motherboards
        """
        sql_hdd = """
            SELECT *
            FROM harddrives
        """
        sql_ssd = """
            SELECT *
            FROM soliddrives
        """
        sql_ram = """
            SELECT *
            FROM ram
        """
        sql_gpu = """
            SELECT *
            FROM gpus
        """
        sql_case = """
            SELECT *
            FROM cases
        """
        sql_cooler = """
            SELECT *
            FROM coolers
        """
        sql_nwcard = """
            SELECT *
            FROM networkcard
        """
        sql_psu = """
            SELECT *
            FROM powersupply
        """
        sql_os = """
            SELECT *
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

        # db.execute(sql, params)

        return render_template("pages/components.jinja", cpus=cpus, mbs=mbs, hdds=hdds, ssds=ssds, ram=ram, gpus=gpus, cases=cases, coolers=coolers, nwcards=nwcards, psus=psus, os=os)

@app.get("/configuration/<int:id>/delete")
def delete_config(id):

    # Delting a configuration
    with connect_db() as db:
        sql = """
            DELETE FROM configurations
            WHERE id=?
        """

        params = (id,)
        flash("Successfully deleted configuration", "success")
        db.execute(sql, params)
        return redirect("/configurations")


#===================================================
# Helper funcs
#===================================================

def get_mb():
    mb = None
    mb_id = session.get("mb", None)

    with connect_db() as db:
        sql = """
            select id, name, cost, platform, ram_gen, ram_slots, sata_ports, m2_ports
            from motherboards
            WHERE id=?
        """
        params = (mb_id, )
        mb = db.execute(sql, params).fetchone()

    return mb

def get_mb2():

    with connect_db() as db:
        sql = """
            select id, name, cost, platform, ram_gen, ram_slots, sata_ports
            from motherboards
        """
        mb = db.execute(sql,).fetchall()

    return mb

def get_cpus(mb):
    mb = mb 

    with connect_db() as db:
        platform = mb.get("platform")

        sql = """
            SELECT id, name, cost, platform
            FROM cpus
            WHERE platform=?
        """
        params = (platform, )
        cpus = db.execute(sql, params).fetchall()

    return cpus

def get_ram(mb):
    mb = mb

    with connect_db() as db:
        ram_gen = mb.get("ram_gen")

        sql = """
            SELECT id, name, cost, generation
            FROM ram
            WHERE generation=?
        """
        params = (ram_gen, )
        ram = db.execute(sql, params).fetchall()

    return ram

def get_hdds():
    with connect_db() as db:
        sql = """
            SELECT id, name, cost
            FROM harddrives
        """
        hdds = db.execute(sql, ).fetchall()

    return hdds

def get_ssds():
    with connect_db() as db:
        sql = """
            SELECT id, cost, name
            FROM soliddrives
        """
        sdds = db.execute(sql, ).fetchall()

    return sdds

def get_gpus():
    with connect_db() as db:
        sql = """
            SELECT id, cost, name
            FROM gpus
        """
        gpus = db.execute(sql, ).fetchall()

    return gpus

def get_coolers():
    with connect_db() as db:
        sql = """
            SELECT id, cost, name
            FROM coolers
        """
        coolers = db.execute(sql, ).fetchall()

    return coolers

def get_coolers():
    with connect_db() as db:
        sql = """
            SELECT id, cost, name
            FROM coolers
        """
        coolers = db.execute(sql, ).fetchall()

    return coolers

def get_nwcards():
    with connect_db() as db:
        sql = """
            SELECT id, cost, name
            FROM networkcard
        """
        nwcards = db.execute(sql, ).fetchall()

    return nwcards

def get_psus():
    with connect_db() as db:
        sql = """
            SELECT id, cost, name
            FROM powersupply
        """
        psus = db.execute(sql, ).fetchall()

    return psus
    
def get_oses():
    with connect_db() as db:
        sql = """
            SELECT id, cost, name
            FROM os
        """
        oses = db.execute(sql, ).fetchall()

    return oses

def get_cases():
    with connect_db() as db:
        sql = """
            SELECT id, cost, name
            FROM cases
        """
        cases = db.execute(sql, ).fetchall()

    return cases

@app.get("/configuration/new/mb")
def show_newconf():
    if not session.get("mb"):
        session["mb"] = None

    mb = get_mb2()

    return render_template(
        "pages/select_motherboard.jinja",
        mbs = mb,
    )

@app.post("/configuration/new/mb")
def config_pick_mb():
    mb_id = request.form.get("mb")
    session["mb"] = int(mb_id)
    
    return redirect("/configuration/new/components")

@app.get("/configuration/new/components")
def show_newconf_stage2():

    mb = get_mb()

    if not mb:
        flash("Please choose a suitable MB first!", "error")
        return redirect("/config/mb")

    mb = get_mb()
    cpus = get_cpus(mb)
    ram = get_ram(mb)
    hdds = get_hdds()
    ssds = get_ssds()
    gpus = get_gpus()
    coolers = get_coolers()
    nwcards = get_nwcards()
    psus = get_psus()
    oses = get_oses()
    cases = get_cases()
    


    return render_template(
        "pages/new_configuration.jinja",
        mb = mb,
        cpus = cpus,
        ram = ram,
        hdds = hdds,
        ssds = ssds,
        gpus = gpus,
        coolers = coolers,
        nwcards = nwcards,
        psus = psus,
        cases = cases

    )

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

