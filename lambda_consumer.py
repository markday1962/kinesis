import json
import logging
import boto3
import base64

stream_name = "mark-day-test-stream"
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event: dict, _context):
    if event and "Records" in event:
        for record in event["Records"]:
            try:
                body = record['kinesis']
                data_in_stream_time = body['approximateArrivalTimestamp']
                data = body['data']
                message_JSON = base64.b64decode(data)
                message_JSON = json.dumps(message_JSON)
                partition_key = {body['partition_key']}
                logger.info("Record consumed with partition key {} with an approximate time stamp of {}.".format(partition_key, partition_key))
                logger.info(message_JSON)
            except KeyError as err:
                logger.error(err)
                raise err




if __name__ == "__main__":
    e = ""

    lambda_handler(e)