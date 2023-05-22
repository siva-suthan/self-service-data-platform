# API data fetching

The sample python template api-scraping.py can be used to fetch data from different api's

## Example Flow Diagram

image.png


## /testapi/scheduleapi

DE person can calls this endpoint to schedule a new api for data fetching.

EXAMPLE
curl -X POST https://api.dataplatform.com/scrapapi/scheduleapi \
    -H 'content-type: application/json'
    -d '{“access_token”: “”,
		“api_name”: "",
		“target_table” : “db.schema.table”,
        "host":,
        "port":,
        "username":,
        "password":,
        "python-template" : "api-scraping-1.py"
		“cron” : “0 15 10 ? * *”
		}'
Sample response
{
  "status": 200,
  “body” : {	“jobid” : “123a”,
			“ScheduleddAt” : <timestamp>,
	}
}


