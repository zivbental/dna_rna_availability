# YBR056W
Status: ok. Length: 1582 nt. Measured usable bases: 829. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 829 | 0.3562 | 0.3568 |
| rnafold | ok | 829 | 0.2916 | 0.2929 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 169 | -0.0430 | -0.1570 |
| seed_p | 169 | -0.1192 | -0.2325 |
| seed_p_vs_seed_pars | 145 | -0.0971 | -0.1735 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
