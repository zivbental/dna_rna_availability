# YLR193C
Status: ok. Length: 747 nt. Measured usable bases: 354. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 354 | 0.1756 | 0.1735 |
| rnafold | ok | 354 | 0.2036 | 0.1779 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 117 | 0.3909 | 0.2732 |
| seed_p | 117 | 0.6144 | 0.4767 |
| seed_p_vs_seed_pars | 80 | 0.7928 | 0.6160 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
