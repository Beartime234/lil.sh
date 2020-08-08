import json
import os

from api.src.handler import lambda_handler
from api.tests import test_bucket, test_prefix
from api.tests.aws_mocks import aws_credentials, s3, surl_bucket

test_check_event = {"resource": "/check", "path": "/v1/check", "httpMethod": "GET", "headers": {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br", "accept-language": "en-US,en;q=0.9", "Host": "api.lil.sh",
    "sec-fetch-dest": "document", "sec-fetch-mode": "navigate", "sec-fetch-site": "none", "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    "X-Amzn-Trace-Id": "", "X-Forwarded-For": "",
    "X-Forwarded-Port": "443", "X-Forwarded-Proto": "https"}, "multiValueHeaders": {"accept": [
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"],
    "accept-encoding": [
        "gzip, deflate, br"],
    "accept-language": [
        "en-US,en;q=0.9"],
    "Host": ["api.lil.sh"],
    "sec-fetch-dest": ["document"],
    "sec-fetch-mode": ["navigate"],
    "sec-fetch-site": ["none"],
    "sec-fetch-user": ["?1"],
    "upgrade-insecure-requests": ["1"],
    "User-Agent": [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"],
    "X-Amzn-Trace-Id": [
        ""],
    "X-Forwarded-For": [
        ""],
    "X-Forwarded-Port": ["443"],
    "X-Forwarded-Proto": ["https"]},
                    "queryStringParameters": {"suffix": "test"}, "multiValueQueryStringParameters": "null",
                    "pathParameters": "null", "stageVariables": "null",
                    "requestContext": {"resourceId": "2e4d37", "resourcePath": "/check", "httpMethod": "GET",
                                       "extendedRequestId": "Q122iE8voAMFhdQ=",
                                       "requestTime": "06/Aug/2020:09:47:47 +0000", "path": "/v1/check",
                                       "accountId": "", "protocol": "HTTP/1.1", "stage": "prod",
                                       "domainPrefix": "api", "requestTimeEpoch": 1596707267366,
                                       "requestId": "83125087-8b84-458a-aa20-94bc02a4a883"},
                    "body": None, "isBase64Encoded": "false"}

test_create_w_suffix_event = {"resource": "/create", "path": "/v1/create", "httpMethod": "POST", "headers": {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br", "accept-language": "en-US,en;q=0.9", "Host": "api.lil.sh",
    "sec-fetch-dest": "document", "sec-fetch-mode": "navigate", "sec-fetch-site": "none", "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    "X-Amzn-Trace-Id": "", "X-Forwarded-For": "",
    "X-Forwarded-Port": "443", "X-Forwarded-Proto": "https"}, "multiValueHeaders": {"accept": [
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"],
    "accept-encoding": [
        "gzip, deflate, br"],
    "accept-language": [
        "en-US,en;q=0.9"],
    "Host": ["api.lil.sh"],
    "sec-fetch-dest": ["document"],
    "sec-fetch-mode": ["navigate"],
    "sec-fetch-site": ["none"],
    "sec-fetch-user": ["?1"],
    "upgrade-insecure-requests": ["1"],
    "User-Agent": [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"],
    "X-Amzn-Trace-Id": [
        ""],
    "X-Forwarded-For": [
        ""],
    "X-Forwarded-Port": ["443"],
    "X-Forwarded-Proto": ["https"]},
                              "queryStringParameters": None, "multiValueQueryStringParameters": "null",
                              "pathParameters": "null", "stageVariables": "null",
                              "requestContext": {"resourceId": "", "resourcePath": "/check", "httpMethod": "POST",
                                        "extendedRequestId": "Q122iE8voAMFhdQ=",
                                        "requestTime": "06/Aug/2020:09:47:47 +0000", "path": "/v1/create",
                                        "accountId": "", "protocol": "HTTP/1.1", "stage": "prod",
                                        "domainPrefix": "api", "requestTimeEpoch": 1596707267366,
                                        "requestId": ""},
                              "body": json.dumps({"suffix": "testsuffix", "redirectLocation": "https://google.com"}),
                              "isBase64Encoded": "false"}


test_create_w_out_suffix_event = {"resource": "/create", "path": "/v1/create", "httpMethod": "POST", "headers": {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br", "accept-language": "en-US,en;q=0.9", "Host": "api.lil.sh",
    "sec-fetch-dest": "document", "sec-fetch-mode": "navigate", "sec-fetch-site": "none", "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    "X-Amzn-Trace-Id": "", "X-Forwarded-For": "",
    "X-Forwarded-Port": "443", "X-Forwarded-Proto": "https"}, "multiValueHeaders": {"accept": [
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"],
    "accept-encoding": [
        "gzip, deflate, br"],
    "accept-language": [
        "en-US,en;q=0.9"],
    "Host": ["api.lil.sh"],
    "sec-fetch-dest": ["document"],
    "sec-fetch-mode": ["navigate"],
    "sec-fetch-site": ["none"],
    "sec-fetch-user": ["?1"],
    "upgrade-insecure-requests": ["1"],
    "User-Agent": [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"],
    "X-Amzn-Trace-Id": [
        ""],
    "X-Forwarded-For": [
        ""],
    "X-Forwarded-Port": ["443"],
    "X-Forwarded-Proto": ["https"]},
                              "queryStringParameters": None, "multiValueQueryStringParameters": "null",
                              "pathParameters": "null", "stageVariables": "null",
                              "requestContext": {"resourceId": "", "resourcePath": "/check", "httpMethod": "POST",
                                        "extendedRequestId": "Q122iE8voAMFhdQ=",
                                        "requestTime": "06/Aug/2020:09:47:47 +0000", "path": "/v1/create",
                                        "accountId": "", "protocol": "HTTP/1.1", "stage": "prod",
                                        "domainPrefix": "api", "requestTimeEpoch": 1596707267366,
                                        "requestId": ""},
                              "body": json.dumps({"redirectLocation": "https://google.com"}),
                              "isBase64Encoded": "false"}

def test_check_handler(aws_credentials, s3, surl_bucket):
    res = lambda_handler(test_check_event, {})
    assert res["statusCode"] == 200
    assert json.loads(res["body"])["exists"] is False
    s3.put_object(
        Body=b'',  # empty object
        Bucket=test_bucket,
        Key=f"{test_prefix}test",
        WebsiteRedirectLocation="https://google.com",
    )
    res = lambda_handler(test_check_event, {})
    assert res["statusCode"] == 200
    assert json.loads(res["body"])["exists"] is True


def test_create_w_suffix_handler(aws_credentials, s3, surl_bucket):
    res = lambda_handler(test_create_w_suffix_event, {})
    assert res["statusCode"] == 200
    s3.head_object(
        Bucket=test_bucket,
        Key=f"{test_prefix}testsuffix",
    )


def test_create_w_out_suffix_handler(aws_credentials, s3, surl_bucket):
    res = lambda_handler(test_create_w_out_suffix_event, {})
    assert res["statusCode"] == 200
