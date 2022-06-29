#!/bin/bash
stream_arn="arn:aws:kinesis:eu-west-1:111177312954:stream/mark-day-test-stream"
aws kinesis register-stream-consumer --stream-arn $stream_arn --consumer kinesis-consumer-application