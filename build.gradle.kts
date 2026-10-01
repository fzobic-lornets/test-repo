plugins {
    java
}

group = "com.example"
version = "1.0.0"

repositories {
    mavenCentral()
}

dependencies {
    // All intentionally OLD, well-known-vulnerable versions
    implementation("org.apache.logging.log4j:log4j-core:2.14.1")               // CVE-2021-44228 (Log4Shell, CRITICAL)
    implementation("com.fasterxml.jackson.core:jackson-databind:2.9.10")      // multiple CVEs (CRITICAL/HIGH)
    implementation("org.springframework:spring-web:5.3.0")                    // CVE-2022-22965 (Spring4Shell, CRITICAL)
    implementation("org.apache.commons:commons-text:1.9")                     // CVE-2022-42889 (Text4Shell, CRITICAL)
    implementation("commons-collections:commons-collections:3.2.1")           // CVE-2015-6420 (HIGH)
    implementation("org.yaml:snakeyaml:1.30")                                 // CVE-2022-1471 (HIGH)
}

dependencyLocking {
    lockAllConfigurations()
}

java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(17)
    }
}
