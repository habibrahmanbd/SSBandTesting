# Asynchronous Http Client

We have added `pom.xml` files for following versions in their respective folders:

1. async-http-client-project-2.0.25
2. async-http-client-project-2.0.28
3. async-http-client-project-2.0.30

## Reports Versions

Our artifacts include reports for all following versions.

* async-http-client-project-2.0.25
* async-http-client-project-2.0.28
* async-http-client-project-2.0.30
* async-http-client-project-2.0.32
* async-http-client-project-2.0.34
* async-http-client-project-2.0.36
* async-http-client-project-2.1.0-RC3
* async-http-client-project-2.1.0-RC4
* async-http-client-project-2.1.0-alpha12
* async-http-client-project-2.1.0-alpha20
* async-http-client-project-2.1.0-alpha21
* async-http-client-project-2.1.0-alpha26
* async-http-client-project-2.1.0
* async-http-client-project-2.1.1

Use `git checkout <VERSION_NAME>` to checkout to the particular release.

## Generating report for a new version

In `pom.xml` file at the root, add the following xml code inside ```<build> <plugins> ... </plugins> </build>```.

```xml
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <version>0.8.3</version>
    <configuration>
        <destFile>${project.basedir}/../target/jacoco.exec</destFile>
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
                <dataFile>${project.basedir}/../target/jacoco.exec</dataFile>
                <outputEncoding>UTF-8</outputEncoding>
                <outputDirectory>${project.basedir}/../target/</outputDirectory>
            </configuration>
        </execution>
    </executions>
</plugin>
```

inside ```<build> <plugins> ... </plugins> </build>```, in the following section:
```xml
<plugin>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>2.19.1</version>
    <configuration>
        ...
    </configuration>
</plugin>
```

Add this config:

```xml
<testFailureIgnore>true</testFailureIgnore>
```

Then in the ```<modules> ... </modules>``` tag, remove:

1. `<module>netty-bp</module>`
2. `<module>example</module>`

They are external integration and cause issue during build locally for some reason.

Once done,  run `mvn clean test`. Note that while running tests when it prints 'Running TestSuite', it takes quite a while to move forward.

It will generate reports in the `/target` folder at root directory.
