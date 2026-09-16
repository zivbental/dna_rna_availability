# YIL027C
Status: ok. Length: 549 nt. Measured usable bases: 321. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 321 | 0.3104 | 0.2809 |
| rnafold | ok | 321 | 0.3112 | 0.2795 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 122 | -0.2081 | -0.1747 |
| seed_p | 122 | -0.1115 | -0.1857 |
| seed_p_vs_seed_pars | 90 | -0.6938 | -0.6183 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
