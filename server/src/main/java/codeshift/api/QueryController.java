package codeshift.api;

import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.http.HttpStatus;

@RestController
@CrossOrigin(origins="http://localhost:8080")
@RequestMapping(path="/api/query", produces="application/json")
public class QueryController {
  private static final org.slf4j.Logger log =
    org.slf4j.LoggerFactory.getLogger(QueryController.class);

  @GetMapping
  public String getQuery() {
    log.info("GET /api/query called");
    return "{\"message\": \"Hello from QueryController\"}";
  }
}
