# API data fetching

The sample python template api-scraping.py can be used to fetch data from different api's

## Example Flow Diagram

![image](https://github.com/siva-suthan/self-service-data-platform/assets/56590665/bafbefb2-b74c-499e-a51e-276a18ac00d1)


<img width="557" alt="image" src="https://github.com/siva-suthan/self-service-data-platform/assets/56590665/bc9b40ea-1b89-489c-a971-c80cb7476323">

1. DE person can hit the either one of the api endpoint for api schedule or delete or modify.
2. The api call the relavant lambda function to create a lambda/ glue based on the given information.
3. For example, If it is a scheduleapi call, then credentials are stored in the secret manager, and new lambda/glue job will be created and scheduled based on the given information. boto3 with sample python template or terreform template can be used.
4. sample api request and response for scheduling a api is given below

<img width="381" alt="image" src="https://github.com/siva-suthan/self-service-data-platform/assets/56590665/79c3298d-9160-4578-b34f-b23a7aa3fc67">

## /scrapapi/scheduleapi

DE person can calls this endpoint to schedule a new api for data fetching.

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
				“api_name”: "",
				"lambda/glue_name":,
				"arn":,
				"secret_id":
			}
		}


## /scrapapi/modifyapi
	curl -X POST https://api.dataplatform.com/scrapapi/modifyapi \
    -H 'content-type: application/json'
    -d '{“access_token”: “”,
	“api_name”: "",
	“target_table” : “db.schema.table”,
        "host":,
        "port":,
        "username":,
        "password":,
        "python-template" : "api-scraping-1.py"
	“cron” : “0 15 10 ? * *”,
	"lambda/glue_name":,
	"arn":,
	"secret_id":,
	}'
Sample response

	{
	  "status": 200,
	  “body” : {	“jobid” : “123a”,
			“ScheduleddAt” : <timestamp>,
			“api_name”: "",
			"lambda/glue_name":,
			"lambda/glue_arn":,
			"secret_id":
		}
	}


## /scrapapi/deleteapi
	curl -X POST https://api.dataplatform.com/scrapapi/deleteapi \
    -H 'content-type: application/json'
    -d '{“access_token”: “”,
	“jobid” : “123a”,
	“ScheduleddAt” : <timestamp>,
	“api_name”: "",
	"lambda/glue_name":,
	"lambda/glue_arn":,
	"secret_id":
	}'
Sample response
	
	{
  	"status": 200,
  	“body” : {	“message” : “”,
				“timestamp” : <timestamp>,	
		}
	}




