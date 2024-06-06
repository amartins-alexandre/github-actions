package com.example.feature.user.data

import com.example.feature.user.data.dao.UserDao
import com.example.feature.user.data.dao.UserTable
import com.example.feature.user.data.dao.suspendTransaction
import com.example.feature.user.domain.User
import com.example.shared.data.Repository
import org.jetbrains.exposed.sql.SqlExpressionBuilder.eq
import org.jetbrains.exposed.sql.deleteWhere
import org.jetbrains.exposed.sql.update
import java.util.UUID

class UserRepositoryImpl : Repository {
    override suspend fun find(): List<User>  = suspendTransaction {
        UserDao.all()
            .map(UserDao::toUser)
    }

    override suspend fun findBy(id: UUID): User? = suspendTransaction {
        UserDao.find { UserTable.id eq id }
            .map(UserDao::toUser)
            .firstOrNull()
    }

    override suspend fun add(user: User): Unit = suspendTransaction {
        UserDao.new {
            name = user.name
            email = user.email
        }
    }

    override suspend fun transform(user: User): User = suspendTransaction {
        UserTable.update(
            where = { UserTable.id eq UUID.fromString(user.id) }
        ) {
            it[name] = user.name
            it[email] = user.email
        }

        user
    }

    override suspend fun removeIf(id: UUID): Boolean = suspendTransaction {
        val rowsDeleted = UserTable.deleteWhere { UserTable.id eq id }
        rowsDeleted == 1
    }
}
