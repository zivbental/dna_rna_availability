# YAL058W
Status: ok. Length: 1614 nt. Measured usable bases: 856. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 856 | 0.3552 | 0.3592 |
| rnafold | ok | 856 | 0.2419 | 0.2633 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 173 | -0.0025 | 0.0655 |
| seed_p | 173 | -0.0808 | -0.0205 |
| seed_p_vs_seed_pars | 142 | -0.5112 | -0.4381 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
