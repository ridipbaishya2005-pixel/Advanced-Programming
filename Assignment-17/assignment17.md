<?xml version="1.0" encoding="UTF-8"?>

<project xmlns="http://maven.apache.org/POM/4.0.0"

&#x20;        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

&#x20;        xsi:schemaLocation="http://maven.apache.org/POM/4.0.0

&#x20;                            https://maven.apache.org/xsd/maven-4.0.0.xsd">

&#x20; <modelVersion>4.0.0</modelVersion>



&#x20; <groupId>com.onboarding</groupId>

&#x20; <artifactId>registration-module</artifactId>

&#x20; <version>1.0.0</version>

&#x20; <packaging>jar</packaging>



&#x20; <properties>

&#x20;   <java.version>17</java.version>

&#x20;   <maven.compiler.source>${java.version}</maven.compiler.source>

&#x20;   <maven.compiler.target>${java.version}</maven.compiler.target>

&#x20;   <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>

&#x20;   <junit.version>5.10.2</junit.version>

&#x20; </properties>



&#x20; <dependencies>

&#x20;   <!-- JUnit 5 -->

&#x20;   <dependency>

&#x20;     <groupId>org.junit.jupiter</groupId>

&#x20;     <artifactId>junit-jupiter</artifactId>

&#x20;     <version>${junit.version}</version>

&#x20;     <scope>test</scope>

&#x20;   </dependency>

&#x20; </dependencies>



&#x20; <build>

&#x20;   <plugins>

&#x20;     <plugin>

&#x20;       <groupId>org.apache.maven.plugins</groupId>

&#x20;       <artifactId>maven-surefire-plugin</artifactId>

&#x20;       <version>3.2.5</version>

&#x20;       <!-- Enable assertions so assert statements fire during tests -->

&#x20;       <configuration>

&#x20;         <argLine>-ea</argLine>

&#x20;       </configuration>

&#x20;     </plugin>

&#x20;   </plugins>

&#x20; </build>

</project>

