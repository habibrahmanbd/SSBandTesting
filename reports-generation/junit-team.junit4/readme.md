# Jsoup

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
