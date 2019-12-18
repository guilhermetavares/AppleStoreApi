# AppleStoreApi

To follow and run this instructions, you need a (https://www.docker.com/get-started)[Docker] installed.
You can run using some virtualenv.


# Step-by-step

1. For started the project, you need build the container, for this use the command
```
make build
```

2. To run the project, the api is server on http://0.0.0.0:4000/.
You need to execute the command
```
make run
```

3. You need to load the csv apple data, using the the command
```
make load url=url_to_file_.csv
```
Or you can make the data import by api
```
curl --request POST \
  --url 'http://0.0.0.0:4000/load/' \
  --header 'content-type: application/json' \
  --data '{"path": "url_to_file_.csv"}'
```

4. To identify genres and their highlights, you need to use the api for genres. This is already ordered by n_citacoes
```
curl --request GET --url http://0.0.0.0:4000/genres/
```
And for filter the genres, by the get param prime_genre for example
```
curl --request GET --url 'http://0.0.0.0:4000/genres/?prime_genre=Music%2CBook'
```
And for limit the results, like 10 with more quotes for example, just use the limit param
```
curl --request GET --url 'http://0.0.0.0:4000/genres/?limit=1&prime_genre=Music%2CBook'
```

5. This projet has 100% code coverage by tests, for running the tests just
```
make test
```
