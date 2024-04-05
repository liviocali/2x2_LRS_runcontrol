import click
from lrsctrl.client import Client
from lrsctrl import server


@click.group()
def lrsctrl():
    pass

#Data run controls
@lrsctrl.command()
def start_data_run():
    Client().start_data_run()

@lrsctrl.command()
def stop_data_run():
    Client().stop_data_run()


#Calibration run controls
@lrsctrl.command()
def start_calib_run():
    Client().start_calib_run()

@lrsctrl.command()
def stop_calib_run():
    Client().stop_calib_run()
    

# DAQ software controls
@lrsctrl.command()
def start_adc64():
    Client().send_start_adc64()

@lrsctrl.command()
def stop_adc64():
    Client().send_stop_adc64()

@lrsctrl.command()
def start_rc():
    Client().send_start_rc()

@lrsctrl.command()
def stop_rc():
    Client().send_stop_rc()

@lrsctrl.command()
def serve():
    server.start_app()
