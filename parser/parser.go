package main

import (
	"fmt"
	"os"
	"log"
)

func main() {
	var input string

	for {
		fmt.Println("Open a file: ")
		fmt.Scan(&input)
		
		file, err := os.Open(input)
		if err != nil {
			log.Fatal(err)
		}
	}
};