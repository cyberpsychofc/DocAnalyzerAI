FROM gradle:8.0.2-jdk17 AS build
WORKDIR /app
COPY . .
RUN ./gradlew build && java -jar build/libs/gs-spring-boot-docker-0.1.0.jar --no-daemon
COPY build/libs/app.jar app.jar

FROM openjdk:17-jdk-alpine
ARG JAR_FILE=build/libs/*.jar
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java","-jar","/app.jar"]