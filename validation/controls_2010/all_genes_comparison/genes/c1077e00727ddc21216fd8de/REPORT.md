# YPL081W
Status: ok. Length: 824 nt. Measured usable bases: 477. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 477 | 0.3050 | 0.3016 |
| rnafold | ok | 477 | 0.2378 | 0.2422 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 235 | -0.1243 | -0.1876 |
| seed_p | 235 | -0.2288 | -0.2206 |
| seed_p_vs_seed_pars | 188 | -0.2930 | -0.1288 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
