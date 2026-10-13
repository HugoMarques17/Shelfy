package infrastructure;

import domain.ports.IConfigRepository;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.BufferedWriter;
import java.nio.charset.StandardCharsets;
import java.util.Properties;


public class ConfigRepository implements IConfigRepository {
    private final Properties config = new Properties();
    private final String path;

    public ConfigRepository() {
        this("config.properties");
    }

    public ConfigRepository(String path) {
        try (InputStreamReader reader = new InputStreamReader(
                new FileInputStream(path), StandardCharsets.UTF_8)) {

            this.path = path;
            this.config.load(reader);

        } catch (IOException e) {
            throw new RuntimeException(
                    "Erro ao ler arquivo de configuração: " + path, e
            );
        }
    }

    @Override
    public String getValue(String option) {
        String value = this.config.getProperty(option);

        if (value == null || value.isBlank()) {
            throw new IllegalArgumentException(
                    "Valor vazio para " + option
            );
        }

        return value;
    }

    @Override
    public void setItem(String option, String value) {
        config.setProperty(option, value);
        this.save();
    }

    @Override
    public void save() {
        try (OutputStreamWriter writer = new OutputStreamWriter(
                new FileOutputStream(this.path), StandardCharsets.UTF_8)) {
            config.store(new BufferedWriter(writer), "Configurações da aplicação");

        } catch (IOException e) {
            throw new RuntimeException(
                    "Erro ao salvar arquivo de configuração: " + path, e
            );
        }

    }
}
