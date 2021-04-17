# Bukkit

We have added `pom.xml` files for following versions in their respective folders:

1. HikariCP-2.3.0
2. HikariCP-2.3.10
3. HikariCP-2.3.11

## Reports Versions

Our artifacts include reports for all following versions.

* HikariCP-2.3.0
* HikariCP-2.3.10
* HikariCP-2.3.11
* HikariCP-2.3.13
* HikariCP-2.3.3
* HikariCP-2.3.6
* HikariCP-2.3.8
* HikariCP-2.4.0
* HikariCP-2.4.1
* HikariCP-2.4.2
* HikariCP-2.4.3


Use `git checkout <VERSION_NAME>` to checkout to the particular release.

## Generating report for a new version

In `pom.xml` file at the root, add the following xml code inside ```<build> <pluginManagement> <plugins>  ... </plugins> </pluginManagement> </build>``` and then also add the same xml code inside ```<build> <plugins> ... </plugins> </build>``` but in the `<profiles> ... </profiles>` tag.

```xml
<plugin>
        <groupId>org.jacoco</groupId>
        <artifactId>jacoco-maven-plugin</artifactId>
        <version>0.8.3</version>
    <configuration>
        <destFile>${project.basedir}/../../target/jacoco.exec</destFile>
        <append>true</append>
    </configuration>
        <executions>
        <execution>
            <id>default-prepare-agent</id>
            <goals>
                <goal>prepare-agent</goal>
            </goals>
        </execution>
        <execution>
            <id>default-report</id>
            <phase>test</phase>
            <goals>
                <goal>report</goal>
            </goals>
            <configuration>
                <dataFile>${project.basedir}/../../target/jacoco.exec</dataFile>
                <outputEncoding>UTF-8</outputEncoding>
                <outputDirectory>${project.basedir}/../../target/</outputDirectory>
            </configuration>
        </execution>
        </executions>
</plugin>
```

Then for the `pom.xml` file at the root, add the following line:

```xml
<testFailureIgnore>true</testFailureIgnore>
```

inside the `<configuration>` tag at the following place:

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>2.15</version>
    <configuration>
        ....
    </configuration>
</plugin>
```

Then for the `pom.xml` file at the `/hikaricp` directory, add the following line:

```xml
<testFailureIgnore>true</testFailureIgnore>
```

inside the `<configuration>` tag at the following place:

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <configuration>
        ....
    </configuration>
</plugin>
```
in the `<build>` tag.

After that, in the same file, replace:

```xml
<outputDirectory>${project.reporting.outputDirectory}/jacoco</outputDirectory>
```

by

```xml
<outputDirectory>${project.build.directory}/coverage-reports/jacoco</outputDirectory>
```

run `mvn clean test`.

It will generate reports in the in `/hikaricp/target/coverage-reports/jacoco` directory.
