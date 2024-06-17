FROM gradle:8.8-jdk21-alpine AS build
WORKDIR /app
COPY . /app/
RUN ./gradlew --no-daemon --refresh-dependencies clean build

FROM amazoncorretto:21-alpine
WORKDIR /app
COPY --from=build /app/build/libs/*.jar /app/ktor-user.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/app/ktor-user.jar"]
