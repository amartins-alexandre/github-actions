package com.example.feature.user.domain

import kotlinx.serialization.Serializable

@Serializable
data class User(
    val id: String? = null,
    val name: String,
    val email: String
)
