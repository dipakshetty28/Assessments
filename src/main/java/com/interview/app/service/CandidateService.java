package com.interview.app.service;

import com.interview.app.model.Candidate;
import com.interview.app.repository.CandidateRepository;
import java.util.List;
import org.springframework.stereotype.Service;

@Service
public class CandidateService {
    private final CandidateRepository repository;

    public CandidateService(CandidateRepository repository) {
        this.repository = repository;
    }

    public List<Candidate> listCandidates(int page, int size) {
        return repository.findAll();
    }
}
