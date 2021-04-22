# Druid

Clone repo: `git clone https://github.com/alibaba/druid.git`

We have added `pom.xml` files for following versions in their respective folders:

1. 1.1.10
2. 1.1.11
3. 1.1.13

## Reports Versions

Our artifacts include reports for all following versions.

* 1.1.10
* 1.1.11
* 1.1.13
* 1.1.14
* 1.1.16
* 1.1.18
* 1.1.19

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
    <version>2.12.4</version>
    <configuration>
        <includes>
            <include>**/bvt/**/*.java</include>
        </includes>
    </configuration>
</plugin>
```

In the `<configuration>..</configuration>` add: `<testFailureIgnore>true</testFailureIgnore>`. Then in the root directory run `mvn clean test`.

It will generate reports in the `/target` folder at root directory.
