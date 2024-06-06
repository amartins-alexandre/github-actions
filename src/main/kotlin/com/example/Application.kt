package com.example

import com.example.plugins.*
import io.ktor.server.application.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*

fun main() {
    val port = System.getenv()
        .getOrDefault("SERVER_PORT", "8080")
        .toInt()

    embeddedServer(
        Netty,
        port = port,
        module = Application::module
    ).start(wait = true)
}

fun Application.module() {
    configureSerialization()
    configureDatabases()
    configureRouting()
}
