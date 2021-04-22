# Auto

Clone repo: `git clone https://github.com/google/auto.git`

We have added `pom.xml` files for following versions in their respective folders:

1. auto-value-1.1
2. auto-value-1.2
3. auto-value-1.3

These needs to placed in the in the `value` directory. The root of this project do not have a test
runner. It manages it through the one in `value` directory. So `pom.xml` needs to be replaced in that directory and `mvn clean test` should be run inside `value` directory.

## Reports Versions

Our artifacts include reports for all following versions.

* auto-value-1.1
* auto-value-1.2
* auto-value-1.3
* auto-value-1.4-rc2
* auto-value-1.4-rc3
* auto-value-1.4.1
* auto-value-1.5.1
* auto-value-1.5.2
* auto-value-1.5.3
* auto-value-1.5
* auto-value-1.6.2
* auto-value-1.6


Use `git checkout <VERSION_NAME>` to checkout to the particular release.

## Generating report for a new version

Add the following xml code inside ```<build> <plugins> ... </plugins> </build>``` in the `pom.xml` file in the `value` directory and run `mvn clean test` in the `value` directory.

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
