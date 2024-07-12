# kafka-python-golang-docker


- Understanding of Apache Kafka working with python producer and Golang consumer

### Kafka Cluster Information
- 1 producer (Written in Python)
- 1 Consumer (Written in Golang)
- 3 Kafka Broker
- 1 Zookeeper
- 1 Kafka Dashboard

### Installation

- #### Install Docker & Docker Compose
- #### Python Setup
    - Run below command to create virtual envrionment.
    ```
    python -m venv venv
    ```
    - Activate `venv` using below command.
    ```
    source venv/bin/activate
    ```
    - Install Requirements.
    ```
    pip install -r requirements.txt
    ```
- #### Golang setup
    - Install dependencies using below command
    ```
    go get -u github.com/confluentinc/confluent-kafka-go
    ```

### Running the Project
- Create Kafka Cluster using below command.
    ```
    docker compose up -d
    ```
- Run Python producer using 
    ```
    cd python-producer
    python main.py
    ```
- Run Golang consumer using
    ```
    go run main.go
    ```