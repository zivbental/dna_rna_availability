# YML094W
Status: ok. Length: 588 nt. Measured usable bases: 276. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 276 | 0.2671 | 0.2444 |
| rnafold | ok | 276 | 0.2085 | 0.1944 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 53 | -0.4057 | -0.0793 |
| seed_p | 53 | -0.5217 | -0.4918 |
| seed_p_vs_seed_pars | 34 | -0.4410 | -0.4500 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
