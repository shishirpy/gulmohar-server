# Gulmohar-Server

[![<shishirpy>](https://circleci.com/gh/shishirpy/gulmohar-server.svg?style=svg)](https://app.circleci.com/pipelines/github/shishirpy/gulmohar-server)


This server is build upon the [MDP/0.1](https://rfc.zeromq.org/spec/7/) specification. The inital code is borrowed from the [zeromq guide](http://zguide.zeromq.org/page:chapter4#toc12). The aim of the project is to expose set of high level APIs for service oriented queueing.

## Install
The fastest way to install the server is via docker. Use the following commands:
```bash
docker build -t gulmohar .
docker run -dp 5555:5555 gulmohar
```

The server runs at port `5555` within the container.
