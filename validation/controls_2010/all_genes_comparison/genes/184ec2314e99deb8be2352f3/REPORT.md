# YNL099C
Status: ok. Length: 987 nt. Measured usable bases: 424. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 424 | 0.1616 | 0.1780 |
| rnafold | ok | 424 | 0.0835 | 0.1232 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 76 | 0.2686 | 0.6162 |
| seed_p | 76 | 0.4732 | 0.5419 |
| seed_p_vs_seed_pars | 54 | 0.5782 | 0.5979 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
