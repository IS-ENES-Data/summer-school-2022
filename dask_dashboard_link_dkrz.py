# set the correct status link for dashboard
import dask
from dask.distributed import Client

dask.config.config.get('distributed').get('dashboard').update({'link':'{JUPYTERHUB_SERVICE_PREFIX}/proxy/{port}/status'})