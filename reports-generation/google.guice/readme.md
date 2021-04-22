# Guice

Clone repo: `git clone https://github.com/google/guice.git`

We have added `pom.xml` files for following versions in their respective folders:

1. 3.0-rc3
2. 4.0-beta4

All the bugs in the dataset are covered by these versions.

## Reports Versions

Our artifacts include reports for all following versions.

* 3.0-rc3
* 4.0-beta4

Use `git checkout <VERSION_NAME>` to checkout to the particular release.

## Generating report for a new version

Guice do not have a test runner at root. It runs tests via `pom.xml` file at `core/`. So in `pom.xml` file at `core/`, add the following xml code inside ```<build> <plugins> ... </plugins> </build>```.
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
    <groupId>org.codehaus.mojo</groupId>
    <artifactId>animal-sniffer-maven-plugin</artifactId>
    </plugin>
    <plugin>
    <artifactId>maven-surefire-plugin</artifactId>
    <configuration>
        <!--
        | Temporarily excluded tests
        -->
        <excludes>
        <exclude>**/OSGiContainerTest*</exclude>
        <exclude>**/ScopesTest*</exclude>
        <exclude>**/TypeConversionTest*</exclude>
        </excludes>
    </configuration>
</plugin>
```

In the `<configuration>..</configuration>` add: `<testFailureIgnore>true</testFailureIgnore>`.

Then go to `core/src/com/google/inject/spi/DefaultBindingTargetVisitor.java` file and replace line number 75 with following line: `return visitOther(providerBinding);` (This one was required for v3.0-rc3)

For the version 4.0-beta4, you have comment the line number 228 in the `pom.xml` file at the root of the project. The line looks like this:

```xml
<argLine>-Dguice_include_stack_traces=ONLY_FOR_DECLARING_SOURCE</argLine>
```

Then in the `core/` directory run `mvn clean test`.

It will generate reports in the `/target` folder at root directory.
