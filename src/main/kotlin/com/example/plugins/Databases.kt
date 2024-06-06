package com.example.plugins

import io.ktor.server.application.*
import org.jetbrains.exposed.sql.Database

fun Application.configureDatabases() {
    val dbHost = System.getenv().getOrDefault("DB_HOST", "localhost:5432")
    Database.connect(
        driver = "org.postgresql.Driver",
        url = "jdbc:postgresql://$dbHost/postgres",
        user = System.getenv().getOrDefault("DB_USER", "postgres"),
        password = System.getenv().getOrDefault("DB_PWD", "123124"),
    )
}
