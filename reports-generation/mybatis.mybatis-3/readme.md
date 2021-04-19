# MyBatis

We have added `pom.xml` files for following versions in their respective folders:

1. mybatis-3.2.4
2. mybatis-3.2.5
3. mybatis-3.2.6

## Reports Versions

Our artifacts include reports for all following versions.

* mybatis-3.2.4
* mybatis-3.2.5
* mybatis-3.2.6
* mybatis-3.2.7
* mybatis-3.2.8
* mybatis-3.3.0
* mybatis-3.3.1
* mybatis-3.4.1
* mybatis-3.4.5

Use `git checkout <VERSION_NAME>` to checkout to the particular release.

## Generating report for a new version

In `pom.xml` file at the root, add the following xml code inside ```<build> <plugins> ... </plugins> </build>```.

```xml
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

Then, in the same file, inside ```<build> <plugins> ... </plugins> </build>```, for the `maven-surefire` plugin, which looks like this:

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <configuration>
        <forkMode>pertest</forkMode>
    </configuration>
</plugin>
```

In the `<configuration>..</configuration>` add: `<testFailureIgnore>true</testFailureIgnore>`.

Then at the root, run `mvn clean test`.

It will generate reports in the `/target` folder at root directory.
