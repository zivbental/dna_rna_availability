# YMR088C
Status: ok. Length: 1857 nt. Measured usable bases: 1028. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1028 | 0.2651 | 0.2495 |
| rnafold | ok | 1028 | 0.1331 | 0.1232 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 261 | 0.0612 | -0.1251 |
| seed_p | 261 | -0.0917 | -0.1443 |
| seed_p_vs_seed_pars | 204 | -0.3008 | -0.3646 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
