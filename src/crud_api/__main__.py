import uvicorn
from argparse import ArgumentParser

parser = ArgumentParser("Crud API", description="A REST API CRUD application to manage the time you dedicate to your company's projects.")

parser.add_argument("--host", default="127.0.0.1")
parser.add_argument("-p", "--port", default=8000, type=int)

args = parser.parse_args()
uvicorn.run("crud:_api.main:app", reload=True, host="127.0.0.1", port=8000)