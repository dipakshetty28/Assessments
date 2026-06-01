package com.interview.app.controller;

import com.interview.app.model.Candidate;
import com.interview.app.service.CandidateService;
import java.util.List;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CandidateController {
    private final CandidateService candidateService;

    public CandidateController(CandidateService candidateService) {
        this.candidateService = candidateService;
    }

    @GetMapping("/api/candidates")
    public List<Candidate> listCandidates(@RequestParam(defaultValue = "0") int page, @RequestParam(defaultValue = "25") int size) {
        return candidateService.listCandidates(page, size);
    }
}
