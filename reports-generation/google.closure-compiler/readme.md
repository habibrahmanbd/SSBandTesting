# Closure Compiler

Clone repo: `git clone https://github.com/google/closure-compiler.git`

We have added `pom.xml` files for following versions in their respective folders:

 1. v20171203
 2. v20180204
 3. v20180506

## Reports Versions

Our artifacts include reports for all following versions.

 * v20171203
 * v20180204
 * v20180506
 * v20180805
 * v20181028
 * v20190121
 * v20190325
 * v20190618
 * v20190709
 * v20190819
 * webpack-v20180621
 * webpack-v20180701

Use `git checkout <VERSION_NAME>` to checkout to the particular release.

## Generating report for a new version

In the ```<build> <plugins> ... </plugins> </build>``` in the `pom-main.xml` file at the root directory, replace:

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
...
...
</plugin>
```
by

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
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

and run `mvn clean test`. It will generate reports in the `/target` folder at root directory.
