# JUnit

Clone repo: `git clone https://github.com/junit-team/junit4.git`

We have added `pom.xml` files for following versions in their respective folders:

1. r4.11-beta-1
2. r4.11
3. r4.12-beta-1

These are the versions from the high density area. If we go past these versions, a JUnit uses a very old version of Maven, almost around 2010 or early, we could not generate reports there.

## Reports Versions

Our artifacts include reports for all following versions.

* r4.11-beta-1
* r4.11
* r4.12-beta-1


Use `git checkout <VERSION_NAME>` to checkout to the particular release.

## Generating report for a new version

From r4.12-beta-1 onwards, the following needs to be added to generate the report.

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
    <!--
    A plugin which uses the JUnit framework in order to start
    our junit suite "AllTests" after the sources are compiled.
    -->
    <artifactId>maven-surefire-plugin</artifactId>
    <version>2.17</version>
    <configuration>
        <test>org/junit/tests/AllTests.java</test>
        <useSystemClassLoader>true</useSystemClassLoader>
        <enableAssertions>false</enableAssertions>
    </configuration>
</plugin>
```

In the `<configuration>..</configuration>` add: `<testFailureIgnore>true</testFailureIgnore>`.

For the earlier version (r4.11-beta-1, r4.11), it gets little complex due to major maven version changes.

There is not `pom.xml` file present for those versions. You need to add a `pom.xml` file at the root. The file is provided for r4.11-beta-1 and r4.11. Place that in the root. After that you need to replace the following files. They are all provided in the respective directories.

* src/main/java/org/junit/internal/AssumptionViolatedException.java
* src/main/java/org/junit/internal/runners/InitializationError.java
* src/main/java/org/junit/rules/ExternalResource.java
* src/main/java/org/junit/runner/Request.java
* src/main/java/org/junit/runners/BlockJUnit4ClassRunner.java
* src/test/java/org/junit/tests/experimental/rules/ClassRulesTest.java
* src/test/java/org/junit/tests/experimental/rules/TestRuleTest.java

Then at the root, run `mvn clean test`.

It will generate reports in the `/target` folder at root directory.
