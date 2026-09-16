# YDR120C
Status: ok. Length: 1911 nt. Measured usable bases: 939. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 939 | 0.3171 | 0.3050 |
| rnafold | ok | 939 | 0.2793 | 0.2552 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 234 | -0.2283 | -0.2315 |
| seed_p | 234 | -0.1590 | -0.0788 |
| seed_p_vs_seed_pars | 187 | -0.2510 | -0.1192 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
