package com.example;

import com.mongodb.MongoClient;

public class Main {
    public static void main(String[] args) {
        MongoClient m = new MongoClient();
        System.out.println("MongoDB client created successfully!");
    }
}