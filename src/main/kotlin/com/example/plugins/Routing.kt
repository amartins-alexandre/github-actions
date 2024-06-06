package com.example.plugins

import com.example.feature.user.data.UserRepositoryImpl
import com.example.feature.user.routes.userRouting
import io.ktor.server.application.*
import io.ktor.server.routing.*

fun Application.configureRouting() {
    val repository = UserRepositoryImpl()

    routing {
        userRouting(repository)
    }
}
