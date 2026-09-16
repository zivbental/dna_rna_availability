# YLR110C
Status: ok. Length: 507 nt. Measured usable bases: 466. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 466 | 0.2205 | 0.1758 |
| rnafold | ok | 466 | 0.1813 | 0.1116 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 445 | -0.5196 | -0.1143 |
| seed_p | 445 | -0.2401 | 0.0419 |
| seed_p_vs_seed_pars | 442 | -0.1713 | 0.1186 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
