import json
import uuid
import boto3

stream_name = "mark-day-test-stream"
message = {"record_id": "18742"}


def producer():
    kinesis = boto3.client('kinesis')
    data = json.dumps(message)
    partition_key = str(uuid.uuid4())
    response = kinesis.put_record(
        StreamName=stream_name,
        Data=data,
        PartitionKey=partition_key
    )
    print(json.dumps(response))


if __name__ == "__main__":
    producer()