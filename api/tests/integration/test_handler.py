from api.src.handler import lambda_handler

test_check_event = {"resource": "/check", "path": "/v1/check", "httpMethod": "GET", "headers": {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br", "accept-language": "en-US,en;q=0.9", "Host": "api.lil.sh",
    "sec-fetch-dest": "document", "sec-fetch-mode": "navigate", "sec-fetch-site": "none", "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-5f2bd1c3-83b4047c1728c182c19eb4b2", "X-Forwarded-For": "125.237.45.15",
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
        "Root=1-5f2bd1c3-83b4047c1728c182c19eb4b2"],
    "X-Forwarded-For": [
        "125.237.45.15"],
    "X-Forwarded-Port": ["443"],
    "X-Forwarded-Proto": ["https"]},
                    "queryStringParameters": "null", "multiValueQueryStringParameters": "null",
                    "pathParameters": "null", "stageVariables": "null",
                    "requestContext": {"resourceId": "2e4d37", "resourcePath": "/check", "httpMethod": "GET",
                                       "extendedRequestId": "Q122iE8voAMFhdQ=",
                                       "requestTime": "06/Aug/2020:09:47:47 +0000", "path": "/v1/check",
                                       "accountId": "934679804324", "protocol": "HTTP/1.1", "stage": "prod",
                                       "domainPrefix": "api", "requestTimeEpoch": 1596707267366,
                                       "requestId": "83125087-8b84-458a-aa20-94bc02a4a883",
                                       "identity": {"cognitoIdentityPoolId": "null", "accountId": "null",
                                                    "cognitoIdentityId": "null", "caller": "null",
                                                    "sourceIp": "125.237.45.15", "principalOrgId": "null",
                                                    "accessKey": "null", "cognitoAuthenticationType": "null",
                                                    "cognitoAuthenticationProvider": "null", "userArn": "null",
                                                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
                                                    "user": "null"}, "domainName": "api.lil.sh", "apiId": "7d06ku4lwj"},
                    "body": "null", "isBase64Encoded": "false"}


def test_handler():
    res = lambda_handler(test_check_event, {})
    assert res["statusCode"] == 200
