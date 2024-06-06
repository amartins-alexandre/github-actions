package com.example.feature.user.data.dao

import org.jetbrains.exposed.dao.id.UUIDTable

object UserTable : UUIDTable("ktor.user") {
    val name = varchar("name", 50)
    val email = varchar("email", 50)
}