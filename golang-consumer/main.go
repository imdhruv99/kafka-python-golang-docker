package main

import (
	"fmt"
	"log"

	"github.com/confluentinc/confluent-kafka-go/kafka"
)

func main() {
	c, err := kafka.NewConsumer(&kafka.ConfigMap{
		"bootstrap.servers": "localhost:9091,localhost:9092,localhost:9093",
		"group.id":          "log-consumers",
		"auto.offset.reset": "earliest",
		"security.protocol": "PLAINTEXT",
	})

	if err != nil {
		log.Fatalf("Failed to create consumer: %s\n", err)
	}

	err = c.SubscribeTopics([]string{"logs"}, nil)
	if err != nil {
		log.Fatalf("Failed to subscribe to topics: %s\n", err)
	}

	for {
		msg, err := c.ReadMessage(-1)
		if err == nil {
			fmt.Printf("Received: %s\n", string(msg.Value))
		} else {
			// The client will automatically try to recover from all errors.
			fmt.Printf("Consumer error: %v (%v)\n", err, msg)
		}
	}
}
