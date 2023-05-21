Data platform API v1
The Data platform API allows developers to work with Data platform.
Test Api
The Data platform Test API allows developers to work with the test tool within Data platform, 

/testapi/createtest

A person calls this endpoint to do a adhoc test and the test results will sent to the email id.

EXAMPLE
curl -X POST https://api.dataplatform.com/testapi/createtest \
    -H 'content-type: application/json'
    -d '{“access_token”: “”,
		“source”: "snowflake",
		“table” : “db.schema.table”,
		“type”	: “adhoc”,
		“email” : “user@sendreports.com”
			 }'
Sample response
{
  "status": 200,
  “body” : {	“runid” : “123a”,
			“ScheduleddAt” : <timestamp>,
		}
}

/testapi/scheduletest

A person calls this endpoint to schedule a table for testing and the test results will be populated in the test dashboard.

EXAMPLE
curl -X POST https://api.dataplatform.com/testapi/scheduletest \
    -H 'content-type: application/json'
    -d '{“access_token”: “”,
		“source”: "snowflake",
		“table” : “db.schema.table”,
		“test-types” : [list of tests to be done]
		“type”	: “schedule”,
		“cron” : “0 15 10 ? * *”
		}'
Sample response
{
  "status": 200,
  “body” : {	“jobid” : “123a”,
			“ScheduleddAt” : <timestamp>,
	}
}
/testapi/removeschedule

A person calls this endpoint to remove a particular table from scheduled testing table.

EXAMPLE
curl -X POST https://api.dataplatform.com/testapi/createtest \
    -H 'content-type: application/json'
    -d '{“access_token”: “”,
		“source”: "snowflake",
		“table” : “db.schema.table”,
		“type”	: “schedule”,
		“jobid” : “123a”
			 }'
Sample response
{
  "status": 200,
  “body” : {	“message” : “the < jobid > for the table <table> has been removed from scheduled run list”
		}
}
/testapi/modifytest

A person calls this endpoint to modify a scheduled test.

EXAMPLE
curl -X POST https://api.dataplatform.com/testapi/scheduletest \
    -H 'content-type: application/json'
    -d '{“access_token”: “”,
		“jobid” : “123a”,
		“source”: "snowflake",
		“table” : “db.schema.table”,
		“test-types” : [list of tests to be done]
		“type”	: “schedule”,
		“cron” : “0 15 10 ? * *”
		}'
Sample response
{
  "status": 200,
  “body” : {	“jobid” : “123a”,
			“ScheduleddAt” : <timestamp>,
	}
}
Errors
Errors are returned using standard HTTP error code syntax. Depending on the status code, the response body may be in JSON or plaintext.

Response Attribute

Attribute	Data Type	Description
s	string	“error”
code	int	Negative integer to identify the specific error
message	string	Error message to identify error
HTTP Header	int	Refer to the error codes table

Errors by status code
The status codes contain the following
Status Code	Meaning
200	Request was successful
400	Bad request. The request is invalid or certain other errors
401	Authorization error. User could not be authenticated
403	Permission error. User does not have the necessary permissions
500	Internal server error.
Authorization
Data platform supports OAuth 2.0 for authorizing API requests. Authorized requests to the API should use an Authorization header with the value Bearer <TOKEN>, where <TOKEN> is an access token obtained through the OAuth flow.













/oauth2/authorize
METHOD
GET
EXAMPLE
Example: Auth URL for code flow
https://www.api.dataplatform.com/oauth2/authorize?client_id=<APP_KEY>&response_type=code
Sample response
[REDIRECT_URI]#token_type=bearer&account_id=dbid%& access_token=ABCDEFG&
access_token String A token which can be used to make calls to the dataplatform API.
token_type String The type of token, which will always be bearer.
account_id String A user's account identifier used by API v1.
 
/oauth2/token
An app calls this endpoint to acquire a bearer token once the user has authorized the app.

Calls to /oauth2/token need to be authenticated using the apps's key and secret. These can either be passed as application/x-www-form-urlencoded POST parameters (see parameters below) or via HTTP basic authentication. If basic authentication is used, the app key should be provided as the username, and the app secret should be provided as the password.

URL STRUCTURE
https://api.dataplatform.com/oauth2/token
METHOD
POST
EXAMPLE
Example: code flow access token request
curl https://api.Data platform.com/oauth2/token \
    -d code=<AUTHORIZATION_CODE> \
    -d grant_type=authorization_code \
    -d redirect_uri=<REDIRECT_URI> \
    -d client_id=<APP_KEY> \
    -d client_secret=<APP_SECRET>
Sample response
Example: short-lived token
{
  "access_token": "sl.AbX9y6Fe3AuH5o66-gmJpR032jwAwQPIVVzWXZNkdzcYT02akC2de219dZi6gxYPVnYPrpvISRSf9lxKWJzYLjtMPH-d9fo_0gXex7X37VIvpty4-G8f4-WX45AcEPfRnJJDwzv-",
  "expires_in": 14400,
  "token_type": "bearer",
  "scope": "account_info.read files.content.read files.content.write files.metadata.read",
  "account_id": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc",
  "uid": "12345"
}

