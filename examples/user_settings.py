import datetime, time, logging

PYBPOD_API_LOG_LEVEL = logging.WARNING #logging.WARNING; logging.DEBUG
PYBPOD_API_LOG_FILE  = 'pybpod-api.log'


WORKSPACE_PATH 	= 'BPOD-WORKSPACE'

PROTOCOL_NAME 	= datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

SERIAL_PORT 	= '/dev/ttyACM0'


PYBPOD_API_PUBLISH_DATA_FUNC = print




BPOD_BNC_PORTS_ENABLED 		= [True, True]
BPOD_WIRED_PORTS_ENABLED 	= [True, True]
BPOD_BEHAVIOR_PORTS_ENABLED = [False, False, False, False, False, False, False, False]