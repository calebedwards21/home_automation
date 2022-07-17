import datetime
import influxdb

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS # There is an option for asynchronous if needed


class Influx_Client_V1:
    def __init__(
        self,
        host='localhost', 
        port=8086,
        user = 'admin',
        password = 'admin',
        dbname = 'db0'
    ):
        self.client = influxdb.InfluxDBClient(host=host, port=port, username=user, password=password, database=dbname)

    def write_v1(self, measurement, tags, fields):
        data = [
            {
                'measurement' : measurement,
                'tags' : tags,
                'fields' : fields,
                'time' : datetime.datetime.now()
            }
        ]

        self.client.write_points(data)
    
    
class Influx_Client_V2:
    def __init__(self, url='http://localhost:8086', token='my-token', org='my-org', bucket='my-bucket'):
        self.client = InfluxDBClient(url=url, token=token, org=org)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)
        self.query_api = self.client.query_api()
        self.org = org
        self.bucket = bucket
    
    
    def write(self, measurement, tags, fields, bucket=None):
        '''
            https://influxdb-client.readthedocs.io/en/v1.2.0/api.html#writeapi
        '''
        if bucket is None:
            bucket = self.bucket
        
        p = Point(measurement)
        for key, value in tags.items():
            p = p.tag(key, value)
        for key, value in fields.items():
            p = p.field(key, value)
        
        self.write_api.write(bucket=bucket, org=self.org, record=p)
        
        
    def query(self, query):
        tables = self.query_api.query(query)

        for table in tables:
            print(table)
            for row in table.records:
                print (row.values)
       
        
    def dispose(self):
        self.client.close()
    