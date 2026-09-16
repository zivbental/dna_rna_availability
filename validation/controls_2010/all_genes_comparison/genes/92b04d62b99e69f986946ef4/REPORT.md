# YIL094C
Status: ok. Length: 1207 nt. Measured usable bases: 1003. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1003 | 0.3479 | 0.3342 |
| rnafold | ok | 1003 | 0.2747 | 0.2732 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 901 | -0.1578 | -0.1017 |
| seed_p | 901 | -0.1669 | -0.1202 |
| seed_p_vs_seed_pars | 760 | -0.3291 | -0.2612 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
