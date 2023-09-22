# Test API Request

This repo tests the following api request...

```
https://app.leadconduit.com/flows/64f88c209fdcbc91ead79a18/sources/64f88bb312e29022f8da4df2/submit Headers: Accept: application/json Content-Type: application/x-www-form-urlencoded Data: --data-urlencode 'first_name=' \ --data-urlencode 'last_name= \ --data-urlencode 'email=' \ --data-urlencode 'repo_url='*
```

<br>

Response received...

```
    response status code: 201
    response reason: Created

    response text:
    {
        "outcome": "success",
        "lead": {
            "id": "650de324f53035d7b74436cc"
        },
        "price": 0
    }
```
<br>
