# YBR170C
Status: ok. Length: 1913 nt. Measured usable bases: 880. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 880 | 0.2912 | 0.2908 |
| rnafold | ok | 880 | 0.2138 | 0.2083 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 153 | 0.3905 | 0.2755 |
| seed_p | 153 | 0.1222 | 0.1204 |
| seed_p_vs_seed_pars | 99 | 0.1140 | 0.0719 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
