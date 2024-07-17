package org.cyberpsych.docanalyzer;

import org.cyberpsych.docanalyzer.services.StorageService;
import org.cyberpsych.docanalyzer.services.storage.StorageProperties;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
@EnableConfigurationProperties(StorageProperties.class)
public class DocAnalyzerApplication {

	public static void main(String[] args) {
		SpringApplication.run(DocAnalyzerApplication.class, args);
	}
	@Bean
	CommandLineRunner init(StorageService storageService) {
		return (args) -> {
			storageService.deleteAll();
			storageService.init();
		};
	}
}
