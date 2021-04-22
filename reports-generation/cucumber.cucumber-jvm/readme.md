# Cucumber JVM

Clone repo: `git clone https://github.com/cucumber/cucumber-jvm.git`

We have added `pom.xml` files for following versions in their respective folders:

1. v3.0.0
2. v4.0.0
3. v4.1.0

## Reports Versions

Our artifacts include reports for all following versions.

* v3.0.0
* v4.0.0
* v4.1.0
* v4.2.1
* v4.2.5
* v4.4.0

Use `git checkout <VERSION_NAME>` to checkout to the particular release.

## Generating report for a new version

In `pom.xml` file at the root, inside ```<build> <pluginManagement> <plugins> ... </plugins> </pluginManagement> </build>```, for the `maven-surefire-plugin`, which looks like this:

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>2.20</version>
    <configuration>
        <argLine>-Duser.language=en</argLine>
        <argLine>-Xmx1024m</argLine>
        <argLine>-XX:MaxPermSize=256m</argLine>
        <argLine>-Dfile.encoding=UTF-8</argLine>
        <useFile>false</useFile>
    </configuration>
</plugin>
```

Add this configuration: `<testFailureIgnore>true</testFailureIgnore>` inside the `<configuration></configuration>` tag. In the same tag, comment out all the `<argLine>` type configs. It should look something like this:

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>2.20</version>
    <configuration>
        <testFailureIgnore>true</testFailureIgnore>
        <!-- <argLine>-Duser.language=en</argLine>
        <argLine>-Xmx1024m</argLine>
        <argLine>-XX:MaxPermSize=256m</argLine>
        <argLine>-Dfile.encoding=UTF-8</argLine> -->
        <useFile>false</useFile>
    </configuration>
</plugin>
```

Now, go to the `core/pom.xml` file, inside the inside `<build> <plugins> ... </plugins> </build>`, tag for the `maven-surefire-plugin`, which looks like this:

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <configuration>
        <argLine>-Duser.language=en</argLine>
    </configuration>
</plugin>
```

Add this configuration: `<testFailureIgnore>true</testFailureIgnore>` inside the `<configuration></configuration>` tag. In the same tag, comment out all the `<argLine>` type configs. It should look something like this:


```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <configuration>
        <!-- <argLine>-Duser.language=en</argLine> -->
        <testFailureIgnore>true</testFailureIgnore>
    </configuration>
</plugin>
```

After that, within `<build> <plugins> ... </plugins> </build>`, paste the following code.

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


Now, at the root of the project, run `mvn clean test`. It will generate report in the `core/target` folder.
