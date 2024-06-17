package com.example.feature.user.data.dao

import com.example.feature.user.domain.User
import org.jetbrains.exposed.dao.UUIDEntity
import org.jetbrains.exposed.dao.UUIDEntityClass
import org.jetbrains.exposed.dao.id.EntityID
import java.util.*

class UserDao(id: EntityID<UUID>) : UUIDEntity(id) {
    companion object : UUIDEntityClass<UserDao>(UserTable)

    var name by UserTable.name
    var email by UserTable.email

    fun toUser() = User(
        id = id.value.toString(),
        name = name,
        email = email
    )
}

