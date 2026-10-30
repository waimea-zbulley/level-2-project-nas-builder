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
# Renders the home page for root (/) dir of the website
def main_page():
    return render_template("pages/homepage.jinja")

@app.get("/configurations")
# Function for the configurations route
def configurations():

    # Pulls all the required information from configurations for displaying a users config on this page
    with connect_db() as db:
        sql = """
            SELECT
                configurations.name,
                configurations.id,
                configurations.cost,
                configurations.icon  
            FROM configurations

        """
        params = ()
        configs = db.execute(sql, params).fetchall()

        return render_template("pages/configurations.jinja", configs=configs)

@app.get("/configuration/<int:id>")
# Function for rendering the page for viewing the comonents/details of a specific configuration.
def show_config(id):

    # Pulls all the required information for displaying a users configuration, linking with all 12 tables
    with connect_db() as db:
        sql = """
            SELECT 
                configurations.id   AS con_id,
                configurations.name AS con_name,
                configurations.cost AS con_cost,
                configurations.hard_drive_qty as hddqty,
                configurations.hard_drive as hdd,
                configurations.solid_drive_qty as ssdqty,
                configurations.solid_drive as ssd,
                configurations.ram_qty as ramqty,
                configurations.gpu as gpu,
                configurations.network_card as nwcard,
                cpus.name           AS cpu_name,
                cpus.url            AS cpu_url,
                motherboards.name   AS motherboard_name,
                motherboards.url   AS motherboard_url,
                harddrives.name     AS harddrive_name,
                harddrives.capacity     AS harddrive_capacity,
                harddrives.url     AS harddrive_url,
                soliddrives.name    AS soliddrive_name,
                soliddrives.url    AS soliddrive_url,
                soliddrives.capacity    AS soliddrive_capacity,
                ram.name            AS ram_name,
                ram.capacity            AS ram_capacity,
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
            LEFT JOIN soliddrives ON configurations.solid_drive = soliddrives.id
            JOIN ram ON configurations.ram = ram.id
            LEFT JOIN gpus ON configurations.gpu = gpus.id
            JOIN cases ON configurations.`case` = cases.id
            JOIN coolers ON configurations.cooler = coolers.id
            LEFT JOIN networkcard ON configurations.network_card = networkcard.id
            JOIN powersupply ON configurations.psu = powersupply.id
            JOIN os ON configurations.os = os.id WHERE configurations.id = ?

        """
        params = (id,)
        configs = db.execute(sql, params).fetchone()


        return render_template("pages/configuration.jinja", config=configs)

@app.get("/components")
# Function for rendering the page showing all components in the database
def compnents():
    with connect_db() as db:

        # SQL for pulling all components in the database
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

        # Seting variable names for all components to be used in the jinja template
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

        return render_template("pages/components.jinja", cpus=cpus, mbs=mbs, hdds=hdds, ssds=ssds, ram=ram, gpus=gpus, cases=cases, coolers=coolers, nwcards=nwcards, psus=psus, os=os)

@app.get("/configuration/<int:id>/delete")
# Function for deleting configuration
def delete_config(id):

    # Deleting a configuration
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
    """Retives all components from session relevant to the users build, this is used to pass through the data for the final part of the configuration"""
    
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
    gpu_id = session.get("gpu", None)

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
    nwcard_id = session.get("nwcard", None)

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
    case_id = session.get("case", None)

    with connect_db() as db:
        sql = """
            SELECT id, name, cost
            FROM cases
            WHERE id=?
        """

        params = (case_id, )
        case = db.execute(sql, params).fetchone()

    ram_qty = session["ram_qty"]
    ssd_qty = session["ssd_qty"]
    hdd_qty = session["hdd_qty"]

    return cpu, ram, hdd, ssd, gpu, cooler, nwcard, case, ram_qty, ssd_qty, hdd_qty

def get_mb():
    """Gets the motherboard from the users session to pass through to next stage of form"""
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
    """Gets all motherboards to display to the user as options for selection"""
    with connect_db() as db:
        sql = """
            SELECT id, name, cost, platform, ram_gen, ram_slots, sata_ports
            FROM motherboards
        """
        mb = db.execute(sql,).fetchall()

    return mb

def get_cpus(mb):
    """Pulls CPUs comptabible with the user's chosen motherboard"""
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
    """Pulls RAM comptabible with the user's chosen motherboard"""
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
    """Pulls all HDDs from the database"""
    with connect_db() as db:
        sql = """
            SELECT id, name, cost, capacity
            FROM harddrives
        """
        hdds = db.execute(sql, ).fetchall()

    return hdds

def get_ssds():
    """Pulls all SSDs from the database"""
    with connect_db() as db:
        sql = """
            SELECT id, cost, name
            FROM soliddrives
        """
        sdds = db.execute(sql, ).fetchall()

    return sdds

def get_gpus():
    """Pulls all GPU from the database"""

    with connect_db() as db:
        sql = """
            SELECT id, cost, name, powerdraw
            FROM gpus
        """
        gpus = db.execute(sql, ).fetchall()

    return gpus

def get_coolers():
    """Pulls all CPU Coolers from the database"""

    with connect_db() as db:
        sql = """
            SELECT id, cost, name
            FROM coolers
        """
        coolers = db.execute(sql, ).fetchall()

    return coolers

def get_nwcards():
    """Pulls all network cards from the database"""
    with connect_db() as db:
        sql = """
            SELECT id, cost, name
            FROM networkcard
        """
        nwcards = db.execute(sql, ).fetchall()

    return nwcards

def get_psus():
    """Gets PSUs compatable with the users component choices"""
    gpu_id = session.get("gpu", None)

    with connect_db() as db:
        # Checks weather the user has a gpu (requiring a higher wattage PSU if they do)
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
    """Pulls all Operating Systems from the database"""
    with connect_db() as db:
        sql = """
            SELECT id, cost, name
            FROM os
        """
        oses = db.execute(sql, ).fetchall()

    return oses

def get_cases():
    """Pulls all cases from the database"""
    with connect_db() as db:
        sql = """
            SELECT id, cost, name
            FROM cases
        """
        cases = db.execute(sql, ).fetchall()

    return cases


#===========================================================
#           Edit Specific Help Funcs
#===========================================================

def get_mb_edit(id):
    """Retrives the motherboard and it's relivant data for the select configuration to edit"""
    mb = None
    config_id = id

    with connect_db() as db:
        sql = """
            SELECT motherboard
            FROM configurations
            WHERE id=?
        """
        params = (config_id, )
        mb_id = db.execute(sql, params).fetchone()["motherboard"]

        sql = """
            SELECT id, name, cost, platform, ram_gen, ram_slots, sata_ports, m2_ports
            FROM motherboards
            WHERE id=?
        """

        params = (mb_id, )
        mb = db.execute(sql, params).fetchone()

        return mb

def get_name_edit(id):
    """Retrives name for the select configuration to allow editing"""
    name = None

    config_id = id
    with connect_db() as db:
        sql = """
            SELECT name
            FROM configurations
            WHERE id=?
        """
        params = (config_id, )
        name = db.execute(sql, params).fetchone()["name"]

        return name

def get_config_edit(id):
    """Retrives components from select configuration to allow editing"""
    config_id = id

    with connect_db() as db:
        sql = """
            SELECT *
            FROM configurations
            WHERE id = ?
        """
        params = (config_id,)
        config_edit = db.execute(sql, params).fetchone()

    return config_edit

@app.get("/configuration/new/mb")
# function for showing new configuration page (inital page of the form)
def show_newconf():
    if not session.get("mb"):
        session["mb"] = None

    mbs = get_mbs()

    return render_template(
        "pages/select_motherboard.jinja",
        mbs = mbs
    )

@app.post("/configuration/new/mb")
# Posts the inital form answers to the session to be passed to next form page/to be used to determine what components are valid for the user to pick (based off motherboard)
def config_pick_mb():
    mb_id = request.form.get("mb")
    session["mb"] = int(mb_id)
    session["name"] = request.form.get("name")
    session["icon"] = request.form.get("icon")
    
    return redirect("/configuration/new/components")

@app.get("/configuration/new/components")
# Function to show component selection/second stage of form
def show_newconf_stage2():
    mb = get_mb()

    # Ensures that user cant accidently go to the part of the form without selecting a motherboard
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
    name = session["name"]
    icon = session["icon"]
    


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
        name = name,
        cases = cases

    )

@app.post("/configuration/new/components")
# Function for posting second stage/component selections to the final stage of the form
def config_pick_stage2():


    session["cost"] = request.form.get("cost", "unknown").strip()
    session["cpu"] = int(request.form.get("cpu"))
    session["ram"] = int(request.form.get("ram"))
    session["cooler"] = int(request.form.get("cooler"))
    session["case"] = int(request.form.get("case"))

    session["hdd_qty"] = int(request.form.get("hddqty"))
    session["ssd_qty"] = int(request.form.get("ssdqty"))
    session["ram_qty"] = int(request.form.get("ramqty"))
    
    # Optional things in the form to prevent them getting messed up in some situations
    gpu = request.form.get("gpu")
    if gpu:
        session["gpu"] = int(request.form.get("gpu"))
    if gpu == "":
        session["gpu"] = None

    hdd = request.form.get("hdd")
    if hdd:
        session["hdd"] = int(request.form.get("hdd"))
    if hdd == "":
        session["hdd"] = None

    ssd = request.form.get("ssd")
    if ssd:
        session["ssd"] = int(request.form.get("ssd"))
    if ssd == "":
        session["ssd"] = None

    nwcard = request.form.get("nwcard")
    if nwcard:
        session["nwcard"] = int(request.form.get("nwcard"))
    if nwcard == "":
        session["nwcard"] = None
    
    return redirect("/configuration/new/final")

@app.get("/configuration/new/final")
# Final stage of form for PSU & OS selection
def config_pick_stage3():
    mb = get_mb()
    cpu, ram, hdd, ssd, gpu, cooler, nwcard, case, ram_qty, ssd_qty, hdd_qty = get_config_2()
    psus = get_psus()
    oses = get_oses()
    ssds = get_ssds()
    name = session["name"]
    icon = session["icon"]
    
    

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
        ram_qty = ram_qty,
        ssd_qty = ssd_qty,
        hdd_qty = hdd_qty,
        psus = psus,
        oses = oses,
        ssds = ssds,
        name = name,
        icon = icon
    )


@app.post("/configuration/new/final")
# Posts final form selections & all previous selections
def finish_config():

    name = session["name"]
    cpu = session["cpu"]
    mb = session["mb"]
    hdd = session["hdd"]
    hddqty = session["hdd_qty"]
    ssd = session["ssd"]
    ssdqty = session["ssd_qty"]
    ram = session["ram"]
    ramqty = session["ram_qty"]
    gpu = session["gpu"]
    case = session["case"]
    cooler = session["cooler"]
    nwcard = session["nwcard"]
    psu = request.form.get("psu")
    os = request.form.get("os")
    cost = request.form.get("cost", "unknown").strip()
    icon = session["icon"]

    

    # Adds the users configuration to the database
    with connect_db() as db:

        sql = """
            INSERT INTO configurations (name, cost, cpu, motherboard, hard_drive, hard_drive_qty, solid_drive, solid_drive_qty, ram, ram_qty, gpu, `case`, cooler, network_card, psu, os, icon)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        params = (name, cost, cpu, mb, hdd, hddqty, ssd, ssdqty, ram, ramqty, gpu, case, cooler, nwcard, psu, os, icon)

        db.execute(sql, params)

        flash(f"Successfully added configuration {name}", "success")
        return redirect("/configurations") 


#===================================================
#   Edit Routes
#===================================================
@app.get("/configuration/<int:id>/edit")
# Component, name & icon edit page
def edit_config(id):
    
        params = (id,)
        config = get_config_edit(id,)
        mb = get_mb_edit(id,)
        cpus = get_cpus(mb)
        ram = get_ram(mb)
        hdds = get_hdds()
        ssds = get_ssds()
        gpus = get_gpus()
        coolers = get_coolers()
        nwcards = get_nwcards()
        cases = get_cases()
        name = get_name_edit(id,)

        return render_template(
            "/pages/edit_components.jinja",
            config = config,
            mb = mb,
            ssds = ssds,
            cpus = cpus,
            ram = ram,
            hdds = hdds,
            gpus = gpus,
            coolers = coolers,
            nwcards = nwcards,
            name = name,
            cases = cases
            )

@app.post("/configuration/<int:id>/edit")
# Posts the first stage of the edit form to the final edit form
def edit_config_post(id):

    # Setting users choices into session
    session["cost"] = request.form.get("cost", "unknown").strip()
    session["cpu"] = int(request.form.get("cpu"))
    session["ram"] = int(request.form.get("ram"))
    session["cooler"] = int(request.form.get("cooler"))
    session["case"] = int(request.form.get("case"))

    session["hdd_qty"] = int(request.form.get("hddqty"))
    session["ssd_qty"] = int(request.form.get("ssdqty"))
    session["ram_qty"] = int(request.form.get("ramqty"))
    
    # Optional things in the form
    gpu = request.form.get("gpu")
    if gpu:
        session["gpu"] = int(request.form.get("gpu"))
    if gpu == "":
        session["gpu"] = None

    hdd = request.form.get("hdd")
    if hdd:
        session["hdd"] = int(request.form.get("hdd"))
    if hdd == "":
        session["hdd"] = None

    ssd = request.form.get("ssd")
    if ssd:
        session["ssd"] = int(request.form.get("ssd"))
    if ssd == "":
        session["ssd"] = None

    nwcard = request.form.get("nwcard")
    if nwcard:
        session["nwcard"] = int(request.form.get("nwcard"))
    if nwcard == "":
        session["nwcard"] = None

    session["name"] = request.form.get("name")
    session["icon"] = request.form.get("icon")
    
    return redirect(f"/configuration/{id}/final/edit")

@app.get("/configuration/<int:id>/final/edit")
# Final edit page (Power Supply & Operating System)
def edit_final(id):
    mb = get_mb_edit(id,)
    cpu, ram, hdd, ssd, gpu, cooler, nwcard, case, ram_qty, ssd_qty, hdd_qty = get_config_2()
    psus = get_psus()
    oses = get_oses()
    ssds = get_ssds()
    name = session["name"]
    icon = session["icon"]

    config = get_config_edit(id,)

    return render_template(
        "pages/final_config_edit.jinja",
        config = config,
        mb = mb,
        cpu = cpu,
        ram = ram,
        hdd = hdd,
        ssd = ssd,
        gpu = gpu,
        cooler = cooler,
        nwcard = nwcard,
        case = case,
        ram_qty = ram_qty,
        ssd_qty = ssd_qty,
        hdd_qty = hdd_qty,
        psus = psus,
        oses = oses,
        ssds = ssds,
        icon=icon,
        name = name
    )

@app.post("/configuration/<int:id>/final/edit")
# Posts final edit page
def edit_final_edit(id):
    cpu = session["cpu"]
    mb = get_mb_edit(id,)
    hdd = session["hdd"]
    hddqty = session["hdd_qty"]
    ssd = session["ssd"]
    ssdqty = session["ssd_qty"]
    ram = session["ram"]
    ramqty = session["ram_qty"]
    gpu = session["gpu"]
    case = session["case"]
    cooler = session["cooler"]
    nwcard = session["nwcard"]
    psu = request.form.get("psu")
    os = request.form.get("os")
    cost = request.form.get("cost", "unknown").strip()
    name = session["name"]
    icon = session["icon"]

    config_id = id

    # Updates the selected configuration based off the users changes
    with connect_db() as db:

        sql = """
            UPDATE configurations
            SET name=?, cost=?, cpu=?, motherboard=?, hard_drive=?, hard_drive_qty=?, solid_drive=?, solid_drive_qty=?, ram=?, ram_qty=?, gpu=?, `case`=?, cooler=?, network_card=?, psu=?, os=?, icon=?
            WHERE id = ?
        """

        params = (name, cost, cpu, mb["id"], hdd, hddqty, ssd, ssdqty, ram, ramqty, gpu, case, cooler, nwcard, psu, os, icon, config_id )

        db.execute(sql, params)

        flash(f"Successfully updated {name}", "success")
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

