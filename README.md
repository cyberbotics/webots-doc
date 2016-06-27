# webots-doc

MODIFICATION ADDED

This repository holds the documentation for the Cyberbotics' Webots software.
You are very welcome to contribute to make this documentation better!
In order to proceed, simply fork this repository, make your modifications and
open a pull request that we will review and merge.

## To view a specific version:

You can display the documentation corresponding to a specific version of Webots
by using the version argument in the URL, for example:

- https://www.cyberbotics.com/doc/guide/guide?version=8.5

This version argument corresponds to a git tag on this repository.

Alternatively, it is possible to display the documentation corresponding to
a github branch of this repository:

- https://www.cyberbotics.com/doc/guide/guide?version=master

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
