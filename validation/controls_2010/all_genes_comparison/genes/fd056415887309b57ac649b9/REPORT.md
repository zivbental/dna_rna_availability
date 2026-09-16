# YHR055C
Status: ok. Length: 367 nt. Measured usable bases: 176. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 176 | 0.0352 | 0.0606 |
| rnafold | ok | 176 | 0.0493 | 0.0808 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 101 | 0.0231 | -0.4154 |
| seed_p | 101 | -0.1592 | -0.4453 |
| seed_p_vs_seed_pars | 69 | -0.0914 | -0.3097 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
