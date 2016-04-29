# webots-doc

Documentation for the Cyberbotics' Webots software


## To view a specific branch:

- https://www.cyberbotics.com/doc/guide/guide?version=branch-name


## Run the doc offline

Create or update the local_index.html page:

``` shell
python local_exporter.py
```

Run a simple HTTP server:

``` shell
python -m SimpleHTTPServer
```

In a browser, open:

- [http://localhost:8000/local_index.html?url=&book=guide](http://localhost:8000/local_index.html?url=&book=guide)
- [http://localhost:8000/local_index.html?url=&book=reference](http://localhost:8000/local_index.html?url=&book=reference)
- [http://localhost:8000/local_index.html?url=&book=automobile](http://localhost:8000/local_index.html?url=&book=automobile)
- [http://localhost:8000/local_index.html?url=&book=darwin-op](http://localhost:8000/local_index.html?url=&book=darwin-op)


## Run the unit tests

``` python
python -m unittest discover
```
