# YDL100C
Status: ok. Length: 1147 nt. Measured usable bases: 960. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 960 | 0.3502 | 0.3456 |
| rnafold | ok | 960 | 0.3110 | 0.2952 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 875 | -0.0983 | -0.0809 |
| seed_p | 875 | -0.2820 | -0.2311 |
| seed_p_vs_seed_pars | 758 | -0.3911 | -0.3420 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
