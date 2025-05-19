FROM eclipse-temurin:17-jdk
ARG JAR_FILE=build/libs/*.jar
COPY ${JAR_FILE} app.jar
RUN gradlew build && java -jar build/libs/gs-spring-boot-docker-0.1.0.jar
ENTRYPOINT ["java","-jar","/app.jar"]