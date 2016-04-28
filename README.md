# webots-doc

Documentation for the Cyberbotics' Webots software

## To view the current gh-pages branch:

- https://www.cyberbotics.com/doc/guide/
- https://www.cyberbotics.com/doc/reference/
- https://www.cyberbotics.com/doc/automobile/
- https://www.cyberbotics.com/doc/darwin-op/

## To view a specific branch:

- https://www.cyberbotics.com/doc/guide/guide?version=branch-name


## Run the doc offline

Run a simple HTTP server:

``` python
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

