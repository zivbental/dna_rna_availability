# YDR372C
Status: ok. Length: 1410 nt. Measured usable bases: 715. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 715 | 0.3752 | 0.3629 |
| rnafold | ok | 715 | 0.3332 | 0.3183 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 101 | -0.5005 | -0.2014 |
| seed_p | 101 | -0.4065 | -0.1748 |
| seed_p_vs_seed_pars | 73 | -0.5435 | -0.4029 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
