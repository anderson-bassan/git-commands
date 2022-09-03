content = '';

with open('pom.xml') as base_pom:
	for i in range(9):
		content += base_pom.readline();

content += """
<properties>
	<maven.compiler.release>17</maven.compiler.release>
</properties>
<dependencies>
	<dependency>
		<groupId>org.junit.jupiter</groupId>
		<artifactId>junit-jupiter</artifactId>
		<version>5.9.0</version>
		<scope>test</scope>
	</dependency>
	<dependency>
		<groupId>org.mockito</groupId>
		<artifactId>mockito-core</artifactId>
		<version>4.7.0</version>
		<scope>test</scope>
	</dependency>
	<dependency>
		<groupId>org.hamcrest</groupId>
		<artifactId>hamcrest</artifactId>
		<version>2.2</version>
		<scope>test</scope>
	</dependency>
	<dependency>
		<groupId>org.mockito</groupId>
		<artifactId>mockito-junit-jupiter</artifactId>
		<version>4.7.0</version>
		<scope>test</scope>
	</dependency>
</dependencies>
<build>
    <pluginManagement>
		<plugins>
			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-compiler-plugin</artifactId>
				<version>3.10.1</version>
			</plugin>
			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-surefire-plugin</artifactId>
				<version>3.0.0-M7</version>
			</plugin>
		</plugins>
	</pluginManagement>
</build>
</project>
""";

with open('pom2.xml', 'w') as new_pom:
	new_pom.write(content);