# Fastjson

Clone repo: `git clone https://github.com/alibaba/fastjson.git`

We have added `pom.xml` files for following versions in their respective folders:

1. 1.2.47
2. 1.2.49
3. 1.2.51

## Reports Versions

Our artifacts include reports for all following versions.

* 1.2.47
* 1.2.49
* 1.2.51
* 1.2.52
* 1.2.54
* 1.2.55
* 1.2.56
* 1.2.57
* 1.2.58
* 1.2.59
* 1.1.71.android

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
        <includes>
            <include>**/bvt/**/*.java</include>
        </includes>
    </configuration>
</plugin>
```

In the `<configuration>..</configuration>` add: `<testFailureIgnore>true</testFailureIgnore>`.

After that, comment completely the following files (in the versions where they exist). We know for sure it causes issue in v.1.2.49. Generally approach would be to comment the files in shown in the console error.

* src/test/java/com/alibaba/json/bvt/serializer/NoneStringKeyTest_2.java
* src/test/java/com/alibaba/json/bvt/support/spring/security/DefaultOAuth2AccessTokenTest.java
* src/test/java/com/alibaba/json/test/benchmark/jdk10/StringBenchmark_jackson.java
* src/test/java/com/alibaba/json/test/benchmark/jdk10/StringBenchmark.java


Then in the root directory run `mvn clean test`.

It will generate reports in the `/target` folder at root directory.
