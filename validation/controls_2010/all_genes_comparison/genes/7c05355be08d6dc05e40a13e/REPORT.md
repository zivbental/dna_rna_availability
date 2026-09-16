# YDR376W
Status: ok. Length: 1560 nt. Measured usable bases: 775. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 775 | 0.3840 | 0.3742 |
| rnafold | ok | 775 | 0.3375 | 0.3257 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 69 | 0.0588 | -0.0231 |
| seed_p | 69 | -0.2586 | -0.1171 |
| seed_p_vs_seed_pars | 45 | -0.2347 | -0.2061 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
