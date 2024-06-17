package com.example.shared.data

import com.example.feature.user.domain.User
import kotlinx.coroutines.Dispatchers
import org.jetbrains.exposed.sql.Transaction
import org.jetbrains.exposed.sql.transactions.experimental.newSuspendedTransaction
import java.util.*

interface Repository {
    suspend fun find(): List<User>
    suspend fun findBy(id: UUID): User?
    suspend fun add(user: User)
    suspend fun transform(user: User): User
    suspend fun removeIf(id: UUID): Boolean
}

suspend fun <T> suspendTransaction(block: suspend Transaction.() -> T): T =
    newSuspendedTransaction(Dispatchers.IO, statement = block)