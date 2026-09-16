# YGL142C
Status: ok. Length: 2008 nt. Measured usable bases: 892. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 892 | 0.2562 | 0.2523 |
| rnafold | ok | 892 | 0.2303 | 0.2332 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 170 | -0.0644 | -0.2052 |
| seed_p | 170 | -0.2568 | -0.2057 |
| seed_p_vs_seed_pars | 131 | -0.3193 | -0.1590 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
