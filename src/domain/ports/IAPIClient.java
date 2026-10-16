package domain.ports;

import domain.entities.APIResponse;

import java.io.IOException;


public interface IAPIClient {
    APIResponse get(String url) throws IOException, InterruptedException;
}
