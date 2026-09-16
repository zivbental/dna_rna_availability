# YDL195W
Status: ok. Length: 4069 nt. Measured usable bases: 2472. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2472 | 0.2172 | 0.2065 |
| rnafold | ok | 2472 | 0.2085 | 0.2002 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1035 | 0.0628 | 0.0448 |
| seed_p | 1035 | 0.0912 | 0.1383 |
| seed_p_vs_seed_pars | 832 | 0.0321 | 0.0192 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
