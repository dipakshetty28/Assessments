package com.interview.app.repository;

import com.interview.app.model.Candidate;
import java.util.List;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Repository;

@Repository
public class CandidateRepository {
    private final List<Candidate> candidates = List.of(
        new Candidate("cand_1", "Ada Lovelace", "active"),
        new Candidate("cand_2", "Grace Hopper", "active"),
        new Candidate("cand_3", "Katherine Johnson", "paused"),
        new Candidate("cand_4", "Edsger Dijkstra", "active")
    );

    public List<Candidate> findAll() {
        return candidates;
    }

    public List<Candidate> findPage(Pageable pageable) {
        int start = Math.toIntExact(pageable.getOffset());
        int end = Math.min(start + pageable.getPageSize(), candidates.size());
        if (start >= candidates.size()) {
            return List.of();
        }
        return candidates.subList(start, end);
    }
}
