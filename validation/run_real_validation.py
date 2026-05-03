from serial_reader import SerialReader
from logger import Logger
from report_generator import ReportGenerator
import json

reader=SerialReader(115200,'COM3')
logger=Logger("logs")
report=ReportGenerator(logger)

for i in range (20):
    data_json=reader.read_line()
    if (data_json is None):    
        continue
    else:
        try: 
            data=json.loads(data_json)
            temp=data["temp"]
            humidity=data["humidity"]
            if ((-40<=temp<=80) and (0<=humidity<=100)):
                logger.log(data,"PASS")
            else:
                logger.log(data,"FAIL","OUT_OF_RANGE")
       
        except json.JSONDecodeError:
            logger.log({}, "FAIL", "CORRUPTED_DATA")
        
        
       

reader.close()
report.generate()











