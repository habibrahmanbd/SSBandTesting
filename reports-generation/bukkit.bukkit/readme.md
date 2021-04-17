# Bukkit

We have added `pom.xml` files for following versions in their respective folders:

1. 1.4.7-R0.1
2. 1.5.1-R0.1
3. 1.5.2-R0.1

## Reports Versions

Our artifacts include reports for all following versions.

* 1.4.7-R0.1
* 1.5.1-R0.1
* 1.5.2-R0.1
* 1.5.2-R1.0
* 1.6.2-R0.1
* 1.6.2-R1.0
* 1.6.4-R1.0
* 1.7.2-R0.1
* 1.7.2-R0.3
* 1.7.9-R0.2

Use `git checkout <VERSION_NAME>` to checkout to the particular release.

## Generating report for a new version

In `pom.xml` file at the root, add the following xml code inside ```<build> <plugins> ... </plugins> </build>``` and run `mvn clean test`.

It will generate reports in the `/target` folder at root directory.

```xml
<plugin>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>2.19.1</version>
    <configuration>
        <testFailureIgnore>true</testFailureIgnore>
    </configuration>
</plugin>
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <version>0.8.3</version>

    <executions>
        <execution>
            <id>default-prepare-agent</id>
            <goals>
                <goal>prepare-agent</goal>
            </goals>
            <configuration>
                <destFile>${project.basedir}/target/jacoco.exec</destFile>
            </configuration>
        </execution>
        <execution>
            <id>default-report</id>
            <phase>test</phase>
            <goals>
                <goal>report</goal>
            </goals>
            <configuration>
                <dataFile>${project.basedir}/target/jacoco.exec</dataFile>
                <outputEncoding>UTF-8</outputEncoding>
                <outputDirectory>${project.basedir}/target/</outputDirectory>
            </configuration>
        </execution>
    </executions>
</plugin>
```
