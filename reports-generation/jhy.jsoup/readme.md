# Jsoup

We have added `pom.xml` files for following versions in their respective folders:

1. jsoup-1.6.0
2. jsoup-1.6.1
3. jsoup-1.6.2

## Reports Versions

Our artifacts include reports for all following versions.

* jsoup-1.6.0
* jsoup-1.6.1
* jsoup-1.6.2
* jsoup-1.6.3
* jsoup-1.7.1
* jsoup-1.7.2
* jsoup-1.7.3
* jsoup-1.8.1.a
* jsoup-1.8.2


Use `git checkout <VERSION_NAME>` to checkout to the particular release.

## Generating report for a new version

In the `pom.xml` file at root, add the following xml code inside ```<build> <plugins> ... </plugins> </build>```.

There could be multiple such tags, make sure it is not the one inside the `<profiles>..</profiles>` tag.
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
    <configuration>
        <destFile>${project.basedir}/target/jacoco.exec</destFile>
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
            <dataFile>${project.basedir}/target/jacoco.exec</dataFile>
            <outputEncoding>UTF-8</outputEncoding>
            <outputDirectory>${project.basedir}/target/</outputDirectory>
        </configuration>
        </execution>
    </executions>
</plugin>
```

Then at the root, run `mvn clean test`.

It will generate reports in the `/target` folder at root directory.
