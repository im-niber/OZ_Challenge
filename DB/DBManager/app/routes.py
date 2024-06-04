from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
)
import yaml
from sqlalchemy import create_engine, inspect, MetaData
from sqlalchemy import inspect, Table, URL
from sqlalchemy.schema import CreateTable
from .dummy import generate_dummy_data

main = Blueprint("main", __name__)

engine = None
insp = None
conn = None
metadata_obj = MetaData()
schema = ""

# DB 선택
@main.route("/", methods=["GET"])
def home():
    db_list = {}

    with open('./config.yaml') as f:
        file = yaml.full_load(f)
        for database in file:
            db_list[database] = file[database]

    return render_template("index.html", db_list = db_list)

# DB 연결
def conn_db(db_url:str):
    global engine, insp, conn, metadata_obj
    url = db_url
  
    engine = create_engine(url)
    metadata_obj.reflect(engine)
    insp = inspect(engine)
    conn = engine.connect()


@main.route('/db', methods=["POST"])
def getdb():
    db_url = request.form['db']
    conn_db(db_url)

    schemas = get_schemas()

    return render_template("schema.html", schemas = schemas)

@main.route('/set_schema', methods=["GET"])
def set_schema():
    global schema

    if schema == request.args.get('schema'):

        tables = get_tables(schema=schema)
        views = get_views(schema=schema)
        return render_template("schemainfo.html", datas = {"tables":tables, "views":views})

    schema = request.args.get('schema')
    engine_url = engine.url

    new_url = URL.create(
        drivername=engine_url.drivername,
        username=engine_url.username,
        password=engine_url.password,
        host=engine_url.host,
        port=engine_url.port,
        database=schema,
        query=engine_url.query
    )
    conn_db(new_url)

    tables = get_tables(schema=schema)
    views = get_views(schema=schema)

    return render_template("schemainfo.html", datas = {"tables":tables, "views":views})

@main.route('/table_detail', methods=["GET"])
def get_detail_table():
    table_name = request.args.get('table')
    (columns, comments) = get_columns_and_comments(table_name)
    ddl = get_table_ddl(Table(table_name, metadata_obj))
    return render_template("table_detail.html", datas={"columns": columns,
                                                        "comments": comments,
                                                        "ddl": ddl})

@main.route('/set_dummy', methods=["POST"])
def set_dummy():
    table_name = request.args.get('table')
    count = int(request.form["count"])
    
    try:
        isTruncated = True if request.form["truncate"] == "on" else False
    except:
        isTruncated = False

    generate_dummy_data(conn, metadata_obj, table_name, count, isTruncated)
    conn.commit()
    url = request.args.get('back')
    return redirect(url)


def get_schemas() -> list[str]:
    return insp.get_schema_names()

def get_tables(schema: str) -> list[str]:
    return insp.get_table_names(schema)

def get_views(schema: str) -> list[str]:
    return insp.get_view_names(schema)

def get_columns_and_comments(name:str):
    columns = insp.get_columns(name)
    comments = insp.get_table_comment(name)

    return columns, comments

def get_table_ddl(name: Table):
    global engine
    return CreateTable(name).compile(engine)
