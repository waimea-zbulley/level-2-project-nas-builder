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
                cpus.url            AS cpu_url,
                motherboards.name   AS motherboard_name,
                motherboards.url   AS motherboard_url,
                harddrives.name     AS harddrive_name,
                harddrives.url     AS harddrive_url,
                soliddrives.name    AS soliddrive_name,
                soliddrives.url    AS soliddrive_url,
                ram.name            AS ram_name,
                ram.url            AS ram_url,
                gpus.name           AS gpu_name,
                gpus.url           AS gpu_url,
                cases.name          AS case_name,
                cases.url          AS case_url,
                coolers.name        AS cooler_name,
                coolers.url        AS cooler_url,
                networkcard.name    AS networkcard_name,
                networkcard.url    AS networkcard_url,
                powersupply.name    AS psu_name,
                powersupply.url    AS psu_url,
                os.name             AS os_name,
                os.url             AS os_url

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

def get_config_2():
    # Get cpu from component selection
    cpu = None
    cpu_id = session.get("cpu", None)

    with connect_db() as db:
        sql = """
            SELECT id, name, cost
            FROM cpus
            WHERE id=?
        """

        params = (cpu_id, )
        cpu = db.execute(sql, params).fetchone()


    # Get ram from component selection
    ram = None
    ram_id = session.get("ram", None)

    with connect_db() as db:
        sql = """
            SELECT id, name, cost
            FROM ram
            WHERE id=?
        """

        params = (ram_id, )
        ram = db.execute(sql, params).fetchone()

    # Get Hard Drive from component selection
    hdd = None
    hdd_id = session.get("hdd", None)


    with connect_db() as db:
        sql = """
            SELECT id, name, cost
            FROM harddrives
            WHERE id=?
        """

        params = (hdd_id, )
        hdd = db.execute(sql, params).fetchone()

    # Get Hard Drive from component selection
    ssd = None
    ssd_id = session.get("ssd", None)

    with connect_db() as db:
        sql = """
            SELECT id, name, cost
            FROM soliddrives
            WHERE id=?
        """

        params = (ssd_id, )
        ssd = db.execute(sql, params).fetchone()

    # Get GPU from config form
    gpu = None
    gpu_id = session.get("ssd", None)

    with connect_db() as db:
        sql = """
            SELECT id, name, cost
            FROM gpus
            WHERE id=?
        """

        params = (gpu_id, )
        gpu = db.execute(sql, params).fetchone()

    # Get Cooler from config form
    cooler = None
    cooler_id = session.get("cooler", None)

    with connect_db() as db:
        sql = """
            SELECT id, name, cost
            FROM coolers
            WHERE id=?
        """

        params = (cooler_id, )
        cooler = db.execute(sql, params).fetchone()

    # Get Network Card from config form
    nwcard = None
    nwcard_id = session.get("cooler", None)

    with connect_db() as db:
        sql = """
            SELECT id, name, cost
            FROM networkcard
            WHERE id=?
        """

        params = (nwcard_id, )
        nwcard = db.execute(sql, params).fetchone()

    # Get Case from config form
    case = None
    case_id = session.get("cooler", None)

    with connect_db() as db:
        sql = """
            SELECT id, name, cost
            FROM cases
            WHERE id=?
        """

        params = (cooler_id, )
        case = db.execute(sql, params).fetchone()

    return cpu, ram, hdd, ssd, gpu, cooler, nwcard, case


def get_mb():
    mb = None
    mb_id = session.get("mb", None)

    with connect_db() as db:
        sql = """
            SELECT id, name, cost, platform, ram_gen, ram_slots, sata_ports, m2_ports
            FROM motherboards
            WHERE id=?
        """
        params = (mb_id, )
        mb = db.execute(sql, params).fetchone()

    return mb

def get_mbs():

    with connect_db() as db:
        sql = """
            SELECT id, name, cost, platform, ram_gen, ram_slots, sata_ports
            FROM motherboards
        """
        mb = db.execute(sql,).fetchall()

    return mb

def get_cpus(mb):
    mb = mb 

    with connect_db() as db:
        platform = mb.get("platform")

        sql = """
            SELECT id, name, cost, platform, powerdraw
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
            SELECT id, name, cost, capacity
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
            SELECT id, cost, name, powerdraw
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
    gpu_id = session.get("gpu", None)

    with connect_db() as db:

        if gpu_id is not None:

            sql = """
                SELECT id, cost, name
                FROM powersupply
                WHERE power >= 800
            """

        else:
            
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

    mb = get_mbs()

    return render_template(
        "pages/select_motherboard.jinja",
        mbs = mb
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
        return redirect("/configuration/new/mb")

    mb = get_mb()
    cpus = get_cpus(mb)
    ram = get_ram(mb)
    hdds = get_hdds()
    ssds = get_ssds()
    gpus = get_gpus()
    coolers = get_coolers()
    nwcards = get_nwcards()
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
        cases = cases

    )

@app.post("/configuration/new/components")
def config_pick_stage2():


    session["components_selected"] = 1
    session["cpu"] = int(request.form.get("cpu"))
    session["ram"] = int(request.form.get("ram"))
    session["ssd"] = int(request.form.get("ssd"))
    session["cooler"] = int(request.form.get("cooler"))
    session["nwcard"] = int(request.form.get("nwcard"))
    session["case"] = int(request.form.get("case"))

    # Optional things in the form
    gpu = request.form.get("gpu")
    if gpu:
        session["gpu"] = int(request.form.get("gpu"))
    else:
        session["gpu"] = None

    hdd = request.form.get("hdd")
    if hdd:
        session["hdd"] = int(request.form.get("hdd"))
    else:
        session["hdd"] = None

    nwcard = request.form.get("nwcard")
    if nwcard:
        session["nwcard"] = int(request.form.get("nwcard"))
    else:
        session["nwcard"] = None
    
    return redirect("/configuration/new/final")

@app.get("/configuration/new/final")
def config_pick_stage3():
    mb = get_mb()
    cpu, ram, hdd, ssd, gpu, cooler, nwcard, case = get_config_2()
    psus = get_psus()
    oses = get_oses()

    return render_template(
        "pages/final_config.jinja",
        mb = mb,
        cpu = cpu,
        ram = ram,
        hdd = hdd,
        ssd = ssd,
        gpu = gpu,
        cooler = cooler,
        nwcard = nwcard,
        case = case,
        psus = psus,
        oses = oses
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

