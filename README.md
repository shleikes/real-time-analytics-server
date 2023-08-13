# Real Time Analytics Server

## Description
This is a real-time analytics server that provides real-time analytics for users.

The platform collects user interactions from various sources, processes the data, and provides real-time analytics for users.

## Features
- Fake data generator
- Real-time data processing
- Real-time Analytics
- Data storage - Not implemented yet
- Real-time data streaming - Not implemented yet

## Architecture (Implemented)
There are 3 main components in the system:
### fake-data-generator
This component generates fake data and sends it to Kafka.
It uses the Fake library to generate fake data.

### user-interaction-storer
This component consumes data from Kafka, process it and stores it in Redis.

### analytics-engine
This component consumes data from Redis and provides real-time analytics.
(Not fully implemented yet)


## Run the application
### Prerequisites
- Docker
- Kafka Server
- Redis Server

### Run the application
1. Clone the repository
2. CD into the repository
3. Run the following command to build the docker images:
    ```
    docker compose build
    ```
4. Run the following command to start the application:
    ```
    docker compose up
    ```
5. Run the following command to stop the application:
    ```
    docker compose down
    ```