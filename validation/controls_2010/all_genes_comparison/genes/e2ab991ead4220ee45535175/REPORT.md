# YDR105C
Status: ok. Length: 1738 nt. Measured usable bases: 971. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 971 | 0.3847 | 0.3597 |
| rnafold | ok | 971 | 0.3410 | 0.3319 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 361 | 0.0580 | -0.0155 |
| seed_p | 361 | -0.2113 | -0.1423 |
| seed_p_vs_seed_pars | 291 | -0.4797 | -0.3296 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
