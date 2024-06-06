package com.example.feature.user.routes

import com.example.feature.user.domain.User
import com.example.shared.data.Repository
import io.ktor.http.*
import io.ktor.serialization.*
import io.ktor.server.application.*
import io.ktor.server.request.*
import io.ktor.server.response.*
import io.ktor.server.routing.*
import java.util.*

fun Route.userRouting(repository: Repository) {
    route("/user") {
        get {
            val users = repository.find()
            if (users.isNotEmpty()) {
                call.respond(users)
            } else {
                call.respondText("Users not found", status = HttpStatusCode.NotFound)
            }
        }
        get("{id?}") {
            val id = call.parameters["id"] ?: return@get call.respondText(
                "Missing or malformed id",
                status = HttpStatusCode.BadRequest
            )

            val user = repository.findBy(UUID.fromString(id)) ?: return@get call.respondText(
                "No user with id $id",
                status = HttpStatusCode.NotFound
            )

            call.respond(user)
        }
        post {
            try {
                val user = call.receive<User>()
                repository.add(user)
                call.respond(HttpStatusCode.NoContent)
            } catch(e: IllegalStateException) {
                call.respondText(
                    "Missing fields or wrong format",
                    status = HttpStatusCode.BadRequest
                )
            } catch (e: JsonConvertException) {
                call.respondText(
                    "Invalid JSON format",
                    status = HttpStatusCode.BadRequest
                )
            }
        }
        put("{id?}") {
            val id = call.parameters["id"] ?: return@put call.respondText(
                "Missing or malformed id",
                status = HttpStatusCode.BadRequest
            )

            val user = repository.findBy(UUID.fromString(id)) ?: return@put call.respondText(
                "No user with id $id",
                status = HttpStatusCode.NotFound
            )

            val newUser = call.receive<User>()
            repository.transform(
                user.copy(
                    name = newUser.name,
                    email = newUser.email
                )
            )
            call.respondText("User updated correctly")
        }
        delete("{id?}") {
            val id = call.parameters["id"] ?: return@delete call.respondText(
                "Missing or malformed id",
                status = HttpStatusCode.BadRequest
            )

            if (repository.removeIf(UUID.fromString(id))) {
                call.respondText("User removed correctly", status = HttpStatusCode.Accepted)
            } else {
                call.respondText("No user with id $id", status = HttpStatusCode.NotFound)
            }
        }
    }
}