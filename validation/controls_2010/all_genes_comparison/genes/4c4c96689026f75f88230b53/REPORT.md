# YGR029W
Status: ok. Length: 666 nt. Measured usable bases: 382. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 382 | 0.3016 | 0.2902 |
| rnafold | ok | 382 | 0.3448 | 0.3289 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 153 | -0.2138 | -0.2177 |
| seed_p | 153 | -0.2095 | -0.2606 |
| seed_p_vs_seed_pars | 92 | -0.2240 | -0.0303 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
