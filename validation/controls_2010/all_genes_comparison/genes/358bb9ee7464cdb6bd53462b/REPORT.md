# YPL198W
Status: ok. Length: 856 nt. Measured usable bases: 248. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 248 | 0.4989 | 0.5037 |
| rnafold | ok | 248 | 0.4912 | 0.4766 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 92 | -0.4561 | -0.5203 |
| seed_p | 92 | -0.3763 | -0.4312 |
| seed_p_vs_seed_pars | 50 | -0.2330 | -0.3057 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
